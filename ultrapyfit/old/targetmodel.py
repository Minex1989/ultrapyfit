import numpy as np
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt
import lmfit
import random
import sys
import keyword
import copy
import math
import pickle

# firstly create populations and put them i model
# then add arrows. Create arrow binded by two populations and add to model list
# arrow should add itself to both end-populations
# remove arrow by calling kill() in this arrow and removing from model list
# arrow should remove itself from both end-populations
# if you kill population, firstly remove all arrows inside


def isIdentifier(identifier):  # check if string is valid python identifier
    if not(isinstance(identifier, str)):
        return False
    if not(identifier.isidentifier()):
        return False
    if keyword.iskeyword(identifier):
        return False
    return True


class ModPopulation:
    def __init__(self, new_name):
        self.arrows = list()  # processes associated with this population
        self.name = new_name  # name of the population
        # self.epsilon = dict() # define epsilons for irr and probe wavelengths
        self.initial = 0.0
        
        self.c = 0
        self.k_all = 1  # both used depending on mode selected
        self.tau = 1
        self.c_fixed = True
        self.k_all_fixed = False
        self.tau_fixed = False
        self.c_active = True
        self.k_all_active = False  # active means editable by user
        self.tau_active = False
        self.c_enabled = True
        self.k_all_enabled = False  # enabled means that user is allowed to turn it active
        self.tau_enabled = False  # if enabled is False, then active also must be False
        
    def remove(self, model):  # before calling ensure that all arrows with this population are removed, in other case there will be exception!
        if len(self.arrows) != 0:
            raise Exception('Attempted to invalid population removal!!')
        n = model.populations.index(self)
        model.populations.pop(n)
        
    def countActive(self):  # count active arrows plus this population
        active_counter = 0
        
        if self.k_all_active:
            active_counter += 1
        if self.tau_active:
            active_counter += 1
        
        for arrow in self.arrows:
            if arrow.source is self:
                if arrow.k_active:
                    active_counter += 1
                if arrow.sf_active:
                    active_counter += 1
                    
        return active_counter
    
    def countFixed(self):
        fixed_counter = 0
        
        if self.k_all_fixed:
            fixed_counter += 1
        elif self.tau_fixed:
            fixed_counter += 1
        
        for arrow in self.arrows:
            if arrow.source is self:
                if arrow.k_fixed:
                    fixed_counter += 1
                if arrow.sf_fixed:
                    fixed_counter += 1
                    
        return fixed_counter    
    
    def countActiveSFs(self):  # count active Scalling Factor fields
        active_counter = 0        
        for arrow in self.arrows:
            if arrow.source is self:
                if arrow.sf_active:
                    active_counter += 1
                    
        return active_counter    
    
    def countActiveSFsValues(self):  # count active Scalling Factor fields
        sfall = 0.0
        for arrow in self.arrows:
            if arrow.source is self:
                if arrow.sf_active:
                    sfall += arrow.sf
                    
        return sfall
    
    def countOutgoingArrows(self):  # count all arrows going out from this population
        arrow_counter = 0
        
        for arrow in self.arrows:
            if arrow.source is self:
                arrow_counter += 1
        
        return arrow_counter
 
    def enableDisableKs(self):  # rewrite enable/disable states in this branch
        active_counter = self.countActive()
        active_SF_counter = self.countActiveSFs()        
        arrow_counter = self.countOutgoingArrows()
        
        if arrow_counter == 0:
            if not self.tau_active:
                self.k_all_enabled = True
            else:
                self.k_all_enabled = False
            if not self.k_all_active:
                self.tau_enabled = True
            else:
                self.tau_enabled = False
            
        elif active_counter < arrow_counter:  # enable everything which is inactive and can be enabled
            double_present = False  # if in some arrow two fields are active, it determines k_all value.
            for arrow in self.arrows:
                if arrow.source is self:
                    if arrow.k_active and arrow.sf_active:
                        double_present = True

            if double_present:
                self.k_all_enabled = False
                self.tau_enabled = False
                for arrow in self.arrows:
                    if arrow.source is self:
                        if not arrow.sf_active:
                            arrow.k_enabled = True
                        else:
                            arrow.k_enabled = False

                        condition = not arrow.k_active and active_SF_counter < arrow_counter - 1
                        if condition or arrow.sf_active:
                            arrow.sf_enabled = True
                        else:
                            arrow.sf_enabled = False
                
            else:
                self.k_all_enabled = True if not self.tau_active else False
                self.tau_enabled = True if not self.k_all_active else False
                for arrow in self.arrows:
                    if arrow.source is self:
                        if not self.k_all_active and not self.tau_active:
                            arrow.k_enabled = True
                            if active_SF_counter < arrow_counter - 1 or arrow.sf_active:
                                arrow.sf_enabled = True
                            else:
                                arrow.sf_enabled = False
                        else:
                            if not arrow.sf_active:
                                arrow.k_enabled = True
                            else:
                                arrow.k_enabled = False

                            condition = not arrow.k_active and active_SF_counter < arrow_counter - 1
                            if condition or arrow.sf_active:
                                arrow.sf_enabled = True
                            else:
                                arrow.sf_enabled = False
                            
        else:  # disable everything which is inactive
            for arrow in self.arrows:
                if arrow.source is self:
                    if not arrow.k_active:
                        arrow.k_enabled = False
                    if not arrow.sf_active:
                        arrow.sf_enabled = False                        
                        
            if not self.k_all_active:
                self.k_all_enabled = False
            if not self.tau_active:
                self.tau_enabled = False              
                
    def updateBranchKs(self):  # calculate not active fields from active ones
        taskdone = False
        arrow_counter = self.countOutgoingArrows()
        lacking = arrow_counter - self.countActive()
        # 0.set markers
        self.k_all_determined = self.k_all_active
        self.tau_determined = self.tau_active
        if self.tau_active == True:
            self.k_all_determined = True
            self.k_all = 1/self.tau if self.tau != 0 else np.inf
        for arr in self.arrows:
            if arr.source is self:
                arr.k_determined = arr.k_active
                arr.sf_determined = arr.sf_active
            
        for i in range(2):
            # 1. search for solutions of sf_x * k_x = k_all (thirds)
            for j in range(2):
                for arr in self.arrows:
                    if arr.source is self:
                        if arr.k_determined and arr.sf_determined and not self.k_all_determined:
                            self.k_all = arr.k / arr.sf if arr.sf != 0 else 0
                            self.k_all_determined = True if arr.sf != 0 else False
                        if arr.k_determined and not arr.sf_determined and self.k_all_determined:
                            arr.sf = arr.k / self.k_all if self.k_all != 0 else 0
                            arr.sf_determined = True if self.k_all != 0 else False
                        if not arr.k_determined and arr.sf_determined and self.k_all_determined:
                            arr.k = arr.sf * self.k_all
                            arr.k_determined = True
                        if not arr.k_determined and arr.sf_determined and arr.sf == 0:
                            arr.k = 0
                            arr.k_determined = True
                        if self.k_all_determined and self.k_all == 0 and not arr.k_determined:
                            arr.k_determined = True
                            arr.k = 0    
            # 2. check if k's and k_al can give all (k_all=k_1+k_2+... equation)
            counter = 0
            if self.k_all_determined:
                counter += 1
            for arr in self.arrows:
                if arr.source is self:
                    if arr.k_determined:
                        counter += 1
            if counter >= arrow_counter:  # means that system is determined
                sumk = 0
                for arr in self.arrows:
                    if arr.source is self and arr.k_determined:
                        sumk += arr.k                
                if not self.k_all_determined:
                    self.k_all = sumk
                    self.k_all_determined = True
                else:
                    for arr in self.arrows:
                        if arr.source is self and not arr.k_determined:
                            arr.k = self.k_all - sumk
                            arr.k_determined = True    
                            break
            # 3. if not all possible parameters are given,
            # add sf's = (1-other known sf's)/no of lacking sf's
            if lacking > 0:
                sf_init = (1-self.countActiveSFsValues())/lacking
                for arr in self.arrows:
                    if lacking > 0 and arr.source is self and not arr.sf_determined:
                        arr.sf = sf_init
                        arr.sf_determined = True
                        lacking -= 1
            # 4. do sf's excluding thing to get k_all or some k's
            # (like in point 2)
            if not self.k_all_determined:
                ksum = 0.0
                sfsum = 0.0
                arrowssum = 0
                for arr in self.arrows:
                    if arr.source is self:
                        if arr.sf_determined:
                            sfsum += arr.sf
                            arrowssum += 1
                        if arr.k_determined:
                            ksum += arr.k
                            arrowssum += 1  
                if arrowssum == arrow_counter:
                    self.k_all = ksum / (1-sfsum) if sfsum != 1 else 0
                    self.k_all_determined = True if sfsum != 1 else False
            # 5. stop if all values are determined
            if self.k_all_determined:
                det_sum = 0
                for arr in self.arrows:
                    if arr.source is self:
                        if arr.k_determined and arr.sf_determined:
                            det_sum += 1
                if det_sum == arrow_counter:
                    taskdone = True
                    break  # everything is determined!! (except tau)

        # take care of tau
        if not self.tau_determined and self.k_all_determined:
            self.tau = 1/self.k_all if self.k_all != 0 else np.inf
            self.tau_determined = True
            
            
class ModProcess:
    def __init__(self, new_name, pop_source, pop_target):
        self.name = new_name  # name of the process
        self.source = pop_source  # initialize yourself with both neighbour populations
        self.target = pop_target
        self.source.arrows.append(self)  # initialize neighbour populations with yourself
        self.target.arrows.append(self)
        
        self.k = 1  # both used depending on mode selected
        self.sf = 1
        self.k_fixed = False
        self.sf_fixed = False
        self.k_active = False  # active means editable by user
        self.sf_active = False
        self.k_enabled = False  # enabled means that user is allowed to turn it active
        self.sf_enabled = False  # if enabled is False, then active also must be False

    def remove(self, model):  # removes arrow from neighbouring populations and model
        n1 = self.source.arrows.index(self)
        self.source.arrows.pop(n1)
        n2 = self.target.arrows.index(self)
        self.target.arrows.pop(n2)  # here you have to recount arrows between populations...
        count = 1
        for arr in self.source.arrows:
            if arr.source is self.target or arr.target is self.target:
                arr.number = count
                count += 1
        n3 = model.processes.index(self)
        model.processes.pop(n3)

class Model:
    def __init__(self):    
        self.populations = list()
        self.processes = list()
        self.psplit = False
        
    def addPopulation(self, new_population):
        self.populations.append(new_population)
        
    def addProcess(self, new_process):
        self.processes.append(new_process)

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        
    def load(filename):  # this is static method intentionally
        with open(filename, "rb") as f:
            loaded = pickle.load(f)
        return loaded

#    def setKmatrix(self, paths): #array of (source, destination, rate, varied)
#
#        sources = ["" for i in range(self.exp_no)]
#        for i in paths:
#            source = i[0]
#            destination = i[1]
#            rate = i[2]
#            varied = i[3]
#            if(source != destination):
#                self.params['k_%i%i' % (destination,source)].set(rate, vary=varied)
#                sources[source-1] += '-k_%i%i' % (destination,source)
#            else:
#                self.params['k_%i%i' % (destination,source)].set(-rate, vary=varied) #if destination == source, it means that this is the terminal component...
#
#        for i in range(self.exp_no):
#            if(len(sources[i]) > 0):
#                self.params['k_%i%i' % (i+1,i+1)].set(expr=sources[i])

    def genParameters(self):  # parameters are fixed by default, unfix some of them before fitting procedure
        self.params = lmfit.Parameters()
        # ASSUMES THAT SFs are not zero or 1!!!
        self.params.add('exp_no', value=len(self.populations), vary=False)
        if len(self.populations) < 1:
            raise Exception("Algorithm failure, because model is empty!") 
        
        for i in range(len(self.populations)):        
            self.params.add('c_%i' % (i+1), self.populations[i].c, False,
                            None, None, None, None)
            for j in range(len(self.populations)):
                self.params.add('k_%i%i' % (i+1, j+1), 0, False,
                                None, None, None, None)
        
        for i in range(len(self.populations)):
            popul = self.populations[i]
            print(popul.name)
            source = i
            if popul.countOutgoingArrows() == 0:
                vary = not(popul.k_all_fixed or popul.tau_fixed)
                self.params['k_%i%i' % (source+1, source+1)].set(-popul.k_all,
                                                                 vary=vary)
            else:
                # NOW YOU ARE GOING INTO BRANCH
                k_all_fixed = False
                total_sfs = 0.0
                if popul.k_all_fixed or popul.tau_fixed:  # if k_all fixed then do it
                    self.params['k_%i%i' % (source+1, source+1)].set(-popul.k_all,
                                                                     vary=False)
                    k_all_fixed = True  # name should be done not fixed, but nevermind
                    
                for arr in popul.arrows:
                    arr.done = False  # indicator if arrow remains to be done
                    if arr.source is popul:
                        target = self.populations.index(arr.target)
                        if arr.k_fixed and arr.sf_fixed and not k_all_fixed:  # if k_all can be fixed based on arrow then do it
                            self.params['k_%i%i' % (source+1, source+1)].set(expr="-"+'k_%i%i' % (target+1,source+1)+"/"+str(arr.sf))
                            self.params['k_%i%i' % (target+1, source+1)].set(arr.k, vary=False)
                            k_all_fixed = True
                            total_sfs += arr.sf
                            arr.done = True
                        elif arr.k_fixed:  # fix all direclty fixed k's
                            self.params['k_%i%i' % (target+1, source+1)].set(arr.k, vary=False)
                            arr.done = True
                        elif arr.sf_fixed:  # set proper expression for defined sf's
                            expr = "-"+'k_%i%i' % (source+1, source+1)+"*"+str(arr.sf)
                            self.params['k_%i%i' % (target+1, source+1)].set(expr=expr)
                            total_sfs += arr.sf
                            arr.done = True
                    
                freedom = popul.countOutgoingArrows()-popul.countFixed()  # how many free parameters will be
                if not k_all_fixed and freedom > 0:  # start vary from k_all
                    self.params['k_%i%i' % (source+1, source+1)].set(-popul.k_all, vary=True)
                    k_all_fixed = True  # means that now you can put this into eq
                    freedom -= 1

                # go egein over branch and set things to vary
                for arr in popul.arrows:
                    if arr.source is popul and not arr.done:
                        target = self.populations.index(arr.target)                            
                        if freedom > 0:
                            self.params['k_%i%i' % (target+1, source+1)].set(arr.k, vary=True)
                            arr.done = True
                            freedom -= 1
                if freedom > 0:
                    raise Exception("Algorithm failure, id 1002!")
                    
                expression = "("  # sum all k's which are fixed directly or varied
                count = 0
                for arr in popul.arrows:
                    if arr.source is popul and arr.done and not arr.sf_fixed:
                        target = self.populations.index(arr.target)                            
                        expression += '-k_%i%i' % (target+1, source+1)
                        count += 1
                expression += ")"
                if total_sfs == 1:
                    raise Exception("Algorithm failure, id 1003!") 

                if not k_all_fixed:  # set proper eq for k_all based only on not-sf arrows
                    if count == 0:
                        raise Exception("Algorithm failure, id 1005!")
                    expression += "/(1-" + str(total_sfs) + ")" 
                    self.params['k_%i%i' % (source+1, source+1)].set(expr=expression)
                    k_all_fixed = True

                else:  # set eq's for last k, assumes that k_all is fixed
                    expr_begining = '-k_%i%i' % (source+1, source+1) + \
                                    "*(1-"+str(total_sfs) + ")"
                    if count == 0:
                        expression = expr_begining
                    else:
                        expression = expr_begining + "+" + expression
                    count2 = 0
                    for arr in popul.arrows:  # go egein over branch and set remaining expr's (only one can be found)
                        if arr.source is popul and not arr.done and not arr.sf_fixed:
                            target = self.populations.index(arr.target)                                                     
                            self.params['k_%i%i' % (target+1, source+1)].set(expr=expression)
                            arr.done = True
                            count2 += 1
                    if count2 > 1:
                        raise Exception("Algorithm failure, id 1004!")

                # just check, probbaly not needed, but i am too tired to ensure that
                for arr in popul.arrows:
                    if arr.source is popul:
                        if arr.done == False:
                            raise Exception("Algorithm failure, id 1006!")
                            
        return self.params
        
#    def updateParameters(self, params):#updates values of existing parameters. does not add new values, does not modify model structure
#        p = params.valuesdict()
#        for elem in self.populations:
#            
#            if(self.psplit == False):
#                elem.initial = p[elem.name]
#            else:
#                for num in range(len(elem.initial)):
#                    elem.initial[num] = p['_' + str(num) + '_' + elem.name]
#            
#            for l, eps in elem.epsilon.items():
#                elem.epsilon[l] = p[elem.name + '__' + str(l).replace('.','_')]
#            
#        for elem in self.processes:
#            if elem.type == 'fi':
#                elem.fi = p[elem.name + '__fi']    
#            elif elem.type == 'k':
#                elem.k = p[elem.name + '__k']           
        
    def checkParams(self, experiment):  # run tests if params are correctly set. experiment object is to validiate its compatibility with model
        result = True                   # it should be run after updataParameers for both model and experiment, and assume that funcs loaded them correctly

        return result   

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:35:41 2020

@author: lucas
"""
from ultrapyfit.utils.divers import FiguresFormating, solve_kmatrix, TimeUnitFormater
from ultrapyfit.utils.Preprocessing import ExperimentException
from ultrapyfit.graphics.styles.set_styles import use_style
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from ultrapyfit.fit.ModelCreator import ModelCreator
import scipy.integrate as integral
from matplotlib.widgets import Slider


class ExploreResults:
    def __init__(self, fits, **kwargs):
        units = dict({'time_unit': 'ps', 'wavelength_unit': 'nm'}, **kwargs)
        if type(fits) == dict:
            self._fits = fits
        else:
            self._fits = {1: fits}
        self._units = units
        self._unit_formater = TimeUnitFormater(self._units['time_unit'])
        self._l = None
        self._ll = None
        self._lll = None
        self._fig = None
        self._residues = None
        self._data_fit = None
        self._x_fit = None
        self._fittes = None
        self._sspec = None
        self._x_verivefit = None
        self._residues = None
        self._wavelength_fit = None
        self._title = None

    def _get_cmap(self, name='tab10'):
        """Helper to securely get modern matplotlib colormaps (Python 3.14 safe)."""
        try:
            return mpl.colormaps[name]
        except AttributeError:
            # Fallback for older matplotlib versions just in case
            return plt.cm.get_cmap(name)

    @property
    def time_unit(self):
        return f'{self._unit_formater._multiplicator.name}s'

    @property
    def wavelength_unit(self):
        return self._units['wavelength_unit']

    @time_unit.setter
    def time_unit(self, val: str):
        try:
            val = val.lower()
            self._units['time_unit'] = val
            self._unit_formater.multiplicator = val
        except Exception:
            msg = 'An unknown time unit cannot be set'
            raise ExperimentException(msg)

    @wavelength_unit.setter
    def wavelength_unit(self, val: str):
        val = val.lower()
        if 'nanom' in val or 'wavelen' in val:
            val = 'nm'
        if 'centim' in val or 'wavenum' in val or 'cm' in val:
            val = 'cm-1'
        self._units['wavelength_unit'] = val

    def get_gloabl_fit_curve_results(self, fit_number=None, verify_svd_fit=False):
        """
        Returns a data set created from the best parameters values.

        Parameters
        ----------
        fit_number: int or None (default None)
            defines the fit number of the results all_fit dictionary. If None
            the last fit in  will be considered

        verify_svd_fit: bool (default  False)
            If True it will return the single fit perform to every trace of the
            spectra after an svd fit. If false and the fit is an SVD, the
            values return are the fit to the svd left vectors.
            If is not an SVD fit this parameter is not applicable
        """
        x, data, wavelength, result_params, exp_no, deconv, tau_inf, svd_fit, type_fit, derivative_space = \
            self._get_values(fit_number=fit_number,
                             verify_svd_fit=verify_svd_fit)
        model = ModelCreator(exp_no, x, tau_inf)
        ndata, nx = data.shape
        if type_fit == 'Exponential':
            if deconv:
                curve_resultados = data * 0.0
                for i in range(nx):
                    curve_resultados[:, i] = model.expNGaussDataset(result_params, i)
            else:
                t0 = result_params['t0_1'].value
                index = np.argmin([abs(i - t0) for i in x])
                curve_resultados = 0.0 * data[index:, :]
                for i in range(nx):
                    curve_resultados[:, i] = model.expNDataset(result_params, i)

        elif type_fit == 'Exponential convolved':
            curve_resultados = data * 0.0
            # t0 = result_params['t0_1'].value
            # index = np.argmin([abs(i - t0) for i in x])
            # curve_resultados = 0.0 * data[index:, :]
            for i in range(nx):
                curve_resultados[:, i] = model.expNDatasetIRF(result_params,
                                                              i, deconv)

        else:
            coeffs, eigs, eigenmatrix = solve_kmatrix(exp_no, result_params)
            curve_resultados = data * 0.0
            for i in range(nx):
                curve_resultados[:, i] = model.expNGaussDatasetTM(result_params,
                                                                  i,
                                                                  [coeffs,
                                                                   eigs,
                                                                   eigenmatrix])
        return curve_resultados

    @use_style
    def plot_global_fit(self, fit_number=None, selection=None,
                        plot_residues=True, style='lmu_res', ):
        """
        Function that generates a figure with the results of the fit stored in
        the all_fit attributes.  If less than 10 traces are fitted or selected
        a legend will be displayed
        
        Parameters
        ----------
        fit_number: int or None (default None)
            defines the fit number of the results all_fit dictionary. If None
            the last fit in  will be considered
        
        selection: list or None (default None)    
            If None all the traces fitted will be plotted, if a list only those
            selected in the list
        
        plot_residues: Bool (default True)
            If True the Figure returned will contain two axes a top one with
            the residues, and the bottom one with the fit and data
            
        style: style valid name (default 'lmu_res')
            defines the style to format the output figure, it can be any defined
            matplotlib style, any ultrapyfit style (utf) or any user defined
            style that follows matplotlib or utf styles and is saved in the
            correct folder. Check styles for more information.
        
        Returns
        ----------
        Figure and axes matplotlib objects
        """
        x, data, wavelength, params, exp_no, deconv, tau_inf, svd_fit, type_fit, derivative_space = \
            self._get_values(fit_number=fit_number)

        if wavelength is None:
            wavelength = np.array([i for i in range(len(data[1]))])
        if svd_fit:
            selection = None
        if selection is None:
            puntos = [i for i in range(data.shape[1])]
        else:
            puntos = [min(range(len(wavelength)), key=lambda i: abs(wavelength[i] - num)) for num in selection]
        xlabel = f'Time ({self.time_unit})'
        if plot_residues is False:
            fig, ax = plt.subplots()
            ax = ['_', ax]
        else:
            fig, ax = plt.subplots(2, 1, sharex=True,
                                   gridspec_kw={'height_ratios': [1, 5]})
        fittes = self.get_gloabl_fit_curve_results(fit_number=fit_number)
        alpha, s = 0.80, 8
        if type(deconv) == bool:
            if deconv:
                residues = data - fittes
                x_residues = x*1.0
            else:
                t0 = params['t0_1'].value
                index = np.argmin([abs(i - t0) for i in x])
                residues = data[index:, :] - fittes
                x_residues = x[index:]
        else:
            residues = data - fittes
            x_residues = x * 1.0
            # t0 = params['t0_1'].value
            # index = np.argmin([abs(i - t0) for i in x])
            # residues = data[index:, :] - fittes
            # x_residues = x[index:]
            ax[1].scatter(x, deconv, marker='o', alpha=alpha, s=s, c='k')
        for i in puntos:
            if plot_residues:
                ax[0].scatter(x_residues, residues[:, i], marker='o', alpha=alpha, s=s)
            ax[1].scatter(x, data[:, i], marker='o', alpha=alpha, s=s)
            ax[1].plot(x_residues, fittes[:, i], '-', color='r', alpha=0.5, lw=1.5)
            if len(puntos) <= 10:
                legenda = self._legend_for_plot(svd_fit, data, wavelength, puntos)
                ax[1].legend(legenda, loc='best', ncol=1 if svd_fit else 2)
        if plot_residues:
            # FiguresFormating.format_figure(ax[0], residues, x, size=size)
            ax[0].set_ylabel('Residues')
        # iguresFormating.format_figure(ax[1], data, x)
        FiguresFormating.axis_labels(ax[1], xlabel, r'$\Delta$A')
        plt.subplots_adjust(left=0.145, right=0.95)
        return fig, ax

    def get_DAS(self, number='all', fit_number=None, convert_to_EAS=False):
        """
        returns an array of the Decay associated spectra. The number of rows is
        the number of species and the number of columns correspond to the
        wavelength vector.

        Parameters
        ----------
        number: list of inst or 'all'
            Defines the DAS spectra wanted, if there is tau_inf include -1 in
            the list:
            e.g.: for a fit with three exponential, if the last two are wanted;
                   number = [1, 2]
            e.g.2: the last two exponential plus tau_inf; number = [1, 2, -1]

        fit_number: int or None (default None)
            defines the fit number of the results all_fit dictionary.
            If None the last fit in  will be considered
        
        convert_to_EAS:
            return the especies associted spectra, obtained as a linear 
            combination of the DAS and considering a sequential model.
            
        Returns
        ----------
        numpy 2d array
        """
        x, data, wavelength, params, exp_no, deconv, tau_inf, svd_fit, type_fit, derivative_space = \
            self._get_values(fit_number=fit_number)
        if svd_fit and hasattr(self._fits[fit_number], 'params_svd'):
            params = self._fits[fit_number].params_svd
        values = [[params['pre_exp%i_' % (ii + 1) + str(i + 1)].value for i in range(data.shape[1])]
                  for ii in range(exp_no)]
        if type(deconv) == bool:
            if deconv and tau_inf is not None:
                values.append([params['yinf_' + str(i + 1)].value for i in range(data.shape[1])])
            elif not deconv:
                values.append([params['y0_' + str(i + 1)].value for i in
                               range(data.shape[1])])
        das = np.array(values)
        if convert_to_EAS:
            das = self.das_to_eas(das, params, wavelength,
                                  exp_no, tau_inf, deconv)
        if number != 'all':
            msg = 'Number should be "all" or a list containing the desired ' \
                  'species if tau inf include -1 in the list'
            assert type(number) == list, msg
            wanted = self._wanted_DAS(exp_no, number, tau_inf)
            das = das[wanted, :]

        return das

    @use_style
    def plot_DAS(self, fit_number=1, wanted_das=None, normalize=False, style='lmu_spec'):
        """Plots the Decay Associated Spectra (DAS) - Qt GUI Compatible."""
        # verify type of fit is: either fit to Singular vectors or global fit to traces
        if fit_number not in self._fits:
            raise ExperimentException(f"Fit number {fit_number} not found.")

        fit_result = self._fits[fit_number]
        exp_no = fit_result.exp_no

        amplitudes = fit_result.amplitudes
        wave = fit_result.wavelength
        taus = [fit_result.params[f't{i + 1}'].value for i in range(exp_no)]

        if wanted_das is None:
            wanted_das = list(range(exp_no))
            if fit_result.tau_inf:
                wanted_das.append(-1)

        valid_indices = self._wanted_DAS(exp_no, wanted_das)

        fig = plt.figure(figsize=(8, 6))

        self._fig = fig
        ax = fig.add_subplot(111)
        cmap = self._get_cmap('tab10')  # Modern colormap

        for idx, i in enumerate(valid_indices):
            amp_data = amplitudes[i, :]
            if normalize:
                # FIXED: Used standard python float() instead of np.float()
                amp_data = amp_data / float(np.max(np.abs(amp_data)))

            label = f"$\\tau_{idx + 1}$ = {self._unit_formater.format(taus[idx])}" if i != -1 else "$\\tau_{\\infty}$"
            ax.plot(wave, amp_data, label=label, color=cmap(idx % 10), linewidth=2)

        ax.set_xlabel(f"Wavelength ({self._units.get('wavelength_unit')})")
        ax.set_ylabel("Amplitude (Norm)" if normalize else "Amplitude")
        ax.set_title(f"Decay Associated Spectra (Fit {fit_number})")
        ax.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        fig.tight_layout()
        return fig, ax

    def das_to_eas(self, das, params, wavelength, n_exp, tau_inf, deconv):
        """
        Recalculates DAS spectra into EAS, treating y_inf as final product.
        Replaces DAS with EAS, so one should treat this data as EAS after
        calling this method.
        It works with matrices and should be correct for any number of exp's.
        """

        no_of_wavelengths = wavelength.shape[0]
        tau_inf_enabled = tau_inf  # set here if it is enabled
        no_of_exps = int(n_exp)  # load here number of exponentials
        # params = self.params.copy()
        if not deconv:
            offset = das[-1, :]
            das = das[:-1, :]
        eas = np.zeros(das.shape)
        ##########
        if tau_inf_enabled:
            size_of_kmatrix = no_of_exps + 1
        else:
            size_of_kmatrix = no_of_exps


        # build kmatrix of the sequential model
        kmatrix = np.zeros((size_of_kmatrix, size_of_kmatrix))
        k_values = []
        for i in range(no_of_exps):
            k_value = 1 / params['tau%i_' % (i + 1) + str(1)].value
            kmatrix[i, i] = -k_value
            if (i + 1 < size_of_kmatrix):
                kmatrix[i + 1, i] = k_value
            k_values.append(k_value)

        # initialize initial concentration values,
        c_initials = np.zeros(size_of_kmatrix)
        # since it's sequential only the first is 1
        c_initials[0] = 1.0

        # now extract eigenvalues and eigenvectors, to be able to reduce kmatrix
        # to the only-diagonal form. then we can easily differentiate and get solution
        eigs_out, vects_out = np.linalg.eig(kmatrix)

        # note that eigenvalues can come out not ordered. we want them in the
        # same order and values as k1,k2,k3... note that the same values are
        # obtained only if kmatrix describes sequential model. more complicated
        # models can give different k values than these used to build kmatrix
        if tau_inf_enabled and deconv:
            oryginal_k_order = -np.array(k_values + [0.0])
        else:
            oryginal_k_order = -np.array(k_values)

        ks_ordering = np.argsort(oryginal_k_order)
        ks_reverse_ordering = np.argsort(ks_ordering)

        # sort eigenthings
        sort_ordering = np.argsort(eigs_out)
        eigs_sorted = eigs_out[sort_ordering]
        vects_sorted = vects_out[:, sort_ordering]

        # order eigenthings like k1,k2,k3....
        eigs = eigs_sorted[ks_reverse_ordering]
        vects = vects_sorted[:, ks_reverse_ordering]

        # then solve linear equation, where t=0 so you have
        # eigvects_matrix*vect_of_concentrations = vect_of_initial_values
        # by this you get coeffs which are before diagonalized exp functions
        # print(vects.shape)
        # print(c_initials.shape)
        coeffs = np.linalg.solve(vects, c_initials)

        # ok, now you make diagonal array with these coeffs
        em_matrix = np.identity(coeffs.shape[0]) * np.transpose(
            coeffs[np.newaxis])
        # and you multiply eigenvector matrix by this. so you have:
        # fit_of_data = eas_array * d_matrix * exp_matrix
        # fit_of_data = das_array * exp_matrix
        d_matrix = np.dot(vects, em_matrix)

        # now you can just transpose that, and by comparison of das and sas,
        # you can get eas values from linear equation:
        d_t = np.transpose(d_matrix)
        # like below, but need to do this in loop for all kinetics:
        # EASv = np.linalg.solve(d_t, DASv)

        # idea is to iterate slowly over every kinetic, and change exp-associated
        # preexp factors into species associated preexp factors
        for wavelength_num in range(no_of_wavelengths):
            DASv = das[:, wavelength_num]
            # DASv = [params[
            #        'pre_exp%i_%i' % (i + 1, wavelength_num + 1)].value
            #        for i in range(no_of_exps)]
            # if tau_inf_enabled:
            #     DASv.append(
            #         self.params['yinf_%i' % (wavelength_num + 1)].value)


            EASv = np.linalg.solve(d_t, np.array(DASv))
            eas[:, wavelength_num] = EASv
            # lets replace das with eas:
            # for i in range(no_of_exps):
            #    params['pre_exp%i_' % (i + 1) + str(wavelength_num + 1)].set(
            #        value=EASv[i])
            # if (tau_inf_enabled):
            #    params['yinf_' + str(wavelength_num + 1)].set(
            #        value=EASv[no_of_exps])
        if not deconv:
            # add offset (vertical stacking)
            eas = np.r_[eas, [offset]]
        return eas
        # lets put back the params, but now pre_exps are EAS, not DAS!
        # self.params = params

    def verify_fit(self, fit_number=1, fig=None):
        """
        Interactive plot to scan through fit residuals.
        Fixed np.int deprecation for slider index.
        """
        if fit_number not in self._fits:
            raise ExperimentException(f"Fit number {fit_number} not found.")

        fit_res = self._fits[fit_number]
        data = fit_res.data
        fit_data = fit_res.fit
        residues = fit_res.residues
        x = fit_res.x

        fig = plt.figure(figsize=(10, 8))

        self._fig = fig

        # Adjust layout to make room for slider at the bottom
        plt.subplots_adjust(bottom=0.2)

        ax_trace = fig.add_subplot(211)
        ax_res = fig.add_subplot(212, sharex=ax_trace)

        # Initial plot (Index 0)
        l_data, = ax_trace.plot(x, data[:, 0], 'ko', alpha=0.5, label='Data')
        l_fit, = ax_trace.plot(x, fit_data[:, 0], 'r-', linewidth=2, label='Fit')
        l_res, = ax_res.plot(x, residues[:, 0], 'b-', label='Residuals')

        ax_res.axhline(0, color='black', linestyle='--')
        ax_trace.set_ylabel("Amplitude")
        ax_trace.legend()
        ax_trace.set_title(f"Verify Fit {fit_number} - Trace 0")
        ax_res.set_ylabel("Residuals")
        ax_res.set_xlabel(f"Time ({self._units.get('time_unit')})")

        # Setup matplotlib slider
        axcolor = 'lightgoldenrodyellow'
        axpos = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor=axcolor)
        spos = Slider(axpos, 'Trace Idx', 0, data.shape[1] - 1, valinit=0, valfmt='%0.0f')

        def update(val):
            # FIXED: standard int() instead of deprecated np.int()
            pos = int(spos.val)
            l_data.set_ydata(data[:, pos])
            l_fit.set_ydata(fit_data[:, pos])
            l_res.set_ydata(residues[:, pos])

            # Rescale axes based on new data
            ax_trace.relim()
            ax_trace.autoscale_view()
            ax_res.relim()
            ax_res.autoscale_view()
            ax_trace.set_title(f"Verify Fit {fit_number} - Trace {pos}")
            fig.canvas.draw_idle()

        spos.on_changed(update)

        # Keep reference to slider so it doesn't get garbage collected
        self._slider = spos

        return fig, (ax_trace, ax_res)

    def _update_verified_Fit(self, val):
        """
        updates the verified_fit function
        """
        # amp is the current value of the slider
        value = self._sspec.val
        value = int(round(value))
        # update curve
        title = round(self._wavelength_fit[value])
        self._title.set_text(f'{title} nm')
        plt.title(f'{title} nm')
        self._l.set_ydata(self._data_fit[:, value])
        self._ll.set_ydata(self._fittes[:, value])
        self._lll.set_ydata(self._residues[:, value])
        # redraw canvas while idle
        self._fig.canvas.draw_idle()

    @use_style
    def plot_concentrations(self, fit_number=None, names=None,
                            plot_total_c=True, legend=True,
                            style='lmu_res'):  # temporal function.
        """
        Function that generates a figure with the concentration evolution of a
        Target fit
        
        Parameters
        ----------
        fit_number: int or None (default None)
            defines the fit number of the results all_fit dictionary.
            If None the last fit in  will be considered.
        
        names: list (default None)
            List that allows to redefine the names of the components. 
            Is none the default names "specie" is use.
            The names are display in the legend if legend is True
        
        plot_total_c: bool (default True)
            Defines if the Total concentration is 
        
        legend: bool (default True)
            Defines if the legend is display

        style: style valid name (default 'lmu_res')
            defines the style to format the output figure, it can be any defined
            matplotlib style, any ultrapyfit style (utf) or any user defined
            style that follows matplotlib or utf styles and is saved in the
            correct folder. Check styles for more information.

        Returns
        ----------
        Figure and axes matplotlib objects
        """
        x, data, wavelength, params, exp_no, deconv, tau_inf, svd_fit, type_fit, derivative_space = \
            self._get_values(fit_number=fit_number)

        if type_fit == 'Exponential':
            msg = 'This function is only available for target fit'
            raise ExperimentException(msg)
        xlabel = f'Time ({self.time_unit})'
        maxi_tau = -1 / params['k_%i%i' % (exp_no - 1, exp_no - 1)].value
        if maxi_tau > x[-1]:
            maxi_tau = x[-1]
        # size of the matrix = no of exponenses = no of species
        coeffs, eigs, eigenmatrix = solve_kmatrix(exp_no, params)
        t0 = params['t0_1'].value
        if deconv:
            fwhm = params['fwhm_1'].value/2.35482
            expvects = [coeffs[i] * ModelCreator.expGauss(x - t0, -1/eigs[i], 
                                                          fwhm)
                        for i in range(len(eigs))]
        else:
            expvects = [coeffs[i] * ModelCreator.exp1(x - t0, -1/eigs[i])
                        for i in range(len(eigs))]
        concentrations = [sum([eigenmatrix[i, j] * expvects[j]
                               for j in range(len(eigs))])
                          for i in range(len(eigs))]
        if names is None or len(names) != self._exp_no:
            if fit_number is None:
                fit_number = max(self._fits.keys())
            if "model_names" in self._fits[fit_number].details.keys():
                names = self._fits[fit_number].details["model_names"]
            else:
                names = [f"Species {i + 1}" for i in range(self._exp_no)]
        fig, ax = plt.subplots(1)
        for i in range(len(eigs)):
            ax.plot(x, concentrations[i], label=names[i])
        if plot_total_c:
            allc = sum(concentrations)
            ax.plot(x, allc, label='Total concentration')  # sum of all for checking => should be unity
        if legend:
            plt.legend(loc='best')
        FiguresFormating.axis_labels(ax, xlabel, 'Concentration (A.U.)')
        plt.xlim(-3, round(maxi_tau * 7))
        return fig, ax
    
    def print_fit_results(self, fit_number=None):
        """
        Print out a summarize result of the fit.
        
        Parameters
        ----------
        fit_number: int or None (default None)
            defines the fit number of the results all_fit dictionary. If None the last fit in  will
            be considered.
        """
        if fit_number is None:
            fit_number = max(self._fits.keys())
        fit = self._fits[fit_number]
        print(f"Fit number {fit_number}: \t" + fit.__str__())
        
    def _get_wave_label_res(self, wavelength):
        """
        Returns a formatted string from the units attribute
        """
        if wavelength is None:
            xlabel = 'pixel'
        elif self.wavelength_unit == 'cm-1':
            xlabel = 'Wavenumber (cm$^{-1}$)'
        else:
            xlabel = f'Wavelength ({self.wavelength_unit})'
        return xlabel

    def _legend_plot_DAS(self, params, exp_no, deconv, tau_inf, type_fit, precision):
        """
        returns legend for plot_DAS function
        """
        times_val = [abs(params['tau%i_1' % (i + 1)].value)
                     for i in range(exp_no)]
        add_tau_inf = False
        for i in times_val:
            if i < np.inf:
                pass
            else:
                times_val.remove(i)
                add_tau_inf = True
        legenda = [self._unit_formater.value_formated(i, precision)
                   for i in times_val]

        if deconv and type_fit == 'Exponential':
            if tau_inf is None:
                pass
            elif tau_inf != 1E+12:
                legenda.append(self._unit_formater.value_formated(tau_inf,
                                                                  precision))
            else:
                legenda.append(r'$\tau$ = inf')
        elif add_tau_inf and type_fit == 'Target':
            legenda.append(r'$\tau$ = inf')
        if not deconv:
            legenda.append(r'Offset')
        print(deconv)
        return legenda

    def _legend_for_plot(self, svd_fit, data, wavelength, puntos):
        """Generates legend for plots depending on whether it's SVD or traces."""
        if wavelength is None:
            wavelength = np.array([i for i in range(len(data[1]))])

        if svd_fit:
            legend = ['_' for i in range(data.shape[1])] + \
                     [f'left SV {i}' for i in range(1, data.shape[1] + 1)]
        elif wavelength is not None:
            val = 'cm$^{-1}$' if self._units.get('wavelength_unit') == 'cm-1' else self._units.get('wavelength_unit')
            legend = ['_' for i in range(len(puntos))] + \
                     [f'{round(wavelength[i])} {val}' for i in puntos]
        else:
            legend = ['_' for i in range(len(puntos))] + \
                     [f'curve {i}' for i in range(data.shape[1])]
        return legend

    @staticmethod
    def _wanted_DAS(exp_no, number, tau_inf):
        """
        return a list of numbers equivalent to the sub-array of DAS wanted.
        Note counting starts at 0.
        """
        posible = [i for i in range(exp_no)]
        posible.append(-1)
        wanted = [posible[ii] for ii, i in enumerate(posible) if i in number]
        return wanted

    def _get_values(self, fit_number=None, verify_svd_fit=False):
        """
        return values from the results object
        """
        if fit_number is None:
            fit_number = max(self._fits.keys())
        fit = self._fits[fit_number]
        return fit.get_values()
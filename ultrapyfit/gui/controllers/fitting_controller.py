import io
import sys
import re
import numpy as np
from PySide6 import QtWidgets, QtCore


class FittingController:
    def __init__(self, main_window):
        self.mw = main_window

    def execute_fitting(self):
        self.mw.statusBar().showMessage("Checking parameters...")
        params = self.get_fit_parameters()
        if not self.validate_pre_fit(params):
            self.mw.statusBar().clearMessage()
            return
        self.mw._fit_aborted = False
        self.mw._is_fitting = True
        experiment = self.mw.get_experiment()
        (fit_mode, data_sel_type, svd_comps, traces_list, average, region_min, region_max, single_wave, single_average, mask_list, exp_no, irf_w, irf_mu, initial_taus, tau_inf) = params
        self.mw.settings_manager._save_current_dataset_settings()
        if not initial_taus:
            initial_taus = [10.0 ** (i) for i in range(exp_no)]
        self.mw.btnRunFit.setText("Cancel Fitting")
        self.mw.btnRunFit.setStyleSheet("background-color: #d9534f; color: white; font-weight: bold;")
        self.mw.setCursor(QtCore.Qt.CursorShape.WaitCursor)
        self.mw.statusBar().showMessage("Data preparation and slicing...")
        QtWidgets.QApplication.processEvents()
        try:
            if fit_mode == 0:
                if data_sel_type == 'svd': experiment.select_SVD_vectors(val=svd_comps)
                elif data_sel_type == 'traces': experiment.select_traces(points=traces_list, average=average, avoid_regions=mask_list)
                elif data_sel_type == 'region': experiment.select_region(mini=region_min, maxi=region_max)
            elif fit_mode == 1:
                experiment.select_traces(points=[single_wave], average=single_average)
            self.mw.statusBar().showMessage("Levenberg-Marquardt fitting in progress... Please wait!")
            QtWidgets.QApplication.processEvents()
            sys.stdout = self.mw.stdout_redirector
            self.mw.textFitLog.clear()
            self.mw.textFitLog.append("--- Start Fitting ---")
            if fit_mode == 0:
                experiment.fitting.initialize_exp_params(irf_mu, irf_w, *initial_taus, tau_inf=tau_inf)
                experiment.fitting._active_minimizer = experiment.fitting
                experiment.fitting.fit_global(vary=True, verbose=True)
            elif fit_mode == 1:
                experiment.fitting.fit_single_exp(single_wave, single_average, irf_mu, irf_w, *initial_taus, tau_inf=tau_inf, plot=False)
            sys.stdout = sys.__stdout__
            if self.mw._fit_aborted:
                self.mw.statusBar().showMessage("Fitting interrupted.", 5000)
                return
            self.mw.textFitLog.append("--- Fitting Complete ---")
            self.mw.statusBar().showMessage("The fitting has been successfully completed!", 5000)
            self.mw.settings_manager._save_current_dataset_settings()
            self._add_fit_to_tree()
        except Exception as e:
            self.mw.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            self.mw.statusBar().showMessage("Error during fitting!", 5000)
            sys.stdout = sys.__stdout__
            QtWidgets.QMessageBox.critical(self.mw, "Mathematical Error", f"The fitting algorithm encountered an error:\n\n{str(e)}\n\nSuggestion: Try adjusting the initial values (Tau) or the excluded ranges.")
        finally:
            self.mw._is_fitting = False
            self.mw.btnRunFit.setText("Run Fitting")
            self.mw.btnRunFit.setStyleSheet("")
            self.mw.btnRunFit.setEnabled(True)
            self.mw.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

    def abort_fitting(self):
        experiment = self.mw.get_experiment()
        if hasattr(experiment.fitting, '_active_minimizer'):
            self.mw._fit_aborted = True
            experiment.fitting._active_minimizer.stop_fit()
            self.mw.textFitLog.append("\n⚠️ --- FITTING INTERRUPTED BY THE USER --- ⚠️")
            self.mw.btnRunFit.setText("Shutting down...")
            self.mw.btnRunFit.setStyleSheet("background-color: #f0ad4e; color: black;")
            self.mw.btnRunFit.setEnabled(False)

    def handle_fit_button_click(self):
        if not self.mw._is_fitting: self.execute_fitting()
        else: self.abort_fitting()

    def get_fit_parameters(self):
        fit_mode = self.mw.cbFittingType.currentIndex()
        data_sel_type = None
        if fit_mode == 0:
            if self.mw.rbGlobalFitSvd.isChecked(): data_sel_type = 'svd'
            elif self.mw.rbGlobalFitTraces.isChecked(): data_sel_type = 'traces'
            elif self.mw.rbGlobalFitRegion.isChecked(): data_sel_type = 'region'
        else: data_sel_type = 'single'
        svd_comps = self.mw.sbGlobalFitSvdComps.value()
        global_average = self.mw.sbGlobalFitAverage.value()
        single_wave = self.mw.sbSingleFitWave.value()
        single_average = self.mw.sbSingleFitAverage.value()
        region_min = self.mw.sbGlobalFitRegionMin.value(); region_max = self.mw.sbGlobalFitRegionMax.value()
        if region_min > region_max: region_min, region_max = region_max, region_min
        traces_text = self.mw.leGlobalFitTraces.text().strip()
        traces_list = [float(m) for m in re.findall(r"\d+(?:\.\d+)?", traces_text)] if traces_text else []
        mask_text = self.mw.leGlobalFitMasking.text().strip(); mask_list = None
        if mask_text and data_sel_type != 'svd':
            mask_list = []
            matches = re.findall(r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)", mask_text)
            for m_min, m_max in matches:
                val1, val2 = float(m_min), float(m_max)
                if val1 > val2: val1, val2 = val2, val1
                mask_list.append([val1, val2])
        tau_text = self.mw.leInitialTau.text().strip(); initial_taus = None
        if tau_text:
            matches = re.findall(r"\d+(?:\.\d+)?", tau_text)
            if matches: initial_taus = [float(m) for m in matches]
        exp_no = self.mw.sbExpNo.value(); irf_w = self.mw.dsbIRFw.value()
        if irf_w == 0: irf_w = None
        irf_mu = self.mw.dsbIRFmu.value(); tau_inf = 1e12 if self.mw.chkTauInf.isChecked() else None
        return (fit_mode, data_sel_type, svd_comps, traces_list, global_average, region_min, region_max, single_wave, single_average, mask_list, exp_no, irf_w, irf_mu, initial_taus, tau_inf)

    def validate_pre_fit(self, params):
        (fit_mode, data_sel_type, svd_comps, traces_list, average, region_min, region_max, single_wave, single_average, mask_list, exp_no, irf_w, irf_mu, initial_taus, tau_inf) = params
        if self.mw.treeExperiment.currentItem() is None: return False
        experiment = self.mw.get_experiment()
        if initial_taus is not None and len(initial_taus) != exp_no:
            self._show_validation_error("Invalid Tau parameters", f"The number of initial tau values provided ({len(initial_taus)}) does not match the number of requested exponentials ({exp_no}).")
            return False
        min_wave, max_wave = np.min(experiment.wavelength), np.max(experiment.wavelength)
        if fit_mode == 0:
            if data_sel_type == 'traces' and not traces_list:
                self._show_validation_error("Missing traces", "The 'Traces' mode is selected, but no wavelengths have been specified.")
                return False
            if data_sel_type == 'region':
                if region_min == region_max:
                    self._show_validation_error("Invalid range", "The start and end points of the range cannot be the same.")
                    return False
                if region_max < min_wave or region_min > max_wave:
                    self._show_validation_error("Range error", f"The specified range is completely outside the wavelength range of the data ({min_wave:.1f} - {max_wave:.1f} nm).")
                    return False
        elif fit_mode == 1:
            if single_wave < min_wave or single_wave > max_wave:
                self._show_validation_error("Wavelength error", f"The specified wavelength is outside the data range ({min_wave:.1f} - {max_wave:.1f} nm).")
                return False
        return True

    def _show_validation_error(self, title, message):
        msg_box = QtWidgets.QMessageBox(self.mw); msg_box.setIcon(QtWidgets.QMessageBox.Icon.Warning); msg_box.setWindowTitle(title); msg_box.setText(message); msg_box.exec()

    def _add_fit_to_tree(self):
        current_item = self.mw.treeExperiment.currentItem()
        if current_item is None: return
        parent_item = current_item
        while parent_item.parent() is not None: parent_item = parent_item.parent()
        experiment = self.mw.get_experiment(); fit_mode = self.mw.cbFittingType.currentIndex()
        if fit_mode == 0:
            fit_dict = experiment.fitting.fit_records.global_fits; fit_category = 'global'
            if not fit_dict: return
            fit_number = list(fit_dict.keys())[-1]; latest_fit = fit_dict[fit_number]; exp_no = latest_fit.details.get('exp_no', '?')
            mode_str = "SVD" if self.mw.rbGlobalFitSvd.isChecked() else "Global"
            node_text = f"Fit {fit_number}: {exp_no} exp ({mode_str})"
        elif fit_mode == 1:
            fit_dict = experiment.fitting.fit_records.single_fits; fit_category = 'single'
            if not fit_dict: return
            fit_number = list(fit_dict.keys())[-1]; latest_fit = fit_dict[fit_number]; exp_no = latest_fit.details.get('exp_no', '?')
            node_text = f"Fit {fit_number}: {exp_no} exp (Single Trace)"
        fit_item = QtWidgets.QTreeWidgetItem([node_text])
        fit_item.setData(0, QtCore.Qt.UserRole, {'type': 'fit_result', 'fit_category': fit_category, 'fit_number': fit_number})
        parent_item.addChild(fit_item); parent_item.setExpanded(True); self.mw.treeExperiment.setCurrentItem(fit_item)

    def _update_fit_text_report(self, experiment, fit_number, text_browser):
        captured_output = io.StringIO(); original_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            experiment.fitting.print_fit_results(fit_number)
        except Exception as e: print(f"Error while generating the report: {e}", file=original_stdout)
        finally: sys.stdout = original_stdout
        text_browser.setText(captured_output.getvalue())

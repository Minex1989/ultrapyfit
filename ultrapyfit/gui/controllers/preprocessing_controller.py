import re
from matplotlib import pyplot as plt
from ultrapyfit.utils.Preprocessing import ExperimentException

class PreprocessingController:
    def __init__(self, main_window):
        self.mw = main_window

    def on_preprocess_tool_changed(self, index):
        self.mw.stackedPreprocessTools.setCurrentIndex(index)
        tool_name = self.mw.cbPreprocessingTool.currentText()
        if hasattr(self.mw, '_chirp_click_cid') and self.mw._chirp_click_cid is not None:
            try: self.mw.preprocessingMplWidget.canvas.figure.canvas.mpl_disconnect(self.mw._chirp_click_cid)
            except Exception: pass
            self.mw._chirp_click_cid = None
        self.plot_preprocessing_preview()

    def apply_preprocessing(self):
        experiment = self.mw.get_experiment()
        if not experiment:
            self.mw.statusBar().showMessage("Nincs kísérlet betöltve! (No experiment loaded)", 5000)
            return
        tool = self.mw.cbPreprocessingTool.currentText()
        prep = experiment.preprocessing
        try:
            if tool == "Cut Time": prep.cut_time(**self._get_cut_time_params())
            elif tool == "Cut Wavelength": prep.cut_wavelength(**self._get_cut_wave_params())
            elif tool == "Shift Time": prep.shift_time(**self._get_shift_time_params())
            elif tool == "Baseline Subtraction": prep.baseline_substraction(**self._get_baseline_sub_params())
            elif tool == "Polynomial Baseline": prep.subtract_polynomial_baseline(**self._get_poly_baseline_params())
            elif tool == "Average Time": prep.average_time(**self._get_average_time_params())
            elif tool == "Derivate": prep.derivate_data(**self._get_derivate_params())
            elif tool == "Delete Points": prep.delete_points(**self._get_delete_points_params())
            elif tool == "Calibrate Wavelength": prep.calibrate_wavelength(**self._get_calibrate_wave_params())
            elif tool == "Chirp Correction (Polynomial)":
                prep.chirp_correction_polynomial(**self._get_chirp_polynomial_params())
                self.mw.leChirpPoints.clear()
            elif tool == "Chirp Correction (Sellmeier)": prep.chirp_correction_sellmeier(**self._get_chirp_sellmeier_params())
            elif tool == "Correct Overlap": prep.correct_overlap(**self._get_correct_overlap_params())
            else: raise ValueError(f"Unknown tool selected: {tool}")
            self.mw.statusBar().showMessage(f"Successfully applied: {tool}", 5000)
            self.plot_preprocessing_preview()
            self.update_history_list()
            self.mw.settings_manager._save_current_dataset_settings()
        except (ValueError, ExperimentException) as e: self.mw.statusBar().showMessage(f"Input Error: {str(e)}", 7000)
        except Exception as e: self.mw.statusBar().showMessage(f"Math Error ({tool}): {str(e)}", 7000)

    def update_history_list(self):
        self.mw.listPreprocessHistory.clear()
        experiment = self.mw.get_experiment()
        if not experiment: return
        for container in experiment.preprocessing.history_stack:
            self.mw.listPreprocessHistory.addItem(container.action_name)

    def undo_preprocessing(self):
        experiment = self.mw.get_experiment()
        if not experiment or not experiment.preprocessing.history_stack:
            self.mw.statusBar().showMessage("No actions to undo.", 3000)
            return
        try:
            experiment.preprocessing.undo_last_preprocesing()
            self.plot_preprocessing_preview()
            self.update_history_list()
            self.mw.statusBar().showMessage("Last action undone successfully.", 4000)
            self.mw.settings_manager._save_current_dataset_settings()
        except Exception as e: self.mw.statusBar().showMessage(f"Undo Error: {str(e)}", 5000)

    def on_history_double_clicked(self, item):
        experiment = self.mw.get_experiment()
        if not experiment: return
        target_index = self.mw.listPreprocessHistory.row(item)
        try:
            experiment.preprocessing.restore_data(target_index)
            self.plot_preprocessing_preview()
            self.mw.statusBar().showMessage(f"Restored data to state: {item.text()}", 4000)
            self.update_history_list()
            self.mw.settings_manager._save_current_dataset_settings()
        except Exception as e: self.mw.statusBar().showMessage(f"Restore Error: {str(e)}", 5000)

    def plot_preprocessing_preview(self):
        experiment = self.mw.get_experiment()
        if not experiment or experiment.data is None: return
        tool_name = self.mw.cbPreprocessingTool.currentText()
        spectral_tools = ["Cut Wavelength", "Baseline Subtraction", "Polynomial Baseline", "Calibrate Wavelength", "Correct Overlap"]
        if tool_name == "Delete Points" and hasattr(self.mw, 'cbDeleteDim') and self.mw.cbDeleteDim.currentText().lower() == "wavelength":
            spectral_tools.append("Delete Points")
        try:
            if tool_name.startswith("Chirp Correction"): fig, ax = experiment.plot_2D(time_range=None, z_limit=None)
            elif tool_name in spectral_tools: fig, ax = experiment.plot_spectra(times='all')
            else: fig, ax = experiment.plot_traces(traces=experiment.wavelength.tolist())
            self.mw.preprocessingMplWidget.update_figure(fig)
            self.mw._chirp_click_cid = None; self.mw._active_span_selector = None
            if tool_name == "Chirp Correction (Polynomial)": self.mw._chirp_click_cid = self.mw.plot_controller.enable_2d_point_picking(fig=fig, ax=ax, target_lineedit=self.mw.leChirpPoints)
            elif tool_name == "Cut Time": self.mw._active_span_selector = self.mw.plot_controller.enable_range_picking(ax=ax, le_min=self.mw.leCutTimeMin, le_max=self.mw.leCutTimeMax)
            elif tool_name == "Cut Wavelength": self.mw._active_span_selector = self.mw.plot_controller.enable_range_picking(ax=ax, le_min=self.mw.leCutWaveMin, le_max=self.mw.leCutWaveMax)
            plt.close(fig)
        except Exception as e: self.mw.statusBar().showMessage(f"Preview Error: {str(e)}", 4000)

    def _get_cut_time_params(self):
        min_str, max_str = self.mw.leCutTimeMin.text().strip(), self.mw.leCutTimeMax.text().strip()
        return {'mini': float(min_str) if min_str else None, 'maxi': float(max_str) if max_str else None}

    def _get_cut_wave_params(self):
        min_str, max_str = self.mw.leCutWaveMin.text().strip(), self.mw.leCutWaveMax.text().strip()
        mini = float(min_str) if min_str else None; maxi = float(max_str) if max_str else None
        return {'mini': mini, 'maxi': maxi, 'innerdata': self.mw.cbCutWaveInner.currentText().strip().lower() if mini is not None and maxi is not None else None}

    def _get_shift_time_params(self):
        val_str = self.mw.leShiftTime.text().strip()
        if not val_str: raise ValueError("Shift value cannot be empty.")
        return {'value': float(val_str)}

    def _get_baseline_sub_params(self):
        val_str = self.mw.leBaseSpec.text().strip()
        if not val_str: raise ValueError("Baseline spectra cannot be empty.")
        try: parts = [int(x.strip()) for x in val_str.split(',') if x.strip()]
        except ValueError: raise ValueError("Please enter whole numbers only (e.g., '5' or '2, 5').")
        if len(parts) == 1: number_spec = parts[0]
        elif len(parts) == 2: number_spec = parts
        else: raise ValueError("Enter either a single number or two numbers separated by a comma.")
        return {'number_spec': number_spec, 'only_one': self.mw.chkBaseOnlyOne.isChecked()}

    def _get_poly_baseline_params(self):
        pts_str = self.mw.lePolyBasePoints.text().strip()
        if not pts_str: raise ValueError("Must provide at least one zero point.")
        return {'points': [float(x.strip()) for x in pts_str.split(',')], 'order': self.mw.sbPolyBaseOrder.value()}

    def _get_average_time_params(self):
        start_str = self.mw.leAvgTimeStart.text().strip(); step_str = self.mw.leAvgTimeStep.text().strip()
        if not start_str or not step_str: raise ValueError("Start and Step cannot be empty.")
        return {'starting_point': float(start_str), 'step': float(step_str), 'method': self.mw.cbAvgTimeMethod.currentText().lower(), 'grid_dense': self.mw.sbAvgTimeGrid.value()}

    def _get_derivate_params(self):
        window = self.mw.sbDerivWindow.value()
        if window % 2 == 0: raise ValueError("Window length must be an odd number.")
        return {'window_length': window, 'polyorder': self.mw.sbDerivPoly.value(), 'deriv': self.mw.sbDerivOrder.value()}

    def _get_delete_points_params(self):
        pts_str = self.mw.leDeletePoints.text().strip()
        if not pts_str: raise ValueError("No points provided to delete.")
        return {'points': [float(x.strip()) for x in pts_str.split(',')], 'dimension': self.mw.cbDeleteDim.currentText().lower()}

    def _get_calibrate_wave_params(self):
        pix_str = self.mw.leCalibPixels.text().strip(); wave_str = self.mw.leCalibWaves.text().strip()
        if not pix_str or not wave_str: raise ValueError("Both Pixels and True Waves are required.")
        def parse_input(val_str):
            clean_str = val_str.replace('[', '').replace(']', '').strip()
            result = []
            matches = re.finditer(r"(-?\d+\.?\d*)\s*-\s*(-?\d+\.?\d*)|(-?\d+\.?\d*)", clean_str)
            for match in matches:
                if match.group(1) and match.group(2):
                    start, end = float(match.group(1)), float(match.group(2))
                    step = 1.0 if start <= end else -1.0
                    curr = start
                    if start <= end:
                        while curr <= end + 1e-9:
                            result.append(curr)
                            curr += step
                    else:
                        while curr >= end - 1e-9:
                            result.append(curr)
                            curr += step
                elif match.group(3):
                    result.append(float(match.group(3)))
            if not result: raise ValueError(f"Could not understand the input format: '{val_str}'")
            return result
        pixels = parse_input(pix_str); waves = parse_input(wave_str)
        if len(pixels) != len(waves): raise ValueError("Number of pixels must match number of waves.")
        order = self.mw.sbCalibOrder.value()
        if len(pixels) == 2 and order > 1: self.mw.sbCalibOrder.setValue(1); order = 1
        return {'pixels': pixels, 'wavelength': waves, 'order': order}

    def _get_chirp_polynomial_params(self):
        pts_str = self.mw.leChirpPoints.text().strip()
        if not pts_str: raise ValueError("Please click on the graph to pick points first.")
        pairs = [p.split(':') for p in pts_str.split(',') if ':' in p]
        x_pts = [float(p[0]) for p in pairs]; y_pts = [float(p[1]) for p in pairs]
        if len(x_pts) < 2: raise ValueError("Need at least 2 points for a polynomial fit.")
        return {'x_points': x_pts, 'y_points': y_pts}

    def _get_chirp_sellmeier_params(self):
        return {'excitation': self.mw.dsbChirpExc.value(), 'bk7': self.mw.dsbChirpBK7.value(), 'sio2': self.mw.dsbChirpSiO2.value(), 'caf2': self.mw.dsbChirpCaF2.value(), 'offset': self.mw.dsbChirpOffset.value()}

    def _get_correct_overlap_params(self):
        val_str = self.mw.leStitchPoint.text().strip()
        if not val_str: raise ValueError("Stitch point cannot be empty.")
        return {'stitch_point': float(val_str)}

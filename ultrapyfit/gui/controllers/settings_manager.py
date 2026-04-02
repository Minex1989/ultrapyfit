import numpy as np
from PySide6 import QtCore


class SettingsManager:
    def __init__(self, main_window):
        self.mw = main_window
        self.dataset_settings: dict[str, dict] = {}

    def _save_current_dataset_settings(self):
        item = self.mw.treeExperiment.currentItem()
        if item is None: return
        parent_item = item
        while parent_item.parent() is not None: parent_item = parent_item.parent()
        exp_id = parent_item.data(0, QtCore.Qt.UserRole)
        if not exp_id or isinstance(exp_id, dict): return
        spec_mode = 'all' if self.mw.rbAllSpectra.isChecked() else 'auto' if self.mw.rbAutomaticSpectra.isChecked() else 'custom'
        trace_mode = 'all' if self.mw.rbAllTrace.isChecked() else 'auto' if self.mw.rbAutomaticTrace.isChecked() else 'custom'
        global_fit_mode = 'svd' if self.mw.rbGlobalFitSvd.isChecked() else 'region' if self.mw.rbGlobalFitRegion.isChecked() else 'custom'
        settings = {
            'view_mode': self.mw.cbViewMode.currentIndex(),
            '3d_cmap': self.mw.cbColormaps3D.currentIndex(),
            '3d_style': self.mw.cbStyle3D.currentIndex(),
            '3d_resolution': self.mw.sbRenderQuality3D.value(),
            'spec_time_mode': spec_mode,
            'spec_num': self.mw.sbNumberOfSpectra.value(),
            'spec_at_wavelength_checkbox': self.mw.chkAtWavelengthSpectra.isChecked(),
            'spec_at_wavelength_num': self.mw.dsbAtWavelengthSpectra.value(),
            'spec_custom_times': self.mw.leCustomTimesSpectral.text(),
            'spec_time_range_checkbox': self.mw.chkTimeRangeSpectra.isChecked(),
            'spec_time_range_start': self.mw.dsbTimeRangeStartSpectra.value(),
            'spec_time_range_stop': self.mw.dsbTimeRangeStopSpectra.value(),
            'spec_from_max_to_min': self.mw.chkFromMaxToMinSpectra.isChecked(),
            'spec_average': self.mw.sbAverageSpectra.value(),
            'spec_mask_checkbox': self.mw.chkMaskRangeSpectra.isChecked(),
            'spec_mask_range_start': self.mw.dsbMaskRangeStartSpectra.value(),
            'spec_mask_range_stop': self.mw.dsbMaskRangeStopSpectra.value(),
            'spec_colormap': self.mw.cbColormapsSpectra.currentIndex(),
            'spec_style': self.mw.cbStyleSpectra.currentIndex(),
            'spec_legend': self.mw.cbLegendSpectra.currentIndex(),
            'trace_mode': trace_mode,
            'trace_custom_waves': self.mw.leCustomWavelengthTrace.text(),
            'trace_style': self.mw.cbStyleTrace.currentIndex(),
            'trace_legend': self.mw.cbLegendTrace.currentIndex(),
            'svd_calculated_components': self.mw.sbSvdCalcComps.value(),
            'svd_shown_spin_box_components': self.mw.sbSvdShowComps.value(),
            'svd_shown_slider_components': self.mw.sldSvdShowComps.value(),
            'svd_log_scale': self.mw.chkSvdLogScale.isChecked(),
            'fitting_type': self.mw.cbFittingType.currentIndex(),
            'global_fit_mode': global_fit_mode,
            'global_fit_svd_comps': self.mw.sbGlobalFitSvdComps.value(),
            'global_fit_region_min': self.mw.sbGlobalFitRegionMin.value(),
            'global_fit_region_max': self.mw.sbGlobalFitRegionMax.value(),
            'global_fit_traces': self.mw.leGlobalFitTraces.text(),
            'global_fit_average': self.mw.sbGlobalFitAverage.value(),
            'global_fit_masking': self.mw.leGlobalFitMasking.text(),
            'single_fit_trace': self.mw.sbSingleFitWave.value(),
            'single_fit_average': self.mw.sbSingleFitAverage.value(),
            'fitting_exp_num': self.mw.sbExpNo.value(),
            'fitting_fwhm': self.mw.dsbIRFw.value(),
            'fitting_t0': self.mw.dsbIRFmu.value(),
            'fitting_taus': self.mw.leInitialTau.text(),
            'fitting_inf_tau': self.mw.chkTauInf.isChecked(),
            'fitting_progress_log': self.mw.textFitLog.toPlainText(),
            'active_tab': self.mw.tabMain.currentIndex()
        }
        self.dataset_settings[exp_id] = settings

    def _load_dataset_settings(self):
        item = self.mw.treeExperiment.currentItem()
        if item is None: return
        parent_item = item
        while parent_item.parent() is not None: parent_item = parent_item.parent()
        exp_id = parent_item.data(0, QtCore.Qt.UserRole)
        if not exp_id or isinstance(exp_id, dict): return
        s = self.dataset_settings.get(exp_id, {})
        experiment = self.mw.experiment_manager.experiments[exp_id]
        data, wavelength = experiment.data, experiment.wavelength
        wave_idx = np.unravel_index(np.argmax(np.abs(data), axis=None), data.shape)[1]
        self.mw._is_loading_settings = True
        try:
            self.mw.cbViewMode.setCurrentIndex(s.get('view_mode', 0))
            self.mw.sbRenderQuality3D.setValue(s.get('3d_resolution', 1))
            self.mw.cbColormaps3D.setCurrentIndex(s.get('3d_cmap', 0))
            self.mw.cbStyle3D.setCurrentIndex(s.get('3d_style', 0))
            spec_mode = s.get('spec_time_mode', 'all')
            if spec_mode == 'all': self.mw.rbAllSpectra.setChecked(True)
            elif spec_mode == 'auto': self.mw.rbAutomaticSpectra.setChecked(True)
            else: self.mw.rbCustomSpectra.setChecked(True)
            self.mw.sbNumberOfSpectra.setValue(s.get('spec_num', 8))
            self.mw.chkAtWavelengthSpectra.setChecked(s.get('spec_at_wavelength_checkbox', False))
            self.mw.dsbAtWavelengthSpectra.setValue(s.get('spec_at_wavelength_num', wavelength[wave_idx]))
            self.mw.leCustomTimesSpectral.setText(s.get('spec_custom_times', ""))
            self.mw.chkTimeRangeSpectra.setChecked(s.get('spec_time_range_checkbox', False))
            self.mw.dsbTimeRangeStartSpectra.setValue(s.get('spec_time_range_start', experiment.time[0]))
            self.mw.dsbTimeRangeStopSpectra.setValue(s.get('spec_time_range_stop', experiment.time[-1]))
            self.mw.chkFromMaxToMinSpectra.setChecked(s.get('spec_from_max_to_min', False))
            self.mw.sbAverageSpectra.setValue(s.get('spec_average', 0))
            self.mw.chkMaskRangeSpectra.setChecked(s.get('spec_mask_checkbox', False))
            self.mw.dsbMaskRangeStartSpectra.setValue(s.get('spec_mask_range_start', 0))
            self.mw.dsbMaskRangeStopSpectra.setValue(s.get('spec_mask_range_stop', 0))
            self.mw.cbColormapsSpectra.setCurrentIndex(s.get('spec_colormap', 0))
            self.mw.cbStyleSpectra.setCurrentIndex(s.get('spec_style', 0))
            self.mw.cbLegendSpectra.setCurrentIndex(s.get('spec_legend', 0))
            trace_mode = s.get('trace_mode', 'all')
            if trace_mode == 'all': self.mw.rbAllTrace.setChecked(True)
            elif trace_mode == 'auto': self.mw.rbAutomaticTrace.setChecked(True)
            else: self.mw.rbCustomTrace.setChecked(True)
            self.mw.leCustomWavelengthTrace.setText(s.get('trace_custom_waves', ""))
            self.mw.cbStyleTrace.setCurrentIndex(s.get('trace_style', 0))
            self.mw.cbLegendTrace.setCurrentIndex(s.get('trace_legend', 0))
            self.mw.sbSvdCalcComps.setValue(s.get('svd_calculated_components', 15))
            self.mw.sbSvdShowComps.setValue(s.get('svd_shown_spin_box_components', 3))
            self.mw.sldSvdShowComps.setValue(s.get('svd_shown_slider_components', 3))
            self.mw.chkSvdLogScale.setChecked(s.get('svd_log_scale', False))
            self.mw.cbFittingType.setCurrentIndex(s.get('fitting_type', 0))
            global_fit_mode = s.get('global_fit_mode', 'svd')
            if global_fit_mode == 'svd': self.mw.rbGlobalFitSvd.setChecked(True)
            elif global_fit_mode == 'region': self.mw.rbGlobalFitRegion.setChecked(True)
            else: self.mw.rbGlobalFitTraces.setChecked(True)
            self.mw.sbGlobalFitSvdComps.setValue(s.get('global_fit_svd_comps', 3))
            self.mw.sbGlobalFitRegionMin.setValue(s.get('global_fit_region_min', wavelength[0]))
            self.mw.sbGlobalFitRegionMax.setValue(s.get('global_fit_region_max', wavelength[-1]))
            self.mw.leGlobalFitTraces.setText(s.get('global_fit_traces', ""))
            self.mw.sbGlobalFitAverage.setValue(s.get('global_fit_average', 0))
            self.mw.leGlobalFitMasking.setText(s.get('global_fit_masking', ""))
            self.mw.sbSingleFitWave.setValue(s.get('single_fit_trace', wavelength[wave_idx]))
            self.mw.sbSingleFitAverage.setValue(s.get('single_fit_average', 0))
            self.mw.sbExpNo.setValue(s.get('fitting_exp_num', 0))
            self.mw.dsbIRFw.setValue(s.get('fitting_fwhm', 0))
            self.mw.dsbIRFmu.setValue(s.get('fitting_t0', 0))
            self.mw.leInitialTau.setText(s.get('fitting_taus', ""))
            self.mw.chkTauInf.setChecked(s.get('fitting_inf_tau', False))
            self.mw.textFitLog.setText(s.get('fitting_progress_log', ""))
            self.mw.tabMain.setCurrentIndex(s.get('active_tab', 0))
        finally:
            self.mw._is_loading_settings = False
        self.mw.on_view_mode_changed()

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRegularExpression, QObject, Signal
from PySide6.QtGui import QRegularExpressionValidator, QDoubleValidator, QCloseEvent
from ultrapyfit.gui.ui.ui_main_window import Ui_MainWindow
from ultrapyfit.experiment import Experiment
from ultrapyfit.gui.controllers.experiment_manager import ExperimentManager
from ultrapyfit.gui.controllers.plot_controller import PlotController
from ultrapyfit.gui.controllers.preprocessing_controller import PreprocessingController
from ultrapyfit.gui.controllers.fitting_controller import FittingController
from ultrapyfit.gui.controllers.settings_manager import SettingsManager
from ultrapyfit.gui.controllers.svd_controller import SVDController


class EmittingStream(QObject):
    text_written = Signal(str)

    def write(self, text):
        self.text_written.emit(text)

    def flush(self):
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Initialize Controllers
        self.settings_manager = SettingsManager(self)
        self.experiment_manager = ExperimentManager(self)
        self.svd_controller = SVDController(self)
        self.plot_controller = PlotController(self)
        self.preprocessing_controller = PreprocessingController(self)
        self.fitting_controller = FittingController(self)

        self.import_dialog = None
        self._scroll_cid = None
        self._cursor = None
        self._cid_move = None
        self._cid_click = None
        self._chirp_click_cid = None
        self._active_span_selector = None
        
        self.setupUi(self)
        self._setup_connections()
        self._is_fitting = False
        self._set_workspace_mode(False)
        
        # Setup Validators
        regex_list = QRegularExpression(r"^[0-9\.\s,]+$")
        positive_float_validator = QRegularExpressionValidator(regex_list)
        float_validator = QDoubleValidator()
        float_validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        
        update_positive_float_validators = [
            self.leGlobalFitTraces, self.leInitialTau, self.leCustomTimesSpectral,
            self.leCustomWavelengthTrace, self.leGlobalKineticsSel, self.leCutWaveMin,
            self.leCutWaveMax, self.lePolyBasePoints, self.leAvgTimeStart,
            self.leAvgTimeStep, self.leDeletePoints, self.leCalibPixels, self.leCalibWaves,
            self.leStitchPoint
        ]
        for line_edit in update_positive_float_validators:
            line_edit.setValidator(positive_float_validator)
            
        update_float_validators = [self.leCutTimeMin, self.leCutTimeMax, self.leShiftTime]
        for line_edit in update_float_validators:
            line_edit.setValidator(float_validator)
            
        regex_mask = QRegularExpression(r"[0-9\.\s\-,]+")
        range_validator = QRegularExpressionValidator(regex_mask)
        self.leGlobalFitMasking.setValidator(range_validator)
        self.leCalibWaves.setValidator(range_validator)
        self.leCalibPixels.setValidator(range_validator)
        
        # Redirect stdout
        self.stdout_redirector = EmittingStream()
        self.stdout_redirector.text_written.connect(self.append_fit_log)
        
        # Tree Context Menu
        self.treeExperiment.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeExperiment.customContextMenuRequested.connect(self.show_tree_context_menu)

        # Style Dictionaries
        self.viewStyleDict3D = {"Surface": "surface", "Wireframe": "wireframe", "Contour": "contour"}
        self.viewStyleDictSpectral = {
            "Ultrapyfit bright": "lmu_spec", "Ultrapyfit dark": "lmu_specd", "Default": "default",
            "Seaborn white grid": "seaborn-v0_8-whitegrid", "Seaborn dark grid": "seaborn-v0_8-darkgrid",
            "Dark background": "dark_background", "ggplot": "ggplot"
        }
        self.viewStyleDictTrace = {
            "Ultrapyfit bright": "lmu_trac", "Ultrapyfit dark": "lmu_tracd", "Default": "default",
            "Seaborn white grid": "seaborn-v0_8-whitegrid", "Seaborn dark grid": "seaborn-v0_8-darkgrid",
            "Dark background": "dark_background", "ggplot": "ggplot"
        }
        
        self._is_loading_settings = False
        self.experiments = self.experiment_manager.experiments
        self.dataset_settings = self.settings_manager.dataset_settings

    def _setup_connections(self):
        self.actImport.triggered.connect(self.experiment_manager.open_import_dialog)
        self.actSave.triggered.connect(self.experiment_manager.save_experiment)
        self.actLoad.triggered.connect(self.experiment_manager.load_experiment)
        self.treeExperiment.currentItemChanged.connect(self.experiment_manager.on_tree_selection_changed)
        self.tabMain.currentChanged.connect(self.on_tab_changed)
        self.cbViewMode.currentIndexChanged.connect(self.on_view_mode_changed)
        self.btnExportPlot.clicked.connect(self.plot_controller.export_plot)
        self.btnResetView3D.clicked.connect(self.plot_controller.reset_3d_camera)
        self.btnRunFit.clicked.connect(self.fitting_controller.handle_fit_button_click)
        self.cbPreprocessingTool.currentIndexChanged.connect(self.preprocessing_controller.on_preprocess_tool_changed)
        self.btnApplyPreprocess.released.connect(self.preprocessing_controller.apply_preprocessing)
        self.btnUndoPreprocess.released.connect(self.preprocessing_controller.undo_preprocessing)
        self.listPreprocessHistory.itemDoubleClicked.connect(self.preprocessing_controller.on_history_double_clicked)

        # Plot Triggers
        update_3D_plot_triggers = [self.cbColormaps3D.currentIndexChanged, self.sbRenderQuality3D.valueChanged, self.cbStyle3D.currentIndexChanged]
        for signal in update_3D_plot_triggers: signal.connect(self.plot_controller.plot_current_data_3D)

        update_spectral_plot_triggers = [
            self.rbAllSpectra.toggled, self.rbAutomaticSpectra.toggled, self.sbNumberOfSpectra.valueChanged,
            self.chkAtWavelengthSpectra.toggled, self.dsbAtWavelengthSpectra.valueChanged, self.leCustomTimesSpectral.editingFinished,
            self.chkTimeRangeSpectra.toggled, self.dsbTimeRangeStartSpectra.valueChanged, self.dsbTimeRangeStopSpectra.valueChanged,
            self.chkFromMaxToMinSpectra.toggled, self.sbAverageSpectra.valueChanged, self.chkMaskRangeSpectra.toggled,
            self.dsbMaskRangeStartSpectra.valueChanged, self.dsbMaskRangeStopSpectra.valueChanged, self.cbColormapsSpectra.currentIndexChanged,
            self.cbLegendSpectra.currentIndexChanged, self.cbStyleSpectra.currentIndexChanged
        ]
        for signal in update_spectral_plot_triggers: signal.connect(self.plot_controller.plot_current_data_spectrum)

        update_trace_plot_triggers = [
            self.rbAllTrace.toggled, self.rbAutomaticTrace.toggled, self.rbCustomTrace.toggled,
            self.leCustomWavelengthTrace.editingFinished, self.cbStyleTrace.currentIndexChanged, self.cbLegendTrace.currentIndexChanged
        ]
        for signal in update_trace_plot_triggers: signal.connect(self.plot_controller.plot_current_data_traces)

        self.sbSvdCalcComps.valueChanged.connect(self.svd_controller.update_svd_math)
        update_svd_plot_triggers = [self.sbSvdShowComps.valueChanged, self.chkSvdLogScale.stateChanged]
        for signal in update_svd_plot_triggers: signal.connect(self.plot_controller.plot_current_data_svd)

        update_fitting_preview_plot_trigger = [
            self.cbFittingType.currentIndexChanged, self.rbGlobalFitSvd.toggled, self.rbGlobalFitRegion.toggled,
            self.rbGlobalFitTraces.toggled, self.sbGlobalFitSvdComps.valueChanged, self.sbGlobalFitRegionMin.valueChanged,
            self.sbGlobalFitRegionMax.valueChanged, self.leGlobalFitTraces.editingFinished, self.sbGlobalFitAverage.valueChanged,
            self.leGlobalFitMasking.editingFinished, self.sbSingleFitWave.valueChanged, self.sbSingleFitAverage.valueChanged
        ]
        for signal in update_fitting_preview_plot_trigger: signal.connect(self.plot_controller.plot_current_data_fit_preview)

        self.cbGlobalViewMode.currentIndexChanged.connect(self._route_stacked_settings)
        update_global_fit_plot_trigger = [self.cbGlobalViewMode.currentIndexChanged, self.chkConvertToEAS.toggled, self.leGlobalKineticsSel.editingFinished]
        for signal in update_global_fit_plot_trigger: signal.connect(self.plot_controller.plot_current_data_global_fit)
        
        self.chkSingleDetails.stateChanged.connect(self.plot_controller.plot_current_data_single_fit)
        self.cbDeleteDim.currentIndexChanged.connect(self.preprocessing_controller.plot_preprocessing_preview)

    def _enable_controls(self, state: bool = True):
        controls = [
            self.cbViewMode, self.cbColormaps3D, self.cbStyle3D, self.sbRenderQuality3D, self.btnResetView3D,
            self.btnExportPlot, self.sbSvdCalcComps, self.sbSvdShowComps, self.sldSvdShowComps, self.chkSvdLogScale,
            self.cbFittingType, self.rbGlobalFitSvd, self.rbGlobalFitRegion, self.rbGlobalFitTraces, self.sbGlobalFitSvdComps,
            self.sbExpNo, self.dsbIRFw, self.dsbIRFmu, self.leInitialTau, self.chkTauInf, self.btnRunFit,
            self.cbPreprocessingTool, self.leCutTimeMin, self.leCutTimeMax, self.btnApplyPreprocess,
            self.btnUndoPreprocess, self.listPreprocessHistory
        ]
        for control in controls: control.setEnabled(state)

    def append_fit_log(self, text):
        if text.strip():
            self.textFitLog.append(text.strip())
            QtWidgets.QApplication.processEvents()

    def show_tree_context_menu(self, position):
        item = self.treeExperiment.itemAt(position)
        if not item: return
        node_data = item.data(0, Qt.UserRole)
        if node_data is None: return
        menu = QtWidgets.QMenu(self)
        if isinstance(node_data, dict) and node_data.get('type') == 'fit_result':
            action = menu.addAction("Delete Fit")
            if menu.exec(self.treeExperiment.viewport().mapToGlobal(position)) == action:
                self.delete_fit_node(item, node_data)
        else:
            action = menu.addAction("Close Experiment")
            if menu.exec(self.treeExperiment.viewport().mapToGlobal(position)) == action:
                self.experiment_manager.close_experiment_node(item)

    def delete_fit_node(self, item, node_data):
        experiment = self.get_experiment()
        reply = QtWidgets.QMessageBox.question(self, 'Confirm deletion', 'Are you sure you want to delete this fit?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            fit_cat, fit_num = node_data.get('fit_category'), node_data.get('fit_number')
            try:
                if fit_cat == 'global': del experiment.fitting.fit_records.global_fits[fit_num]
                elif fit_cat == 'single': del experiment.fitting.fit_records.single_fits[fit_num]
            except KeyError: pass
            parent = item.parent()
            if parent: parent.removeChild(item)

    def get_experiment(self) -> Experiment:
        return self.experiment_manager.get_experiment()

    def _set_workspace_mode(self, show_results: bool):
        for page, visible in [(self.pagePreprocessing, not show_results), (self.pageDataExplorer, not show_results), (self.pageSvd, not show_results), (self.pageFitting, not show_results), (self.pageResults, show_results)]:
            idx = self.tabMain.indexOf(page)
            if idx != -1: self.tabMain.setTabVisible(idx, visible)

    def on_tab_changed(self, index):
        if index == 0: self.preprocessing_controller.plot_preprocessing_preview()
        elif index == 1:
            vm = self.cbViewMode.currentIndex()
            if vm == 0: self.plot_controller.plot_current_data_3D()
            elif vm == 1: self.plot_controller.plot_current_data_spectrum()
            elif vm == 2: self.plot_controller.plot_current_data_traces()
        elif index == 2: self.plot_controller.plot_current_data_svd()
        elif index == 3: self.plot_controller.plot_current_data_fit_preview()

    def on_view_mode_changed(self):
        index = self.cbViewMode.currentIndex(); self.stackedViewModeOptions.setCurrentIndex(index)
        if self.treeExperiment.currentItem() is None:
            self.plot_controller._clear_plot_with_message(self.mplWidget, "No experiments loaded.")
            return
        heights = {0: 61, 1: 211, 2: 151}
        h = heights.get(index, 61)
        self.stackedViewModeOptions.setMaximumHeight(h); self.stackedViewModeOptions.setMinimumHeight(h)
        if index == 0: self.plot_controller.plot_current_data_3D()
        elif index == 1: self.plot_controller.plot_current_data_spectrum()
        elif index == 2: self.plot_controller.plot_current_data_traces()

    def _route_stacked_settings(self, index):
        self.stackedGlobalSettings.setCurrentIndex(0 if index == 0 else 1)

    def _save_current_dataset_settings(self):
        self.settings_manager._save_current_dataset_settings()

    def _load_dataset_settings(self):
        self.settings_manager._load_dataset_settings()

    def closeEvent(self, event: QCloseEvent):
        """
        Intercepts the close event to ask for confirmation if not saved.
        """
        reply = QtWidgets.QMessageBox.question(
            self,
            "Confirm closing",
            "Are you sure you want to close it?\nAny unsaved changes will be lost.",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
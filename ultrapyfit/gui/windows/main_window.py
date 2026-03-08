from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRegularExpression, QObject, Signal
from PySide6.QtGui import QRegularExpressionValidator
from ultrapyfit.gui.ui.ui_main_window import Ui_MainWindow
from ultrapyfit.gui.windows.import_dialog import ImportDialog
from ultrapyfit.experiment import Experiment
from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor
from typing import Any
import numpy as np
import uuid
import sys
import re
from pathlib import Path


class EmittingStream(QObject):
    text_written = Signal(str)

    def write(self, text):
        self.text_written.emit(text)

    def flush(self):
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.import_dialog = None
        self._scroll_cid = None
        self._cursor = None
        self._cid_move = None
        self._cid_click = None
        self.setupUi(self)
        self._setup_connections()
        self._is_fitting = False

        regex_list = QRegularExpression(r"^[0-9\.\s,]+$")
        validator_list = QRegularExpressionValidator(regex_list)
        self.leGlobalFitTraces.setValidator(validator_list)
        self.leInitialTau.setValidator(validator_list)
        self.leCustomTimesSpectral.setValidator(validator_list)
        self.leCustomWavelengthTrace.setValidator(validator_list)
        regex_mask = QRegularExpression(r"[0-9\.\s\-,]+")
        validator = QRegularExpressionValidator(regex_mask)
        self.leGlobalFitMasking.setValidator(validator)
        self.stdout_redirector = EmittingStream()
        self.stdout_redirector.text_written.connect(self.append_fit_log)

        self.viewStyleDict3D = {"Felület": "surface",
                                "Vázlat": "wireframe",
                                "Kontúr": "contour"}
        self.viewStyleDictSpectral = {"Ultrapyfit világos": "lmu_spec",
                                      "Ultrapyfit sötét": "lmu_specd",
                                      "Alapértelmezett": "default",
                                      "Seaborn világos rács": "seaborn-v0_8-whitegrid",
                                      "Seaborn sötét rács": "seaborn-v0_8-darkgrid",
                                      "Sötét háttér": "dark_background",
                                      "ggplot": "ggplot"}
        self.viewStyleDictTrace = {"Ultrapyfit világos": "lmu_trac",
                                   "Ultrapyfit sötét": "lmu_tracd",
                                   "Alapértelmezett": "default",
                                   "Seaborn világos rács": "seaborn-v0_8-whitegrid",
                                   "Seaborn sötét rács": "seaborn-v0_8-darkgrid",
                                   "Sötét háttér": "dark_background",
                                   "ggplot": "ggplot"}
        # A dictionary to map TreeItems back to actual Python Objects
        # Format: { QTreeWidgetItem_ID : Experiment_Object }
        self._is_loading_settings = False
        self.experiments: dict[str, Experiment] = {}
        self.dataset_settings: dict[str, dict[str, Any]] = {}

    def _setup_connections(self):
        self.actImport.triggered.connect(self.open_import_dialog)
        self.treeExperiment.itemClicked.connect(self.on_tree_click)
        self.tabMain.currentChanged.connect(self.on_tab_changed)
        self.cbViewMode.currentIndexChanged.connect(self.on_view_mode_changed)
        self.btnExportPlot.clicked.connect(self.export_plot)
        self.btnResetView3D.clicked.connect(self.reset_3d_camera)
        self.btnRunFit.clicked.connect(self.handle_fit_button_click)

        update_3D_plot_triggers = [
            self.cbColormaps3D.currentIndexChanged,
            self.sbRenderQuality3D.valueChanged,
            self.cbStyle3D.currentIndexChanged
        ]
        for signal in update_3D_plot_triggers:
            signal.connect(self.plot_current_data_3D)

        update_spectral_plot_triggers = [
            self.rbAllSpectra.toggled,
            self.rbAutomaticSpectra.toggled,
            self.sbNumberOfSpectra.valueChanged,
            self.chkAtWavelengthSpectra.toggled,
            self.dsbAtWavelengthSpectra.valueChanged,
            self.leCustomTimesSpectral.editingFinished,
            self.chkTimeRangeSpectra.toggled,
            self.dsbTimeRangeStartSpectra.valueChanged,
            self.dsbTimeRangeStopSpectra.valueChanged,
            self.chkFromMaxToMinSpectra.toggled,
            self.sbAverageSpectra.valueChanged,
            self.chkMaskRangeSpectra.toggled,
            self.dsbMaskRangeStartSpectra.valueChanged,
            self.dsbMaskRangeStopSpectra.valueChanged,
            self.cbColormapsSpectra.currentIndexChanged,
            self.cbLegendSpectra.currentIndexChanged,
            self.cbStyleSpectra.currentIndexChanged
        ]
        for signal in update_spectral_plot_triggers:
            signal.connect(self.plot_current_data_spectrum)

        update_trace_plot_triggers = [
            self.rbAllTrace.toggled,
            self.rbAutomaticTrace.toggled,
            self.rbCustomTrace.toggled,
            self.leCustomWavelengthTrace.editingFinished,
            self.cbStyleTrace.currentIndexChanged,
            self.cbLegendTrace.currentIndexChanged
        ]
        for signal in update_trace_plot_triggers:
            signal.connect(self.plot_current_data_traces)
        self.sbSvdCalcComps.valueChanged.connect(self.update_svd_math)

        update_svd_plot_triggers = [
            self.sbSvdShowComps.valueChanged,
            self.chkSvdLogScale.stateChanged
        ]
        for signal in update_svd_plot_triggers:
            signal.connect(self.plot_current_data_svd)

        update_fitting_preview_plot_trigger = [
            self.cbFittingType.currentIndexChanged,
            self.rbGlobalFitSvd.toggled,
            self.rbGlobalFitRegion.toggled,
            self.rbGlobalFitTraces.toggled,
            self.sbGlobalFitSvdComps.valueChanged,
            self.sbGlobalFitRegionMin.valueChanged,
            self.sbGlobalFitRegionMax.valueChanged,
            self.leGlobalFitTraces.editingFinished,
            self.sbGlobalFitAverage.valueChanged,
            self.leGlobalFitMasking.editingFinished,
            self.sbSingleFitWave.valueChanged,
            self.sbSingleFitAverage.valueChanged
        ]
        for signal in update_fitting_preview_plot_trigger:
            signal.connect(self.plot_current_data_fit_preview)

    def _enable_controls(self):
        self.cbViewMode.setEnabled(True)
        self.cbColormaps3D.setEnabled(True)
        self.cbStyle3D.setEnabled(True)
        self.sbRenderQuality3D.setEnabled(True)
        self.btnResetView3D.setEnabled(True)
        self.btnExportPlot.setEnabled(True)
        self.sbSvdCalcComps.setEnabled(True)
        self.sbSvdShowComps.setEnabled(True)
        self.sldSvdShowComps.setEnabled(True)
        self.chkSvdLogScale.setEnabled(True)
        self.cbFittingType.setEnabled(True)
        self.rbGlobalFitSvd.setEnabled(True)
        self.rbGlobalFitRegion.setEnabled(True)
        self.rbGlobalFitTraces.setEnabled(True)
        self.sbGlobalFitSvdComps.setEnabled(True)
        self.sbExpNo.setEnabled(True)
        self.dsbIRFw.setEnabled(True)
        self.dsbIRFmu.setEnabled(True)
        self.leInitialTau.setEnabled(True)
        self.chkTauInf.setEnabled(True)
        self.btnRunFit.setEnabled(True)

    def append_fit_log(self, text):
        """Appends intercepted console print statements to the GUI."""
        # Optional: Filter out empty newlines if you want it cleaner
        if text.strip():
            self.textFitLog.append(text.strip())
            QtWidgets.QApplication.processEvents()

    def open_import_dialog(self):
        """Open the parameter dialog and connect to its signals"""
        self.import_dialog = ImportDialog(self)

        # Connect to the dialog's signals
        self.import_dialog.parameters_accepted.connect(self.on_experiment_received)

        # Show the dialog (non-blocking with signals approach)
        self.import_dialog.exec()

    def on_experiment_received(self, imported_experiment: Experiment) -> None:
        """Slot called when parameters_accepted signal is emitted"""
        experiment = imported_experiment
        self.add_experiment(experiment)
        # Optional: Close the dialog if it's still open
        if self.import_dialog.isVisible():
            self.import_dialog.close()

    def add_experiment(self, experiment_obj: Experiment):
        """Called when Import Window finishes."""

        # 1. Generate a unique ID for this new experiment
        # This ensures that even if you load the same file twice, they don't clash
        exp_id = str(uuid.uuid4())

        # 2. Store the OBJECT in your dictionary
        self.experiments[exp_id] = experiment_obj

        # 3. Create the Root Item for the Tree
        root_item = QtWidgets.QTreeWidgetItem(self.treeExperiment)
        root_item.setText(0, experiment_obj._data_path.split("/")[-1])
        root_item.setExpanded(True)

        # 4. Store ONLY THE ID in the GUI Item
        # Qt.UserRole is a hidden slot for data
        root_item.setData(0, Qt.UserRole, exp_id)

        # 4. Select the new item
        self.treeExperiment.setCurrentItem(root_item)
        self.dataset_settings[exp_id] = {}
        self._load_dataset_settings()
        self.plot_current_data_3D()
        self._enable_controls()
        self.stackedViewModeOptions.setCurrentIndex(0)
        self.cbViewMode.setCurrentIndex(0)

    def on_tree_click(self, item):
        """
        Retrieves the experiment object from the dictionary based on the clicked item.
        """
        # 1. Determine if we clicked a Root or a Child
        parent = item.parent()

        if parent is None:
            # We clicked the Root (The Experiment Name)
            exp_id = item.data(0, Qt.UserRole)
            target_experiment = self.experiments.get(exp_id)

            if target_experiment:
                print(f"Selected Experiment: {target_experiment.describe_data()}")
                self._load_dataset_settings()
                if self.cbViewMode.currentIndex() == 0:
                    self.plot_current_data_3D()
                elif self.cbViewMode.currentIndex() == 1:
                    self.plot_current_data_spectrum()
                elif self.cbViewMode.currentIndex() == 2:
                    self.plot_current_data_traces()
        else:
            # We clicked a Child (Raw Data, SVD, etc.)
            # We must get the ID from the PARENT
            exp_id = parent.data(0, Qt.UserRole)
            target_experiment = self.experiments.get(exp_id)
            node_type = item.text(0)

            if target_experiment:
                if node_type == "Raw Data":
                    # self.plot_raw(target_experiment)
                    pass
                elif node_type == "SVD Analysis":
                    # self.plot_svd(target_experiment)
                    pass

    def get_experiment(self) -> Experiment:
        item = self.treeExperiment.currentItem()
        exp_id = item.data(0, Qt.UserRole)
        experiment = self.experiments.get(exp_id)
        return experiment

    def on_tab_changed(self, index):
        """
        Triggered whenever the user switches tabs in the main area.
        """
        # Option A: Check by Index (Assuming Data Explorer is 0, SVD is 1)
        if index == 0:
            if self.cbViewMode.currentIndex() == 0:
                self.plot_current_data_3D()
            elif self.cbViewMode.currentIndex() == 1:
                self.plot_current_data_spectrum()
            elif self.cbViewMode.currentIndex() == 2:
                self.plot_current_data_traces()
        elif index == 1:
            self.plot_current_data_svd()
        elif index == 2:
            self.plot_current_data_fit_preview()

    def export_plot(self):
        # 1. Define your supported formats using the standard Qt filter syntax
        # Format: "Description (*.ext1 *.ext2);;Next Description (*.ext3)"
        file_filters = (
            "Portable Document Format (*.pdf);;"
            "Scalable Vector Graphics (*.svg);;"
            "Portable Network Graphics (*.png);;"
            "Encapsulated PostScript (*.eps);;"
            "Tagged Image File Format (*.tif);;"
            "All Files (*)"
        )

        # 2. Open the save file dialog
        # Returns a tuple: (file_path: str, selected_filter: str)
        file_path, selected_filter = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Export Plot As",
            "",  # Default directory (empty means current/last used)
            file_filters
        )

        # 3. Handle cancellation
        if not file_path:
            print("Export cancelled by user.")
            return
        self.statusbar.showMessage(f"Exporting to {file_path}...")
        # 4. Determine the file extension
        # Method A: Try to get the extension directly from the user's input
        path_obj = Path(file_path)
        extension = path_obj.suffix.lower()

        # Method B: Fallback if the user typed "my_plot" without an extension
        # Some OS native dialogs auto-append the extension, some do not.
        if not extension and selected_filter != "All Files (*)":
            # Use regex to extract the extension from strings like "Portable Document Format (*.pdf)"
            match = re.search(r'\*\.([a-zA-Z0-9]+)', selected_filter)
            if match:
                extension = f".{match.group(1).lower()}"
                # Append the extension to the file path so we save it correctly
                file_path += extension

        # 5. Pass the complete file path directly to matplotlib
        # Matplotlib's savefig() infers the format directly from the file extension
        self.save_matplotlib_figure(file_path)
        self.statusbar.showMessage(f"Successfully exported: {file_path}", 5000)

    def save_matplotlib_figure(self, path):
        """Passes the path to matplotlib, which handles formatting automatically."""
        experiment = self.get_experiment()
        if self.cbViewMode.currentIndex() == 0:
            current_fig = self.mplWidget.canvas.figure
            old_ax = current_fig.axes[0]
            saved_state = {
                'elev': old_ax.elev,
                'azim': old_ax.azim,
                'roll': getattr(old_ax, 'roll', 0),
                'zoom_level': getattr(old_ax, '_custom_zoom_level', 0.85)
            }
            cmap, stride, plot_type = self.get_3D_options()
            plot_type = self.viewStyleDict3D.get(plot_type)
            fig, ax = experiment.plot_3D(cmap=cmap, figsize=(8, 6), plot_type=plot_type, stride=stride,
                                         azim=old_ax.azim, elev=old_ax.elev)
            ax.view_init(
                elev=saved_state['elev'],
                azim=saved_state['azim'],
                roll=saved_state['roll']
            )
            ax._custom_zoom_level = saved_state['zoom_level']
            current_aspect = ax.get_box_aspect()
            ax.set_box_aspect(current_aspect, zoom=saved_state['zoom_level'])
        elif self.cbViewMode.currentIndex() == 1:
            times_arg, rango_arg, cover_arg, legend_arg = self.get_spectrum_options()
            style = self.viewStyleDictSpectral.get(self.cbStyleSpectra.currentText())
            if style == "lmu_spec_gui":
                style = "lmu_spec"
            elif style == "lmu_specd_gui":
                style = "lmu_specd"
            fig, ax = experiment.plot_spectra(
                times=times_arg,
                rango=rango_arg,
                average=self.sbAverageSpectra.value(),
                cover_range=cover_arg,
                from_max_to_min=self.chkFromMaxToMinSpectra.isChecked(),
                legend=legend_arg,
                cmap=self.cbColormapsSpectra.currentText().lower() or None,
                style=style,
            )
        else:
            traces_val, legend_val, style_val = self.get_trace_options()
            if style_val == "lmu_trac_gui":
                style_val = "lmu_trac"
            elif style_val == "lmu_tracd_gui":
                style_val = "lmu_tracd"
            fig, ax = experiment.plot_traces(traces=traces_val, style=style_val, legend=legend_val)
        fig.savefig(path, dpi=600, bbox_inches='tight', pad_inches=0.05, transparent=False, facecolor='w',
                    edgecolor='w')
        plt.close(fig)

    def reset_3d_camera(self):
        """
        Triggered by the Reset Camera button.
        Forces the 3D view to redraw from scratch, clearing zoom and rotation.
        """
        if self.treeExperiment.currentItem() is None:
            return

        print("Resetting 3D camera to default view...")
        # Call our update function, but pass a flag telling it to ignore saved state
        self.plot_current_data_3D(reset_camera=True)

    def plot_current_data_3D(self, *args, reset_camera=False):
        if self.treeExperiment.currentItem() is None:
            return
        if getattr(self, '_is_loading_settings', False):
            return
        saved_state = None
        current_elev = 30
        current_azim = -60
        experiment = self.get_experiment()
        current_fig = self.mplWidget.canvas.figure
        if not reset_camera and current_fig.axes:
            old_ax = current_fig.axes[0]
            if hasattr(old_ax, 'elev') and hasattr(old_ax, 'azim'):
                saved_state = {
                    'elev': old_ax.elev,
                    'azim': old_ax.azim,
                    'roll': getattr(old_ax, 'roll', 0),
                    'zoom_level': getattr(old_ax, '_custom_zoom_level', 0.85)
                }
        cmap, stride, plot_type = self.get_3D_options()
        plot_type = self.viewStyleDict3D.get(plot_type)
        fig, ax = experiment.plot_3D(cmap=cmap, plot_type=plot_type, stride=stride, azim=current_azim,
                                     elev=current_elev)
        if saved_state:
            ax.view_init(
                elev=saved_state['elev'],
                azim=saved_state['azim'],
                roll=saved_state['roll']
            )
            ax._custom_zoom_level = saved_state['zoom_level']
            current_aspect = ax.get_box_aspect()
            ax.set_box_aspect(current_aspect, zoom=saved_state['zoom_level'])
        self.enable_scroll_zoom(ax)
        self.mplWidget.update_figure(fig)
        plt.close(fig)
        self._save_current_dataset_settings()

    def get_3D_options(self):
        return self.cbColormaps3D.currentText().lower(), 11 - self.sbRenderQuality3D.value(), self.cbStyle3D.currentText()

    def plot_current_data_spectrum(self):
        if self.treeExperiment.currentItem() is None:
            return
        if getattr(self, '_is_loading_settings', False):
            return
        experiment = self.get_experiment()
        times_arg, rango_arg, cover_arg, legend_arg = self.get_spectrum_options()
        fig, ax = experiment.plot_spectra(
            times=times_arg,
            rango=rango_arg,
            average=self.sbAverageSpectra.value(),
            cover_range=cover_arg,
            from_max_to_min=self.chkFromMaxToMinSpectra.isChecked(),
            legend=legend_arg,
            cmap=self.cbColormapsSpectra.currentText().lower() or None,
            style=self.viewStyleDictSpectral.get(self.cbStyleSpectra.currentText()),
        )
        self.enable_interactive_features(fig, ax, experiment.wavelength, target_lineedit=self.leCustomWavelengthTrace)
        fig.tight_layout()
        self.mplWidget.update_figure(fig)
        plt.close(fig)
        self._save_current_dataset_settings()

    def get_spectrum_options(self):
        times_arg = 'all'
        if self.rbAutomaticSpectra.isChecked():
            n_spec = self.sbNumberOfSpectra.value()
            if self.chkAtWavelengthSpectra.isChecked():
                wl = self.dsbAtWavelengthSpectra.value()
                times_arg = ["auto", n_spec, wl]
            else:
                times_arg = ["auto", n_spec]

        elif self.rbCustomSpectra.isChecked():
            text = self.leCustomTimesSpectral.text()
            try:
                times_arg = [float(x.strip()) for x in text.split(',') if x.strip()]
            except ValueError:
                times_arg = 'auto'

        rango_arg = None
        if self.chkTimeRangeSpectra.isChecked():
            rango_arg = [self.dsbTimeRangeStartSpectra.value(), self.dsbTimeRangeStopSpectra.value()]

        cover_arg = None
        if self.chkMaskRangeSpectra.isChecked():
            cover_arg = [self.dsbMaskRangeStartSpectra.value(),
                         self.dsbMaskRangeStopSpectra.value()]

        index = self.cbLegendSpectra.currentIndex()
        if index == 0:
            legend_arg = True
        elif index == 1:
            legend_arg = "bar"
        else:
            legend_arg = False
        return times_arg, rango_arg, cover_arg, legend_arg

    def plot_current_data_traces(self):
        if self.treeExperiment.currentItem() is None:
            return
        if getattr(self, '_is_loading_settings', False):
            return
        experiment = self.get_experiment()
        traces_val, legend_val, style_val = self.get_trace_options()
        fig, ax = experiment.plot_traces(traces=traces_val,
                                         style=style_val,
                                         legend=legend_val)
        self.enable_interactive_features(fig, ax, experiment.time, target_lineedit=self.leCustomTimesSpectral)
        fig.tight_layout()
        self.mplWidget.update_figure(fig)
        plt.close(fig)
        self._save_current_dataset_settings()

    def get_trace_options(self):
        """
        Collects, parses, and formats all GUI inputs from the Traces Settings page.
        Returns a dictionary of keyword arguments ready for plot_traces().
        """
        experiment = self.get_experiment()
        if self.rbAllTrace.isChecked():
            traces_val = experiment.wavelength.tolist()
        elif self.rbAutomaticTrace.isChecked():
            traces_val = "auto"
        else:
            raw_text = self.leCustomWavelengthTrace.text()
            clean_text = raw_text.replace(';', ',')
            try:
                traces_val = [float(x.strip()) for x in clean_text.split(',') if x.strip()]
                if not traces_val:
                    traces_val = "auto"
            except ValueError:
                print("Warning: Nem megfelelő formátum (Invalid format). Falling back to 'select'.")
                traces_val = "auto"
        legend_text = self.cbLegendTrace.currentText()
        if legend_text == "Mindig látható":
            legend_val = True
        elif legend_text == "Elrejtve":
            legend_val = False
        else:
            legend_val = 'auto'
        style_text = self.cbStyleTrace.currentText()
        style_val = self.viewStyleDictTrace.get(style_text)
        return traces_val, legend_val, style_val

    def update_svd_math(self):
        """
        Gathers parameters, calculates the SVD matrices, and triggers a redraw.
        Linked to: spinCalcComps.editingFinished
        """
        if self.treeExperiment.currentItem() is None:
            return
        if getattr(self, '_is_loading_settings', False):
            return
        experiment = self.get_experiment()
        calc_comps, show_comps, log_scale = self.get_svd_parameters()

        # 1. Do the heavy math
        experiment.calculate_svd(n_components=calc_comps)

        # 2. Forward to the plotting function
        self.plot_current_data_svd()

    def plot_current_data_svd(self):
        if self.treeExperiment.currentItem() is None:
            return
        if getattr(self, '_is_loading_settings', False):
            return
        experiment = self.get_experiment()

        calc_comps, show_comps, log_scale = self.get_svd_parameters()

        if not hasattr(experiment, '_S') or experiment._S is None or len(experiment._S) < show_comps:
            self.update_svd_math()
            return  # update_svd_math will call this function again, so we stop here.

        # 1. Get the figure from the experiment object
        fig, axes = experiment.plot_full_svd(
            components=show_comps,
            log_scale=log_scale
        )
        fig.tight_layout()
        self.svdMplWidget.update_figure(fig)
        # 3. Clean up memory
        plt.close(fig)
        self._save_current_dataset_settings()

    def get_svd_parameters(self):
        """
        Reads and returns all current user inputs from the SVD tab.
        """
        # Read raw values from the Qt widgets
        calc_comps = self.sbSvdCalcComps.value()
        show_comps = self.sldSvdShowComps.value()
        log_scale = self.chkSvdLogScale.isChecked()

        # Sanity check: Ensure we don't try to show more components than we calculate
        if calc_comps < show_comps:
            calc_comps = show_comps
            self.sbSvdCalcComps.blockSignals(True)  # Prevent infinite loops
            self.sbSvdCalcComps.setValue(calc_comps)
            self.sbSvdCalcComps.blockSignals(False)

        return calc_comps, show_comps, log_scale

    def plot_current_data_fit_preview(self):
        if self.treeExperiment.currentItem() is None:
            return
        if getattr(self, '_is_loading_settings', False):
            return
        experiment = self.get_experiment()
        # 1. Grab all the current settings from our UI
        (
            fit_mode, data_sel_type, svd_comps, traces_list, average,
            region_min, region_max, single_wave, single_average, mask_list,
            exp_no, irf_w, irf_mu, initial_taus, tau_inf
        ) = self.get_fit_parameters()
        if fit_mode == 0:
            if data_sel_type == 'svd':
                experiment.select_SVD_vectors(val=svd_comps)
            elif data_sel_type == 'traces' and traces_list:
                experiment.select_traces(points=traces_list, average=average, avoid_regions=mask_list)
            elif data_sel_type == 'region':
                experiment.select_region(mini=region_min, maxi=region_max)
        elif fit_mode == 1:
            # For a single trace, we just tell the backend to select that one point
            experiment.select_traces(points=[single_wave], average=single_average)
        fig, ax = experiment.plot_traces(traces='select', legend='auto')

        # Make it look tight and professional
        fig.tight_layout()

        # Trigger the actual redraw!
        self.fittingPreviewMplWidget.update_figure(fig)
        self._save_current_dataset_settings()

    def get_fit_parameters(self):
        """
        Retrieves, validates, and formats all inputs from the Fit Setup tab.
        Returns a comprehensive tuple of all variables needed for fitting.
        """
        # 1. Mode and Data Selection Logic
        fit_mode = self.cbFittingType.currentIndex()  # 0 for Global, 1 for Single

        # Determine the exact data selection method active on Page 0
        data_sel_type = None
        if fit_mode == 0:
            if self.rbGlobalFitSvd.isChecked():
                data_sel_type = 'svd'
            elif self.rbGlobalFitTraces.isChecked():
                data_sel_type = 'traces'
            elif self.rbGlobalFitRegion.isChecked():
                data_sel_type = 'region'
        else:
            data_sel_type = 'single'

        # Fetch Data Selection Values
        svd_comps = self.sbGlobalFitSvdComps.value()
        global_average = self.sbGlobalFitAverage.value()
        single_wave = self.sbSingleFitWave.value()
        single_average = self.sbSingleFitAverage.value()
        region_min = self.sbGlobalFitRegionMin.value()
        region_max = self.sbGlobalFitRegionMax.value()
        # Safety net: Ensure min is actually smaller than max to prevent backend slicing errors
        if region_min > region_max:
            region_min, region_max = region_max, region_min

        # 2. LineEdit Parsing & Validation

        # Parse selected traces (e.g., "450, 500, 550" -> [450.0, 500.0, 550.0])
        traces_text = self.leGlobalFitTraces.text().strip()
        traces_list = []
        if traces_text:
            # Grabs every distinct number (integer or decimal) from the string
            matches = re.findall(r"\d+(?:\.\d+)?", traces_text)
            traces_list = [float(m) for m in matches]

        # Parse masking regions (e.g., "390-410, 790-810" -> [[390.0, 410.0], [790.0, 810.0]])
        mask_text = self.leGlobalFitMasking.text().strip()
        mask_list = None
        if mask_text and data_sel_type != 'svd':
            mask_list = []
            # This regex looks for: (Number) optionally followed by decimals, spaces, a hyphen, spaces, (Number)
            # It cleanly extracts all matching pairs into a list of lists: [['390', '410'], ['790', '810']]
            matches = re.findall(r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)", mask_text)

            for m_min, m_max in matches:
                val1 = float(m_min)
                val2 = float(m_max)

                # Safety net: ensure correct min/max order
                if val1 > val2:
                    val1, val2 = val2, val1
                mask_list.append([val1, val2])

        # Parse initial taus (e.g., "1.5, 10, 200" -> [1.5, 10.0, 200.0])
        tau_text = self.leInitialTau.text().strip()
        initial_taus = None  # Default to None so backend auto-guesses if left blank
        if tau_text:
            # Grabs every distinct number (integer or decimal)
            matches = re.findall(r"\d+(?:\.\d+)?", tau_text)
            if matches:
                initial_taus = [float(m) for m in matches]

        # 3. Shared Physical Parameters
        exp_no = self.sbExpNo.value()
        irf_w = self.dsbIRFw.value()
        if irf_w == 0:
            irf_w = None
        irf_mu = self.dsbIRFmu.value()

        # Map tau_inf checkbox to the float the backend wants
        tau_inf = 1e12 if self.chkTauInf.isChecked() else None

        # 4. Return the massive tuple
        return (
            fit_mode,
            data_sel_type,
            svd_comps,
            traces_list,
            global_average,
            region_min,
            region_max,
            single_wave,
            single_average,
            mask_list,
            exp_no,
            irf_w,
            irf_mu,
            initial_taus,
            tau_inf
        )

    def execute_fitting(self):
        """
        The main execution engine for the fitting process.
        Gathers parameters, slices the data, initializes the mathematical model,
        and runs the Levenberg-Marquardt algorithm with Status Bar feedback.
        """
        self.statusBar().showMessage("Paraméterek ellenőrzése...")

        # 1. Grab parameters and run the Bouncer
        params = self.get_fit_parameters()
        if not self.validate_pre_fit(params):
            self.statusBar().clearMessage()  # Clear if validation fails
            return
        self._fit_aborted = False
        self._is_fitting = True
        experiment = self.get_experiment()
        # Safely unpack the tuple
        (
            fit_mode, data_sel_type, svd_comps, traces_list, average,
            region_min, region_max, single_wave, single_average, mask_list,
            exp_no, irf_w, irf_mu, initial_taus, tau_inf
        ) = params
        self._save_current_dataset_settings()
        if not initial_taus:
            initial_taus = [10.0 ** (i) for i in range(exp_no)]
            print(f"Auto-generált kezdeti tau értékek: {initial_taus}")

        # 2. Lock the UI and update Status Bar
        self.btnRunFit.setText("Illesztés Megszakítása")
        self.btnRunFit.setStyleSheet("background-color: #d9534f; color: white; font-weight: bold;")  # Make it Red!
        self.setCursor(Qt.CursorShape.WaitCursor)
        self.statusBar().showMessage("Adatok előkészítése és szeletelése...")
        QtWidgets.QApplication.processEvents()  # Force the UI to draw the message!

        try:
            # ---------------------------------------------------------
            # 3. DATA PREPARATION
            # ---------------------------------------------------------
            if fit_mode == 0:
                if data_sel_type == 'svd':
                    experiment.select_SVD_vectors(val=svd_comps)
                elif data_sel_type == 'traces':
                    experiment.select_traces(points=traces_list, average=average, avoid_regions=mask_list)
                elif data_sel_type == 'region':
                    experiment.select_region(mini=region_min, maxi=region_max)

            elif fit_mode == 1:
                experiment.select_traces(points=[single_wave], average=single_average)

            # ---------------------------------------------------------
            # 4. EXECUTE THE MATH
            # ---------------------------------------------------------
            self.statusBar().showMessage("Levenberg-Marquardt illesztés folyamatban... Kérem várjon!")
            QtWidgets.QApplication.processEvents()  # Force the UI to update again before the heavy freeze!
            sys.stdout = self.stdout_redirector
            self.textFitLog.clear()
            self.textFitLog.append("--- Illesztés Indítása ---")

            if fit_mode == 0:
                experiment.fitting.initialize_exp_params(irf_mu, irf_w, *initial_taus, tau_inf=tau_inf)
                experiment.fitting._active_minimizer = experiment.fitting
                experiment.fitting.fit_global(vary=True, verbose=True)

            elif fit_mode == 1:
                experiment.fitting.fit_single_exp(
                    single_wave, single_average, irf_mu, irf_w, *initial_taus, tau_inf=tau_inf, plot=False
                )

            sys.stdout = sys.__stdout__
            if self._fit_aborted:
                self.statusBar().showMessage("Illesztés megszakítva.", 5000)
                return  # STOP HERE! Don't show the success message or add it to the tree.

            self.textFitLog.append("--- Illesztés Befejezve ---")
            # ---------------------------------------------------------
            # 5. POST-FIT SUCCESS
            # ---------------------------------------------------------

            # Show success message for exactly 5000 milliseconds (5 seconds)
            self.statusBar().showMessage("Illesztés sikeresen befejeződött!", 5000)
            self._save_current_dataset_settings()
            self._add_fit_to_tree()
            QtWidgets.QMessageBox.information(
                self,
                "Sikeres Illesztés",
                "Az illesztés sikeresen lefutott! Az eredmények megtekinthetők az Eredmények fülön."
            )
        except Exception as e:
            # ---------------------------------------------------------
            # 6. POST-FIT FAILURE
            # ---------------------------------------------------------
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self.statusBar().showMessage("Hiba az illesztés során!", 5000)
            sys.stdout = sys.__stdout__
            QtWidgets.QMessageBox.critical(
                self,
                "Matematikai Hiba",
                f"Az illesztési algoritmus hibába ütközött:\n\n{str(e)}\n\n"
                "Javaslat: Próbálja meg módosítani a kezdeti értékeket (Tau) vagy a kizárt tartományokat."
            )
        finally:
            # 6. TRANSFORM BACK TO "RUN" (Guaranteed to execute!)
            self._is_fitting = False
            self.btnRunFit.setText("Illesztés Futtatása")
            self.btnRunFit.setStyleSheet("")  # Clears the custom color
            self.btnRunFit.setEnabled(True)
            self.setCursor(Qt.CursorShape.ArrowCursor)


    def _add_fit_to_tree(self):
        """
        Retrieves the latest fit from the backend and adds it as a child node
        to the currently active experiment in the QTreeWidget.
        """
        # 1. Get the current experiment node from the tree
        current_item = self.treeExperiment.currentItem()
        if current_item is None:
            return

        # If the user somehow had a child node selected, find the parent experiment node
        parent_item = current_item
        while parent_item.parent() is not None:
            parent_item = parent_item.parent()
        experiment = self.get_experiment()
        # 2. Get the latest fit ID and result from the ultrpyfit backend
        fit_mode = self.cbFittingType.currentIndex()
        if fit_mode == 0:  # Global Fit
            fit_dict = experiment.fitting.fit_records.global_fits
            fit_category = 'global'

            if not fit_dict:
                print("Hiba: Nem található elmentett globális illesztés a memóriában!")
                return

            # Grab the very last key added to the dictionary
            fit_number = list(fit_dict.keys())[-1]
            latest_fit = fit_dict[fit_number]

            exp_no = latest_fit.details.get('exp_no', '?')
            if self.rbGlobalFitSvd.isChecked():
                mode_str = "SVD"
            elif self.rbGlobalFitTraces.isChecked():
                mode_str = "Nyomok"
            elif self.rbGlobalFitRegion.isChecked():
                mode_str = "Tartomány"
            else:
                mode_str = "Globális"
            node_text = f"Illesztés {fit_number}: {exp_no} exp ({mode_str})"

        elif fit_mode == 1:  # Single Fit
            fit_dict = experiment.fitting.fit_records.single_fits
            fit_category = 'single'

            if not fit_dict:
                print("Hiba: Nem található elmentett single illesztés a memóriában!")
                return

            # Grab the very last key added to the dictionary
            fit_number = list(fit_dict.keys())[-1]
            latest_fit = fit_dict[fit_number]

            exp_no = latest_fit.details.get('exp_no', '?')
            node_text = f"Illesztés {fit_number}: {exp_no} exp (Egyetlen nyom)"

        fit_item = QtWidgets.QTreeWidgetItem([node_text])

        # We add 'fit_category' to the payload so the tree click event knows where to look!
        node_data = {
            'type': 'fit_result',
            'fit_category': fit_category,
            'fit_number': fit_number
        }
        fit_item.setData(0, Qt.UserRole, node_data)

        # 6. Attach it to the tree and expand the folder so the user sees it
        parent_item.addChild(fit_item)
        parent_item.setExpanded(True)

        # Select the newly created fit node automatically
        self.treeExperiment.setCurrentItem(fit_item)

    def abort_fitting(self):
        """Slot to safely abort a running fit."""
        # Check if the minimizer exists and the math is running
        experiment = self.get_experiment()
        if hasattr(experiment.fitting, '_active_minimizer'):
            self._fit_aborted = True
            # This flips the boolean flag inside the backend!
            experiment.fitting._active_minimizer.stop_fit()

            # Print a warning to our custom text log
            self.textFitLog.append("\n⚠️ --- ILLESZTÉS MEGSZAKÍTVA A FELHASZNÁLÓ ÁLTAL --- ⚠️")
            self.btnRunFit.setText("Leállítás folyamatban...")
            self.btnRunFit.setStyleSheet("background-color: #f0ad4e; color: black;")  # Warning yellow
            self.btnRunFit.setEnabled(False)

    def handle_fit_button_click(self):
        """Traffic cop for the Transformer button."""
        if not self._is_fitting:
            self.execute_fitting()
        else:
            self.abort_fitting()

    def on_view_mode_changed(self):
        """
        Triggered whenever the user changes the view mode dropdown.
        index 0: 3D Surface
        index 1: Spectra (Wavelength vs Amp, sliced by Time)
        index 2: Kinetic Traces (Time vs Amp, sliced by Wavelength)
        """
        index = self.cbViewMode.currentIndex()
        self.stackedViewModeOptions.setCurrentIndex(index)

        print(self.treeExperiment.currentItem())
        if self.treeExperiment.currentItem() is None:
            # If no data is loaded, just clear the plot and stop here.
            self._clear_plot_with_message(
                "No Experiment Loaded.\nPlease select an experiment from the Project Explorer.")
            return

        if index == 0:
            print("Switching to 3D View...")
            self.stackedViewModeOptions.setMaximumHeight(61)
            self.stackedViewModeOptions.setMinimumHeight(61)
            self.plot_current_data_3D()

        elif index == 1:
            print("Switching to Spectra View...")
            self.stackedViewModeOptions.setMaximumHeight(211)
            self.stackedViewModeOptions.setMinimumHeight(211)
            self.plot_current_data_spectrum()

        elif index == 2:
            print("Switching to Traces View...")
            self.stackedViewModeOptions.setMaximumHeight(151)
            self.stackedViewModeOptions.setMinimumHeight(151)
            self.plot_current_data_traces()

    def _clear_plot_with_message(self, message):
        """
        Clears the current canvas and displays a text message.
        """
        # Access the figure inside your MplWidget
        fig = self.mplWidget.canvas.figure
        fig.clear()

        ax = fig.add_subplot(111)
        # Hide the axis lines and ticks for a cleaner look
        ax.axis('off')

        # Place text right in the middle
        ax.text(0.5, 0.5, message,
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=12, color='gray')

        self.mplWidget.canvas.draw()

    def enable_scroll_zoom(self, ax):
        """
        Enables zoom by scrolling the mouse wheel on a 3D plot.
        """
        ax._custom_zoom_level = getattr(ax, '_custom_zoom_level', 1.0)

        def on_scroll(event):
            # Only zoom if the mouse is actually over the 3D plot
            if event.inaxes != ax:
                return

            # 2. Define the zoom multiplier
            # Scroll Up = Zoom In (increase size)
            # Scroll Down = Zoom Out (decrease size)
            zoom_multiplier = 1.1 if event.button == 'up' else 0.9

            # 3. Update the internal zoom tracker
            ax._custom_zoom_level *= zoom_multiplier

            # 4. Apply the zoom using the modern Matplotlib API
            # We grab the current box aspect (so we don't accidentally squash the plot)
            # and apply our new zoom level.
            current_aspect = ax.get_box_aspect()
            ax.set_box_aspect(current_aspect, zoom=ax._custom_zoom_level)

            # 5. Redraw the canvas
            ax.figure.canvas.draw_idle()

        # Connect the event to the canvas
        self._scroll_cid = ax.figure.canvas.mpl_connect('scroll_event', on_scroll)

    def enable_interactive_features(self, fig, ax, x_data, target_lineedit=None):
        """
        Provides a fast blitting crosshair, floating coordinates, and click-to-save functionality.
        """

        # 1. The Fast Crosshair (Solves Problem 1 & 2)
        self._cursor = Cursor(ax, useblit=True, color='gray', linewidth=1, linestyle='--')

        # 2. The Custom Floating Coordinate Box (Solves Problem 3)
        coord_box = ax.annotate(
            "", xy=(1, 1), xycoords='axes fraction', xytext=(-10, -10), textcoords='offset points',
            ha='right', va='top', bbox=dict(boxstyle='round,pad=0.4', fc='white', alpha=0.85, ec='gray'),
            fontsize=10, zorder=200
        )
        coord_box.set_visible(False)

        drawn_lines = []

        def sync_red_lines(vals):
            for line in drawn_lines:
                try:
                    line.remove()
                except ValueError:
                    pass
            drawn_lines.clear()

            for val in vals:
                line = ax.axvline(val, color='red', linestyle=':', alpha=0.6, zorder=1)
                drawn_lines.append(line)

            fig.canvas.draw_idle()

        def on_mouse_move(event):
            if event.inaxes != ax:
                if coord_box.get_visible():
                    coord_box.set_visible(False)
                    ax.figure.canvas.draw_idle()
                return
            x_label = ax.get_xlabel()
            y_label = ax.get_ylabel()
            coord_box.set_text(f"{x_label}: {event.xdata:.1f} | {y_label}: {event.ydata:.5f}")
            if not coord_box.get_visible():
                coord_box.set_visible(True)
            ax.figure.canvas.draw_idle()

        def on_click(event):
            if event.inaxes != ax or target_lineedit is None:
                return
            if event.button not in [1, 3]:
                return

            current_text = target_lineedit.text()
            current_vals = [float(x.strip()) for x in current_text.replace(';', ',').split(',') if x.strip()]

            if event.button == 1:  # LEFT CLICK -> ADD
                idx = np.argmin(np.abs(x_data - event.xdata))
                clicked_val = x_data[idx]

                if clicked_val not in current_vals:
                    current_vals.append(clicked_val)
                    current_vals.sort()
                    target_lineedit.setText(", ".join([f"{v:.1f}" for v in current_vals]))
                    sync_red_lines(current_vals)

            elif event.button == 3:  # RIGHT CLICK -> REMOVE
                if not current_vals:
                    return

                current_vals_array = np.array(current_vals)
                closest_idx = np.argmin(np.abs(current_vals_array - event.xdata))
                closest_val = current_vals[closest_idx]

                click_px = ax.transData.transform((event.xdata, 0))
                line_px = ax.transData.transform((closest_val, 0))
                pixel_distance = abs(click_px[0] - line_px[0])

                if pixel_distance <= 15.0:
                    current_vals.pop(closest_idx)
                    target_lineedit.setText(", ".join([f"{v:.1f}" for v in current_vals]))
                    sync_red_lines(current_vals)

        self._cid_move = fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
        self._cid_click = fig.canvas.mpl_connect('button_press_event', on_click)

        if target_lineedit is not None:
            initial_text = target_lineedit.text()
            initial_vals = [float(x.strip()) for x in initial_text.replace(';', ',').split(',') if x.strip()]
            sync_red_lines(initial_vals)

    def validate_pre_fit(self, params):
        """
        Validates all fitting parameters before sending them to the backend.
        Returns True if safe to proceed, False if there is a critical error.
        """
        # Unpack the parameters exactly as they come from get_fit_parameters()
        (
            fit_mode, data_sel_type, svd_comps, traces_list, average,
            region_min, region_max, single_wave, single_average, mask_list,
            exp_no, irf_w, irf_mu, initial_taus, tau_inf
        ) = params

        # ---------------------------------------------------------
        # 1. CRITICAL: Is there actually data to fit?
        # ---------------------------------------------------------
        if self.treeExperiment.currentItem() is None:
            return False
        experiment = self.get_experiment()
        # ---------------------------------------------------------
        # 2. LOGIC CHECK: Exponent Number vs. Initial Taus
        # ---------------------------------------------------------
        # If the user typed something, it MUST match the spinbox number exactly.
        if initial_taus is not None:
            if len(initial_taus) != exp_no:
                self._show_validation_error(
                    "Érvénytelen Tau paraméterek",
                    f"A megadott kezdeti tau értékek száma ({len(initial_taus)}) nem egyezik "
                    f"a kért exponenciálisok számával ({exp_no}).\n\n"
                    "Kérjük, pontosítsa a listát, vagy hagyja teljesen üresen az automatikus generáláshoz."
                )
                return False

        # ---------------------------------------------------------
        # 3. MODE-SPECIFIC DATA CHECKS
        # ---------------------------------------------------------
        min_wave = np.min(experiment.wavelength)
        max_wave = np.max(experiment.wavelength)

        if fit_mode == 0:  # GLOBAL FIT

            if data_sel_type == 'traces' and not traces_list:
                self._show_validation_error(
                    "Hiányzó nyomok",
                    "Nyomok (Traces) mód van kiválasztva, de nem adott meg hullámhosszakat.\n"
                    "Kérjük, adjon meg értékeket (pl. 450, 500)."
                )
                return False

            if data_sel_type == 'region':
                if region_min == region_max:
                    self._show_validation_error(
                        "Érvénytelen tartomány",
                        "A tartomány kezdő és végpontja nem lehet azonos."
                    )
                    return False
                # Check if the region completely misses the actual dataset
                if region_max < min_wave or region_min > max_wave:
                    self._show_validation_error(
                        "Tartomány hiba",
                        f"A megadott tartomány teljesen kívül esik az adatok hullámhossz-tartományán "
                        f"({min_wave:.1f} - {max_wave:.1f} nm)."
                    )
                    return False

        elif fit_mode == 1:  # SINGLE FIT
            if single_wave < min_wave or single_wave > max_wave:
                self._show_validation_error(
                    "Hullámhossz hiba",
                    f"A megadott hullámhossz kívül esik az adatok tartományán "
                    f"({min_wave:.1f} - {max_wave:.1f} nm)."
                )
                return False

        # If it survives all these checks, it is 100% mathematically safe to fit!
        return True

    def _show_validation_error(self, title, message):
        """Helper method to pop a warning dialog without crashing."""
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def _save_current_dataset_settings(self):
        """
        Scrapes the current state of all GUI widgets (checkboxes, spinboxes, etc.)
        and saves them into a dictionary keyed by the current filename.
        """
        if self.treeExperiment.currentItem() is None:
            return
        exp_id = self.treeExperiment.currentItem().data(0, Qt.UserRole)

        if self.rbAllSpectra.isChecked():
            spec_mode = 'all'
        elif self.rbAutomaticSpectra.isChecked():
            spec_mode = 'auto'
        else:
            spec_mode = 'custom'

            # --- 3. Determine Traces Mode ---
        if self.rbAllTrace.isChecked():
            trace_mode = 'all'
        elif self.rbAutomaticTrace.isChecked():
            trace_mode = 'auto'
        else:
            trace_mode = 'custom'

        if self.rbGlobalFitSvd.isChecked():
            global_fit_mode = 'svd'
        elif self.rbGlobalFitRegion.isChecked():
            global_fit_mode = 'region'
        else:
            global_fit_mode = 'custom'

        # 1. Scrape All Settings
        settings = {
            # Data Explorer Tab
            'view_mode': self.cbViewMode.currentIndex(),

            # 3D Page
            '3d_cmap': self.cbColormaps3D.currentIndex(),
            '3d_style': self.cbStyle3D.currentIndex(),
            '3d_resolution': self.sbRenderQuality3D.value(),

            # Spectra Page
            'spec_time_mode': spec_mode,
            'spec_num': self.sbNumberOfSpectra.value(),
            'spec_at_wavelength_checkbox': self.chkAtWavelengthSpectra.isChecked(),
            'spec_at_wavelength_num': self.dsbAtWavelengthSpectra.value(),
            'spec_custom_times': self.leCustomTimesSpectral.text(),
            'spec_time_range_checkbox': self.chkTimeRangeSpectra.isChecked(),
            'spec_time_range_start': self.dsbTimeRangeStartSpectra.value(),
            'spec_time_range_stop': self.dsbTimeRangeStopSpectra.value(),
            'spec_from_max_to_min': self.chkFromMaxToMinSpectra.isChecked(),
            'spec_average': self.sbAverageSpectra.value(),
            'spec_mask_checkbox': self.chkMaskRangeSpectra.isChecked(),
            'spec_mask_range_start': self.dsbMaskRangeStartSpectra.value(),
            'spec_mask_range_stop': self.dsbMaskRangeStopSpectra.value(),
            'spec_colormap': self.cbColormapsSpectra.currentIndex(),
            'spec_style': self.cbStyleSpectra.currentIndex(),
            'spec_legend': self.cbLegendSpectra.currentIndex(),

            # Traces Page
            'trace_mode': trace_mode,
            'trace_custom_waves': self.leCustomWavelengthTrace.text(),
            'trace_style': self.cbStyleTrace.currentIndex(),
            'trace_legend': self.cbLegendTrace.currentIndex(),

            # SVD Tab
            'svd_calculated_components': self.sbSvdCalcComps.value(),
            'svd_shown_spin_box_components': self.sbSvdShowComps.value(),
            'svd_shown_slider_components': self.sldSvdShowComps.value(),
            'svd_log_scale': self.chkSvdLogScale.isChecked(),

            # Fitting Settings Tab
            'fitting_type': self.cbFittingType.currentIndex(),
            # Global Fit Settings
            'global_fit_mode': global_fit_mode,
            'global_fit_svd_comps': self.sbGlobalFitSvdComps.value(),
            'global_fit_region_min': self.sbGlobalFitRegionMin.value(),
            'global_fit_region_max': self.sbGlobalFitRegionMax.value(),
            'global_fit_traces': self.leGlobalFitTraces.text(),
            'global_fit_average': self.sbGlobalFitAverage.value(),
            'global_fit_masking': self.leGlobalFitMasking.text(),

            # Single Fit Settings
            'single_fit_trace': self.sbSingleFitWave.value(),
            'single_fit_average': self.sbSingleFitAverage.value(),

            # Fitting Initial Values
            'fitting_exp_num': self.sbExpNo.value(),
            'fitting_fwhm': self.dsbIRFw.value(),
            'fitting_t0': self.dsbIRFmu.value(),
            'fitting_taus': self.leInitialTau.text(),
            'fitting_inf_tau': self.chkTauInf.isChecked(),
            'fitting_progress_log': self.textFitLog.toPlainText(),

            # Active Tab (so we return to the same view!)
            'active_tab': self.tabMain.currentIndex()
        }

        # Save it to our master dictionary
        self.dataset_settings[exp_id] = settings

    def _load_dataset_settings(self):
        """
        Restores the GUI widgets to the saved state for this specific file.
        If no settings exist, it loads defaults.
        """
        if self.treeExperiment.currentItem() is None:
            return
        exp_id = self.treeExperiment.currentItem().data(0, Qt.UserRole)
        s = self.dataset_settings[exp_id]
        data = self.experiments[exp_id].data
        wavelength = self.experiments[exp_id].wavelength

        # 1. Find the 1D index of the maximum absolute value in the entire matrix
        flat_idx = np.argmax(np.abs(data), axis=None)

        # 2. Convert that 1D index back into a 2D (row, col) coordinate
        row_col_idx = np.unravel_index(flat_idx, data.shape)

        # row_col_idx[0] is the Time index
        # row_col_idx[1] is the Wavelength index
        wave_idx = row_col_idx[1]
        # Block signals so restoring settings doesn't trigger 50 useless replots!
        self._is_loading_settings = True
        try:
            self.cbViewMode.setCurrentIndex(s.get('view_mode', 0))
            # Restore 3D
            self.sbRenderQuality3D.setValue(s.get('3d_resolution', 5))
            self.cbColormaps3D.setCurrentIndex(s.get('3d_cmap', 0))
            self.cbStyle3D.setCurrentIndex(s.get('3d_style', 0))

            # Restore Spectra Radio Buttons
            spec_mode = s.get('spec_time_mode', 'all')
            if spec_mode == 'all':
                self.rbAllSpectra.setChecked(True)
            elif spec_mode == 'auto':
                self.rbAutomaticSpectra.setChecked(True)
            else:
                self.rbCustomSpectra.setChecked(True)

            self.sbNumberOfSpectra.setValue(s.get('spec_num', 8))
            self.chkAtWavelengthSpectra.setChecked(s.get('spec_at_wavelength_checkbox', False))
            self.dsbAtWavelengthSpectra.setValue(s.get('spec_at_wavelength_num', wavelength[wave_idx]))
            self.leCustomTimesSpectral.setText(s.get('spec_custom_times', ""))
            self.chkTimeRangeSpectra.setChecked(s.get('spec_time_range_checkbox', False))
            self.dsbTimeRangeStartSpectra.setValue(s.get('spec_time_range_start', self.experiments.get(exp_id).time[0]))
            self.dsbTimeRangeStopSpectra.setValue(s.get('spec_time_range_stop', self.experiments.get(exp_id).time[-1]))
            self.chkFromMaxToMinSpectra.setChecked(s.get('spec_from_max_to_min', False))
            self.sbAverageSpectra.setValue(s.get('spec_average', 0))
            self.chkMaskRangeSpectra.setChecked(s.get('spec_mask_checkbox', False))
            self.dsbMaskRangeStartSpectra.setValue(s.get('spec_mask_range_start', 0))
            self.dsbMaskRangeStopSpectra.setValue(s.get('spec_mask_range_stop', 0))
            self.cbColormapsSpectra.setCurrentIndex(s.get('spec_colormap', 0))
            self.cbStyleSpectra.setCurrentIndex(s.get('spec_style', 0))
            self.cbLegendSpectra.setCurrentIndex(s.get('spec_legend', 0))

            # Restore Traces Radio Buttons
            trace_mode = s.get('trace_mode', 'all')
            if trace_mode == 'all':
                self.rbAllTrace.setChecked(True)
            elif trace_mode == 'auto':
                self.rbAutomaticTrace.setChecked(True)
            else:
                self.rbCustomTrace.setChecked(True)

            self.leCustomWavelengthTrace.setText(s.get('trace_custom_waves', ""))
            self.cbStyleTrace.setCurrentIndex(s.get('trace_style', 0))
            self.cbLegendTrace.setCurrentIndex(s.get('trace_legend', 0))

            # SVD Tab
            self.sbSvdCalcComps.setValue(s.get('svd_calculated_components', 15))
            self.sbSvdShowComps.setValue(s.get('svd_shown_spin_box_components', 3))
            self.sldSvdShowComps.setValue(s.get('svd_shown_slider_components', 3))
            self.chkSvdLogScale.setChecked(s.get('svd_log_scale', False))

            # Fitting Settings Tab
            self.cbFittingType.setCurrentIndex(s.get('fitting_type', 0))

            # Global Fit Settings
            global_fit_mode = s.get('global_fit_mode', 'svd')
            if global_fit_mode == 'svd':
                self.rbGlobalFitSvd.setChecked(True)
            elif global_fit_mode == 'region':
                self.rbGlobalFitRegion.setChecked(True)
            else:
                self.rbGlobalFitTraces.setChecked(True)

            self.sbGlobalFitSvdComps.setValue(s.get('global_fit_svd_comps', 3))
            self.sbGlobalFitRegionMin.setValue(
                s.get('global_fit_region_min', self.experiments.get(exp_id).wavelength[0]))
            self.sbGlobalFitRegionMax.setValue(
                s.get('global_fit_region_max', self.experiments.get(exp_id).wavelength[-1]))
            self.leGlobalFitTraces.setText(s.get('global_fit_traces', ""))
            self.sbGlobalFitAverage.setValue(s.get('global_fit_average', 0))
            self.leGlobalFitMasking.setText(s.get('global_fit_masking', ""))

            # Single Fit Settings
            self.sbSingleFitWave.setValue(s.get('single_fit_trace', wavelength[wave_idx]))
            self.sbSingleFitAverage.setValue(s.get('single_fit_average', 0))

            # Fitting Initial Values
            self.sbExpNo.setValue(s.get('fitting_exp_num', 0))
            self.dsbIRFw.setValue(s.get('fitting_fwhm', 0))
            self.dsbIRFmu.setValue(s.get('fitting_t0', 0))
            self.leInitialTau.setText(s.get('fitting_taus', ""))
            self.chkTauInf.setChecked(s.get('fitting_inf_tau', False))
            self.textFitLog.setText(s.get('fitting_progress_log', ""))

            # Restore Tab
            self.tabMain.setCurrentIndex(s.get('active_tab', 0))

        finally:
            # Unblock signals
            self._is_loading_settings = False

            # Trigger exactly ONE update to render the correct view!
        self.on_view_mode_changed()

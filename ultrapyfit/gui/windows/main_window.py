from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import uuid
from ultrapyfit.gui.ui.ui_main_window import Ui_MainWindow
from ultrapyfit.gui.windows.import_dialog import ImportDialog
from ultrapyfit.experiment import Experiment
from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor
from typing import Any
import numpy as np


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self._setup_connections()
        self._spectra_cursor = None
        self.viewStyleDict3D = {"Felület": "surface",
                                "Vázlat": "wireframe",
                                "Kontúr": "contour"}
        self.viewStyleDictSpectral = {"Ultrapyfit világos": "lmu_spec_gui",
                                      "Ultrapyfit sötét": "lmu_specd_gui",
                                      "Alapértelmezett": "default",
                                      "Seaborn világos rács": "seaborn-v0_8-whitegrid",
                                      "Seaborn sötét rács": "seaborn-v0_8-darkgrid",
                                      "Sötét háttér": "dark_background",
                                      "ggplot": "ggplot"}
        self.viewStyleDictTrace = {"Ultrapyfit világos": "lmu_res_gui",
                                   "Ultrapyfit sötét": "lmu_resd_gui",
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
        self.cbViewMode.currentIndexChanged.connect(self.on_view_mode_changed)
        self.btnResetView3D.clicked.connect(self.reset_3d_camera)
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

    def _enable_controls(self):
        self.cbViewMode.setEnabled(True)
        self.cbColormaps3D.setEnabled(True)
        self.cbStyle3D.setEnabled(True)
        self.sbRenderQuality3D.setEnabled(True)
        self.btnResetView3D.setEnabled(True)

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

        # 5. Create Sub-nodes (Glotaran Style)
        node_data = QtWidgets.QTreeWidgetItem(root_item)
        node_data.setText(0, "Raw Data")

        node_svd = QtWidgets.QTreeWidgetItem(root_item)
        node_svd.setText(0, "SVD Analysis")

        node_fit = QtWidgets.QTreeWidgetItem(root_item)
        node_fit.setText(0, "Global Fit")

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
                print(f"Action: Show {node_type} for experiment {exp_id}")

                if node_type == "Raw Data":
                    # self.plot_raw(target_experiment)
                    pass
                elif node_type == "SVD Analysis":
                    # self.plot_svd(target_experiment)
                    pass

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
        item = self.treeExperiment.currentItem()
        exp_id = item.data(0, Qt.UserRole)
        experiment = self.experiments.get(exp_id)
        current_fig = self.mplWidget.canvas.figure
        if not reset_camera and current_fig.axes:
            old_ax = current_fig.axes[0]
            if hasattr(old_ax, 'elev') and hasattr(old_ax, 'azim'):
                saved_state = {
                    'elev': old_ax.elev,
                    'azim': old_ax.azim,
                    'roll': getattr(old_ax, 'roll', 0),
                    # 'xlim': old_ax.get_xlim3d(),
                    # 'ylim': old_ax.get_ylim3d(),
                    # 'zlim': old_ax.get_zlim3d(),
                    'zoom_level': getattr(old_ax, '_custom_zoom_level', 0.85)
                }
        cmap, stride, plot_type = self.get_3D_options()
        plot_type = self.viewStyleDict3D.get(plot_type)
        fig, ax = experiment.plot_3D(cmap=cmap, plot_type=plot_type, stride=stride, azim=current_azim, elev=current_elev)
        if saved_state:
            ax.view_init(
                elev=saved_state['elev'],
                azim=saved_state['azim'],
                roll=saved_state['roll']
            )
            # ax.set_xlim3d(saved_state['xlim'])
            # ax.set_ylim3d(saved_state['ylim'])
            # ax.set_zlim3d(saved_state['zlim'])
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
        item = self.treeExperiment.currentItem()
        exp_id = item.data(0, Qt.UserRole)
        experiment = self.experiments.get(exp_id)
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
        fig.tight_layout()
        self._spectra_cursor = Cursor(ax, useblit=True, color='gray', linewidth=1, linestyle='--')
        self.enable_coordinate_tracker(ax)
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
        item = self.treeExperiment.currentItem()
        exp_id = item.data(0, Qt.UserRole)
        experiment = self.experiments.get(exp_id)
        traces_val, legend_val, style_val = self.get_trace_options()
        fig, ax = experiment.plot_traces(traces=traces_val,
                                         style=style_val,
                                         legend=legend_val)
        fig.tight_layout()
        self._spectra_cursor = Cursor(ax, useblit=True, color='gray', linewidth=1, linestyle='--')
        self.enable_coordinate_tracker(ax)
        self.mplWidget.update_figure(fig)
        plt.close(fig)
        self._save_current_dataset_settings()

    def get_trace_options(self):
        """
        Collects, parses, and formats all GUI inputs from the Traces Settings page.
        Returns a dictionary of keyword arguments ready for plot_traces().
        """
        if self.rbAllTrace.isChecked():
            traces_val = "select"
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
            self._clear_plot_with_message("No Experiment Loaded.\nPlease select an experiment from the Project Explorer.")
            return

        if index == 0:
            print("Switching to 3D View...")
            self.stackedViewModeOptions.setMaximumHeight(31)
            self.stackedViewModeOptions.setMinimumHeight(31)
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

    def enable_coordinate_tracker(self, ax):
        """
        Creates a floating text box in the top right corner of the plot
        that dynamically displays the X and Y coordinates of the mouse.
        """
        # 1. Create a hidden text annotation locked to the top right of the axes
        coord_box = ax.annotate(
            "",
            xy=(1, 1), xycoords='axes fraction',
            xytext=(-10, -10), textcoords='offset points',
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.4', fc='white', alpha=0.85, ec='gray'),
            fontsize=10, zorder=200
        )
        coord_box.set_visible(False)

        def on_mouse_move(event):
            # 2. Hide the box if the mouse leaves the plotting area
            if event.inaxes != ax:
                if coord_box.get_visible():
                    coord_box.set_visible(False)
                    ax.figure.canvas.draw_idle()
                return

            # 3. Update the text with X (Wavelength) and Y (Amplitude)
            # Adjust the formatting (.1f and .4f) based on your typical data values
            x_label = ax.get_xlabel()
            y_label = ax.get_ylabel()
            coord_box.set_text(f"{x_label}: {event.xdata:.1f} | {y_label}: {event.ydata:.5f}")

            if not coord_box.get_visible():
                coord_box.set_visible(True)

            ax.figure.canvas.draw_idle()

        # 4. Attach the event to the canvas
        self._mouse_cid = ax.figure.canvas.mpl_connect('motion_notify_event', on_mouse_move)

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
            trace_mode = 'select'
        elif self.rbAutomaticTrace.isChecked():
            trace_mode = 'auto'
        else:
            trace_mode = 'custom'

        # 1. Scrape 3D Settings
        settings = {
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

            # Active Tab (so we return to the same view!)
            'active_tab': self.stackedViewModeOptions.currentIndex()
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
            trace_mode = s.get('trace_mode', 'select')
            if trace_mode == 'select':
                self.rbAllTrace.setChecked(True)
            elif trace_mode == 'auto':
                self.rbAutomaticTrace.setChecked(True)
            else:
                self.rbCustomTrace.setChecked(True)

            self.leCustomWavelengthTrace.setText(s.get('trace_custom_waves', ''))
            self.cbStyleTrace.setCurrentIndex(s.get('trace_style', 0))
            self.cbLegendTrace.setCurrentIndex(s.get('trace_legend', 0))

            # Restore Tab
            self.stackedViewModeOptions.setCurrentIndex(s.get('active_tab', 0))

        finally:
            # Unblock signals
            self._is_loading_settings = False

            # Trigger exactly ONE update to render the correct view!
        self.on_view_mode_changed()

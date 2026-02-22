from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import uuid
from ultrapyfit.gui.ui.ui_main_window import Ui_MainWindow
from ultrapyfit.gui.windows.import_dialog import ImportDialog
from ultrapyfit.experiment import Experiment
from matplotlib import pyplot as plt


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actImport.triggered.connect(self.open_import_dialog)
        self.viewStyleDict3D = {"Felület": "surface",
                                "Vázlat": "wireframe",
                                "Kontúr": "contour"}
        self.viewStyleDictSpectral = {"Ultrapyfit világos": "lmu_spec_gui",
                                      "Ultrapyfit sötét": "lmu_specd_gui",
                                      "Alapértelmezett": "default",
                                      "Seaborn világos rács": "seaborn-v0_8-whitegrid",
                                      "Seaborn sötét rács": "seaborn-v0_8-darkgrid",
                                      "Seaborn világos": "seaborn-v0_8-bright",
                                      "ggplot": "ggplot"}
        # A dictionary to map TreeItems back to actual Python Objects
        # Format: { QTreeWidgetItem_ID : Experiment_Object }
        self.experiments = {}
        self.treeExperiment.itemClicked.connect(self.on_tree_click)
        self.cbColormaps3D.currentIndexChanged.connect(self.plot_current_data_3D)
        self.sbRenderQuality3D.valueChanged.connect(self.plot_current_data_3D)
        self.cbStyle3D.currentIndexChanged.connect(self.plot_current_data_3D)
        self.btnResetView3D.clicked.connect(self.reset_3d_camera)
        self.cbViewMode.currentIndexChanged.connect(self.on_view_mode_changed)

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
        self.plot_current_data_3D()

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
                # self.show_summary(target_experiment)
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
        saved_state = None
        current_elev = 30
        current_azim = -60
        item = self.treeExperiment.currentItem()
        exp_id = item.data(0, Qt.UserRole)
        experiment = self.experiments.get(exp_id)
        current_fig = self.mplWidget.canvas.figure
        if not reset_camera and current_fig.axes:
            old_ax = current_fig.axes[0]
            # Only try to get angles if it was actually a 3D plot
            if hasattr(old_ax, 'elev') and hasattr(old_ax, 'azim'):
                saved_state = {
                    'elev': old_ax.elev,
                    'azim': old_ax.azim,
                    'roll': getattr(old_ax, 'roll', 0),  # Roll is in newer matplotlib versions
                    'xlim': old_ax.get_xlim3d(),
                    'ylim': old_ax.get_ylim3d(),
                    'zlim': old_ax.get_zlim3d(),
                    'zoom_level': getattr(old_ax, '_custom_zoom_level', 0.85)
                }
        # 1. Call the library function (which generates a new fig/ax)
        cmap, stride, plot_type = self.get_3D_options()
        plot_type = self.viewStyleDict3D.get(plot_type)
        fig, ax = experiment.plot_3D(cmap=cmap, plot_type=plot_type, stride=stride, azim=current_azim, elev=current_elev)

        if saved_state:
            # Restore camera rotation
            ax.view_init(
                elev=saved_state['elev'],
                azim=saved_state['azim'],
                roll=saved_state['roll']
            )
            # Restore the custom zoom limits!
            ax.set_xlim3d(saved_state['xlim'])
            ax.set_ylim3d(saved_state['ylim'])
            ax.set_zlim3d(saved_state['zlim'])
            ax._custom_zoom_level = saved_state['zoom_level']
            current_aspect = ax.get_box_aspect()
            ax.set_box_aspect(current_aspect, zoom=saved_state['zoom_level'])

        self.enable_scroll_zoom(ax)
        # 2. Tell your GUI widget to swallow this new figure
        self.mplWidget.update_figure(fig)

        # 3. (Crucial Step) Close the figure in Matplotlib's backend
        # so it doesn't accidentally pop up a secondary standalone window!
        plt.close(fig)

    def get_3D_options(self):
        return self.cbColormaps3D.currentText().lower(), 11 - self.sbRenderQuality3D.value(), self.cbStyle3D.currentText()

    def plot_current_data_spectrum(self):
        if self.treeExperiment.currentItem() is None:
            return
        item = self.treeExperiment.currentItem()
        exp_id = item.data(0, Qt.UserRole)
        experiment = self.experiments.get(exp_id)
        times_arg, rango_arg, cover_arg, legend_arg = self.get_spectrum_options()
        # Note: It creates a new figure internally using plt.subplots()
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

        # 6. Inject the new figure into our PyQt Canvas
        self.mplWidget.update_figure(fig)

        # 7. Close the Matplotlib memory instance
        plt.close(fig)

    def get_spectrum_options(self):
        # 1. Parse 'times' parameter based on Radio Buttons
        times_arg = 'all'
        if self.rbAutomaticSpectra.isChecked():
            n_spec = self.sbNumberOfSpectra.value()
            if self.chkAtWavelengthSpectra.isChecked():
                wl = self.dsbAtWavelengthSpectra.value()
                times_arg = ["auto", n_spec, wl]  # e.g., ["auto", 6, 1440]
            else:
                times_arg = ["auto", n_spec]

        elif self.rbCustomSpectra.isChecked():
            # Parse comma-separated string into a list of floats
            text = self.leCustomTimes.text()
            try:
                times_arg = [float(x.strip()) for x in text.split(',') if x.strip()]
            except ValueError:
                times_arg = 'auto'  # Fallback if user types garbage

        # 2. Parse Time Range (rango)
        rango_arg = None
        if self.chkTimeRangeSpectra.isChecked():
            rango_arg = [self.dsbTimeRangeStartSpectra.value(), self.dsbTimeRangeStopSpectra.value()]

        # 3. Parse Cover Range (e.g., masking the pump laser profile)
        cover_arg = None
        if self.chkMaskRangeSpectra.isChecked():
            # Guaranteed to be floats, no string parsing required!
            cover_arg = [self.dsbMaskRangeStartSpectra.value(),
                         self.dsbMaskRangeStopSpectra.value()]

        # 4. Parse Legend Style
        legend_txt = self.cbLegendSpectra.currentText()
        if legend_txt == "Szöveges címke":
            legend_arg = True
        elif legend_txt == "Idő színskála":
            legend_arg = 'bar'
        else:
            legend_arg = False
        return times_arg, rango_arg, cover_arg, legend_arg

    def plot_current_data_traces(self):
        if self.treeExperiment.currentItem() is None:
            return

    def on_view_mode_changed(self):
        """
        Triggered whenever the user changes the view mode dropdown.
        index 0: 3D Surface
        index 1: Spectra (Wavelength vs Amp, sliced by Time)
        index 2: Kinetic Traces (Time vs Amp, sliced by Wavelength)
        """
        # 1. Flip the control panel (StackedWidget) to match the selected view
        index = self.cbViewMode.currentIndex()
        self.stackedViewModeOptions.setCurrentIndex(index)

        # 2. Safety Check: Do we have an experiment loaded?
        print(self.treeExperiment.currentItem())
        if self.treeExperiment.currentItem() is None:
            # If no data is loaded, just clear the plot and stop here.
            self._clear_plot_with_message("No Experiment Loaded.\nPlease select an experiment from the Project Explorer.")
            return

        # 3. Route to the correct plotting function
        if index == 0:
            print("Switching to 3D View...")
            self.stackedViewModeOptions.setMaximumHeight(51)
            self.stackedViewModeOptions.setMinimumHeight(51)
            self.plot_current_data_3D()

        elif index == 1:
            print("Switching to Spectra View...")
            self.stackedViewModeOptions.setMaximumHeight(211)
            self.stackedViewModeOptions.setMinimumHeight(211)
            self.plot_current_data_spectrum()

        elif index == 2:
            print("Switching to Traces View...")
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


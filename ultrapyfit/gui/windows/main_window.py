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
        self.actionImport.triggered.connect(self.open_import_dialog)
        self.viewStyleDict = {"Felület": "surface", "Vázlat": "wireframe", "Kontúr": "contour"}
        # A dictionary to map TreeItems back to actual Python Objects
        # Format: { QTreeWidgetItem_ID : Experiment_Object }
        self.experiments = {}
        self.ExperimentTreeWidget.itemClicked.connect(self.on_tree_click)
        self.ColorMaps3DComboBox.currentIndexChanged.connect(self.plot_current_data_3D)
        self.RenderQuality3DSpinBox.valueChanged.connect(self.plot_current_data_3D)
        self.ViewStyle3DComboBox.currentIndexChanged.connect(self.plot_current_data_3D)
        self.ResetView3DButton.clicked.connect(self.plot_current_data_3D)

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

    def add_experiment(self, experiment_obj):
        """Called when Import Window finishes."""

        # 1. Generate a unique ID for this new experiment
        # This ensures that even if you load the same file twice, they don't clash
        exp_id = str(uuid.uuid4())

        # 2. Store the OBJECT in your dictionary
        self.experiments[exp_id] = experiment_obj

        # 3. Create the Root Item for the Tree
        root_item = QtWidgets.QTreeWidgetItem(self.ExperimentTreeWidget)
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
        self.ExperimentTreeWidget.setCurrentItem(root_item)
        self.plot_current_data_3D()

    def on_tree_click(self, item, column):
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

    def plot_current_data_3D(self):
        if self.ExperimentTreeWidget.currentItem() is None:
            return
        item = self.ExperimentTreeWidget.currentItem()
        exp_id = item.data(0, Qt.UserRole)
        experiment = self.experiments.get(exp_id)
        # 1. Call the library function (which generates a new fig/ax)
        cmap, stride, plot_type = self.get_3D_options()
        plot_type = self.viewStyleDict.get(plot_type)
        fig, ax = experiment.plot_3D(cmap=cmap, plot_type=plot_type, stride=stride)

        # 2. Tell your GUI widget to swallow this new figure
        self.PlotWidget.update_figure(fig)

        # 3. (Crucial Step) Close the figure in Matplotlib's backend
        # so it doesn't accidentally pop up a secondary standalone window!
        plt.close(fig)

    def get_3D_options(self):
        return self.ColorMaps3DComboBox.currentText().lower(), 11 - self.RenderQuality3DSpinBox.value(), self.ViewStyle3DComboBox.currentText()

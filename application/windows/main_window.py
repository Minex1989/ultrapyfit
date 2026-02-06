from PySide6 import QtWidgets

from application.pyui.ui_main_window import Ui_MainWindow
from application.windows.import_options_dialog import ImportOptionsDialog
from ultrapyfit.experiment import Experiment


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionImport.triggered.connect(self.import_test_results)
        self.separator = ""
        self.decimal = ""
        self.wave_is_row = False
        self.time = 0
        self.wavelength = 0

    def import_test_results(self):
        test_list = []
        dialog = QtWidgets.QFileDialog()
        dialog.setNameFilter("Szöveges fájlok (*.csv *.txt)")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        dialogSuccessful = dialog.exec()
        if dialogSuccessful:
            file_location = dialog.selectedFiles()[0]
            self.open_parameter_dialog()
            with open(file_location, 'r') as f:

                experiment = Experiment.load_data(
                    path=file_location, wavelength=self.wavelength, time=self.time,
                    wave_is_row=self.wave_is_row, separator=self.separator,
                    decimal=self.decimal
                )
                experiment.describe_data()

    def open_parameter_dialog(self):
        """Open the parameter dialog and connect to its signals"""
        self.import_options_dialog = ImportOptionsDialog(self)

        # Connect to the dialog's signals
        self.import_options_dialog.parameters_accepted.connect(self.on_parameters_received)

        # Show the dialog (non-blocking with signals approach)
        self.import_options_dialog.exec()

    def on_parameters_received(self, parameters):
        """Slot called when parameters_accepted signal is emitted"""
        self.separator, self.decimal, self.wave_is_row, self.time, self.wavelength = parameters

        # Optional: Close the dialog if it's still open
        if self.import_options_dialog.isVisible():
            self.import_options_dialog.close()
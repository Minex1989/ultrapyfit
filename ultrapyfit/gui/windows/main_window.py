from PySide6 import QtWidgets

from ultrapyfit.gui.ui.ui_main_window import Ui_MainWindow
from ultrapyfit.gui.windows.import_dialog import ImportDialog
from ultrapyfit.experiment import Experiment


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionImport.triggered.connect(self.open_import_dialog)

    def open_import_dialog(self):
        """Open the parameter dialog and connect to its signals"""
        self.import_dialog = ImportDialog(self)

        # Connect to the dialog's signals
        self.import_dialog.parameters_accepted.connect(self.on_parameters_received)

        # Show the dialog (non-blocking with signals approach)
        self.import_dialog.exec()

    def on_parameters_received(self, parameters):
        """Slot called when parameters_accepted signal is emitted"""
        self.separator, self.decimal, self.wave_is_row, self.time, self.wavelength = parameters

        # Optional: Close the dialog if it's still open
        if self.import_dialog.isVisible():
            self.import_dialog.close()
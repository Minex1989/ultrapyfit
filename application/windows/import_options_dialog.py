from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Signal
from application.pyui.ui_import_dialog import Ui_ImportOptionsDialog


class ImportOptionsDialog(QtWidgets.QDialog, Ui_ImportOptionsDialog):
    parameters_accepted = Signal(tuple)
    def __init__(self, parent=None):
        super(ImportOptionsDialog, self).__init__(parent)
        self.setupUi(self)
        self.ContinueButton.clicked.connect(self.accept)
        self.OtherSepLineEdit.editingFinished.connect(self.disable_separator_combo_box)

    def closeEvent(self, event: QCloseEvent):
        """Handle when the dialog is closed via X button"""
        reply = QtWidgets.QMessageBox.question(
            self, "Confirm Close", "Are you sure you want to close without saving?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
            )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            self.reject()  # Send reject signal
            event.accept()
        else:
            event.ignore()  # Keep the dialog open

    def accept(self):
        """Override accept to emit signal before closing"""
        parameters = self.get_parameters()
        self.parameters_accepted.emit(parameters)  # Emit the signal
        super().accept()

    def get_parameters(self):
        decimal = self.DecComboBox.currentText().split('(')[1].replace(')', '')
        wave_is_row = self.WaveIsRowCheckBox.isChecked()
        time = int(self.TimeSpinBox.value()) - 1
        wavelength = int(self.WavelengthSpinBox.value()) - 1
        if self.SepComboBox.isEnabled():
            separator = self.SepComboBox.currentText().split('(')[1].replace(')', '')
            return separator, decimal, wave_is_row, time, wavelength
        else:
            separator = self.OtherSepLineEdit.currentText().split('(')[1].replace(')', '')
            return separator, decimal, wave_is_row, time, wavelength

    def disable_separator_combo_box(self):
        if self.OtherSepLineEdit.text() == "":
            self.SepComboBox.setEnabled(True)
        else:
            self.SepComboBox.setDisabled(True)

from PySide6 import QtWidgets
from application.pyui.ui_main_window import Ui_MainWindow
from ultrapyfit.experiment import Experiment

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionImport.triggered.connect(self.import_test_results)


    def import_test_results(self):
        test_list = []
        dialog = QtWidgets.QFileDialog()
        dialog.setNameFilter("Szöveges fájlok (*.csv *.txt)")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        dialogSuccessful = dialog.exec()
        if dialogSuccessful:
            fileLocation = dialog.selectedFiles()[0]
            with open(fileLocation, 'r') as f:
                experiment = Experiment.load_data(fileLocation, wave_is_row=True)
                experiment.describe_data()

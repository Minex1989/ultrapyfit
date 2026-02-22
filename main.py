import sys
from ultrapyfit.gui.windows.main_window import MainWindow
from PySide6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())



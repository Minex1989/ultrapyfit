import sys
from ultrapyfit.gui.windows.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.c()))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())



import sys
from ultrapyfit.gui.windows.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale
from PySide6.QtGui import QIcon
import os
from ultrapyfit.utils.resource_paths import get_resource_path

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.c()))
    
    # Set the application window icon
    icon_path = get_resource_path(os.path.join('ultrapyfit', 'gui', 'app_icon.ico'))
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
        
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

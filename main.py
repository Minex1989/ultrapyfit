import sys
from application.windows.main_window import MainWindow
from timeit import default_timer as timer
from datetime import datetime
from PySide6 import QtWidgets

if __name__ == '__main__':
    starting_time = f'The program is running since: {datetime.now()}'
    print(starting_time)
    start = timer()

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    time = timer() - start
    print(f'The total runtime of the program: {time:.2f}s.')
    sys.exit(app.exec())
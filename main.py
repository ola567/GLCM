import sys
from PyQt5 import QtWidgets

from main_view import MainView


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainView()
    ui.setup(main_window)
    main_window.show()
    sys.exit(app.exec_())

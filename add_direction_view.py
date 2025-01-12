from PyQt5 import QtCore, QtGui, QtWidgets


class AddDirectionView(object):
    def setup(self, add_direction_window, parent):
        self.parent = parent

        add_direction_window.resize(330, 212)
        self.centralwidget = QtWidgets.QWidget(add_direction_window)

        self.dx_label = QtWidgets.QLabel(self.centralwidget)
        self.dx_label.setGeometry(QtCore.QRect(30, 60, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dx_label.setFont(font)

        self.enter_directions_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_directions_label.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.enter_directions_label.setFont(font)

        self.dy_label = QtWidgets.QLabel(self.centralwidget)
        self.dy_label.setGeometry(QtCore.QRect(190, 60, 55, 16))
        self.dy_label.setFont(font)

        self.dx_input = QtWidgets.QLineEdit(self.centralwidget)
        self.dx_input.setGeometry(QtCore.QRect(30, 80, 110, 22))
        self.dx_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        dx_validator = QtGui.QIntValidator(self.dx_input)
        self.dx_input.setValidator(dx_validator)

        self.dy_input = QtWidgets.QLineEdit(self.centralwidget)
        self.dy_input.setGeometry(QtCore.QRect(190, 80, 110, 22))
        self.dy_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        dy_validator = QtGui.QIntValidator(self.dy_input)
        self.dy_input.setValidator(dy_validator)

        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(110, 160, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ok_button.setFont(font)
        self.ok_button.clicked.connect(self.on_ok_button_clicked)

        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(210, 160, 90, 28))
        self.cancel_button.setFont(font)
        self.cancel_button.clicked.connect(self.on_cancel_button_clicked)

        add_direction_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(add_direction_window)
        QtCore.QMetaObject.connectSlotsByName(add_direction_window)

    def retranslateUi(self, add_direction_window):
        _translate = QtCore.QCoreApplication.translate
        add_direction_window.setWindowTitle(
            _translate("add_direction_window", "Add direction")
        )
        self.dx_label.setText(_translate("add_direction_window", "dx"))
        self.enter_directions_label.setText(
            _translate("add_direction_window", "Enter directions")
        )
        self.dy_label.setText(_translate("add_direction_window", "dy"))
        self.ok_button.setText(_translate("add_direction_window", "Ok"))
        self.cancel_button.setText(_translate("add_direction_window", "Cancel"))

    def on_ok_button_clicked(self):
        dx = self.dx_input.text()
        dy = self.dy_input.text()
        self.parent.list_data.append(f"dx: {dx} dy: {dy}")
        self.parent.list_model.setStringList(self.parent.list_data)

    def on_cancel_button_clicked(self):
        self.centralwidget.window().close()

from PyQt5 import QtCore, QtGui, QtWidgets


class ResultView(object):
    def setup(self, result_window):
        result_window.resize(1250, 942)
        self.centralwidget = QtWidgets.QWidget(result_window)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(570, 20, 71, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.image_stats_label = QtWidgets.QLabel(self.centralwidget)
        self.image_stats_label.setGeometry(QtCore.QRect(30, 80, 101, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.image_stats_label.setFont(font)

        self.contrast_label = QtWidgets.QLabel(self.centralwidget)
        self.contrast_label.setGeometry(QtCore.QRect(30, 115, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.contrast_label.setFont(font)

        self.contrast_input = QtWidgets.QLineEdit(self.centralwidget)
        self.contrast_input.setGeometry(QtCore.QRect(120, 120, 113, 22))
        self.contrast_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )

        self.dissimilarity_input = QtWidgets.QLineEdit(self.centralwidget)
        self.dissimilarity_input.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.dissimilarity_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )

        self.dissimilarity_label = QtWidgets.QLabel(self.centralwidget)
        self.dissimilarity_label.setGeometry(QtCore.QRect(30, 145, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dissimilarity_label.setFont(font)

        self.homogenity_input = QtWidgets.QLineEdit(self.centralwidget)
        self.homogenity_input.setGeometry(QtCore.QRect(120, 180, 113, 22))
        self.homogenity_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )

        self.homogenity_label = QtWidgets.QLabel(self.centralwidget)
        self.homogenity_label.setGeometry(QtCore.QRect(30, 175, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.homogenity_label.setFont(font)

        self.energy_input = QtWidgets.QLineEdit(self.centralwidget)
        self.energy_input.setGeometry(QtCore.QRect(120, 210, 113, 22))
        self.energy_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )

        self.corelation_input = QtWidgets.QLineEdit(self.centralwidget)
        self.corelation_input.setGeometry(QtCore.QRect(120, 240, 113, 22))
        self.corelation_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )

        self.energy_label = QtWidgets.QLabel(self.centralwidget)
        self.energy_label.setGeometry(QtCore.QRect(30, 205, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.energy_label.setFont(font)

        self.corelation_label = QtWidgets.QLabel(self.centralwidget)
        self.corelation_label.setGeometry(QtCore.QRect(30, 235, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.corelation_label.setFont(font)

        self.average_glcm_image_area = QtWidgets.QScrollArea(self.centralwidget)
        self.average_glcm_image_area.setGeometry(QtCore.QRect(30, 330, 580, 580))
        self.average_glcm_image_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 578, 578))
        self.average_glcm_image_area.setWidget(self.scrollAreaWidgetContents)

        self.block_stats_label = QtWidgets.QLabel(self.centralwidget)
        self.block_stats_label.setGeometry(QtCore.QRect(650, 250, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.block_stats_label.setFont(font)

        self.block_options_input = QtWidgets.QComboBox(self.centralwidget)
        self.block_options_input.setGeometry(QtCore.QRect(650, 280, 160, 28))
        self.block_options_input.setObjectName("block_options_input")
        self.block_options_input.addItem("")
        self.block_options_input.addItem("")
        self.block_options_input.addItem("")
        self.block_options_input.addItem("")
        self.block_options_input.addItem("")

        self.block_result_image_area = QtWidgets.QScrollArea(self.centralwidget)
        self.block_result_image_area.setGeometry(QtCore.QRect(640, 330, 580, 580))
        self.block_result_image_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 578, 578))
        self.block_result_image_area.setWidget(self.scrollAreaWidgetContents_2)

        self.averave_glcm_image_label = QtWidgets.QLabel(self.centralwidget)
        self.averave_glcm_image_label.setGeometry(QtCore.QRect(30, 290, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.averave_glcm_image_label.setFont(font)

        result_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(result_window)
        QtCore.QMetaObject.connectSlotsByName(result_window)

    def retranslateUi(self, result_window):
        _translate = QtCore.QCoreApplication.translate
        result_window.setWindowTitle(_translate("result_window", "result_window"))
        self.title.setText(_translate("result_window", "Result"))
        self.image_stats_label.setText(_translate("result_window", "Image stats"))
        self.contrast_label.setText(_translate("result_window", "Contrast"))
        self.dissimilarity_label.setText(_translate("result_window", "Dissimilarity"))
        self.homogenity_label.setText(_translate("result_window", "Homogenity"))
        self.energy_label.setText(_translate("result_window", "Energy"))
        self.corelation_label.setText(_translate("result_window", "Corelation"))
        self.block_stats_label.setText(_translate("result_window", "Block stats"))
        self.block_options_input.setItemText(0, _translate("result_window", "Contrast"))
        self.block_options_input.setItemText(
            1, _translate("result_window", "Dissimilarity")
        )
        self.block_options_input.setItemText(
            2, _translate("result_window", "Homogenity")
        )
        self.block_options_input.setItemText(3, _translate("result_window", "Energy"))
        self.block_options_input.setItemText(
            4, _translate("result_window", "Corelation")
        )
        self.averave_glcm_image_label.setText(
            _translate("result_window", "Average GLCM")
        )

from PyQt5 import QtCore, QtGui, QtWidgets


class GLCMView(object):
    def setup(self, glcm_window):
        glcm_window.resize(640, 678)
        self.centralwidget = QtWidgets.QWidget(glcm_window)
        self.centralwidget.setObjectName("centralwidget")
        self.glcm_image_area = QtWidgets.QScrollArea(self.centralwidget)
        self.glcm_image_area.setGeometry(QtCore.QRect(30, 70, 580, 580))
        self.glcm_image_area.setWidgetResizable(True)
        self.glcm_image_area.setObjectName("glcm_image_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 578, 578))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.glcm_image_area.setWidget(self.scrollAreaWidgetContents_2)
        self.glcm_label = QtWidgets.QLabel(self.centralwidget)
        self.glcm_label.setGeometry(QtCore.QRect(30, 30, 51, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.glcm_label.setFont(font)
        self.glcm_label.setObjectName("glcm_label")
        glcm_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(glcm_window)
        QtCore.QMetaObject.connectSlotsByName(glcm_window)

    def retranslateUi(self, glcm_window):
        _translate = QtCore.QCoreApplication.translate
        glcm_window.setWindowTitle(_translate("glcm_window", "MainWindow"))
        self.glcm_label.setText(_translate("glcm_window", "GLCM"))

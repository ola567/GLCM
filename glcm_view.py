import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class GLCMView(object):
    def setup(
        self,
        glcm_window,
        input_image,
        glcm_window_title: str,
        glcm_window_description: str,
    ):
        # variables
        self.input_image = input_image
        self.glcm_window_title = glcm_window_title
        self.glcm_window_description = glcm_window_description

        glcm_window.resize(640, 678)
        self.centralwidget = QtWidgets.QWidget(glcm_window)
        self.centralwidget.setObjectName("centralwidget")

        # Label for displaying the image
        self.glcm_image_label = QLabel(self.centralwidget)
        self.glcm_image_label.setGeometry(QtCore.QRect(30, 70, 580, 580))
        self.glcm_image_label.setAlignment(Qt.AlignCenter)

        # Label for GLCM text
        self.glcm_label = QtWidgets.QLabel(self.centralwidget)
        self.glcm_label.setGeometry(QtCore.QRect(30, 30, 581, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.glcm_label.setFont(font)

        glcm_window.setCentralWidget(self.centralwidget)

        self.load_image()

        # Setup window title and label text
        self.retranslateUi(glcm_window)
        QtCore.QMetaObject.connectSlotsByName(glcm_window)

    def retranslateUi(self, glcm_window):
        _translate = QtCore.QCoreApplication.translate
        glcm_window.setWindowTitle(_translate("glcm_window", self.glcm_window_title))
        self.glcm_label.setText(_translate("glcm_window", self.glcm_window_description))

    def load_image(self):
        """
        Loads the image into the scroll area by converting it to a QPixmap
        and adding it to the layout inside the scroll area.
        """
        im_array = np.array(self.input_image)
        height, width = im_array.shape
        bytes_per_line = width
        qimage = QImage(
            im_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8
        )
        pixmap = QPixmap.fromImage(qimage)
        if pixmap.isNull():
            raise Exception("Cannot convert image to QPixmap.")

        # resize
        label_width = self.glcm_image_label.width()
        label_height = self.glcm_image_label.height()
        pixmap = pixmap.scaled(
            label_width,
            label_height,
            Qt.KeepAspectRatio,
            Qt.FastTransformation,
        )

        self.glcm_image_label.setPixmap(pixmap)

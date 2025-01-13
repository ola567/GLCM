import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt


class GLCMView(object):
    def setup(self, glcm_window, input_image):
        # variables
        self.input_image = input_image

        glcm_window.resize(640, 678)
        self.centralwidget = QtWidgets.QWidget(glcm_window)
        self.centralwidget.setObjectName("centralwidget")

        # Create scroll area
        self.glcm_image_area = QtWidgets.QScrollArea(self.centralwidget)
        self.glcm_image_area.setGeometry(QtCore.QRect(30, 70, 580, 580))
        self.glcm_image_area.setWidgetResizable(True)
        self.glcm_image_area.setObjectName("glcm_image_area")

        # Create a widget to hold the content inside the scroll area
        self.scroll_area = QtWidgets.QWidget()
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 578, 578))
        self.glcm_image_area.setWidget(self.scroll_area)

        # Label for GLCM text
        self.glcm_label = QtWidgets.QLabel(self.centralwidget)
        self.glcm_label.setGeometry(QtCore.QRect(30, 30, 51, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.glcm_label.setFont(font)
        self.glcm_label.setObjectName("glcm_label")

        glcm_window.setCentralWidget(self.centralwidget)

        # Setup window title and label text
        self.retranslateUi(glcm_window)
        QtCore.QMetaObject.connectSlotsByName(glcm_window)

    def retranslateUi(self, glcm_window):
        _translate = QtCore.QCoreApplication.translate
        glcm_window.setWindowTitle(_translate("glcm_window", "GLCM"))
        self.glcm_label.setText(_translate("glcm_window", "GLCM"))

    def load_image(self):
        """
        Loads the image into the scroll area by converting it to a QPixmap
        and adding it to the layout inside the scroll area.
        """
        # Convert input image (which is assumed to be a numpy array) to a QImage
        im_array = np.array(self.input_image)
        height, width = im_array.shape
        bytes_per_line = width
        qimage = QImage(
            im_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8
        )

        pixmap = QPixmap.fromImage(qimage)

        # Check if QPixmap conversion was successful
        if pixmap.isNull():
            raise Exception("Cannot convert image to QPixmap.")

        # Create a new QLabel to display the pixmap
        image_label = QtWidgets.QLabel(self.scroll_area)
        image_label.setPixmap(pixmap)
        image_label.setFixedSize(
            pixmap.size()
        )  # Ensure the QLabel has the same size as the image
        image_label.setAlignment(Qt.AlignCenter)

        # Create a layout to add the QLabel
        layout = QtWidgets.QVBoxLayout(
            self.scroll_area
        )  # Use the scroll area widget itself
        layout.addWidget(image_label)

        # Set the layout for the scroll area widget
        self.scroll_area.setLayout(layout)

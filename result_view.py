import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QLabel

from glcm_backend.glcm import GLCMImage, Direction, to_image
from glcm_view import GLCMView


class ResultView(object):
    def setup(
        self,
        result_window,
        grayscale_image,
        gray_levels: int,
        block_size: int,
        average_glcm_from: [Direction],
    ):
        # variables
        print(f"{gray_levels=}")
        print(f"{block_size=}")
        print(f"{average_glcm_from=}")
        self.grayscale_image = grayscale_image
        self.gray_levels = gray_levels
        self.block_size = block_size
        self.average_glcm_from = average_glcm_from

        result_window.resize(1250, 987)
        self.centralwidget = QtWidgets.QWidget(result_window)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(570, 20, 71, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
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
        self.contrast_input.setReadOnly(True)

        self.dissimilarity_label = QtWidgets.QLabel(self.centralwidget)
        self.dissimilarity_label.setGeometry(QtCore.QRect(30, 145, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dissimilarity_label.setFont(font)

        self.dissimilarity_input = QtWidgets.QLineEdit(self.centralwidget)
        self.dissimilarity_input.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.dissimilarity_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.dissimilarity_input.setReadOnly(True)

        self.homogeneity_label = QtWidgets.QLabel(self.centralwidget)
        self.homogeneity_label.setGeometry(QtCore.QRect(30, 175, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.homogeneity_label.setFont(font)

        self.homogeneity_input = QtWidgets.QLineEdit(self.centralwidget)
        self.homogeneity_input.setGeometry(QtCore.QRect(120, 180, 113, 22))
        self.homogeneity_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.homogeneity_input.setReadOnly(True)

        self.energy_label = QtWidgets.QLabel(self.centralwidget)
        self.energy_label.setGeometry(QtCore.QRect(30, 205, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.energy_label.setFont(font)

        self.energy_input = QtWidgets.QLineEdit(self.centralwidget)
        self.energy_input.setGeometry(QtCore.QRect(120, 210, 113, 22))
        self.energy_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.energy_input.setReadOnly(True)

        self.correlation_label = QtWidgets.QLabel(self.centralwidget)
        self.correlation_label.setGeometry(QtCore.QRect(30, 235, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.correlation_label.setFont(font)

        self.correlation_input = QtWidgets.QLineEdit(self.centralwidget)
        self.correlation_input.setGeometry(QtCore.QRect(120, 240, 113, 22))
        self.correlation_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.correlation_input.setReadOnly(True)

        self.show_average_glcm_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_average_glcm_button.setGeometry(QtCore.QRect(30, 280, 201, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.show_average_glcm_button.setFont(font)
        self.show_average_glcm_button.setObjectName("show_average_glcm_button")
        self.show_average_glcm_button.clicked.connect(
            self.on_show_average_glcm_button_clicked
        )

        # Average GLCM display without scroll
        self.average_glcm_image_label = QLabel(self.centralwidget)
        self.average_glcm_image_label.setGeometry(QtCore.QRect(30, 380, 580, 580))
        self.average_glcm_image_label.setAlignment(Qt.AlignCenter)

        self.averave_glcm_image_title = QtWidgets.QLabel(self.centralwidget)
        self.averave_glcm_image_title.setGeometry(QtCore.QRect(30, 340, 201, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.averave_glcm_image_title.setFont(font)
        self.averave_glcm_image_title.setText("Input image in gray scale")

        self.block_stats_label = QtWidgets.QLabel(self.centralwidget)
        self.block_stats_label.setGeometry(QtCore.QRect(650, 300, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.block_stats_label.setFont(font)

        self.block_options_input = QtWidgets.QComboBox(self.centralwidget)
        self.block_options_input.setGeometry(QtCore.QRect(650, 330, 160, 28))
        self.block_options_input.addItems(
            ["Contrast", "Dissimilarity", "Homogenity", "Energy", "Correlation"]
        )

        self.block_result_image_area = QtWidgets.QScrollArea(self.centralwidget)
        self.block_result_image_area.setGeometry(QtCore.QRect(640, 380, 580, 580))
        self.block_result_image_area.setWidgetResizable(True)
        self.block_result_image_label = QLabel()
        self.block_result_image_label.setAlignment(Qt.AlignCenter)
        self.block_result_image_area.setWidget(self.block_result_image_label)

        result_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(result_window)

        # calculate image stats
        self.glcm_image = GLCMImage(
            grayscale_image=self.grayscale_image,
            gray_levels=self.gray_levels,
            block_size=self.block_size,
            average_glcm_from=self.average_glcm_from,
        )
        self.contrast_input.setText(str(round(self.glcm_image.contrast, 10)))
        self.dissimilarity_input.setText(str(round(self.glcm_image.dissimilarity, 10)))
        self.homogeneity_input.setText(str(round(self.glcm_image.homogeneity, 10)))
        self.energy_input.setText(str(round(self.glcm_image.energy, 10)))
        self.correlation_input.setText(str(round(self.glcm_image.correlation, 10)))

        # Load images
        self.load_image_to_label(self.average_glcm_image_label, "Average")
        self.block_options_input.currentTextChanged.connect(
            lambda text: self.load_image_to_label(self.block_result_image_label, text)
        )
        self.load_image_to_label(self.block_result_image_label, "Contrast")

    def on_show_average_glcm_button_clicked(self):
        im = to_image(self.glcm_image.normalized_average_glcm2d)
        self.glcm_view_window = QtWidgets.QMainWindow()
        self.glcm_view_handler = GLCMView()
        self.glcm_view_handler.setup(glcm_window=self.glcm_view_window, input_image=im)
        self.glcm_view_window.show()

    def load_image_to_label(self, label, image_type: str):
        """
        image_type can be:
            - display average GLCM on the left side (not clickable)
                - "Average"
            - display stats on the right side (clickable)
                - "Contrast", "Dissimilarity", "Homogenity", "Energy", "Correlation"
        """
        if image_type == "Average":
            im = to_image(self.glcm_image.normalized_average_glcm2d)
        elif image_type == "Contrast":
            im = to_image(self.glcm_image.normalized_contrast_block)
        elif image_type == "Dissimilarity":
            im = to_image(self.glcm_image.normalized_dissimilarity_block)
        elif image_type == "Homogenity":
            im = to_image(self.glcm_image.normalized_homogeneity_block)
        elif image_type == "Energy":
            im = to_image(self.glcm_image.normalized_energy_block)
        elif image_type == "Correlation":
            im = to_image(self.glcm_image.normalized_correlation_block)
        else:
            raise ValueError(f"Unknown image type: {image_type}")

        im_array = np.array(im)
        height, width = im_array.shape
        bytes_per_line = width
        qimage = QImage(
            im_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8
        )
        pixmap = QPixmap.fromImage(qimage)
        if pixmap.isNull():
            raise Exception("Cannot convert image to QPixmap.")

        if image_type == "Average":
            scroll_area_width = self.average_glcm_image_label.width()
            scroll_area_height = self.average_glcm_image_label.height()
            pixmap = pixmap.scaled(
                scroll_area_width,
                scroll_area_height,
                Qt.KeepAspectRatio,
                Qt.FastTransformation,
            )

        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.size())

        if image_type != "Average":
            label.mousePressEvent = lambda event: self.on_image_click(
                event, pixmap.width(), pixmap.height(), label
            )

    def on_image_click(self, event, image_width, image_height, label):
        x = event.pos().x()
        y = event.pos().y()

        im = to_image(self.glcm_image.normalized_average_glcm2d_for_block(x=x, y=y))
        self.glcm_view_window = QtWidgets.QMainWindow()
        self.glcm_view_handler = GLCMView()
        self.glcm_view_handler.setup(glcm_window=self.glcm_view_window, input_image=im)
        self.glcm_view_window.show()

    def retranslateUi(self, result_window):
        _translate = QtCore.QCoreApplication.translate
        result_window.setWindowTitle(_translate("result_window", "Result"))
        self.title.setText(_translate("result_window", "Result"))
        self.image_stats_label.setText(_translate("result_window", "Image stats"))
        self.contrast_label.setText(_translate("result_window", "Contrast"))
        self.dissimilarity_label.setText(_translate("result_window", "Dissimilarity"))
        self.homogeneity_label.setText(_translate("result_window", "Homogeneity"))
        self.energy_label.setText(_translate("result_window", "Energy"))
        self.correlation_label.setText(_translate("result_window", "Correlation"))
        self.block_stats_label.setText(_translate("result_window", "Block stats"))
        self.show_average_glcm_button.setText(
            _translate("result_window", "Show average GLCM")
        )

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

from glcm_backend.glcm import GLCMImage, Direction, to_image


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
        self.contrast_input.setReadOnly(True)

        self.dissimilarity_input = QtWidgets.QLineEdit(self.centralwidget)
        self.dissimilarity_input.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.dissimilarity_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.dissimilarity_input.setReadOnly(True)

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
        self.homogenity_input.setReadOnly(True)

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
        self.energy_input.setReadOnly(True)

        self.corelation_input = QtWidgets.QLineEdit(self.centralwidget)
        self.corelation_input.setGeometry(QtCore.QRect(120, 240, 113, 22))
        self.corelation_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.corelation_input.setReadOnly(True)

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

        # calculate image stats
        self.glcm_image = GLCMImage(
            grayscale_image=self.grayscale_image,
            gray_levels=self.gray_levels,
            block_size=self.block_size,
            average_glcm_from=self.average_glcm_from,
        )
        self.contrast_input.setText(str(round(self.glcm_image.contrast, 10)))
        self.dissimilarity_input.setText(str(round(self.glcm_image.dissimilarity, 10)))
        self.homogenity_input.setText(str(round(self.glcm_image.dissimilarity, 10)))
        self.energy_input.setText(str(round(self.glcm_image.energy, 10)))
        self.corelation_input.setText(str(round(self.glcm_image.correlation, 10)))

        # load images
        self.load_image_to_scroll_area(
            scroll_area=self.average_glcm_image_area, image_type="Average"
        )
        self.load_image_to_scroll_area(
            scroll_area=self.block_result_image_area,
            image_type=self.block_options_input.currentText(),
        )

        self.block_options_input.currentTextChanged.connect(
            lambda text: self.load_image_to_scroll_area(
                scroll_area=self.block_result_image_area,
                image_type=text,
            )
        )

    def load_image_to_scroll_area(self, scroll_area, image_type: str):
        """
        image_type can be:
            - display average GLCM on the left side (not clickable)
                - "Average"
            - display stats on the right side (clickable)
                - "Contrast", "Dissimilarity", "Homogenity", "Energy", "Correlation"
        """
        widget = scroll_area.widget()
        if widget.layout() is not None:
            while widget.layout().count():
                child = widget.layout().takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
            widget.layout().deleteLater()

        # Generate new image based on image_type
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
        elif image_type == "Corelation":
            im = to_image(self.glcm_image.normalized_correlation_block)
        else:
            raise ValueError(f"Unknown image type: {image_type}")

        # Debugging: Ensure the image is valid
        if im is None or np.array(im).size == 0:
            raise ValueError(f"Generated image for type {image_type} is invalid.")

        # Convert the image to QPixmap
        im_array = np.array(im)
        height, width = im_array.shape
        bytes_per_line = width
        qimage = QImage(
            im_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8
        )
        pixmap = QPixmap.fromImage(qimage)

        if pixmap.isNull():
            raise Exception("Cannot convert image to QPixmap.")

        # Create a new QLabel and set the pixmap
        image_label = QtWidgets.QLabel(self.centralwidget)
        image_label.setPixmap(pixmap)
        image_label.setFixedSize(pixmap.size())
        image_label.setAlignment(Qt.AlignCenter)

        # Add the label to a new layout and set it to the scroll area
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(image_label)
        widget.setLayout(layout)

        # Set click event for block-specific images
        if image_type != "Average":
            image_label.mousePressEvent = lambda event: self.on_image_click(
                event, pixmap.width(), pixmap.height(), image_label
            )

    def on_image_click(self, event, image_width, image_height, label):
        x = event.pos().x()
        y = event.pos().y()

        cols = image_width // 30
        rows = image_height // 30

        col = x // 30
        row = y // 30

        square_number = row * cols + col

        QtWidgets.QMessageBox.information(
            None, "Square Clicked", f"Clicked square: {square_number}"
        )

    def retranslateUi(self, result_window):
        _translate = QtCore.QCoreApplication.translate
        result_window.setWindowTitle(_translate("result_window", "Result"))
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

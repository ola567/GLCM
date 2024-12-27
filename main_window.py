from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setup(self, main_window):
        main_window.resize(640, 600)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.title = QtWidgets.QLabel(self.central_widget)
        self.title.setGeometry(QtCore.QRect(170, 10, 300, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setStyleSheet("text-align: center;")

        self.image_label = QtWidgets.QLabel(self.central_widget)
        self.image_label.setGeometry(QtCore.QRect(50, 100, 51, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.image_label.setFont(font)

        self.file_path_input = QtWidgets.QTextEdit(self.central_widget)
        self.file_path_input.setGeometry(QtCore.QRect(50, 130, 431, 28))
        self.file_path_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.file_path_input.setReadOnly(True)
        self.file_path_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.file_path_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_path_input.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.file_path_input.horizontalScrollBar().setStyleSheet(
            """
            QScrollBar:horizontal {
                height: 6px;
                background: #f0f0f0;
                border: none;
            }
            QScrollBar::handle:horizontal {
                background: #c0c0c0;
                border-radius: 3px;
                min-width: 10px;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
            }
        """
        )

        self.browse_button = QtWidgets.QPushButton(self.central_widget)
        self.browse_button.setGeometry(QtCore.QRect(500, 130, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.browse_button.setFont(font)
        self.browse_button.clicked.connect(self.browse)

        self.grey_levels_label = QtWidgets.QLabel(self.central_widget)
        self.grey_levels_label.setGeometry(QtCore.QRect(50, 180, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grey_levels_label.setFont(font)
        self.grey_levels_input = QtWidgets.QComboBox(self.central_widget)
        self.grey_levels_input.setGeometry(QtCore.QRect(50, 210, 160, 28))
        self.grey_levels_input.addItem("")
        self.grey_levels_input.addItem("")
        self.grey_levels_input.addItem("")
        self.grey_levels_input.addItem("")

        self.block_size_label = QtWidgets.QLabel(self.central_widget)
        self.block_size_label.setGeometry(QtCore.QRect(50, 260, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.block_size_label.setFont(font)
        self.block_size_input = QtWidgets.QLineEdit(self.central_widget)
        self.block_size_input.setGeometry(QtCore.QRect(50, 290, 160, 28))
        self.block_size_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        int_validator = QtGui.QIntValidator(self.block_size_input)
        self.block_size_input.setValidator(int_validator)

        self.average_glcm_from_label = QtWidgets.QLabel(self.central_widget)
        self.average_glcm_from_label.setGeometry(QtCore.QRect(50, 340, 151, 32))
        self.average_glcm_from_label.setFont(font)

        self.clear_button = QtWidgets.QPushButton(self.central_widget)
        self.clear_button.setGeometry(QtCore.QRect(400, 550, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.clear_button.setFont(font)
        self.clear_button.clicked.connect(self.clear)

        self.apply_button = QtWidgets.QPushButton(self.central_widget)
        self.apply_button.setGeometry(QtCore.QRect(500, 550, 90, 28))
        self.apply_button.setFont(font)
        self.apply_button.clicked.connect(self.apply)

        self.average_glcm_from_input = QtWidgets.QTableWidget(self.central_widget)
        self.average_glcm_from_input.setGeometry(QtCore.QRect(50, 370, 292, 140))
        self.average_glcm_from_input.setStyleSheet(
            "background-color: #e3e3e3;\n" "border: 1px solid #a0a0a0"
        )
        self.average_glcm_from_input.setColumnCount(2)
        self.average_glcm_from_input.setHorizontalHeaderLabels(["dx", "dy"])

        self.add_row_button = QtWidgets.QPushButton(self.central_widget)
        self.add_row_button.setGeometry(QtCore.QRect(50, 520, 120, 28))
        self.add_row_button.setText("Add")
        self.add_row_button.clicked.connect(self.add_row)

        self.remove_row_button = QtWidgets.QPushButton(self.central_widget)
        self.remove_row_button.setGeometry(QtCore.QRect(180, 520, 160, 28))
        self.remove_row_button.setText("Remove")
        self.remove_row_button.clicked.connect(self.remove_selected_row)

        main_window.setCentralWidget(self.central_widget)
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def add_row(self):
        current_row_count = self.average_glcm_from_input.rowCount()
        self.average_glcm_from_input.insertRow(current_row_count)
        self.average_glcm_from_input.setRowHeight(current_row_count, 28)
        for j in range(self.average_glcm_from_input.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.average_glcm_from_input.setItem(current_row_count, j, item)

    def remove_selected_row(self):
        """Removes the selected row from the table."""
        selected_items = self.average_glcm_from_input.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            self.average_glcm_from_input.removeRow(selected_row)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.title.setText(_translate("main_window", "GLCM Analysis"))
        self.image_label.setText(_translate("main_window", "Image"))
        self.browse_button.setText(_translate("main_window", "Browse"))
        self.grey_levels_label.setText(_translate("main_window", "Grey levels"))
        self.grey_levels_input.setItemText(0, _translate("main_window", "4"))
        self.grey_levels_input.setItemText(1, _translate("main_window", "8"))
        self.grey_levels_input.setItemText(2, _translate("main_window", "16"))
        self.grey_levels_input.setItemText(3, _translate("main_window", "32"))
        self.block_size_label.setText(_translate("main_window", "Block size"))
        self.average_glcm_from_label.setText(
            _translate("main_window", "Average GLCM from")
        )
        self.clear_button.setText(_translate("main_window", "Clear"))
        self.apply_button.setText(_translate("main_window", "Apply"))

    def clear(self):
        self.file_path_input.clear()
        self.block_size_input.clear()
        self.average_glcm_from_input.setRowCount(0)
        self.grey_levels_input.setCurrentIndex(0)

    def apply(self):
        file_path = self.file_path_input.toPlainText()
        grey_levels = self.grey_levels_input.currentText()
        block_size = self.block_size_input.text()
        table_data = []
        for row in range(self.average_glcm_from_input.rowCount()):
            row_data = []
            for col in range(self.average_glcm_from_input.columnCount()):
                item = self.average_glcm_from_input.item(row, col)
                row_data.append(item.text() if item else "")
            table_data.append(row_data)

        print("File Path:", file_path)
        print("Grey Levels:", grey_levels)
        print("Block Size:", block_size)
        print("Table Data:")
        for row in table_data:
            print(row)

    def browse(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select File",
            "",
            "All Files (*);;Image Files (*.png;*.jpg;*.bmp)",
            options=options,
        )
        if file_path:
            self.file_path_input.setPlainText(file_path)

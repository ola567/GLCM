from PyQt5 import QtCore, QtGui, QtWidgets

from add_direction_view import AddDirectionView


class MainView(object):
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
        self.browse_button.clicked.connect(self.on_browse_button_clicked)

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
        self.clear_button.clicked.connect(self.on_clear_button_clicked)

        self.apply_button = QtWidgets.QPushButton(self.central_widget)
        self.apply_button.setGeometry(QtCore.QRect(500, 550, 90, 28))
        self.apply_button.setFont(font)
        self.apply_button.clicked.connect(self.on_apply_button_clicked)

        self.average_glcm_from_list = QtWidgets.QListView(self.central_widget)
        self.average_glcm_from_list.setGeometry(QtCore.QRect(50, 370, 191, 131))
        self.average_glcm_from_list.setStyleSheet("background-color: #e3e3e3;")
        self.average_glcm_from_list.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.list_model = QtCore.QStringListModel()
        self.average_glcm_from_list.setModel(self.list_model)
        self.list_data = []

        self.add_button = QtWidgets.QPushButton(self.central_widget)
        self.add_button.setGeometry(QtCore.QRect(50, 510, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.add_button.setFont(font)
        self.add_button.clicked.connect(self.on_add_button_clicked)

        self.remove_button = QtWidgets.QPushButton(self.central_widget)
        self.remove_button.setGeometry(QtCore.QRect(150, 510, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.remove_button.setFont(font)
        self.remove_button.clicked.connect(self.on_remove_button_clicked)

        main_window.setCentralWidget(self.central_widget)
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

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
        self.add_button.setText(_translate("main_window", "Add"))
        self.remove_button.setText(_translate("main_window", "Remove"))

    def on_add_button_clicked(self):
        self.add_direction_view_window = QtWidgets.QMainWindow()
        self.add_direction_view_handler = AddDirectionView()
        self.add_direction_view_handler.setup(
            add_direction_window=self.add_direction_view_window, parent=self
        )
        self.add_direction_view_window.show()

    def on_remove_button_clicked(self):
        selected_indexes = self.average_glcm_from_list.selectedIndexes()
        if selected_indexes:
            for index in sorted(selected_indexes, reverse=True):
                row = index.row()
                del self.list_data[row]
            self.list_model.setStringList(self.list_data)

    def on_clear_button_clicked(self):
        self.file_path_input.clear()
        self.block_size_input.clear()
        self.grey_levels_input.setCurrentIndex(0)
        self.list_data.clear()
        self.list_model.setStringList(self.list_data)

    def on_apply_button_clicked(self):
        file_path = self.file_path_input.toPlainText()
        grey_levels = self.grey_levels_input.currentText()
        block_size = self.block_size_input.text()
        list_data = self.list_model.stringList()
        print("File Path:", file_path)
        print("Grey Levels:", grey_levels)
        print("Block Size:", block_size)
        print("List Data:", list_data)

    def on_browse_button_clicked(self):
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

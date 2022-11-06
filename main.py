import sys
from os import path
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDateEdit,
                             QHBoxLayout, QVBoxLayout, QLabel,
                             QTimeEdit, QComboBox, QLineEdit,
                             QWidget, QSizePolicy, QGridLayout,
                             QPushButton)
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("KI5CGK Log Book")
        self.setWindowIcon(QIcon(path.abspath("Images/logo.png")))
        self.setStyleSheet("background-color: #24252b; color: white;")

        self.labels = ["DATE:", "TIME:", "CALL SIGN:", "FREQUENCY:", "MODE:", "NAME:", "LOCATION:"]
        self.num_entries = 1
        self.h_layout = None
        self.grid = None

        self.date_input = None
        self.time_input = None
        self.call_sign_input = None
        self.frequency_input = None
        self.mode_input = None
        self.name_input = None
        self.location_input = None

        self.init_ui()
        self.init_left_ui()
        self.init_right_ui()


    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        self.h_layout = QHBoxLayout()
        main_widget.setLayout(self.h_layout)


    def init_left_ui(self):
        vert_section = QVBoxLayout()
        vert_section.setAlignment(Qt.AlignmentFlag.AlignTop)
        vert_section.setSpacing(15)
        self.h_layout.addLayout(vert_section)

        for label_text in self.labels:
            row = QHBoxLayout()
            row.setAlignment(Qt.AlignmentFlag.AlignLeft)
            row.setSpacing(20)

            label = QLabel(label_text)
            label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
            row.addWidget(label)

            if label_text == "DATE:":
                self.date_input = QDateEdit(calendarPopup=True)
                self.date_input.setDateTime(QDateTime.currentDateTime())
                form = self.date_input
            elif label_text == "TIME:":
                self.time_input = QTimeEdit()
                self.time_input.setTime(QDateTime.currentDateTime().time())
                form = self.time_input
            elif label_text == "CALL SIGN:":
                self.call_sign_input = QLineEdit()
                form = self.call_sign_input
            elif label_text == "FREQUENCY:":
                self.frequency_input = QLineEdit()
                form = self.frequency_input
            elif label_text == "MODE:":
                self.mode_input = QComboBox()
                self.mode_input.addItem("TEST")
                form = self.mode_input
            elif label_text == "NAME:":
                self.name_input = QLineEdit()
                form = self.name_input
            elif label_text == "LOCATION:":
                self.location_input = QLineEdit()
                form = self.location_input

            form.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            row.addWidget(form)
            vert_section.addLayout(row)

        btn_row = QHBoxLayout()

        btn_add = QPushButton("ADD ENTRY")
        btn_add.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        btn_add.clicked.connect(self.on_add_button_clicked)

        btn_row.addWidget(btn_add)
        vert_section.addLayout(btn_row)


    def init_right_ui(self):
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.grid.setSpacing(15)

        for i in range(len(self.labels)):
            self.grid.setColumnStretch(i, 1)

        self.h_layout.addLayout(self.grid)

        for i, header_text in enumerate(self.labels):
            header_text = header_text[:-1]
            label = QLabel(header_text)
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.grid.addWidget(label, 0, i)


    def on_add_button_clicked(self):
        values = [self.date_input.date().toString("yyyy-MM-dd"),
                  self.time_input.time().toString("hh:mm"),
                  self.call_sign_input.text(),
                  self.frequency_input.text(),
                  self.mode_input.currentText(),
                  self.name_input.text(),
                  self.location_input.text()]

        for i, value in enumerate(values):
            if not value:
                value = "-/-"

            label = QLabel(value)
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.grid.addWidget(label, self.num_entries, i)

        self.num_entries += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("QLabel{letter-spacing: 2px; text-transform: uppercase;}")

    window = MainWindow()
    window.show()

    app.exec()

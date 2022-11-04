import sys
from os import path

from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QPushButton, QLabel, QVBoxLayout,
                             QDateEdit, QFormLayout, QTimeEdit,
                             QLineEdit, QScrollArea)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KI5CGK Log Book")
        self.setWindowIcon(QIcon("logo.png"))
        self.setStyleSheet("background-color: #24252b; color: white;")

        self.date_edit = None
        self.time_edit = None
        self.call_sign_edit = None
        self.freq_edit = None
        self.mode_edit = None
        self.name_edit = None
        self.location_edit = None

        self.col_date = None
        self.col_time = None
        self.col_call_sign = None
        self.col_freq = None
        self.col_mode = None
        self.col_name = None
        self.col_location = None

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # ------------ LEFT SECTION ------------ #
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        left_layout_form = QFormLayout()
        left_layout_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        left_layout_form.setFormAlignment(Qt.AlignmentFlag.AlignRight)

        self.date_edit = QDateEdit(calendarPopup=True)
        self.date_edit.setDateTime(QDateTime.currentDateTime())
        self.date_edit.setStyleSheet("outline: none;")

        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QDateTime.currentDateTime().time())

        self.freq_edit = QLineEdit()
        self.mode_edit = QLineEdit()
        self.call_sign_edit = QLineEdit()
        self.name_edit = QLineEdit()
        self.location_edit = QLineEdit()

        font_id = QFontDatabase.addApplicationFont(path.abspath("VT323-Regular.ttf"))
        families = QFontDatabase.applicationFontFamilies(font_id)
        button_font = QFont(families[0], 20)
        label_font = QFont(families[0], 20)

        labels = {
            "Date:": self.date_edit,
            "Time:": self.time_edit,
            "Call Sign:": self.call_sign_edit,
            "Frequency:": self.freq_edit,
            "Mode:": self.mode_edit,
            "Name:": self.name_edit,
            "Location": self.location_edit
        }

        for label_text in labels:
            label = QLabel(label_text)
            label.setFont(label_font)
            label.setStyleSheet("color: #ff885e;")
            left_layout_form.addRow(label, labels[label_text])

        left_layout.addLayout(left_layout_form)

        btn_style = "background-color: #ff885e; color: black; border: 0; padding: 8px 8px; margin: 4px 0;"

        btn_add = QPushButton("ADD ENTRY")
        btn_add.setStyleSheet(btn_style)
        btn_add.setFont(button_font)
        left_layout.addWidget(btn_add)
        btn_add.clicked.connect(self.on_add_entry)

        layout.addLayout(left_layout)

        # ------------ RIGHT SECTION ------------ #
        right_scroll_area = QScrollArea()
        right_widget = QWidget()
        right_vbox = QVBoxLayout()
        right_vbox.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        right_vbox.setContentsMargins(10, 10, 10, 10)

        self.col_date = QVBoxLayout()
        self.col_time = QVBoxLayout()
        self.col_freq = QVBoxLayout()
        self.col_mode = QVBoxLayout()
        self.col_call_sign = QVBoxLayout()
        self.col_name = QVBoxLayout()
        self.col_location = QVBoxLayout()

        right_hbox = QHBoxLayout()
        columns = [self.col_date, self.col_time, self.col_call_sign, self.col_freq,
                   self.col_mode, self.col_name, self.col_location]

        for column in columns:
            column.setContentsMargins(10, 0, 10, 0)
            right_hbox.addLayout(column)

        right_vbox.addLayout(right_hbox)
        right_widget.setLayout(right_vbox)

        right_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        right_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        right_scroll_area.setWidgetResizable(True)
        right_scroll_area.setMinimumWidth(500)
        right_scroll_area.setWidget(right_widget)

        layout.addWidget(right_scroll_area)

        # ------------ DISPLAY ------------ #
        self.setLayout(layout)
        self.show()

    def on_add_entry(self):
        date = self.date_edit.date().toString("yyyy-MM-dd")
        t = self.time_edit.time().toString("hh:mm")
        freq = self.freq_edit.text()
        mode = self.mode_edit.text()
        call_sign = self.call_sign_edit.text()
        name = self.name_edit.text()
        location = self.location_edit.text()

        values = []
        for value in [date, t, freq, mode, call_sign, name, location]:
            if not value:
                value = "-/-"
            values.append(value)

        columns = [self.col_date, self.col_time, self.col_freq, self.col_mode,
                   self.col_call_sign, self.col_name, self.col_location]
        for i, column in enumerate(columns):
            label = QLabel(values[i])
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            column.addWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("QLabel{letter-spacing: 2px; text-transform: uppercase; word-spacing: -4px;}")

    window = MainWindow()
    sys.exit(app.exec())

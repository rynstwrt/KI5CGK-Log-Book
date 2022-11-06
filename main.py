import sys
from os import path

from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QPushButton, QLabel, QVBoxLayout,
                             QDateEdit, QFormLayout, QTimeEdit,
                             QLineEdit, QScrollArea, QComboBox,
                             QSizePolicy)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KI5CGK Log Book")
        self.setWindowIcon(QIcon("Images/logo.png"))
        self.setStyleSheet("background-color: #24252b; color: white;")

        self.num_entries = 0

        self.columns = None

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
        self.col_delete = None

        self.init_ui()


    def init_ui(self):
        layout = QHBoxLayout()

        # ------------ LEFT SECTION ------------ #
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        left_layout_form = QFormLayout()
        left_layout_form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        left_layout_form.setFormAlignment(Qt.AlignmentFlag.AlignRight)

        self.date_edit = QDateEdit(calendarPopup=True)
        self.date_edit.setDateTime(QDateTime.currentDateTime())
        self.date_edit.setStyleSheet("outline: none;")

        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QDateTime.currentDateTime().time())

        self.freq_edit = QLineEdit()

        self.mode_edit = QComboBox()
        self.mode_edit.addItems(["-/-", "SSB", "CW", "AM",
                                 "FM", "SSTV", "FT8", "FT4",
                                 "Contestia", "Hellschreiber", "PACTOR", "PSK",
                                 "QPSK", "8PSK", "PSKR", "RTTY",
                                 "DominoEX", "FSQ", "IFKP", "MFSK",
                                 "MT63", "OFDM", "Olivia", "THOR",
                                 "Throb", "WEFAX", "Navtex/SitorB"])

        self.call_sign_edit = QLineEdit()
        self.name_edit = QLineEdit()
        self.location_edit = QLineEdit()

        label_font_id = QFontDatabase.addApplicationFont(path.abspath("Fonts/Roboto-Regular.ttf"))
        label_families = QFontDatabase.applicationFontFamilies(label_font_id)
        label_font = QFont(label_families[0], 15)

        labels = {
            "Date:": self.date_edit,
            "Time:": self.time_edit,
            "Call Sign:": self.call_sign_edit,
            "Freq:": self.freq_edit,
            "Mode:": self.mode_edit,
            "Name:": self.name_edit,
            "Location:": self.location_edit
        }

        for label_text in labels:
            label = QLabel(label_text)
            label.setFont(label_font)
            label.setStyleSheet("color: #ff885e;")
            label.setContentsMargins(0, 0, 0, 10)

            text_edit = labels[label_text]
            text_edit.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

            left_layout_form.addRow(label, text_edit)

        left_layout.addLayout(left_layout_form)

        btn_style = "background-color: #ff885e; color: black; border: 0; padding: 8px 4px; margin: 4px 0;"

        button_font_id = QFontDatabase.addApplicationFont(path.abspath("Fonts/Roboto-Regular.ttf"))
        button_families = QFontDatabase.applicationFontFamilies(button_font_id)
        button_font = QFont(button_families[0], 15)

        btn_add = QPushButton("ADD ENTRY")
        btn_add.setStyleSheet(btn_style)
        btn_add.setFont(button_font)
        left_layout.addWidget(btn_add)
        btn_add.clicked.connect(lambda: self.on_add_entry(self.num_entries))

        layout.addLayout(left_layout)

        # ------------ RIGHT SECTION ------------ #
        right_scroll_area = QScrollArea()
        
        right_widget = QWidget()
        
        self.right_vbox = QVBoxLayout()
        self.right_vbox.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.right_vbox.setContentsMargins(10, 10, 10, 10)

        self.col_date = QVBoxLayout()
        self.col_time = QVBoxLayout()
        self.col_freq = QVBoxLayout()
        self.col_mode = QVBoxLayout()
        self.col_call_sign = QVBoxLayout()
        self.col_name = QVBoxLayout()
        self.col_location = QVBoxLayout()
        self.col_delete = QVBoxLayout()

        right_hbox = QHBoxLayout()

        self.columns = [self.col_date, self.col_time, self.col_call_sign, self.col_freq,
                        self.col_mode, self.col_name, self.col_location, self.col_delete]

        for column in self.columns:
            column.setContentsMargins(10, 0, 10, 0)
            right_hbox.addLayout(column)

        self.right_vbox.addLayout(right_hbox)
        right_widget.setLayout(self.right_vbox)

        right_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        right_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        right_scroll_area.setWidgetResizable(True)
        right_scroll_area.setMinimumWidth(800)
        right_scroll_area.setWidget(right_widget)

        layout.addWidget(right_scroll_area)

        for col in self.columns:
            label_text = ""
            if col is self.col_date:
                label_text = "DATE"
            elif col is self.col_time:
                label_text = "TIME"
            elif col is self.col_call_sign:
                label_text = "CALL SIGN"
            elif col is self.col_freq:
                label_text = "FREQUENCY"
            elif col is self.col_mode:
                label_text = "MODE"
            elif col is self.col_name:
                label_text = "NAME"
            elif col is self.col_location:
                label_text = "LOCATION"
            elif col is self.col_delete:
                label_text = "DELETE"
            else:
                label_text = "DUMBASS"

            label = QLabel(label_text)
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
            label.adjustSize()
            col.addWidget(label)

        # ------------ DISPLAY ------------ #
        self.setLayout(layout)
        self.show()


    def on_add_entry(self, entry_num):
        date = self.date_edit.date().toString("yyyy-MM-dd")
        t = self.time_edit.time().toString("hh:mm")
        freq = self.freq_edit.text()
        mode = self.mode_edit.currentText()
        call_sign = self.call_sign_edit.text()
        name = self.name_edit.text()
        location = self.location_edit.text()

        values = []
        for value in [date, t, freq, mode, call_sign, name, location]:
            if not value:
                value = "-/-"
            values.append(value)

        for i, column in enumerate(self.columns[:-1]):
            label = QLabel(values[i])
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
            label.adjustSize()
            column.addWidget(label)

        del_button = QPushButton("X")
        del_button.setStyleSheet("background-color: red;")
        del_button.clicked.connect(lambda: self.on_delete_entry(entry_num))
        self.col_delete.addWidget(del_button)

        self.num_entries += 1


    def on_delete_entry(self, entry_num):
        # for row in self.right_vbox.children():
        #     row.takeAt(entry_num)
        self.right_vbox.takeAt(entry_num)

        self.num_entries -= 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("QLabel{letter-spacing: 2px; text-transform: uppercase; word-spacing: -4px;}")

    window = MainWindow()
    sys.exit(app.exec())

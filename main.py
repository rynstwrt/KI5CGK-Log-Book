import sys
import os
import json
from PySide6.QtCore import QDateTime, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QDateEdit,
                               QHBoxLayout, QVBoxLayout, QLabel,
                               QTimeEdit, QComboBox, QLineEdit,
                               QWidget, QSizePolicy, QTableWidget,
                               QPushButton, QTableWidgetItem, QFormLayout,
                               QHeaderView, QFileDialog)
from PySide6.QtGui import QIcon
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("KI5CGK Log Book")
        self.setWindowIcon(QIcon(os.path.abspath("Images/logo.png")))

        self.labels = ["DATE:", "TIME:", "CALL:", "FREQ:", "MODE:", "NAME:", "LOC:"]
        self.modes = ["/", "SSB", "CW", "AM",
                      "FM", "SSTV", "FT8", "FT4",
                      "Contestia", "Hellschreiber", "PACTOR", "PSK",
                      "QPSK", "8PSK", "PSKR", "RTTY",
                      "DominoEX", "FSQ", "IFKP", "MFSK",
                      "MT63", "OFDM", "Olivia", "THOR",
                      "Throb", "WEFAX", "Navtex/SitorB"]

        self.entries = []

        self.h_layout = None
        self.table = None

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

        form_section = QFormLayout()

        for label_text in self.labels:
            label = QLabel(label_text)
            label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

            if label_text == self.labels[0]:  # date
                self.date_input = QDateEdit(calendarPopup=True)
                current_date = QDateTime.currentDateTime().date()
                self.date_input.setDate(current_date)
                self.date_input.setMaximumDate(current_date)
                form = self.date_input
            elif label_text == self.labels[1]:  # time
                self.time_input = QTimeEdit()
                current_time = QDateTime.currentDateTime().time()
                self.time_input.setTime(current_time)
                self.time_input.setMaximumTime(current_time)
                form = self.time_input
            elif label_text == self.labels[2]:  # call sign
                self.call_sign_input = QLineEdit()
                form = self.call_sign_input
            elif label_text == self.labels[3]:  # frequency
                self.frequency_input = QLineEdit()
                form = self.frequency_input
            elif label_text == self.labels[4]:  # mode
                self.mode_input = QComboBox()
                self.mode_input.addItems(self.modes)
                form = self.mode_input
            elif label_text == self.labels[5]:  # name
                self.name_input = QLineEdit()
                form = self.name_input
            elif label_text == self.labels[6]:  # location
                self.location_input = QLineEdit()
                form = self.location_input

            form.setMinimumWidth(200)
            form.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            form_section.addRow(label, form)

        vert_section.addLayout(form_section)

        btn_row = QHBoxLayout()

        btn_add = QPushButton("ADD ENTRY")
        btn_add.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        btn_add.clicked.connect(self.on_add_button_clicked)

        btn_save = QPushButton("SAVE")
        btn_save.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        btn_save.clicked.connect(self.save_data)
        btn_row.addWidget(btn_save)

        btn_load = QPushButton("LOAD")
        btn_load.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        btn_load.clicked.connect(self.load_data)
        btn_row.addWidget(btn_load)

        btn_row.addWidget(btn_add)
        vert_section.addLayout(btn_row)

    def init_right_ui(self):
        self.table = QTableWidget(len(self.entries), len(self.labels) + 1)
        self.table.setMinimumWidth(800)

        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(self.labels + ["DEL:"])
        self.table.verticalHeader().setVisible(False)

        for i, entry in enumerate(self.entries):
            for j, entry_part in enumerate(entry):
                self.table.setItem(i, j, QTableWidgetItem(entry_part))

        self.h_layout.addWidget(self.table)

    def on_add_button_clicked(self):
        input_values = [self.date_input.date().toString("yyyy-MM-dd"),
                        self.time_input.time().toString("hh:mm"),
                        self.call_sign_input.text(),
                        self.frequency_input.text(),
                        self.mode_input.currentText(),
                        self.name_input.text(),
                        self.location_input.text()]

        values = []

        self.table.setRowCount(self.table.rowCount() + 1)

        for i, value in enumerate(input_values):
            if not value:
                value = "/"

            values.append(value)

            table_item = QTableWidgetItem(value)
            self.table.setItem(len(self.entries), i, table_item)
            table_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.entries += [values]

        del_button = QPushButton("DEL")
        # del_button.clicked.connect(lambda: self.on_delete_button_clicked(del_index))
        self.table.setCellWidget(len(self.entries), len(values), del_button)

        current_date = QDateTime.currentDateTime().date()
        self.date_input.setMaximumDate(current_date)
        self.date_input.setDate(current_date)

        current_time = QDateTime.currentDateTime().time()
        self.time_input.setMaximumTime(current_time)
        self.time_input.setTime(current_time)

        self.call_sign_input.clear()
        self.frequency_input.clear()
        self.mode_input.setCurrentIndex(0)
        self.name_input.clear()
        self.location_input.clear()

    def on_delete_button_clicked(self, index):
        print(index)
        self.table.removeRow(index)

    def load_data(self):
        with open("entries.json", "r") as file_read:
            json_data = json.load(file_read)

        self.entries = json_data["entries"]
        print(self.entries)

    def save_data(self):
        json_data = {"entries": []}
        for entry in self.entries:
            json_data["entries"] += [entry]

        with open("entries.json", "w") as file_write:
            json.dump(json_data, file_write)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    apply_stylesheet(app, theme="dark_cyan.xml")

    window = MainWindow()
    window.show()
    app.exec()

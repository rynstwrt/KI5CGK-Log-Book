import sys
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QPushButton,
                             QLabel,
                             QVBoxLayout,
                             QDateEdit,
                             QFormLayout,
                             QTimeEdit,
                             QLineEdit,
                             QScrollArea,)
from PyQt6.QtGui import (
    QFont,
    QFontDatabase,
    QIcon)
from PyQt6.QtCore import (
    Qt,
    QDateTime,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KI5CGK Log Book")
        self.setWindowIcon(QIcon("logo.png"))
        self.setStyleSheet("background-color: #24252b; color: white;")

        self.location_edit = None
        self.name_edit = None
        self.call_sign_edit = None
        self.mode_edit = None
        self.frequency_edit = None
        self.date_edit = None
        self.time_edit = None

        self.col_date = None
        self.col_time = None
        self.col_call_sign = None
        self.col_freq = None
        self.col_mode = None
        self.col_name = None
        self.col_location = None

        self.right_vbox = None
        self.scroll_area = None

        font_id = QFontDatabase.addApplicationFont("VT323-Regular.ttf")
        if font_id < 0:
            print("ERROR LOADING FONT")
        families = QFontDatabase.applicationFontFamilies(font_id)
        self.button_font = QFont(families[0], 20)
        self.header_font = QFont(families[0], 20)
        self.label_font = QFont(families[0], 20)

        self.entryList = []
        self.init_ui()


    def init_ui(self):
        layout = QHBoxLayout()


        # Left section
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

        self.frequency_edit = QLineEdit()
        self.mode_edit = QLineEdit()
        self.call_sign_edit = QLineEdit()
        self.name_edit = QLineEdit()
        self.location_edit = QLineEdit()

        label_style = "color: #ff885e;"

        date_label = QLabel("Date:")
        date_label.setFont(self.label_font)
        date_label.setStyleSheet(label_style)
        left_layout_form.addRow(date_label, self.date_edit)

        time_label = QLabel("Time:")
        time_label.setFont(self.label_font)
        time_label.setStyleSheet(label_style)
        left_layout_form.addRow(time_label, self.time_edit)

        call_sign_label = QLabel("Call Sign:")
        call_sign_label.setFont(self.label_font)
        call_sign_label.setStyleSheet(label_style)
        left_layout_form.addRow(call_sign_label, self.call_sign_edit)

        freq_label = QLabel("Frequency:")
        freq_label.setFont(self.label_font)
        freq_label.setStyleSheet(label_style)
        left_layout_form.addRow(freq_label, self.frequency_edit)

        mode_label = QLabel("Mode:")
        mode_label.setFont(self.label_font)
        mode_label.setStyleSheet(label_style)
        left_layout_form.addRow(mode_label, self.mode_edit)

        name_label = QLabel("Name:")
        name_label.setFont(self.label_font)
        name_label.setStyleSheet(label_style)
        left_layout_form.addRow(name_label, self.name_edit)

        loc_label = QLabel("Location:")
        loc_label.setFont(self.label_font)
        loc_label.setStyleSheet(label_style)
        left_layout_form.addRow(loc_label, self.location_edit)

        left_layout.addLayout(left_layout_form)

        btn_style = "background-color: #ff885e; color: black; border: 0; padding: 8px 8px; margin: 4px 0;"

        btn_add = QPushButton("ADD ENTRY")
        btn_add.setStyleSheet(btn_style)
        btn_add.setFont(self.button_font)
        left_layout.addWidget(btn_add)
        btn_add.clicked.connect(self.on_add_entry)

        layout.addLayout(left_layout)


        # Right section
        right_scroll_area = QScrollArea()
        right_widget = QWidget()
        self.right_vbox = QVBoxLayout()
        self.right_vbox.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.right_vbox.setContentsMargins(10, 10, 10, 10)

        right_hbox = QHBoxLayout()
        column_margins = [10, 0, 10, 0]

        self.col_date = QVBoxLayout()
        self.col_date.setContentsMargins(*column_margins)
        right_hbox.addLayout(self.col_date)

        self.col_time = QVBoxLayout()
        self.col_time.setContentsMargins(*column_margins)
        right_hbox.addLayout(self.col_time)

        self.col_freq = QVBoxLayout()
        self.col_freq.setContentsMargins(*column_margins)
        right_hbox.addLayout(self.col_freq)

        self.col_mode = QVBoxLayout()
        self.col_mode.setContentsMargins(*column_margins)
        right_hbox.addLayout(self.col_mode)

        self.col_call_sign = QVBoxLayout()
        self.col_call_sign.setContentsMargins(*column_margins)
        right_hbox.addLayout(self.col_call_sign)

        self.col_name = QVBoxLayout()
        self.col_name.setContentsMargins(*column_margins)
        right_hbox.addLayout(self.col_name)

        self.col_location = QVBoxLayout()
        self.col_location.setContentsMargins(*column_margins)
        right_hbox.addLayout(self.col_location)

        self.right_vbox.addLayout(right_hbox)
        right_widget.setLayout(self.right_vbox)

        right_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        right_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        right_scroll_area.setWidgetResizable(True)
        right_scroll_area.setMinimumWidth(500)
        right_scroll_area.setWidget(right_widget)

        layout.addWidget(right_scroll_area)


        # Display
        self.setLayout(layout)
        self.show()


    def on_add_entry(self):
        date = self.date_edit.date().toString("yyyy-MM-dd")
        t = self.time_edit.time().toString("hh:mm")
        freq = self.frequency_edit.text()
        mode = self.mode_edit.text()
        call_sign = self.call_sign_edit.text()
        name = self.name_edit.text()
        location = self.location_edit.text()

        values = []
        for value in [date, t, freq, mode, call_sign, name, location]:
            if not value:
                value = "N/A"
            values.append(value)

        self.col_date.addWidget(QLabel(values[0]))
        self.col_time.addWidget(QLabel(values[1]))
        self.col_freq.addWidget(QLabel(values[2]))
        self.col_mode.addWidget(QLabel(values[3]))
        self.col_call_sign.addWidget(QLabel(values[4]))
        self.col_name.addWidget(QLabel(values[5]))
        self.col_location.addWidget(QLabel(values[6]))

        # values =
        # final_string = ""
        # for i, value in enumerate(values):
        #     if not value:
        #         value = "N/A"
        #
        #     final_string += value
        #
        #     if i is not len(values):
        #         final_string += "    "
        #
        # self.right_vbox.addWidget(QLabel(final_string))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("QLabel{letter-spacing: 2px; text-transform: uppercase; word-spacing: -4px;}")
    window = MainWindow()

    sys.exit(app.exec())
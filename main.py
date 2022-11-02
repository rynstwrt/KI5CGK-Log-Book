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
                             QListView,)
from PyQt6.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QFont,
    QFontDatabase)
from PyQt6.QtCore import (
    Qt,
    QDateTime,
    QDate
)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log Book")
        self.setStyleSheet("background-color: #282c34; color: white;")

        self.location_edit = None
        self.name_edit = None
        self.call_sign_edit = None
        self.mode_edit = None
        self.frequency_edit = None
        self.date_edit = None
        self.time_edit = None

        id = QFontDatabase.addApplicationFont("VT323-Regular.ttf")
        if id < 0:
            print("ERROR LOADING FONT")
        families = QFontDatabase.applicationFontFamilies(id)
        self.button_font = QFont(families[0], 15)
        self.header_font = QFont(families[0], 20)
        self.label_font = QFont(families[0], 15)

        self.entryList = []
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()


        # Left section
        left_layout = QVBoxLayout()

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

        layout.addLayout(left_layout)



        # Middle spacer section
        spacer = QWidget()
        spacer.setLayout(QVBoxLayout())
        spacer.setMinimumWidth(50)
        layout.addWidget(spacer)


        # Right section
        right_layout = QVBoxLayout()

        btn_style = "background-color: #ff885e; color: black; border: 0; padding: 8px 8px;"

        btn_add = QPushButton("ADD ENTRY")
        btn_add.setStyleSheet(btn_style)
        btn_add.setFont(self.button_font)
        right_layout.addWidget(btn_add)
        btn_add.clicked.connect(self.on_add_entry)

        btn_del = QPushButton("DELETE SELECTED ENTRY")
        btn_del.setStyleSheet(btn_style + " margin: 10px 0 20px 0;")
        btn_del.setFont(self.button_font)
        right_layout.addWidget(btn_del)
        btn_del.clicked.connect(self.on_delete_entry)


        entry_label = QLabel("ENTRIES:")
        entry_label.setFont(self.header_font)
        entry_label.setStyleSheet("font-weight: bold; color: #ff885e;")
        entry_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        right_layout.addWidget(entry_label)

        entry_list_view = QListView()
        entry_list_model = QStandardItemModel()
        entry_list_view.setModel(entry_list_model)

        # for i in ["0", "10", "4"]:
        #     item = QStandardItem(i)
        #     entry_list_model.appendRow(item)

        right_layout.addWidget(entry_list_view)
        layout.addLayout(right_layout)


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

        print(date)
        print(t)
        print(freq)
        print(mode)
        print(call_sign)
        print(name)
        print(location)

        s = "   ".join([date, t, freq, mode, call_sign, name, location])



    def on_delete_entry(self):
        print("DEL")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("QLabel{letter-spacing: 2px; text-transform: uppercase; word-spacing: -4px;}")
    window = MainWindow()

    sys.exit(app.exec())
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
                             QListView)
from PyQt6.QtGui import (
    QStandardItemModel,
    QStandardItem)
from PyQt6.QtCore import (
    Qt,
    QDateTime,
    QDate
)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.location_edit = None
        self.name_edit = None
        self.call_sign_edit = None
        self.mode_edit = None
        self.frequency_edit = None
        self.date_edit = None
        self.time_edit = None

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

        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QDateTime.currentDateTime().time())

        self.frequency_edit = QLineEdit()

        self.mode_edit = QLineEdit()

        self.call_sign_edit = QLineEdit()

        self.name_edit = QLineEdit()

        self.location_edit = QLineEdit()

        left_layout_form.addRow("Date:", self.date_edit)
        left_layout_form.addRow("Time:", self.time_edit)
        left_layout_form.addRow("Frequency:", self.frequency_edit)
        left_layout_form.addRow("Mode:", self.mode_edit)
        left_layout_form.addRow("Call Sign:", self.call_sign_edit)
        left_layout_form.addRow("Name:", self.name_edit)
        left_layout_form.addRow("Location:", self.location_edit)
        left_layout.addLayout(left_layout_form)

        layout.addLayout(left_layout)


        # Right section
        right_layout = QVBoxLayout()

        btn_add = QPushButton("ADD ENTRY")
        right_layout.addWidget(btn_add)
        btn_add.clicked.connect(self.on_add_entry)

        btn_del = QPushButton("DELETE SELECTED ENTRY")
        right_layout.addWidget(btn_del)
        btn_del.clicked.connect(self.on_delete_entry)

        entry_label = QLabel("ENTRIES:")
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
        self.setWindowTitle("Log Book")
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
    window = MainWindow()
    sys.exit(app.exec())
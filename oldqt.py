# import sys
# from PyQt6.QtWidgets import (QApplication,
#                              QWidget,
#                              QHBoxLayout,
#                              QPushButton,
#                              QLabel,
#                              QVBoxLayout,
#                              QDateEdit,
#                              QFormLayout,
#                              QTimeEdit,
#                              QLineEdit,
#                              QListView)
# from PyQt6.QtGui import (
#     QStandardItemModel,
#     QStandardItem)
# from PyQt6.QtCore import (
#     Qt,
#     QDateTime,
#     QDate
# )
#
#
# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("Log Book")
#
# layout = QHBoxLayout()
# left_layout = QVBoxLayout()
# left_form = QFormLayout()
#
# left_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
# left_form.setFormAlignment(Qt.AlignmentFlag.AlignRight)
#
# date_edit = QDateEdit(calendarPopup=True)
# date_edit.setDateTime(QDateTime.currentDateTime())
#
# time_edit = QTimeEdit()
# time_edit.setTime(QDateTime.currentDateTime().time())
#
# left_form.addRow("Date:", date_edit)
# left_form.addRow("Time:", time_edit)
# left_form.addRow("Frequency:", QLineEdit())
# left_form.addRow("Mode:", QLineEdit())
# left_form.addRow("Call Sign:", QLineEdit())
# left_form.addRow("Name:", QLineEdit())
# left_form.addRow("Location:", QLineEdit())
# left_layout.addLayout(left_form)
#
# add_button = QPushButton("ADD ENTRY")
#
# def on_add_button_click():
#     print("TEST")
#
# def on_delete_button_click():
#     print("DEL")
#
# add_button.clicked.connect(on_add_button_click)
# left_layout.addWidget(add_button)
# delete_button = QPushButton("DELETE SELECTED ENTRY")
# delete_button.clicked.connect(on_delete_button_click)
# left_layout.addWidget(delete_button)
# layout.addLayout(left_layout)
#
# right_layout = QVBoxLayout()
# right_label = QLabel("ENTRIES:")
# right_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
# right_layout.addWidget(right_label)
#
# entry_list = QListView()
# entry_list_model = QStandardItemModel()
# entry_list.setModel(entry_list_model)
# items = ["1", "3", "5"]
# for i in items:
#     item = QStandardItem(i)
#     entry_list_model.appendRow(item)
#
# right_layout.addWidget(entry_list)
# layout.addLayout(right_layout)
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec())
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
                             QTextEdit)


app = QApplication([])
window = QWidget()
window.setWindowTitle("Log Book")

layout = QHBoxLayout()

left_layout = QFormLayout()
left_layout.addRow("Date", QDateEdit())
left_layout.addRow("Time", QTimeEdit())
left_layout.addRow("Frequency", QTextEdit())
left_layout.addRow("Mode", QTextEdit())
left_layout.addRow("Call Sign", QTextEdit())
left_layout.addRow("Name", QTextEdit())
left_layout.addRow("Location", QTextEdit())



layout.addLayout(left_layout)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
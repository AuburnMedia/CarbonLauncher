from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CarbonQT")


        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")


        layout = QHBoxLayout()
        layout.setSpacing(10)
        layout.addWidget(button1)
        layout.addWidget(button2)

        layoutHolder = QWidget()
        layoutHolder.setLayout(layout)

        self.setCentralWidget(layoutHolder)

        self.setMinimumSize(500,300)
    




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
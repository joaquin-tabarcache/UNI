import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ccxt
from red1 import convertir_audio


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent = parent)
        self.setFixedSize(500, 400)
        self.setWindowTitle("PDF to Audio")
        self.label_title = QLabel("PDF to Audio")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setFont(QFont("Script a", 30))
        self.label_title.setStyleSheet("color: #fff; background-color: #F78E69; border: none; border-radius: 10px;")
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)

        self.make_button = QPushButton("Convertir a Audio", self)
        self.make_button.clicked.connect(convertir_audio)
        layout.addWidget(self.make_button, alignment = Qt.AlignCenter)
        self.make_button.setFixedSize(200, 150)
        self.make_button.setObjectName("make_button")
        self.make_button.setStyleSheet("background-color: #8C001A;  border: none; border-radius: 6px; color: #fff; font-family: SFProText-Regular, Helvetica, Arial, sans-serif; font-size: 18px; line-height: 20px; margin-left: 20px; margin-right: 20px; padding: 0 16px 0 16px; color:white; font-weight: bold; min-width: 150px;")


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("background-color: #5D675B;")
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

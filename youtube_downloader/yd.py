from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from pytube import YouTube

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        #Ust ayarlar
        self.ustAyarlar()
        
        self.anaMenu()

        self.show()

    def anaMenu(self):
        widget = QWidget()

        h_box = QHBoxLayout()

        #TEMEL ELEMENTLER
        yazi = QLabel("<b>Youtube Linkini Giriniz</b>")
        self.link = QLineEdit()
        self.link.setPlaceholderText("https://www.youtube.com/watch?v=YRNyamyBOIQ")
        
        button = QPushButton("Indir")
        button.clicked.connect(self.indir)

        h_box.addWidget(yazi)
        h_box.addWidget(self.link)
        h_box.addWidget(button)

        widget.setLayout(h_box)

        self.setCentralWidget(widget)

    def ustAyarlar(self):
        self.setWindowTitle("Merhabalar aq youtube indirici")
        self.setWindowIcon(QIcon("logo.png"))

        #BOYUT AYARLARI
        self.setGeometry(250, 250, 600, 80)
        self.setMaximumSize(1000, 80)
        self.setMinimumSize(600, 80)

    def indir(self):
        url = self.link.text()
        YouTube(url).streams.first().download()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())

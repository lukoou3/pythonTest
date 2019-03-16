from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap

class Card(QLabel):
    def __init__(self, num = ""):
        super().__init__()
        if num == "":
            self.num = "2"
        else:
            self.num = num
        self.initui()

    def initui(self):
        path = "./res/pokercards/" + self.num + ".png"
        pixmap = QPixmap(path)
        self.setPixmap(pixmap)
        self.setScaledContents(True)
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QFrame
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400,300)
        self.setWindowTitle('学点编程吧')

        label = QLabel(self)
        label.resize(200,100)
        label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label.setText("first line\nsecond line")
        label.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(200, 150)
        self.setWindowTitle('小车快跑（滑动块）')

        self.sld1 = QSlider(Qt.Horizontal, self)
        self.sld1.setGeometry(30, 40, 100, 30)
        self.sld1.setMinimum(0)
        self.sld1.setMaximum(99)
        self.sld1.setTickPosition(QSlider.TicksLeft)

        self.sld2 = QSlider(Qt.Horizontal, self)
        self.sld2.setGeometry(30, 100, 100, 30)
        self.sld2.setMinimum(0)
        self.sld2.setMaximum(99)

        self.sld1.valueChanged[int].connect(self.changevalue)
        self.sld2.valueChanged[int].connect(self.changevalue)

        # self.label1 = QLabel(self)
        # self.label1.setPixmap(QPixmap('icon/01.jpg'))
        # self.label1.setGeometry(80,150,600,180)

        self.label2 = QLabel('滑动块1当前值: 0 ', self)
        self.label2.move(20, 10)

        self.label3 = QLabel('滑动块2当前值: 0 ', self)
        self.label3.move(20, 80)

        self.show()

    def changevalue(self, value):
        sender = self.sender()
        if sender == self.sld1:
            self.sld2.setValue(value)
        else:
            self.sld1.setValue(value)
        self.label2.setText('滑动块1当前值:' + str(value))
        self.label3.setText('滑动块2当前值:' + str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
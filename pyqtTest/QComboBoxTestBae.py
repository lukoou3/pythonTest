from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel
import sys

class ExComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 100)
        self.setWindowTitle("下拉框")
        self.show()

        label1 = QLabel("你可以选择", self)
        combox = QComboBox(self)
        self.combox = combox
        self.label2 = QLabel("a", self)
        self.label3 = QLabel("b", self)

        hlayout1 = QHBoxLayout()
        hlayout1.addStretch(1)
        hlayout1.addWidget(label1)
        hlayout1.addStretch(1)
        hlayout1.addWidget(combox)
        hlayout1.addStretch(1)

        hlayout2 = QHBoxLayout()
        hlayout2.addStretch(1)
        hlayout2.addWidget(self.label2)
        hlayout2.addStretch(1)
        hlayout2.addWidget(self.label3)
        hlayout2.addStretch(1)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)

        infomation = ["我想静静", "我要开始学习了", "我要开始睡觉了", "我要开始装B了"]

        combox.addItems(infomation)

        combox.currentIndexChanged.connect(self.selectionchange)
        combox.activated[str].connect(self.activated)

    def activated(self, text):
        self.label3.setText(text)

    def selectionchange(self,index):
        print(index)
        self.label2.setText(self.combox.currentText())

        for count in range(self.combox.count()):
            print('Item' + str(count) + '=' + self.combox.itemText(count))

        print('current index', self.combox.currentIndex(),
              'selection changed', self.combox.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExComboBox()
    sys.exit(app.exec_())
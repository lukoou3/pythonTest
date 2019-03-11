from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QRadioButton, QButtonGroup, QInputDialog, QPushButton
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(550,320)
        self.setWindowTitle('纯文本（QLabel）')

        self.lb1 = QLabel('学点编程吧，我爱你~！',self)
        self.lb1.setGeometry(0,0,550,50)
        
        self.lb2 = QLabel('我内容很少哦...',self)
        self.lb2.setGeometry(0,100,120,70)
        
        self.lb3 = QLabel('我内容很少哦...',self)
        self.lb3.setGeometry(0,190,120,70)
        self.lb3.setWordWrap(True)
        
        self.bt1 = QPushButton('输入内容1',self)
        self.bt1.move(0,150)
        
        self.bt2 = QPushButton('输入内容2',self)
        self.bt2.move(0,280)    
        
        self.ra1 = QRadioButton('左边',self)
        self.ra2 = QRadioButton('中间',self)
        self.ra3 = QRadioButton('右边',self)
        
        self.ra1.move(10,60)
        self.ra2.move(70,60)
        self.ra3.move(130,60)
        
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.ra1, 1)
        self.bg1.addButton(self.ra2, 2)
        self.bg1.addButton(self.ra3, 3)
        
        self.show()
        
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        

    def rbclicked(self):
        if self.bg1.checkedId() == 1:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        elif self.bg1.checkedId() == 2:
            self.lb1.setAlignment(Qt.AlignCenter)
        elif self.bg1.checkedId() == 3:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
    
    def showDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '内容1', '请输入内容1：')
            if ok:
                self.lb2.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '内容2', '请输入内容2：')
            if ok:
                self.lb3.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
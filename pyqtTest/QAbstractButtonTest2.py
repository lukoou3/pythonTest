#coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMessageBox
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--抽象按钮的学习2（QAbstractButton）')

        label1 = QLabel('密码输入区',self)
        label1.move(50,50)
        
        label2 = QLabel('正确密码：芝麻开门',self)
        label2.move(50,200)
        
        label3 = QLabel('你输入的密码：',self)
        label3.move(50,250)
        
        self.label4 = QLabel('        ',self)
        self.label4.move(150,250)
        
        self.bt1 = QPushButton('芝',self)
        self.bt2 = QPushButton('麻',self)
        self.bt3 = QPushButton('开',self)
        self.bt4 = QPushButton('门',self)
        
        self.bt1.setGeometry(150,50,40,40)
        self.bt3.setGeometry(200,50,40,40)
        self.bt2.setGeometry(150,100,40,40)
        self.bt4.setGeometry(200,100,40,40)
        
        self.bt1.setCheckable(True)
        self.bt2.setCheckable(True)
        self.bt3.setCheckable(True)
        self.bt4.setCheckable(True)
        
        self.show()
        
        self.password = ''
        
        self.bt1.clicked.connect(self.setPassword)
        self.bt2.clicked.connect(self.setPassword)
        self.bt3.clicked.connect(self.setPassword)
        self.bt4.clicked.connect(self.setPassword)
    
    def setPassword(self,pressed):
        word = self.sender().text()
        if pressed:
            if len(self.password) < 4:
                self.password += word
        else:
            self.password = self.password.replace(word,'')
            
        self.label4.setText(self.password)
        if len(self.password) == 4 and self.password == '芝麻开门':
            QMessageBox.information(self,'提示','恭喜，密码正确，可以进入！')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
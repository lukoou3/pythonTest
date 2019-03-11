#coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMessageBox, QButtonGroup
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,300)
        self.setWindowTitle('抽象按钮的学习3（QAbstractButton）')

        label1 = QLabel('密码输入区',self)
        label1.move(50,50)
        
        label2 = QLabel('正确密码：321',self)
        label2.move(50,200)
        
        label3 = QLabel('你输入的密码：',self)
        label3.move(50,250)
        
        self.label4 = QLabel('   ',self)
        self.label4.move(150,250)
        
        self.bt11 = QPushButton('1',self)
        self.bt12 = QPushButton('2',self)
        self.bt13 = QPushButton('3',self)
        self.bt21 = QPushButton('1',self)
        self.bt22 = QPushButton('2',self)
        self.bt23 = QPushButton('3',self)
        self.bt31 = QPushButton('1',self)
        self.bt32 = QPushButton('2',self)
        self.bt33 = QPushButton('3',self)
        
        self.bt11.setGeometry(150,50,40,40)
        self.bt12.setGeometry(200,50,40,40)
        self.bt13.setGeometry(250,50,40,40)
        self.bt21.setGeometry(150,100,40,40)
        self.bt22.setGeometry(200,100,40,40)
        self.bt23.setGeometry(250,100,40,40)
        self.bt31.setGeometry(150,150,40,40)
        self.bt32.setGeometry(200,150,40,40)
        self.bt33.setGeometry(250,150,40,40)
        
        self.btg1 = QButtonGroup(self)
        self.btg2 = QButtonGroup(self)
        self.btg3 = QButtonGroup(self)
        
        self.btg1.addButton(self.bt11,1)
        self.btg1.addButton(self.bt12,2)
        self.btg1.addButton(self.bt13,3)
        self.btg2.addButton(self.bt21,1)
        self.btg2.addButton(self.bt22,2)
        self.btg2.addButton(self.bt23,3)
        self.btg3.addButton(self.bt31,1)
        self.btg3.addButton(self.bt32,2)
        self.btg3.addButton(self.bt33,3)
        
        self.bt11.setCheckable(True)
        self.bt12.setCheckable(True)
        self.bt13.setCheckable(True)
        self.bt21.setCheckable(True)
        self.bt22.setCheckable(True)
        self.bt23.setCheckable(True)
        self.bt31.setCheckable(True)
        self.bt32.setCheckable(True)
        self.bt33.setCheckable(True)
        
        self.show()
        
        self.pwd1,self.pwd2,self.pwd3 = '','',''
        
        self.btg1.buttonClicked.connect(self.setPassword)
        self.btg2.buttonClicked.connect(self.setPassword)
        self.btg3.buttonClicked.connect(self.setPassword)
        
    def setPassword(self,pressed):
        sender = self.sender()
        if sender == self.btg1:
            self.pwd1 = str(self.btg1.checkedId())
        elif sender == self.btg2:
            self.pwd2 = str(self.btg2.checkedId())
        elif sender == self.btg3:
            self.pwd3 = str(self.btg3.checkedId())
            
        self.label4.setText(self.pwd1 + self.pwd2 + self.pwd3)
        
        if self.pwd1 + self.pwd2 + self.pwd3 == '321':
            QMessageBox.information(self,'提示','恭喜，密码正确，可以进入！')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
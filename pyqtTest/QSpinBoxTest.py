from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QSlider, QLabel, QMessageBox
from PyQt5.QtCore import QRegExp, Qt
import sys

class HolyShitBox(QSpinBox):
    def valueFromText(self,str):
        regExp = QRegExp("(\\d+)(\\s*[xx]\\s*\\d+)?")
        if regExp.exactMatch(str):
            return int(regExp.cap(1))
        else:
            return 0
    def textFromValue(self,num):
        return "{0} x {1}".format(num,num)
        
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350,280)
        self.setWindowTitle('学点编程吧--微调框')
        
        lb1 = QLabel('普通微调框',self)
        lb2 = QLabel('加强微调框',self)
        lb3 = QLabel('超神微调框',self)
        
        self.sp1 = QSpinBox(self)
        self.sp2 = QSpinBox(self)
        self.sp3 = HolyShitBox(self)
        
        self.sl = QSlider(Qt.Horizontal,self)
        
        self.sp1.move(130,30)
        self.sp2.move(130,70)
        self.sp3.move(130,100)
        
        lb1.move(30,32)
        lb2.move(30,70)
        lb3.move(30,100)
        
        self.sl.move(30,150)
        
        self.sp1.setRange(-10, 200)
        self.sp1.setSingleStep(10)
        self.sp1.setWrapping(True)
        self.sp1.setValue(-10)
        
        self.sp2.setRange(0, 100)
        self.sp2.setSingleStep(10)
        self.sp2.setValue(10)
        self.sp2.setPrefix("我的帅达到 ")
        self.sp2.setSuffix(" %，正在充帅中...")
        self.sp2.setSpecialValueText('我的帅达到渣的一逼')
        
        self.sp3.setRange(10, 50)
        self.sp3.setValue(10)
        self.sp3.setWrapping(True)
        
        self.sl.setRange(-10, 200)
        self.sl.setValue(-10)
        
        self.sp1.valueChanged.connect(self.slider1_changevalue)
        self.sp2.valueChanged.connect(self.slider2_changevalue)
        self.sl.valueChanged.connect(self.spinbox_changevalue)
        self.show()

    def slider1_changevalue(self,value):
        self.sl.setValue(value)
        
    def slider2_changevalue(self,value):
        if self.sp2.value() == self.sp2.maximum():
            QMessageBox.information(self,'提示','你怎么还再充帅，你不知道你的帅已经引起了别人的嫉妒吗？')
            self.sp2.setSuffix(" %,我踏马太帅了！！")
        elif self.sp2.minimum()< self.sp2.value() < self.sp2.maximum():
            self.sp2.setSuffix(" %，正在充帅中...")
            
    def spinbox_changevalue(self,value):
        self.sp1.setValue(value)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
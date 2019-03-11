from PyQt5.QtWidgets import QWidget, QApplication, QDoubleSpinBox, QLabel, QSlider
from PyQt5.QtCore import Qt
import sys
        
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(370,190)
        self.setWindowTitle('小数微调框')
        
        self.sp = QDoubleSpinBox(self)
        self.sp.setGeometry(10,50,100,20)
        self.sp.setRange(0,20)
        self.sp.setSingleStep(0.1)
        
        self.lb = QLabel("QDoubleSpinBox精度设置为：2",self)
        self.lb.move(120,50)

        self.sl = QSlider(Qt.Vertical,self)
        self.sl.setGeometry(300,30,30,100)
        self.sl.setRange(0,9)
        self.sl.setValue(0)
        self.sl.setTickPosition(QSlider.TicksBelow)
        
        self.sl.valueChanged.connect(self.spinbox_changevalue)
        self.show()
        
    def spinbox_changevalue(self,value):
        if value <= 7:
            self.lb.setText("QDoubleSpinBox精度设置为:" + str(value+2))
            self.sp.setDecimals(value+2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime
from PyQt5.QtGui import QFont
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(370,190)
        self.setWindowTitle('LCD数字')

        self.lcd = QLCDNumber(self)
        lb = QLabel("距离2022年北京-张家口冬季奥林匹克运动会还有",self)
        ft = QFont()
        ft.setPointSize(15)
        lb.setFont(ft)
        vbox = QVBoxLayout(self)
        vbox.addWidget(lb)
        vbox.addWidget(self.lcd)

        self.lcd.setDigitCount(13)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setStyleSheet("border: 2px solid black; color: red; background: silver;")

        time = QTimer(self)
        time.setInterval(1000)
        time.timeout.connect(self.refresh)
        time.start()

        self.show()

    def refresh(self):
        startDate = QDateTime.currentMSecsSinceEpoch()
        endDate = QDateTime(QDate(2022, 2, 4), QTime(0, 0, 0)).toMSecsSinceEpoch()
        interval = endDate - startDate
        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec)
            self.lcd.display(intervals)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
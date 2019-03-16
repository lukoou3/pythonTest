from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle(self.tr("依靠窗口"))

        te = QTextEdit("主窗口")
        te.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(te)

        # 停靠窗口1
        dock1 = QDockWidget("停靠窗口1", self)
        dock1.setFeatures(QDockWidget.DockWidgetMovable)
        dock1.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        te1 = QTextEdit("窗口1,可在Main Window的左部和右部停靠，不可浮动，不可关闭")
        dock1.setWidget(te1)
        self.addDockWidget(Qt.RightDockWidgetArea, dock1)

        # 停靠窗口2
        dock2 = QDockWidget("停靠窗口2", self)
        dock2.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        te2 = QTextEdit("窗口2,只可浮动")
        dock2.setWidget(te2)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        # 停靠窗口3
        dock3 = QDockWidget("停靠窗口3", self)
        dock3.setFeatures(QDockWidget.AllDockWidgetFeatures)
        te3 = QTextEdit("窗口3,可在Main Window任意位置停靠，可浮动，可关闭")
        dock3.setWidget(te3)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock3)

app = QApplication(sys.argv)
main = MainWidget()
main.show()
app.exec_()
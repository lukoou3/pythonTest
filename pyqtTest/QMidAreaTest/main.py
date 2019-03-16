from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea, QMdiSubWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pyqtTest.QMidAreaTest.card import Card
import sys
import random

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('扑克牌模拟')

        self.mid = QMdiArea()
        self.setCentralWidget(self.mid)

        sendOnecardAct = QAction(QIcon('./res/sendOnecard.ico'), '发1张牌', self)
        sendOnecardAct.triggered.connect(self.sendOnecard)

        sendFivecardsAct = QAction(QIcon('./res/sendFivecard.ico'), '随机5张牌', self)
        sendFivecardsAct.triggered.connect(self.sendFivecards)

        clearcardAct = QAction(QIcon('./res/clear.ico'), '清除牌', self)
        clearcardAct.triggered.connect(self.clearCards)

        foldcardAct = QAction(QIcon('./res/fold.ico'), '收牌', self)
        foldcardAct.triggered.connect(self.foldCards)

        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(sendOnecardAct)
        toolbar.addAction(sendFivecardsAct)
        toolbar.addAction(clearcardAct)
        toolbar.addAction(foldcardAct)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    
    def sendOnecard(self):
        randomflag = self.randomsend(1)
        subcard = QMdiSubWindow()
        subcard.setWidget(Card(randomflag))
        self.mid.addSubWindow(subcard)
        subcard.setWindowFlags(Qt.WindowMinimizeButtonHint)
        subcard.show()
    
    def sendFivecards(self):
        randomflag = self.randomsend(5)
        for card in randomflag:
            subcard = QMdiSubWindow()
            subcard.setWidget(Card(card))
            self.mid.addSubWindow(subcard)
            subcard.setWindowFlags(Qt.WindowMinimizeButtonHint)
            subcard.show()
        
    def clearCards(self):
        self.mid.closeAllSubWindows()

    def foldCards(self):
        self.mid.cascadeSubWindows()
    
    def randomsend(self, num):
        cardlist = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "j", "joker", "k", "q"]
        if num == 1:
            return random.choice(cardlist)
        elif num == 5:
            return random.sample(cardlist, 5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
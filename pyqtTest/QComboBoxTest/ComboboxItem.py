from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication, QToolButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QEvent, QObject, pyqtSignal
import sys
import codecs

class ComboBoxItem(QWidget):

    itemOpSignal = pyqtSignal(str)

    def __init__(self, qq, username, user_icon):
        super().__init__()
        self.username = username
        self.qq = qq
        self.user_icon = user_icon
        self. initUi()

    def initUi(self):
        lb_username = QLabel(self.username, self)
        lb_qq = QLabel(self.qq, self)
        lb_icon = QLabel(self)
        lb_icon.setPixmap(QPixmap(self.user_icon))
        self.bt_close = QToolButton(self)
        self.bt_close.setIcon(QIcon("res/close.png"))
        self.bt_close.setAutoRaise(True)

        vlayout = QVBoxLayout()
        vlayout.addWidget(lb_username)
        vlayout.addWidget(lb_qq)

        hlayout = QHBoxLayout()
        hlayout.addWidget(lb_icon)
        hlayout.addLayout(vlayout)
        hlayout.addStretch(1)
        hlayout.addWidget(self.bt_close)
        hlayout.setContentsMargins(5, 5, 5, 5)
        hlayout.setSpacing(5)

        self.setLayout(hlayout)

        self.bt_close.installEventFilter(self)
        self.installEventFilter(self)

    def eventFilter(self, object, event):
        if object is self:
            if event.type() == QEvent.Enter:
                self.setStyleSheet("QWidget{color:white}")
            elif event.type() == QEvent.Leave:
                self.setStyleSheet("QWidget{color:black}")
        elif object is self.bt_close:
            if event.type() == QEvent.MouseButtonPress:  
                self.itemOpSignal.emit(self.qq)
        return QWidget.eventFilter(self, object, event)
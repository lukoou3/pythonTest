from PyQt5.QtWidgets import QWidget, QApplication, QToolButton, QMenu, QAction
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.resize(400,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--工具按钮（QToolButton）')

        tb = QToolButton(self)
        tb.move(100,100)
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # tb.setArrowType(Qt.DownArrow)
        tb.setPopupMode(QToolButton.InstantPopup)
        tb.setText('支付方式')
        tb.setIcon(QIcon('icon/bank.ico'))
        tb.setAutoRaise(True)
       
        menu = QMenu(self)
        self.alipayAct = QAction(QIcon('icon/alipay.ico'),'支付宝支付', self)
        self.wechatAct = QAction(QIcon('icon/wechat.ico'),'微信支付', self)
        self.visaAct = QAction(QIcon('icon/visa.ico'),'Visa卡支付', self)
        self.master_cardAct = QAction(QIcon('icon/master_card.ico'),'万事达卡支付', self)
        menu.addAction(self.alipayAct)
        menu.addAction(self.wechatAct)
        menu.addSeparator()
        menu.addAction(self.visaAct)
        menu.addAction(self.master_cardAct)
        
        tb.setMenu(menu)
        self.show()
         
        self.alipayAct.triggered.connect(self.on_click)
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)
        self.master_cardAct.triggered.connect(self.on_click)

    def on_click(self):
        if self.sender() == self.alipayAct:
            QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
        elif self.sender() == self.wechatAct:
            QDesktopServices.openUrl(QUrl('https://pay.weixin.qq.com/index.php'))
        elif self.sender() == self.visaAct:
            QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
        else:
            QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
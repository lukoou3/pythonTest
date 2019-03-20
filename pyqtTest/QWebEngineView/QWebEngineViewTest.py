from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QObject, pyqtSlot, QUrl,pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
import os
import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 480)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QPlainTextEdit(Form)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setReadOnly(True)
        self.label.appendPlainText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setObjectName("pushButton1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.pushButton1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.webView = QWebEngineView(Form)
        #self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webView.setMinimumSize(QtCore.QSize(500, 0))
        self.horizontalLayout.addWidget(self.webView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "web"))
        self.pushButton.setText(_translate("Form", "发送(run js)"))
        self.pushButton1.setText(_translate("Form", "发送(信号槽)"))

class JsConnect(QObject):
    signalFromJS = pyqtSignal(dict)
    signalToJS = pyqtSignal(str)

    def sendMessageToJS(self, msg):
        self.signalToJS.emit(msg)

    @pyqtSlot(str)
    def sendMessageFromJS(self, msg):
        print('sendMessageFromJS:{}'.format(msg))
        self.signalFromJS.emit(json.loads(msg))

    @pyqtSlot(list,result=str)
    def publicFunction(self, msg):
        print('sendMessageFromJS2:{}'.format(msg[0]))
        return msg[0]

    @pyqtSlot(str,result=list)
    def publicFun(self,msg):
        print('sendMessageFromJS3{}'.format(msg))
        #return "ssss"
        return ["ssss",1,"344"]

class Ui_Main(QtWidgets.QWidget,Ui_Form):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #self.init()

    def init(self):
        channel = QWebChannel()
        jsConnect = JsConnect()
        channel.registerObject('connect', jsConnect)
        self.webView.page().setWebChannel(channel)

        jsConnect.signalFromJS.connect(self.onReceiveMessageFromJS)
        self.jsConnect = jsConnect

        if True:
            print( "file:///{}".format(os.path.abspath("QWebEngineView_page.html")) )
            self.webView.load(QUrl("file:///D:/pycharmWork/pythonTest/pyqtTest/QWebEngineView/QWebEngineView_page.html"))
        else:
            with open("./QWebEngineView_page.html") as fp:
                html = fp.read()
                self.webView.setHtml(html)

        self.pushButton.clicked.connect(self.sendMessageToJS)
        self.pushButton1.clicked.connect(self.sendMessageByRunJavaScript)

    def aa(self):
        if True:
            print("file:///{}".format(os.path.abspath("QWebEngineView_page.html")))
            #self.webView.load(QUrl("file:///D:/pycharmWork/pythonTest/pyqtTest/QWebEngineView/QWebEngineView_page.html"))
            self.webView.setUrl(QUrl.fromLocalFile(os.path.abspath("QWebEngineView_page.html")))
        else:
            with open("./QWebEngineView_page.html") as fp:
                html = fp.read()
                self.webView.setHtml(html)

        self.pushButton.clicked.connect(self.sendMessageToJS)
        self.pushButton1.clicked.connect(self.sendMessageByRunJavaScript)

    def sendMessageToJS(self):
        msg = self.lineEdit.text()
        self.jsConnect.sendMessageToJS(json.dumps({"msg":msg}))
        self.lineEdit.setText("")

    def onReceiveMessageFromJS(self,msg):
        self.label.appendPlainText(str(msg))

    def sendMessageByRunJavaScript(self):
        msg = self.lineEdit.text()
        self.webView.page().runJavaScript("""receiveMsg(JSON.stringify({}));""".format(json.dumps({"msg":msg})))
        self.lineEdit.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Ui_Main()
    widget.show()

    if False:
        channel = QWebChannel()
        jsConnect = JsConnect()
        channel.registerObject('connect', jsConnect)
        widget.webView.page().setWebChannel(channel)

        jsConnect.signalFromJS.connect(widget.onReceiveMessageFromJS)
        widget.jsConnect = jsConnect

        if True:
            print("file:///{}".format(os.path.abspath("QWebEngineView_page.html")))
            widget.webView.load(QUrl("file:///D:/pycharmWork/pythonTest/pyqtTest/QWebEngineView/QWebEngineView_page.html"))
        else:
            with open("./QWebEngineView_page.html") as fp:
                html = fp.read()
                widget.webView.setHtml(html)

        widget.pushButton.clicked.connect(widget.sendMessageToJS)
        widget.pushButton1.clicked.connect(widget.sendMessageByRunJavaScript)
    else:
        widget.aa()

        channel = QWebChannel()
        jsConnect = JsConnect()
        channel.registerObject('connect', jsConnect)
        widget.webView.page().setWebChannel(channel)

        jsConnect.signalFromJS.connect(widget.onReceiveMessageFromJS)
        widget.jsConnect = jsConnect
        pass





    sys.exit(app.exec_())

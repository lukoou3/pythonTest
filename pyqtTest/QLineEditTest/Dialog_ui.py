from PyQt5.QtCore import pyqtSlot, QEvent, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QCompleter
from PyQt5.QtGui import QStandardItemModel, QKeyEvent, QKeySequence
import sys, re
from pyqtTest.QLineEditTest.Ui_UI import Ui_Dialog

class Dialog_ui(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widgets
        @type QWidget
        """
        super(Dialog_ui, self).__init__(parent)
        self.setupUi(self)
        self.ActionStart()
    
    def ActionStart(self):
        self.lineEdit_2.installEventFilter(self)
        self.lineEdit_3.installEventFilter(self)
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.m_model = QStandardItemModel(0, 1, self)
        m_completer = QCompleter(self.m_model, self)
        self.lineEdit_7.setCompleter(m_completer)
        m_completer.activated[str].connect(self.onEmailChoosed)
    
    def onEmailChoosed(self, email):
        self.lineEdit_7.setText(email)
            
    def eventFilter(self, object, event):
        if object == self.lineEdit_2:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        elif object == self.lineEdit_3:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)

    @pyqtSlot()
    def on_lineEdit_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        regex_user = '^[a-zA-Z]\w{5,17}$'
        username = self.lineEdit.text()
        if len(username) > 0:
            self.lineEdit_6.clear()
            rruser = re.compile(regex_user)
            if rruser.match(username) is None:
                self.lineEdit_6.setText('用户名不符合要求!')
        else:
            self.lineEdit_6.setText('用户名未填写!')
    
    @pyqtSlot()
    def on_lineEdit_2_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        regex_pwd = "^([A-Z]|[a-z]|[0-9]|[`~!@#$%^&*()+=|{}':;',\\\\[\\\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“'。，、？]){6,16}$"
        self.pwd1 = self.lineEdit_2.GetPassword()
        if len(self.pwd1) > 0:
            self.lineEdit_6.clear()
            rrpwd = re.compile(regex_pwd)
            if rrpwd.match(self.pwd1) is None:
                self.lineEdit_6.setText('密码不符合要求!')
        else:
            self.lineEdit_6.setText('密码未填写!')

    
    @pyqtSlot()
    def on_lineEdit_3_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.pwd2 = self.lineEdit_3.GetPassword()
        regex_pwd = "^([A-Z]|[a-z]|[0-9]|[`~!@#$%^&*()+=|{}':;',\\\\[\\\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“'。，、？]){6,16}$"
        if len(self.pwd2) > 0:
            self.lineEdit_6.clear()
            rrpwd = re.compile(regex_pwd)
            if rrpwd.match(self.pwd2) is None:
                self.lineEdit_6.setText('密码不符合要求!')
            if self.pwd1 != self.pwd2:
                self.lineEdit_6.setText('两次密码不一致!')
        else:
            self.lineEdit_6.setText('密码未填写!')


    @pyqtSlot()
    def on_lineEdit_4_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        regex_phone = '^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$'
        phone = self.lineEdit_4.text()
        if len(phone) > 0:
            self.lineEdit_6.clear()
            rr1 = re.compile(regex_phone)
            if rr1.match(phone) is None:
                self.lineEdit_6.setText('请填写正确的手机号!')
        else:
            self.lineEdit_6.setText('手机号码未填写!')
    
    @pyqtSlot()
    def on_lineEdit_7_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        regex_mail = '^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$'
        email = self.lineEdit_7.text()
        if len(email) > 0:
            self.lineEdit_6.clear()
            rr1 = re.compile(regex_mail)
            if rr1.match(email) is None:
                self.lineEdit_6.setText('请填写正确的邮箱地址!')
        else:
            self.lineEdit_6.setText('邮箱地址未填写!')

    @pyqtSlot(str)
    def on_lineEdit_7_textChanged(self, text):

        if '@' in self.lineEdit_7.text():
            return

        emaillist = [ "@163.com" , "@qq.com" , "@gmail.com" , "@live.com" , "@126.com", "@139.com"]

        self.m_model.removeRows(0, self.m_model.rowCount())

        for i in range(0, len(emaillist)):
            self.m_model.insertRow(0)
            self.m_model.setData(self.m_model.index(0, 0), text + emaillist[i])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dg = Dialog_ui()
    dg.show()
    sys.exit(app.exec_())

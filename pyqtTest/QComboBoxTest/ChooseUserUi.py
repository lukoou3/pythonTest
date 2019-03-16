# -*- coding: utf-8 -*-

"""
Module implementing ChooseUser.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QListWidget, QListWidgetItem
from pyqtTest.QComboBoxTest.AddUser import DialogAddUser
from pyqtTest.QComboBoxTest.ComboboxItem import ComboBoxItem
from pyqtTest.QComboBoxTest.Ui_ui import Ui_Dialog
import sys
import codecs

class ChooseUser(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    storage_qq = []


    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ChooseUser, self).__init__(parent)
        self.setupUi(self)
        self.setmode()
    
    def setmode(self):
        with codecs.open("res/qcombobox.qss", "r", "utf-8") as f:
            styleSheet = f.readlines()
        style = '\r\n'.join(styleSheet)
        self.comboBox.setStyleSheet(style)

        self.listw = QListWidget()
        self.comboBox.setModel(self.listw.model())
        self.comboBox.setView(self.listw)
    
    @pyqtSlot()
    def on_toolButton_clicked(self):
        """
        新增联系人
        """
        user = DialogAddUser()
        r = user.exec_()
        if r > 0:
            qq, username, user_icon = user.get_userinfo()
            item =  ComboBoxItem(qq, username, user_icon)
            item.itemOpSignal.connect(self.itemOp)
            self.storage_qq.append(qq)
            self.listwitem = QListWidgetItem(self.listw)
            self.listw.setItemWidget(self.listwitem, item)
    
    def itemOp(self, qq):
        """
        删除联系人
        """
        indexqq = self.storage_qq.index(qq)
        self.listw.takeItem(indexqq)
        del self.storage_qq[indexqq]
    
    @pyqtSlot(int)
    def on_comboBox_activated(self, p0):
        """
        将item的索引带过来，选择显示QQ号
        """
        qq = self.storage_qq[p0]
        self.comboBox.setEditText(qq)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ChooseUser()
    ex.show()
    sys.exit(app .exec_())
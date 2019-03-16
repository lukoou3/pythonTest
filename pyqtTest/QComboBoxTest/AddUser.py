# -*- coding: utf-8 -*-

"""
Module implementing DialogAddUser.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from pyqtTest.QComboBoxTest.Ui_adduser import Ui_Dialog
from pyqtTest.QComboBoxTest import Random_Name
import random

class DialogAddUser(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogAddUser, self).__init__(parent)
        self.setupUi(self)
        self.username = Random_Name.getname()
        self.iconpath = "res/user/default.jpg"
        self.qq = str(random.randint(33333333,88888888))
    
    @pyqtSlot(bool)
    def on_radioButton_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        self.lineEdit.setEnabled(False)
    
    @pyqtSlot(bool)
    def on_radioButton_2_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        self.lineEdit.setEnabled(True)
    
    @pyqtSlot(bool)
    def on_radioButton_3_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.pushButton.setEnabled(False)
    
    @pyqtSlot(bool)
    def on_radioButton_4_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        self.pushButton.setEnabled(True)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        file = QFileDialog.getOpenFileName(self, "打开文件", "res/user/", ("Images (*.png *jpg)"))
        if file[0]:
            self.iconpath = file[0]
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.lineEdit.isEnabled() and self.lineEdit.text() == "":
            QMessageBox.warning(self, "警告", "联系人姓名为空")
            self.lineEdit.setFocus()
        else:
            self.done(1)
    
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.done(-1)

    @pyqtSlot()
    def on_lineEdit_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.username = self.lineEdit.text()
    
    def get_userinfo(self):
        return self.qq, self.username, self.iconpath
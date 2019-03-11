# -*- coding: utf-8 -*-

"""
Module implementing Dialog_mainnetwork.
"""

from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtGui import QImage, QTextDocument
from pyqtTest.markdown_pro.Ui_mainnetwork import Ui_Dialog
import requests,sys
from PIL import Image
from io import BytesIO


class Dialog_mainnetwork(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog_mainnetwork, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        
        response = requests.get(self.lineEdit.text())
        image1 = Image.open(BytesIO(response.content))
        image1.save('xxx.png')
        del image1
        image = QImage('xxx.png')
        cursor = self.textEdit.textCursor()
        document = self.textEdit.document()
        document.addResource(QTextDocument.ImageResource, QUrl("image"), image)
        cursor.insertImage("image")
        
        # self.textEdit.append("<img src=\"xxx.png\" />")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    dg = Dialog_mainnetwork()
    dg.show()
    sys.exit(app.exec_())


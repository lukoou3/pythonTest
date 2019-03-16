# -*- coding: utf-8 -*-

"""
Module implementing showTab.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from pyqtTest.QTabWidgetTest.Ui_showeather import Ui_Tab


class showTab(QWidget, Ui_Tab):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(showTab, self).__init__(parent)
        self.setupUi(self)

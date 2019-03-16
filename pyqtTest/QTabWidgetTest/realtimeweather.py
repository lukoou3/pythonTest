# -*- coding: utf-8 -*-

"""
Module implementing RealTimeWeather.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from pyqtTest.QTabWidgetTest.Ui_realtimew import Ui_RealTime


class RealTimeWeather(QWidget, Ui_RealTime):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(RealTimeWeather, self).__init__(parent)
        self.setupUi(self)

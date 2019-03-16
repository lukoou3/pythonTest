# -*- coding: utf-8 -*-

"""
Module implementing Weather.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget,  QApplication
from PyQt5.QtGui import QPixmap
from pyqtTest.QTabWidgetTest.Ui_main import Ui_Form
from pyqtTest.QTabWidgetTest.showtab import showTab
from pyqtTest.QTabWidgetTest.realtimeweather import RealTimeWeather
from pyqtTest.QTabWidgetTest.getweather import GetWeatherInfo
import sys

class Weather(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Weather, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.flag = 0
    
    def initUi(self):
        cities = ["北京", "上海", "广州"]
        self.comboBox.addItems(cities)

        self.showrealweather()

    @pyqtSlot(bool)
    def on_radioButton_toggled(self, checked):
        """
        实时天气
        """
        self.flag = 0
    
    @pyqtSlot(bool)
    def on_radioButton_2_toggled(self, checked):
        """
        近3天天气
        """
        self.flag = 1
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        查询天气
        """
        if self.flag == 0:
            self.showrealweather() 
        else:
            t0, t1, t2, d0, d1, d2 = self.showeather()
            self.tabWidget.addTab(t0, d0)
            self.tabWidget.addTab(t1, d1)
            self.tabWidget.addTab(t2, d2)

    def showrealweather(self):
            city = self.comboBox.currentText()
            ww = GetWeatherInfo(0, city)
            weather, weather_code, weather_temperature, last_update = ww.getweather()
            msg = RealTimeWeather()
            msg.label_tt.setText(weather)
            msg.label_ww.setText(weather_temperature)
            msg.label_icon.setPixmap(QPixmap("./res/" + weather_code + ".png"))
            update = "天气最新更新时间--" + last_update[11:16]
            self.tabWidget.clear()
            self.tabWidget.addTab(msg, update)

    def showeather(self):
        city = self.comboBox.currentText()
        ww = GetWeatherInfo(1, city)
        self.tabWidget.clear()
        weather0, weather1, weather2 = ww.getweather()
        tabwidget0 = showTab()
        tabwidget0.label_wb.setText(weather0["text_day"])
        tabwidget0.label_tb.setPixmap(QPixmap("./res/" + weather0["code_day"] + ".png"))
        tabwidget0.label_wn.setText(weather0["text_night"])
        tabwidget0.label_tw.setPixmap(QPixmap("./res/" + weather0["code_night"] + ".png"))
        tabwidget0.label_tg.setText(weather0["high"])
        tabwidget0.label_tl.setText(weather0["low"])
        tabwidget0.label_fx.setText(weather0["wind_direction"])
        tabwidget0.label_fl.setText(weather0["wind_scale"])

        tabwidget1 = showTab()
        tabwidget1.label_wb.setText(weather1["text_day"])
        tabwidget1.label_tb.setPixmap(QPixmap("./res/" + weather1["code_day"] + ".png"))
        tabwidget1.label_wn.setText(weather1["text_night"])
        tabwidget1.label_tw.setPixmap(QPixmap("./res/" + weather1["code_night"] + ".png"))
        tabwidget1.label_tg.setText(weather1["high"])
        tabwidget1.label_tl.setText(weather1["low"])
        tabwidget1.label_fx.setText(weather1["wind_direction"])
        tabwidget1.label_fl.setText(weather1["wind_scale"])

        tabwidget2 = showTab()
        tabwidget2.label_wb.setText(weather2["text_day"])
        tabwidget2.label_tb.setPixmap(QPixmap("./res/" + weather2["code_day"] + ".png"))
        tabwidget2.label_wn.setText(weather2["text_night"])
        tabwidget2.label_tw.setPixmap(QPixmap("./res/" + weather2["code_night"] + ".png"))
        tabwidget2.label_tg.setText(weather2["high"])
        tabwidget2.label_tl.setText(weather2["low"])
        tabwidget2.label_fx.setText(weather2["wind_direction"])
        tabwidget2.label_fl.setText(weather2["wind_scale"])
        return tabwidget0, tabwidget1, tabwidget2, weather0["date"], weather1["date"], weather2["date"]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    we  = Weather()
    we.show()
    sys.exit(app.exec_())

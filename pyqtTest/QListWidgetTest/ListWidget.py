#coding=utf-8

from PyQt5.QtWidgets import QListWidget, QMenu, QAction, QMessageBox, QListWidgetItem, QAbstractItemView
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont, QBrush
from pyqtTest.QListWidgetTest.Dialog_additem import Dialog_additem
from pyqtTest.QListWidgetTest import Random_Name
import random
import sys

class ListWidget(QListWidget):

    map_listwidget = []

    def __init__(self):
        super().__init__()
        self.Data_init()
        self.Ui_init()

    def Data_init(self):
        randomnum = random.sample(range(26), 10)
        for i in randomnum:
            item = QListWidgetItem()
            randname = Random_Name.getname()
            randicon = "./res/"+ str(i) + ".jpg"
            font = QFont()
            font.setPointSize(16)
            item.setFont(font)
            item.setText(randname)
            flag = random.randint(0,5)
            if flag == 1:
                item.setForeground(QBrush(Qt.red))
                item.setToolTip('会员红名尊享')
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            item.setIcon(QIcon(randicon))
            self.addItem(item)
    
    def Ui_init(self):
        self.setIconSize(QSize(70,70))
        self.setStyleSheet("QListWidget{border:1px solid gray; color:black; }"
                        "QListWidget::Item{padding-top:20px; padding-bottom:4px; }"
                        "QListWidget::Item:hover{background:skyblue; }"
                        "QListWidget::item:selected:!active{border-width:0px; background:lightgreen; }"
                        )
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.itemSelectionChanged.connect(self.getListitems)
    
    def getListitems(self):
        return self.selectedItems()

    def contextMenuEvent(self, event):
        hitIndex = self.indexAt(event.pos()).column()
        if hitIndex > -1:
            pmenu = QMenu(self)
            pDeleteAct = QAction("删除",pmenu)
            pmenu.addAction(pDeleteAct)
            pDeleteAct.triggered.connect(self.deleteItemSlot)
            if self is self.find('我的好友'):
                pAddItem = QAction("新增好友",pmenu)
                pmenu.addAction(pAddItem)     
                pAddItem.triggered.connect(self.addItemSlot)
            if len(self.map_listwidget) > 1:
                pSubMenu = QMenu("转移联系人至" ,pmenu)
                pmenu.addMenu(pSubMenu)
                for item_dic in self.map_listwidget:
                    if item_dic['listwidget'] is not self:
                        pMoveAct = QAction(item_dic['groupname'] ,pmenu)
                        pSubMenu.addAction(pMoveAct)
                        pMoveAct.triggered.connect(self.move)
            pmenu.popup(self.mapToGlobal(event.pos()))
    
    def deleteItemSlot(self):
        dellist = self.getListitems()
        for delitem in dellist:
            del_item = self.takeItem(self.row(delitem))
            del del_item

    def addItemSlot(self):
        dg = Dialog_additem()
        r = dg.exec()
        if r > 0:
            newitem = QListWidgetItem()
            newname = dg.lineEdit.text()
            newicon = dg.geticonpath()
            font = QFont()
            font.setPointSize(16)
            newitem.setFont(font)
            newitem.setText(newname)
            newitem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            newitem.setIcon(QIcon(newicon))
            self.addItem(newitem)

    def setListMap(self, listwidget):
        self.map_listwidget.append(listwidget)

    def move(self):
        tolistwidget = self.find(self.sender().text())
        movelist = self.getListitems()
        for moveitem in movelist:
            pItem = self.takeItem(self.row(moveitem))
            tolistwidget.addItem(pItem)

    def find(self, pmenuname):
        for item_dic in self.map_listwidget:
            if item_dic['groupname'] == pmenuname:
                return item_dic['listwidget']
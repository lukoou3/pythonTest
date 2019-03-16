#coding=utf-8

from PyQt5.QtWidgets import QListView, QMenu, QAction, QMessageBox
#from PyQt5.QtCore import QSize
from pyqtTest.QListViewTest.ListModel import ListModel

class ListView(QListView):

    map_listview = []

    def __init__(self):
        super().__init__()
        self.m_pModel = ListModel()  
        self.setModel(self.m_pModel)
        
    def contextMenuEvent(self, event):
        hitIndex = self.indexAt(event.pos()).column()
        if hitIndex > -1:
            pmenu = QMenu(self)
            pDeleteAct = QAction("删除",pmenu)
            pmenu.addAction(pDeleteAct)
            pDeleteAct.triggered.connect(self.deleteItemSlot)
            pSubMenu = QMenu("转移联系人至" ,pmenu)
            pmenu.addMenu(pSubMenu)
            for item_dic in self.map_listview:
                pMoveAct = QAction(item_dic['groupname'] ,pmenu)
                pSubMenu.addAction(pMoveAct)
                pMoveAct.triggered.connect(self.move)
            pmenu.popup(self.mapToGlobal(event.pos()))
    
    def deleteItemSlot(self):
        index = self.currentIndex().row()
        if index > -1:
            self.m_pModel.deleteItem(index)

    def setListMap(self, listview):
        self.map_listview.append(listview)

    def addItem(self, pitem):
        self.m_pModel.addItem(pitem)

    def move(self):
        tolistview = self.find(self.sender().text())
        if tolistview is self:
            prelistview = self.sender().text()
            QMessageBox.warning(self, "警告", "该联系人就在{}，还怎么移动啊！".format(prelistview))
        else:
            index = self.currentIndex().row()
            pItem = self.m_pModel.getItem(index)
            tolistview.addItem(pItem)
            self.m_pModel.deleteItem(index)

    def find(self, pmenuname):
        for item_dic in self.map_listview:
            if item_dic['groupname'] == pmenuname:
                return item_dic['listview']
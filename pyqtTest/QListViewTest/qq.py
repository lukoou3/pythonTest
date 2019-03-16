#coding=utf-8

from PyQt5.QtWidgets import QApplication, QToolBox, QListView, QMenu, QAction, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from pyqtTest.QListViewTest.ListView import ListView
from PyQt5.QtGui import QIcon
import sys

class QQ(QToolBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('模拟QQ')
        self.setWindowFlags(Qt.Dialog)
        self.setMinimumSize(200,600)
        self.setWhatsThis('这个一个模拟QQ软件')
        self.setWindowIcon(QIcon('./res/log.ico'))
        pListView = ListView() 
        pListView.setViewMode(QListView.ListMode)
        pListView.setStyleSheet("QListView{icon-size:70px}")
        dic_list = {'listview':pListView, 'groupname':"我的好友"}
        pListView.setListMap(dic_list)
        self.addItem(pListView, "我的好友") 
        self.show()
    
    def contextMenuEvent(self, event):
        pmenu = QMenu(self)
        pAddGroupAct = QAction("添加分组", pmenu)
        pmenu.addAction(pAddGroupAct) 
        pAddGroupAct.triggered.connect(self.addGroupSlot)  
        pmenu.popup(self.mapToGlobal(event.pos()))
    
    def addGroupSlot(self):
        groupname = QInputDialog.getText(self, "输入分组名", "")
        if groupname[0] and groupname[1]: 
            pListView1 = ListView()
            pListView1.setViewMode(QListView.ListMode)
            pListView1.setStyleSheet("QListView{icon-size:70px}")
            self.addItem(pListView1, groupname[0])
            dic_list = {'listview':pListView1, 'groupname':groupname[0]}
            pListView1.setListMap(dic_list)
        elif groupname[0] == '' and groupname[1]:
            QMessageBox.warning(self, "警告", "我说你没有填写分组名哦~！")
    
app = QApplication(sys.argv)
qq = QQ()
sys.exit(app.exec_())
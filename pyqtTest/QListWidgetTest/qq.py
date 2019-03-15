#coding=utf-8

from PyQt5.QtWidgets import QApplication, QToolBox, QListView, QMenu, QAction, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from pyqtTest.QListWidgetTest.ListWidget import ListWidget
from PyQt5.QtGui import QIcon
import sys

class QQ(QToolBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QQ')
        self.setWindowFlags(Qt.Dialog)
        self.setMinimumSize(200,600)
        self.setWhatsThis('这个一个模拟QQ软件')
        self.setWindowIcon(QIcon('./res/log.ico'))
        pListWidget = ListWidget()
        dic_list = {'listwidget':pListWidget, 'groupname':"我的好友"}
        pListWidget.setListMap(dic_list)
        self.addItem(pListWidget, "我的好友") 
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
            pListWidget1 = ListWidget()
            self.addItem(pListWidget1, groupname[0])
            dic_list = {'listwidget':pListWidget1, 'groupname':groupname[0]}
            pListWidget1.setListMap(dic_list)
        elif groupname[0] == '' and groupname[1]:
            QMessageBox.warning(self, "警告", "我说你没有填写分组名哦~！")
    
app = QApplication(sys.argv)
qq = QQ()
sys.exit(app.exec_())
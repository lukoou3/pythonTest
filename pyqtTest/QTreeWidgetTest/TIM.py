# -*- coding: utf-8 -*-

"""
Module implementing TIM.
"""

from PyQt5.QtWidgets import QWidget, QApplication, QTreeWidget, QTreeWidgetItem, QMenu, QAction, QTreeWidgetItemIterator, QInputDialog, QMessageBox, QAbstractItemView, QCompleter
from PyQt5.QtCore import Qt, QSize, pyqtSlot, pyqtSignal, QVariant
from PyQt5.QtGui import QIcon, QFont, QBrush,QStandardItemModel
from pyqtTest.QTreeWidgetTest.Ui_ui import Ui_Form
from pyqtTest.QTreeWidgetTest.Dialog_additem import Dialog_additem
from pyqtTest.QTreeWidgetTest import Random_Name
import sys, random, codecs


class TIM(QWidget, Ui_Form):

    #分组信息存储
    grouplist = []
    #用户信息存储
    userslist = []
    tmpuseritem = []

    def __init__(self, parent=None):

        super(TIM, self).__init__(parent)
        self.setupUi(self)
        self.Ui_init()
    
    def Ui_init(self):
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setColumnWidth(0,50)
        self.treeWidget.setHeaderLabels(["好友"])
        self.treeWidget.setIconSize(QSize(70,70))
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeWidget.itemSelectionChanged.connect(self.getListitems)
        self.treeWidget.currentItemChanged.connect(self.restatistic)
        self.treeWidget.itemClicked.connect(self.isclick)

        #样式设置
        with codecs.open('./res/treewidget.qss','r','utf-8') as f:
            styleSheet = f.readlines()
        style = '\r\n'.join(styleSheet)
        self.treeWidget.setStyleSheet(style)
 
        root = self.creategroup('我的好友')
        root.setExpanded(True)

        #是否出现批量操作菜单的标志
        self.menuflag = 1

        #搜索时自动填充姓名
        self.m_model = QStandardItemModel(0, 1, self)
        m_completer = QCompleter(self.m_model, self)
        self.lineEdit.setCompleter(m_completer)
        m_completer.activated[str].connect(self.onUsernameChoosed)

    def creategroup(self, groupname):
        hidernum = 0
        group= QTreeWidgetItem(self.treeWidget)
        groupdic = {'group':group, 'groupname':groupname,'childcount':0,'childishide':0}
        icon = self.searchicon(groupname)
        group.setIcon(0, icon)
        
        randomnum = random.sample(range(26), 10)
        for i in randomnum:  
            child = QTreeWidgetItem()
            randname, randicon, font, isvip, ishider = self.createusers(i)
            userdic = {'user':child, 'username':randname,'ishide':0}
            self.userslist.append(userdic)
            child.setText(0, randname)
            child.setFont(0, font)
            child.setIcon(0, randicon)
            child.setTextAlignment(0, Qt.AlignHCenter|Qt.AlignVCenter)
            if isvip == 1:
                child.setForeground(0, QBrush(Qt.red))
                child.setToolTip(0, '会员红名尊享')
            if ishider == 1:
                hidernum += 1
                userdic['ishide'] = 1
            group.addChild(child)
        childnum = group.childCount()
        lastchildnum = childnum - hidernum
        groupdic['childcount'] = childnum
        groupdic['childishide'] = hidernum
        groupname += ' ' + str(lastchildnum) + '/' + str(childnum)
        group.setText(0,groupname)
        self.grouplist.append(groupdic)
        return group

    def createusers(self, num):
        randname = Random_Name.getname()
        randicon = QIcon("./res/user/"+ str(num) + ".jpg")
        font = QFont()
        font.setPointSize(16)
        isvip = random.randint(0, 5)
        ishider = random.randint(0, 5)
        if ishider == 1:
            randicon = QIcon("./res/user/"+ str(num) + "h.jpg")
        return randname, randicon, font, isvip, ishider

    def contextMenuEvent(self, event):
        hititem = self.treeWidget.currentItem()
        if hititem:
            root = hititem.parent()
            if root is None:
                pgroupmenu = QMenu(self)
                pAddgroupAct = QAction('添加分组',self.treeWidget)
                pRenameAct = QAction('重命名',self.treeWidget)
                pDeleteAct = QAction('删除该组',self.treeWidget)
                pgroupmenu.addAction(pAddgroupAct)
                pgroupmenu.addAction(pRenameAct)
                pgroupmenu.addAction(pDeleteAct)
                pAddgroupAct.triggered.connect(self.addgroup)
                pRenameAct.triggered.connect(self.renamegroup)
                if self.treeWidget.itemAbove(hititem) is None:
                    pDeleteAct.setEnabled(False)
                else:
                    pDeleteAct.triggered.connect(self.deletegroup)
                pgroupmenu.popup(self.mapToGlobal(event.pos()))
            elif root.childCount() > 0:
                pItemmenu = QMenu(self)       
                pDeleteItemAct = QAction('删除联系人',pItemmenu)
                pItemmenu.addAction(pDeleteItemAct)            
                pDeleteItemAct.triggered.connect(self.delete)
                if len(self.grouplist) > 1:
                    pSubMenu = QMenu('转移联系人至' ,pItemmenu)
                    pItemmenu.addMenu(pSubMenu)
                    for item_dic in self.grouplist:
                        if item_dic['group'] is not root:
                            pMoveAct = QAction(item_dic['groupname'] ,pItemmenu)
                            pSubMenu.addAction(pMoveAct)
                            pMoveAct.triggered.connect(self.moveItem)
                if len(self.getListitems(self.menuflag)) == 1:
                    pRenameItemAct = QAction('设定备注',pItemmenu)
                    pItemmenu.addAction(pRenameItemAct)            
                    pRenameItemAct.triggered.connect(self.renameItem)
                if self.menuflag > 0 and root.childCount() > 1:
                    pBatchAct = QAction('分组内批量操作',pItemmenu)
                    pItemmenu.addAction(pBatchAct)
                    pBatchAct.triggered.connect(self.Batchoperation)
                elif self.menuflag < 0:
                    pCancelBatchAct = QAction('取消批量操作',pItemmenu)
                    pItemmenu.addAction(pCancelBatchAct)
                    pCancelBatchAct.triggered.connect(self.CancelBatchoperation)
                    
                pItemmenu.popup(self.mapToGlobal(event.pos()))

    def addgroup(self):
        gname, ok = QInputDialog.getText(self,'提示信息','请输入分组名称')
        if ok:
            if len(gname) == 0:
                QMessageBox.information(self,'提示','分组名称不能为空哦')
            else:
                self.creategroup(gname)

    def renamegroup(self):
        hitgroup = self.treeWidget.currentItem()
        gnewname, ok = QInputDialog.getText(self,'提示信息','请输入分组的新名称')
        if ok:
            if len(gnewname) == 0:
                QMessageBox.information(self,'提示','分组名称不能为空哦')
            else:
                hitgroup.setText(0, gnewname)
                newicon = self.searchicon(hitgroup.text(0))
                hitgroup.setIcon(0, newicon)
                gindex = self.searchgroup(hitgroup)
                self.grouplist[gindex]['groupname'] = gnewname
                self.treeWidget.setCurrentItem(hitgroup.child(0))
                
    def deletegroup(self):
        hitgroup = self.treeWidget.currentItem()
        gindex = self.searchgroup(hitgroup)
        reply = QMessageBox.question(self,'警告','确定要删除这个分组及其联系人吗？', QMessageBox.Yes | QMessageBox.No , QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.treeWidget.takeTopLevelItem(gindex)
            del self.grouplist[gindex]

    def moveItem(self):
        movelist = self.getListitems(self.menuflag)
        togroupname = self.sender().text()
        mindex = self.searchgroup(togroupname)
        togroup = self.grouplist[mindex]['group']
        self.deleteItems(movelist, flag = 0)
        self.add(togroup, movelist)
        self.tmpuseritem.clear()

    def delete(self):
        delitems = self.getListitems(self.menuflag)
        self.deleteItems(delitems)
        self.tmpuseritem.clear()

    def deleteItems(self, items, flag = 1):
        for delitem in items:
            delitem.setData(0, Qt.CheckStateRole, QVariant())#取消删除item的复选框
            pindex = delitem.parent().indexOfChild(delitem)
            dindex = self.searchuser(delitem)
            ishide = self.userslist[dindex]['ishide']
            if flag == 1:
                del self.userslist[dindex]
            fathergroup = delitem.parent()
            findex = self.searchgroup(fathergroup)
            if ishide == 1:
                self.grouplist[findex]['childishide'] -= 1
                self.grouplist[findex]['childcount'] -= 1
            else:
                self.grouplist[findex]['childcount'] -= 1

            delitem.parent().takeChild(pindex)

    def add(self, group, items):
        gindex = self.searchgroup(group)
        for item in items:
            aindex = self.searchuser(item)
            ishide = self.userslist[aindex]['ishide']
            if ishide == 1:
                self.grouplist[gindex]['childishide'] += 1
                self.grouplist[gindex]['childcount'] += 1
            else:
                self.grouplist[gindex]['childcount'] += 1
            group.addChild(item)
            self.treeWidget.setCurrentItem(item)

    def Batchoperation(self):
        self.menuflag *= -1

        group = self.getListitems()[0].parent()
        childnum = group.childCount()
        for c in range(childnum):
            child = group.child(c)
            child.setCheckState(0, Qt.Unchecked)

    def CancelBatchoperation(self):
        self.menuflag *= -1
        group = self.getListitems()[0].parent()
        childnum = group.childCount()
        for c in range(childnum):
            child = group.child(c)
            child.setData(0, Qt.CheckStateRole, QVariant())

    def isclick(self, item):
        if item.checkState(0) == Qt.Checked:
            if self.tmpuseritem.count(item) == 0:
                self.tmpuseritem.append(item)
        else:
            if len(self.tmpuseritem) > 0:
                if self.tmpuseritem.count(item) != 0:
                    i = self.tmpuseritem.index(item)
                    del self.tmpuseritem[i]

    def renameItem(self):
        hituser = self.treeWidget.currentItem()
        uindex = self.searchuser(hituser)
        unewname, ok = QInputDialog.getText(self,'提示信息','请输入备注名称')
        if ok:
            if len(unewname) == 0:
                QMessageBox.information(self,'提示','备注名称不能为空哦')
            else:
                hituser.setText(0,unewname)
                self.userslist[uindex]['username'] = unewname

    def searchgroup(self, hitgroup):
        if isinstance(hitgroup,str):
            for i,g in enumerate(self.grouplist):
                if g['groupname'] == hitgroup:
                    return i
        else:
            for i,g in enumerate(self.grouplist):
                if g['group'] == hitgroup:
                    return i

    def searchuser(self, hituser):
        if isinstance(hituser, str):
            for i,u in enumerate(self.userslist):
                if u['username'] == hituser:
                    return i
        else:
            for i,u in enumerate(self.userslist):
                if u['user'] == hituser:
                    return i

    def searchicon(self, gpname2):
        if gpname2.find('好友') >= 0:
            return QIcon('./res/group/buddy.ico')
        elif gpname2.find('同事') >= 0:
            return QIcon('./res/group/partner.ico')
        elif gpname2.find('黑名单') >= 0:
            return QIcon('./res/group/blacklist.ico')
        else:
            return QIcon('./res/group/buddy_default.ico')

    def getListitems(self, flag = 1):
        if flag > 0:
            return self.treeWidget.selectedItems()
        else:
            return self.tmpuseritem

    def restatistic(self, item, preitem):
        if item:
            fathergroup = item.parent() 
            if fathergroup:
                self.restatistic_op(fathergroup)
            else:
                self.restatistic_op(item)
        elif preitem.parent().childCount() == 1:
            lastgroupname = preitem.parent().text(0).split()[0] + ' 0/0'
            preitem.parent().setText(0, lastgroupname)
            self.menuflag = 1

    def restatistic_op(self, itemorgroup):
        gindex = self.searchgroup(itemorgroup)
        totalcount = self.grouplist[gindex]['childcount']
        hidecount = self.grouplist[gindex]['childishide']
        fathergroupname = self.grouplist[gindex]['groupname']
        fathergroupname += ' ' + str(totalcount - hidecount) + '/' + str(totalcount)    
        itemorgroup.setText(0, fathergroupname)

    def onUsernameChoosed(self, name):
        self.lineEdit.setText(name)

    @pyqtSlot()
    def on_bt_search_clicked(self):

        username = self.lineEdit.text()
        if len(username) > 0:
            useritemindex = self.searchuser(username)
            useritem = self.userslist[useritemindex]['user']
            self.treeWidget.setCurrentItem(useritem)
    
    @pyqtSlot()
    def on_bt_adduser_clicked(self):

        adduser = Dialog_additem()
        for g in self.grouplist:
            adduser.comboBox.addItem(g['groupname'])
        r = adduser.exec_()
        if r > 0:
            newitem = QTreeWidgetItem()
            newname = adduser.lineEdit.text()
            newicon = adduser.geticonpath()
            font = QFont()
            font.setPointSize(16)
            newitem.setFont(0, font)
            newitem.setText(0, newname)
            newitem.setTextAlignment(0, Qt.AlignHCenter|Qt.AlignVCenter)
            newitem.setIcon(0, QIcon(newicon))
            comboxinfo = adduser.comboBox.currentText()
            cindex = self.searchgroup(comboxinfo)
            group = self.grouplist[cindex]['group']
            self.grouplist[cindex]['childcount'] += 1
            userdic = {'user':newitem, 'username':newname,'ishide':0}
            self.userslist.append(userdic)
            group.addChild(newitem)
            self.treeWidget.setCurrentItem(newitem)


    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        namelist = []

        for itm in self.userslist:
            username = itm['username']
            if username.find(text) >= 0:
                namelist.append(itm['username'])
        self.m_model.removeRows(0, self.m_model.rowCount())

        for i in range(0, len(namelist)):
            self.m_model.insertRow(0)
            self.m_model.setData(self.m_model.index(0, 0), namelist[i])
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tim = TIM()
    tim.show()
    sys.exit(app.exec_())
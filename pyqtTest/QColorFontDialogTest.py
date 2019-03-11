from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('记得好看点')
        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)
        self.bt1 = QPushButton('打开文件',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('选择字体',self)
        self.bt2.move(350,70)
        self.bt3 = QPushButton('选择颜色',self)
        self.bt3.move(350,120)
        self.bt4 = QPushButton('选中字体', self)
        self.bt4.move(350, 170)
        self.bt5 = QPushButton('选中颜色', self)
        self.bt5.move(350, 220)
        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)
        self.bt4.clicked.connect(self.choicefont_selected)
        self.bt5.clicked.connect(self.choicecolor_selected)
        self.show()
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件','./')
        if fname[0]:
            with open(fname[0], 'r',encoding='utf-8',errors='ignore') as f:
                self.tx.setText(f.read())
    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setFont(font)
    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setStyleSheet("color:rgb{}".format(col.getRgb()))
    def choicefont_selected(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)
    def choicecolor_selected(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
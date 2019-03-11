from PyQt5.QtWidgets import QLineEdit, QApplication, QDialog, QAction, QMessageBox
from PyQt5.QtGui import QIcon
import sys
from checkword import correct

class Line(QDialog):
    def __init__(self):
        super().__init__()
        self.Ui()
    
    def Ui(self):
        self.resize(450,100)
        self.setWindowTitle('微信公众号：学点编程吧--单词拼写检查')
        self.line = QLineEdit(self)
        self.line.move(20,20)
        action = QAction(self)
        action.setIcon(QIcon('check.ico'))
        action.triggered.connect(self.Check)
        self.line.addAction(action,QLineEdit.TrailingPosition)
        self.show()
    
    def Check(self):
        word = self.line.text()
        if correct(word) != word:
            QMessageBox.information(self,'提示信息','你或许想要表达的单词是：'+correct(word))
        else:
            QMessageBox.information(self,'提示信息','你填写的单词是：'+word)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    line = Line()
    sys.exit(app.exec_())



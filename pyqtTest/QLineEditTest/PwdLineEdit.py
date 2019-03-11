from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QTimer

class PwdLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.m_LineEditText = ""
        self.m_LastCharCount = 0
        self.Action()
    
    def Action(self):
        self.cursorPositionChanged[int,int].connect(self.DisplayPasswordAfterEditSlot)
        self.textEdited[str].connect(self.GetRealTextSlot)
        self.time = QTimer(self)
        self.time.setInterval(200)
        self.time.start()
        self.show()
    
    def DisplayPasswordAfterEditSlot(self, old, new):
        print('new:',new)
        print('old:',old)
        if old >= 0 and new >= 0:
            if new > old:
                self.time.timeout.connect(self.DisplayPasswordSlot)
            else:
                self.setCursorPosition(old)                   

    def DisplayPasswordSlot(self):
        self.setText(self.GetMaskString())      

    def GetRealTextSlot(self, text):
        self.m_LastCharCount = len(self.m_LineEditText)
        
        if len(text) > self.m_LastCharCount:
            self.m_LineEditText += text[-1]
            
        elif len(text) <= self.m_LastCharCount:
            self.m_LineEditText = self.m_LineEditText[:-1]    

    def GetMaskString(self):
        mask = ""
        count = len(self.text())
        if count > 0:
            for i in range(count):
                mask += "*"
        return mask
    
    def GetPassword(self):
        return self.m_LineEditText
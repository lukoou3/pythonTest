from pyqtTest.QTableWidgetTest.mbook import Mbook
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mb = Mbook()
    mb.show()
    sys.exit(app.exec_())
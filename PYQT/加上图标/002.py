import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget,QApplication

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle("天下第二")
        self.setWindowIcon(QIcon("../icons/1.ico"))

myapp = QApplication(sys.argv)
mywidget = MyWidget()
mywidget.show()
sys.exit(myapp.exec_())
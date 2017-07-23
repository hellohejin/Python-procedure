import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle("天下第三")
        self.setWindowIcon(QIcon("../icons/2.ico"))
        #设置提示信息
        self.setToolTip("看什么看！^_^")
        QToolTip.setFont(QFont("楷体",20))

myapp = QApplication(sys.argv)
mywidget = MyWidget()
mywidget.show()
sys.exit(myapp.exec_())
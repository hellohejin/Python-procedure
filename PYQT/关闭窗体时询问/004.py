import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle("天下第四")
        self.setWindowIcon(QIcon("../icons/2.ico"))
        self.setToolTip("看什么看！^_^")
        QToolTip.setFont(QFont("楷体",20))

    def closeEvent(self,event):
        #重新定义 closeEvent
        reply = QMessageBox.question(self,'信息',
                                    "你确定会退出吗？",
                                    QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

myapp = QApplication(sys.argv)
mywidget = MyWidget()
mywidget.show()
sys.exit(myapp.exec_())
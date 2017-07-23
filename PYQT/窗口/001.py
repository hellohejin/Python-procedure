import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        #调整左顶点坐标和窗口大小
        #坐标(0,0),大小:800*600
        self.setGeometry(0,0,800,600)
        #设置窗口程序的标题
        self.setWindowTitle("公无渡河")

#任何窗口程序都要创建QApplication实例
myapp = QApplication(sys.argv)
mywidget = MyWidget()
#显示窗体
mywidget.show()
#退出
sys.exit(myapp.exec_())
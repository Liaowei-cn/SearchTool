##  OS(ALL)
##  VS(Python3 & PyQt5)
##  NAME(桌面搜索工具)
##  INFO(version:1.0 date:2017.05.20)

#   >>>>>(函数库调用)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from L1WEB import*
#   >>>>>(GUI函数)
class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):

        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(200, 300)
        self.centralWidget = QtWidgets.QWidget(SearchWindow)
        self.centralWidget.setObjectName("centralWidget")
        SearchWindow.setWindowFlags(Qt.FramelessWindowHint)
        SearchWindow.setAttribute(Qt.WA_TranslucentBackground)
        SearchWindow.setStyleSheet("background:url(\'background.png\');")

        self.E1 = QtWidgets.QLineEdit(self.centralWidget)
        self.E1.setEnabled(True)
        self.E1.setGeometry(QtCore.QRect(40, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.E1.setFont(font)
        self.E1.setObjectName("E1")
        self.E1.setStyleSheet("background:url(\'botton.jpg\');")

        self.E2 = QtWidgets.QLineEdit(self.centralWidget)
        self.E2.setEnabled(True)
        self.E2.setGeometry(QtCore.QRect(40, 60, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.E2.setFont(font)
        self.E2.setObjectName("E2")
        self.E2.setStyleSheet("background:url(\'botton.jpg\');")

        self.E3 = QtWidgets.QLineEdit(self.centralWidget)
        self.E3.setEnabled(True)
        self.E3.setGeometry(QtCore.QRect(40, 110, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.E3.setFont(font)
        self.E3.setObjectName("E3")
        self.E3.setStyleSheet("background:url(\'botton.jpg\');")

        self.E4 = QtWidgets.QLineEdit(self.centralWidget)
        self.E4.setEnabled(True)
        self.E4.setGeometry(QtCore.QRect(40, 160, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.E4.setFont(font)
        self.E4.setObjectName("E4")
        self.E4.setStyleSheet("background:url(\'botton.jpg\');")

        self.E5 = QtWidgets.QLineEdit(self.centralWidget)
        self.E5.setEnabled(True)
        self.E5.setGeometry(QtCore.QRect(40, 210, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.E5.setFont(font)
        self.E5.setObjectName("E5")
        self.E5.setStyleSheet("background:url(\'botton.jpg\');")

        self.E6 = QtWidgets.QLineEdit(self.centralWidget)
        self.E6.setEnabled(True)
        self.E6.setGeometry(QtCore.QRect(40, 260, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.E6.setFont(font)
        self.E6.setObjectName("E6")
        self.E6.setStyleSheet("background:url(\'botton.jpg\');")

        self.E1.returnPressed.connect(self.Search1)
        self.E2.returnPressed.connect(self.Search2)
        self.E3.returnPressed.connect(self.Search3)
        self.E4.returnPressed.connect(self.Search4)
        self.E5.returnPressed.connect(self.Search5)
        self.E6.returnPressed.connect(self.Search6)
        SearchWindow.setCentralWidget(self.centralWidget)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def Search1(self):
        self.key1 = self.E1.text()
        SearchOnline(1,self.key1)
    def Search2(self):
        self.key2 = self.E2.text()
        SearchOnline(2,self.key2)
    def Search3(self):
        self.key3 = self.E3.text()
        SearchOnline(3,self.key3)
    def Search4(self):
        self.key4 = self.E4.text()
        SearchOnline(4,self.key4)
    def Search5(self):
        self.key5 = self.E5.text()
        SearchOnline(5,self.key5)
    def Search6(self):
        self.key6 = self.E6.text()
        SearchOnline(6,self.key6)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())
import sys
from PyQt5.Qt import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('事件消息的学习')
        self.resize(500, 500)

    def showEvent(self, QShowEvent):
        print("窗口被展示")

    def closeEvent(self, QShowEvent):
        print("窗口被关闭")

    def moveEvent(self, QMoveEvent):
        print("窗口被移动")

    def resizeEvent(self, QResizeEvent):
        print("窗口被调整大小")

    def enterEvent(self, QEvent):
        print("鼠标进入窗口")
        self.setStyleSheet("background-color: red")

    def leaveEvent(self, QEvent):
        print("鼠标离开窗口")
        self.setStyleSheet("background-color: green")

    def mousePressEvent(self, QMouseEvent):
        print("鼠标按下")

    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标释放")

    def mouseDoubleClickEvent(self, QMouseEvent):
        print("鼠标双击")

    def mouseMoveEvent(self, QMouseEvent):
        print("鼠标移动")

    def keyPressEvent(self, QKeyEvent):
        print("键盘按下")

    def keyReleaseEvent(self, QKeyEvent):
        print("键盘释放")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("第一个PyQt")

    #label = QLabel("账号:")
    #label.setParent(w)
    label = QLabel("账号",w)

    #设置位置和大小
    label.setGeometry(20,20,30,30)

    w.show()

    app.exec_()
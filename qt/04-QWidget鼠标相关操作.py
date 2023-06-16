from PyQt5.Qt import *
import sys

class MyWindow(QWidget):
    def mouseMoveEvent(self, me):
        QMouseEvent
        #print("鼠标移动了",me.localPos())
        print("鼠标移动了",me.globalPos())

    pass


app = QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("鼠标操作")
window.resize(400, 300)
window.setMouseTracking(True)
print(window.hasMouseTracking())

window.show()

sys.exit(app.exec_())
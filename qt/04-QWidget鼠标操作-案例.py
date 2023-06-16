import sys
from PyQt5.Qt import *

class MyWindow(QWidget):
    def mouseMoveEvent(self, mv):
        print("鼠标移动了",mv.localPos())
        label = self.findChild(QLabel)
        #label.move(200,200)
        label.move(int(mv.localPos().x()), int(mv.localPos().y()))

app = QApplication(sys.argv)

window = MyWindow()
window.resize(400, 400)
window.move(200,200)
window.setWindowTitle("鼠标相关操作")
window.setMouseTracking(True)

label = QLabel(window)
label.setText("开始烧写")
label.move(100,100)
label.setStyleSheet("background-color: cyan;")






window.show()

sys.exit(app.exec_())
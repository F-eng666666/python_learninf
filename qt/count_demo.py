import sys
from PyQt5.Qt import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.widget_count = 100
        self.column_count = 3

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("MyWidget")
        self.setGeometry(300, 300, 600, 600)

        # 初始化子控件
        for i in range(self.widget_count):
            w = QWidget(self)
            w.setStyleSheet("background-color:red;border:1px solid yellow;")
            w.show()

        self.resizeEvent = self.on_resize_event

    def on_resize_event(self, event):
        # 重新计算控件位置和大小
        widget_width = self.width() // self.column_count
        row_count = (self.widget_count - 1) // self.column_count + 1
        widget_height = self.height() // row_count

        for i, w in enumerate(self.children()):
            # 计算控件位置
            x = i % self.column_count * widget_width
            y = i // self.column_count * widget_height
            w.move(x, y)
            w.resize(widget_width, widget_height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())
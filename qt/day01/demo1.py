import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Hello World!")
        self.setGeometry(100, 100, 300, 200)

        # 创建标签并添加到主窗口中
        self.label = QLabel("Welcome to PyQt5!", self)
        self.label.move(100, 80)

        # 创建按钮并添加到主窗口中
        self.button = QPushButton("Click Me!", self)
        self.button.move(110, 120)
        self.button.clicked.connect(self.on_button_clicked)

    # 按钮点击事件的处理函数，更新标签中的文字
    def on_button_clicked(self):
        self.label.setText("Hello World! Clicked!")
        print("hello world")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
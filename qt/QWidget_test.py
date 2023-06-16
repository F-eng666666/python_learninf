from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
obj = QWidget()
obj.move(0,0)
btn = QPushButton(obj)
btn.setText("Hello World")
btn.resize(200, 200)
btn.move(100, 100)

label = QLabel(obj)
label.setText("Hello World")
label.resize(100, 60)
#label.setAlignment(Qt.AlignRight | Qt.AlignBottom)

obj.show()

sys.exit(app.exec_())
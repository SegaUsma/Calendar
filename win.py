from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QWidget()
win.setWindowTitle('Perfect!')
win.resize(500, 400)
label = QtWidgets.QLabel('<center>Message</center>')
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
win.setLayout(vbox)
win.show()
sys.exit(app.exec())
import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l = QtWidgets.QLabel(w)
    b = QtWidgets.QPushButton(w)
    v = QtWidgets.QVBoxLayout()
    v.addWidget(b)
    v.addWidget(l)
    w.setLayout(v)
    b.setText('Don\'t push me')
    l.setText('Hello World')
    w.setGeometry(100,100, 400, 400)
    w.setWindowTitle('SIW Prototype')
    w.show()
    sys.exit(app.exec_())


window()
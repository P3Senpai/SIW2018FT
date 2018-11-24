import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_gui()

    def init_gui(self):

        self.setWindowTitle("Calculator")

        self.b1 = QtWidgets.QPushButton("1")
        self.b2 = QtWidgets.QPushButton("2")
        self.b3 = QtWidgets.QPushButton("3")
        self.b4 = QtWidgets.QPushButton("4")
        self.b5 = QtWidgets.QPushButton("5")
        self.b6 = QtWidgets.QPushButton("6")
        self.b7 = QtWidgets.QPushButton("7")
        self.b8 = QtWidgets.QPushButton("8")
        self.b9 = QtWidgets.QPushButton("9")
        self.b0 = QtWidgets.QPushButton("0")
        self.l = QtWidgets.QLineEdit()
        self.bp = QtWidgets.QPushButton("+")
        self.bm = QtWidgets.QPushButton("-")
        self.bmu = QtWidgets.QPushButton("*")
        self.bd = QtWidgets.QPushButton("/")
        self.be = QtWidgets.QPushButton("=")
        self.bc = QtWidgets.QPushButton("Clear")


        self.h = QtWidgets.QHBoxLayout()
        self.h.addWidget(self.l)
        self.h1 = QtWidgets.QHBoxLayout()
        self.h1.addWidget(self.b1)
        self.h1.addWidget(self.b2)
        self.h1.addWidget(self.b3)
        self.h1.addWidget(self.bp)

        self.h2 = QtWidgets.QHBoxLayout()
        self.h2.addWidget(self.b4)
        self.h2.addWidget(self.b5)
        self.h2.addWidget(self.b6)
        self.h2.addWidget(self.bm)

        self.h3 = QtWidgets.QHBoxLayout()
        self.h3.addWidget(self.b7)
        self.h3.addWidget(self.b8)
        self.h3.addWidget(self.b9)
        self.h3.addWidget(self.bmu)

        self.h4 = QtWidgets.QHBoxLayout()
        self.h4.addWidget(self.bc)
        self.h4.addWidget(self.b0)
        self.h4.addWidget(self.be)
        self.h4.addWidget(self.bd)


        self.v = QtWidgets.QVBoxLayout()
        self.v.addLayout(self.h)
        self.v.addLayout(self.h1)
        self.v.addLayout(self.h2)
        self.v.addLayout(self.h3)
        self.v.addLayout(self.h4)

        self.setLayout(self.v)

        self.b0.clicked.connect(self.click)
        self.b1.clicked.connect(self.click)
        self.b2.clicked.connect(self.click)
        self.b3.clicked.connect(self.click)
        self.b4.clicked.connect(self.click)
        self.b5.clicked.connect(self.click)
        self.b6.clicked.connect(self.click)
        self.b7.clicked.connect(self.click)
        self.b8.clicked.connect(self.click)
        self.b9.clicked.connect(self.click)
        self.bm.clicked.connect(self.click)
        self.bp.clicked.connect(self.click)
        self.bmu.clicked.connect(self.click)
        self.bd.clicked.connect(self.click)
        self.be.clicked.connect(self.click)
        self.bc.clicked.connect(self.clear)



        self.show()


    def clear(self):
        self.l.setText("")
    def click(self):
        toPrint = self.l.text()
        sender = self.sender()
        toPrint += sender.text()
        self.l.setText(toPrint)
        global first
        first = True
        global toMath2
        toMath2 = ""
        if sender.text() == "=":
            for i in range(len(toPrint) - 1):
                if toPrint[i] == "+" or toPrint[i] == "-" or toPrint[i] == "*" or toPrint[i] == "/":
                    first = False
                    max1 = i
                    toMath = ""
                    for i in range(i + 1, (len(toPrint) - 1)):
                        toMath += toPrint[i]
                elif(first):
                    toMath2 += toPrint[i]
            toMath = int(toMath)
            print(toMath)
            toMath2 = int(toMath2)
            print(toMath2)
            if toPrint[max1] == "+":
                toPrint += str(toMath + toMath2)
            elif toPrint[max1] == "-":
                toPrint += str(toMath2 - toMath)
            elif toPrint[max1] == "*":
                toPrint += str(toMath * toMath2)
            else:
                if toMath == 0:
                    self.l.setText("You can not divide by zero")
                    return
                toPrint += str(toMath2 / toMath)
        self.l.setText(toPrint)












app = QtWidgets.QApplication(sys.argv)
window = Window()
app.exec()
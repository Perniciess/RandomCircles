# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtGui
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        self.d = MyWidget2()
        if self.p:
            self.d.p = False
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            rec = randint(0, 800)
            x = randint(0, 800)
            y = randint(0, 800)
            self.qp.drawEllipse(x, y, rec, rec)
            self.qp.end()


class MyWidget2(MyWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и случайные окружности')
        self.setFixedSize(800, 800)
        self.btn = QtWidgets.QPushButton('Click', self)
        self.btn.resize(300, 60)
        self.btn.move(250, 700)
        self.btn.clicked.connect(self.rep)
        self.p = False

    def rep(self):
        self.repaint()
        self.p = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget2()
    ex.show()
    sys.exit(app.exec_())

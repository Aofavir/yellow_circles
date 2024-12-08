import sys
import random
from PyQt6 import uic

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.btn = QPushButton(self)
        self.btn.setGeometry(30, 30, 121, 41)
        self.btn.setText('Создать окружность')
        self.btn.clicked.connect(self.paint)
        self.resize(1000, 750)

    def initUI(self):
        uic.loadUi('UI.ui')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = random.randint(20, 400)
        qp.drawEllipse(200, 200, x, x)

    def paint(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

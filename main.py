import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.should_draw_flag = False

    def paintEvent(self, event):
        if self.should_draw_flag:
            qp = QPainter(self)
            self.draw_flag(qp)

    def run(self):
        self.should_draw_flag = True
        self.update()

    def draw_flag(self, qp):
        a = randint(5, 400)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(300, 300, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

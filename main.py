import sys, random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Git и желтые окружности
class MyWidget(QMainWindow):
    circles = []
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.BtnCircle.clicked.connect(self.btn_new_circle)
        self.BtnClear.clicked.connect(self.btn_clear_circle)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()


    def draw_circle(self, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setBrush(QColor(255, 255, 0))
        for cirl in self.circles:
            qp.drawEllipse(cirl[0], cirl[1], cirl[2], cirl[2])

    def btn_clear_circle(self):
        self.circles.clear()
        self.repaint()


    def btn_new_circle(self):
        if not self.do_paint:
            self.do_paint= True
        radius = random.randint(5, 150)
        x = random.randint(0, self.width() - radius)
        y = random.randint(0, self.height() - radius)
        self.circles.append([x, y, radius])
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
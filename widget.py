from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtCore import QRectF

class BottomRectangleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)  # Reduced height to make it shorter
        self.margin = 10  # Margin from the bottom and sides

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        rounded_rect = QRectF(rect)
        path = QPainterPath()
        path.addRoundedRect(rounded_rect, 15, 15)  # Rounded corners with radius 15
        painter.fillPath(path, QColor("#444444"))  # Fill with a dark grey color

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Adjust the rectangle's position and size on window resize
        self.setGeometry(self.margin, self.parent().height() - self.height() - self.margin, self.parent().width() - 2 * self.margin, self.height())  # Reduced width by adding margins

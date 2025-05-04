import sys
import importlib
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from widget import BottomRectangleWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove the title bar
        self.setGeometry(100, 100, 400, 800)  # Set window size and position
        self.set_background_color()

        # Add the bottom rectangle widget
        self.bottom_rectangle = BottomRectangleWidget(self)
        self.bottom_rectangle.setGeometry(0, self.height() - 100, self.width(), 100)
        self.bottom_rectangle.show()

    def set_background_color(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#2c2c2c"))  # Dark grey
        self.setPalette(palette)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Adjust the rectangle's position and size on window resize
        self.bottom_rectangle.setGeometry(0, self.height() - 90, self.width(), 100)  # Lowered by 10 pixels


if __name__ == "__main__":
    app = QApplication(sys.argv)

    def reload_window():
        global window
        importlib.reload(sys.modules["widget"])
        position = window.pos()  # Save the current position of the window
        window.close()
        window = MainWindow()
        window.move(position)  # Restore the window to its previous position
        window.show()

    window = MainWindow()
    window.show()

    # Set up a timer to reload the window every 2 seconds (for demonstration purposes)
    timer = QTimer()
    timer.timeout.connect(reload_window)
    timer.start(2000)  # 2000 ms = 2 seconds

    sys.exit(app.exec_())


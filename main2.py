from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from sidebar import MySideBAr  # Ensure MySideBAr is a properly defined class

class MySideBAr(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Sidebar")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        button = QtWidgets.QPushButton("Click Me", self)
        button.setGeometry(100, 100, 100, 30)
        button.clicked.connect(self.on_click)

    def on_click(self):
        print("Button clicked!")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MySideBAr()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

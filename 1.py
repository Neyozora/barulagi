from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

window = QMainWindow()
button = QPushButton("Click Me", window)
button.setGeometry(100, 100, 100, 30)
window.setWindowTitle("Test PySide6")
window.setGeometry(100, 100, 400, 300)
window.show()

app.exec()

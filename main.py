from PySide6.QtWidgets import QApplication
from sidebar import MySideBAr
import sys

app = QApplication(sys.argv)

window = MySideBAr()  
window.show()  
app.exec()

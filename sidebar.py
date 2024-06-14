from coba_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
class MySideBAr(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        
        self.icon_name_widget.setHidden(True)
        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        self.message_1.clicked.connect(self.switch_to_profilePage)
        self.message_2.clicked.connect(self.switch_to_profilePage)

        self.notification_1.clicked.connect(self.switch_to_notificationsPage)
        self.notification_2.clicked.connect(self.switch_to_notificationsPage)

        self.profile_1.clicked.connect(self.switch_to_profilePage)
        self.profile_2.clicked.connect(self.switch_to_profilePage)

        self.settings_1.clicked.connect(self.switch_to_settingsPage)
        self.settings_2.clicked.connect(self.switch_to_settingsPage)

        
    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_profilePage(self):
        self.stackedWidget.setCurrentIndex(3)  

    def switch_to_messagesPage(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_notificationsPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(1)
        
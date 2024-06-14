# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coba.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 545)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 221, 252);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"  background-color: rgb(255, 94, 212);\n"
"}\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"height: 30px;\n"
"border:none;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 221, 252);\n"
"	color: rgb(255, 185, 227);\n"
"    font-weight:bold;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.icon_only_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.icon_only_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icon/profile_pic.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/icon/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.profile_1 = QPushButton(self.icon_only_widget)
        self.profile_1.setObjectName(u"profile_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_1.setIcon(icon1)
        self.profile_1.setCheckable(True)
        self.profile_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile_1)

        self.message_1 = QPushButton(self.icon_only_widget)
        self.message_1.setObjectName(u"message_1")
        icon2 = QIcon()
        icon2.addFile(u":/icon/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.message_1.setIcon(icon2)
        self.message_1.setCheckable(True)
        self.message_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.message_1)

        self.notification_1 = QPushButton(self.icon_only_widget)
        self.notification_1.setObjectName(u"notification_1")
        icon3 = QIcon()
        icon3.addFile(u":/icon/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notification_1.setIcon(icon3)
        self.notification_1.setCheckable(True)
        self.notification_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.notification_1)

        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon4 = QIcon()
        icon4.addFile(u":/icon/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_1.setIcon(icon4)
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 223, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/icon/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)

        self.gridLayout_3.addWidget(self.pushButton_6, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 116, 230);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"height: 30px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 221, 252);\n"
"	color: rgb(255, 185, 227);\n"
"    font-weight:bold;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.icon_name_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label = QLabel(self.icon_name_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icon/profile_pic.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        font1 = QFont()
        font1.setPointSize(8)
        self.dashboard_2.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icon/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icon/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon6)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.profile_2 = QPushButton(self.icon_name_widget)
        self.profile_2.setObjectName(u"profile_2")
        icon7 = QIcon()
        icon7.addFile(u":/icon/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icon/profile.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_2.setIcon(icon7)
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_2)

        self.message_2 = QPushButton(self.icon_name_widget)
        self.message_2.setObjectName(u"message_2")
        icon8 = QIcon()
        icon8.addFile(u":/icon/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icon/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.message_2.setIcon(icon8)
        self.message_2.setCheckable(True)
        self.message_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.message_2)

        self.notification_2 = QPushButton(self.icon_name_widget)
        self.notification_2.setObjectName(u"notification_2")
        self.notification_2.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/icon/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icon/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.notification_2.setIcon(icon9)
        self.notification_2.setCheckable(True)
        self.notification_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.notification_2)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        icon10 = QIcon()
        icon10.addFile(u":/icon/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icon/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_2.setIcon(icon10)
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 223, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.icon_name_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_9, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_3 = QVBoxLayout(self.main_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon11 = QIcon()
        icon11.addFile(u":/icon/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon11)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(167, 37, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon12 = QIcon()
        icon12.addFile(u":/icon/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon12)

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(167, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon13 = QIcon()
        icon13.addFile(u":/icon/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.pushButton_15)


        self.verticalLayout_3.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_4 = QLabel(self.dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 160, 201, 61))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_4.setFont(font2)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_8 = QLabel(self.settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 180, 221, 61))
        self.label_8.setFont(font2)
        self.stackedWidget.addWidget(self.settings_page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.profile_pages = QWidget()
        self.profile_pages.setObjectName(u"profile_pages")
        self.label_7 = QLabel(self.profile_pages)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, 170, 221, 61))
        self.label_7.setFont(font2)
        self.stackedWidget.addWidget(self.profile_pages)
        self.messages_pages = QWidget()
        self.messages_pages.setObjectName(u"messages_pages")
        self.label_5 = QLabel(self.messages_pages)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 160, 201, 61))
        self.label_5.setFont(font2)
        self.stackedWidget.addWidget(self.messages_pages)
        self.notification_page = QWidget()
        self.notification_page.setObjectName(u"notification_page")
        self.label_6 = QLabel(self.notification_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 150, 221, 61))
        self.label_6.setFont(font2)
        self.stackedWidget.addWidget(self.notification_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.notification_1.toggled.connect(self.notification_2.setChecked)
        self.message_1.toggled.connect(self.message_2.setChecked)
        self.profile_1.toggled.connect(self.profile_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.message_2.toggled.connect(self.message_1.setChecked)
        self.profile_2.toggled.connect(self.profile_1.setChecked)
        self.notification_2.toggled.connect(self.notification_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_9.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.dashboard_1.setText("")
        self.profile_1.setText("")
        self.message_1.setText("")
        self.notification_1.setText("")
        self.settings_1.setText("")
        self.pushButton_6.setText("")
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.profile_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.message_2.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.notification_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.menu.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Messages Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notifications Page", None))
    # retranslateUi


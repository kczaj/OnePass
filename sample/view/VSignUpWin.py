#######################################################
# 
# VSignUpWin.py
# Python implementation of the Class VSignUpWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:20
# Original author: KUBA
# 
#######################################################
from sample.controller.PSignUpWin import PSignUpWin
from PyQt5 import QtWidgets, QtCore, QtGui

from sample.view.VWindow import VWindow


class VSignUpWin(VWindow):

    def __init__(self, main_win, _loader, main_win_before, generate_win, hasher):
        super().__init__()
        self.controller = PSignUpWin(self, main_win, _loader, main_win_before, generate_win, hasher)

    def sign_up_button_pressed(self):
        name = self.name_frame.text()
        surname = self.surname_frame.text()
        email = self.email_frame.text()
        login = self.login_frame.text()
        password = self.password_frame.text()
        status = self.controller.sign_up_button_handle(name, surname, email, login, password)
        if status != '1':
            self.error_label.setText(status)
            self.error_label.setVisible(True)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 600)
        MainWindow.setMinimumSize(QtCore.QSize(360, 600))
        MainWindow.setMaximumSize(QtCore.QSize(360, 600))
        MainWindow.setStyleSheet("QLabel{\n"
                                 "    font: 12pt \"Rubik\";\n"
                                 "    color:white;\n"
                                 "}\n"
                                 "QLineEdit{\n"
                                 "    font: 12pt \"Rubik\";\n"
                                 "    color:white;\n"
                                 "    background: rgb(119,119,119);\n"
                                 "    border-radius: 10px;\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "    font: 8pt \"Rubik\";\n"
                                 "    color:white;\n"
                                 "    background: transparent;\n"
                                 "    border-radius:10px\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("view/img/tło_logowanie.png"))
        self.bg.setObjectName("bg")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(85, 405, 255, 100))
        self.error_label.setStyleSheet("QLabel{\n"
                                       "    font: 12pt \"Rubik\";\n"
                                       "    color:rgb(245,0,0);\n"
                                       "}\n")
        self.error_label.setVisible(False)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 240, 341, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.surname_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.surname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.surname_label.setObjectName("surname_label")
        self.gridLayout.addWidget(self.surname_label, 2, 0, 1, 1)
        self.name_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_frame.setObjectName("name_frame")
        self.gridLayout.addWidget(self.name_frame, 0, 1, 1, 1)
        self.surname_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.surname_frame.setObjectName("surname_frame")
        self.gridLayout.addWidget(self.surname_frame, 2, 1, 1, 1)
        self.email_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_frame.setObjectName("email_frame")
        self.gridLayout.addWidget(self.email_frame, 4, 1, 1, 1)
        self.login_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.login_frame.setObjectName("login_frame")
        self.gridLayout.addWidget(self.login_frame, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 8, 0, 1, 1)
        self.login_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 6, 0, 1, 1)

        self.email_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 4, 0, 1, 1)
        self.password_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_frame.setObjectName("password_frame")
        self.password_frame.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.password_frame, 8, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("view/img/sign_up/slabe.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 1, 1, 1)
        self.sign_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_button.setGeometry(QtCore.QRect(170, 470, 161, 34))
        self.sign_up_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/img/sign_up/przycisk_rej.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.sign_up_button.setIcon(icon)
        self.sign_up_button.setIconSize(QtCore.QSize(161, 34))
        self.sign_up_button.setObjectName("sign_up_button")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.arrow_button.setGeometry(QtCore.QRect(15, 15, 41, 41))
        self.arrow_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/img/przycisk_strzałka.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.arrow_button.setIcon(icon1)
        self.arrow_button.setIconSize(QtCore.QSize(34, 31))
        self.arrow_button.setObjectName("arrow_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.arrow_button.clicked.connect(self.arrow_button_pressed)
        self.sign_up_button.clicked.connect(self.sign_up_button_pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REJESTRACJA"))
        self.surname_label.setText(_translate("MainWindow", "NAZWISKO"))
        self.password_label.setText(_translate("MainWindow", "HASŁO"))
        self.login_label.setText(_translate("MainWindow", "LOGIN"))
        self.email_label.setText(_translate("MainWindow", "EMAIL"))
        self.name_label.setText(_translate("MainWindow", "IMIĘ"))

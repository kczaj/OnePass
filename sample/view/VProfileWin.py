#######################################################
# 
# VProfileWin.py
# Python implementation of the Class VProfileWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:01:44
# Original author: KUBA
# 
#######################################################
from sample.controller.PProfileWin import PProfileWin
from sample.view.VWindow import VWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class VProfileWin(VWindow):

    def __init__(self, main_window, main_win_after):
        super().__init__()
        self.controller = PProfileWin(main_window, main_win_after)

    def edit_button_pressed(self):
        self.name_frame.setReadOnly(False)
        self.surname_frame.setReadOnly(False)
        self.email_frame.setReadOnly(False)

    def save_button_pressed(self):
        self.name_frame.setReadOnly(True)
        self.surname_frame.setReadOnly(True)
        self.email_frame.setReadOnly(True)
        data = (self.name_frame.text(), self.surname_frame.text(), self.email_frame.text())
        if self.controller.save_button_handle(data) != 1:
            self.error_label.setVisible(True)
            self.error_label.setText('Błąd we wprowadzonych danych!')
            self._show_data((self.name_frame, self.surname_frame, self.email_frame, self.login_frame))

    def change_password_button_pressed(self):
        password = self.password_frame.text()
        if not self.controller.change_password_button_pressed(password):
            self.error_label.setVisible(True)
            self.password_frame.setText('')
            self.error_label.setText('Musisz podać hasło, aby je zmienić')
        else:
            self.error_label.setVisible(True)
            self.password_frame.setText('')
            self.error_label.setText('Hasło zmieniono pomyślnie')

    def _show_data(self, frames):
        self.controller.show_data(frames)

    def set_profile(self, profile):
        self.controller.set_profile(profile)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 600)
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
        self.bg.setGeometry(QtCore.QRect(0, 0, 512, 600))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("view/img/o_app_tlo.png"))
        self.bg.setObjectName("bg")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(140, 410, 250, 100))
        self.error_label.setStyleSheet("QLabel{\n"
                                 "    font: 12pt \"Rubik\";\n"
                                 "    color:rgb(245,0,0);\n"
                                 "}\n")
        self.error_label.setVisible(False)
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.arrow_button.setGeometry(QtCore.QRect(15, 15, 41, 41))
        self.arrow_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/img/przycisk_strzałka.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.arrow_button.setIcon(icon)
        self.arrow_button.setIconSize(QtCore.QSize(34, 31))
        self.arrow_button.setObjectName("arrow_button")
        self.about_app_label = QtWidgets.QLabel(self.centralwidget)
        self.about_app_label.setGeometry(QtCore.QRect(56, 70, 381, 31))
        self.about_app_label.setStyleSheet("    font: 25pt \"Rubik\";\n"
                                           "    color:white;")
        self.about_app_label.setAlignment(QtCore.Qt.AlignCenter)
        self.about_app_label.setObjectName("about_app_label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 110, 401, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1)
        self.surname_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.surname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.surname_label.setObjectName("surname_label")
        self.gridLayout.addWidget(self.surname_label, 3, 0, 1, 1)
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.surname_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.surname_frame.setReadOnly(True)
        self.surname_frame.setObjectName("surname_frame")
        self.gridLayout.addWidget(self.surname_frame, 3, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.password_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_frame.setReadOnly(False)
        self.password_frame.setObjectName("password_frame")
        self.gridLayout.addWidget(self.password_frame, 9, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.email_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_frame.setReadOnly(True)
        self.email_frame.setObjectName("email_frame")
        self.gridLayout.addWidget(self.email_frame, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.login_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.login_frame.setReadOnly(True)
        self.login_frame.setObjectName("login_frame")
        self.gridLayout.addWidget(self.login_frame, 7, 1, 1, 1)
        self.email_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 5, 0, 1, 1)
        self.name_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_frame.setReadOnly(True)
        self.name_frame.setObjectName("name_frame")
        self.gridLayout.addWidget(self.name_frame, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.change_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_password_button.setGeometry(QtCore.QRect(135, 420, 84, 18))
        self.change_password_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/img/profile_win/pokaz_przycisk.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.change_password_button.setIcon(icon1)
        self.change_password_button.setIconSize(QtCore.QSize(84, 18))
        self.change_password_button.setObjectName("show_button")
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(60, 490, 161, 34))
        self.edit_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view/img/profile_win/edytuj_przycisk.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.edit_button.setIcon(icon2)
        self.edit_button.setIconSize(QtCore.QSize(161, 34))
        self.edit_button.setAutoDefault(False)
        self.edit_button.setDefault(False)
        self.edit_button.setObjectName("edit_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(290, 490, 161, 34))
        self.save_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("view/img/profile_win/zapisz_przycisk.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.save_button.setIcon(icon3)
        self.save_button.setIconSize(QtCore.QSize(161, 34))
        self.save_button.setAutoDefault(False)
        self.save_button.setDefault(False)
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._show_data((self.name_frame, self.surname_frame, self.email_frame, self.login_frame))

        self.edit_button.clicked.connect(self.edit_button_pressed)
        self.save_button.clicked.connect(self.save_button_pressed)
        self.change_password_button.clicked.connect(self.change_password_button_pressed)

        self.arrow_button.clicked.connect(self.arrow_button_pressed)
        self.arrow_button.installEventFilter(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PROFIL"))
        self.about_app_label.setText(_translate("MainWindow", "PROFIL"))
        self.name_label.setText(_translate("MainWindow", "IMIĘ"))
        self.surname_label.setText(_translate("MainWindow", "NAZWISKO"))
        self.password_label.setText(_translate("MainWindow", "HASŁO"))
        self.login_label.setText(_translate("MainWindow", "LOGIN"))
        self.email_label.setText(_translate("MainWindow", "EMAIL"))

    def eventFilter(self, source, event) -> bool:
        if event.type() == QtCore.QEvent.HoverEnter and source is self.arrow_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/przycisk_strzałka_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.arrow_button.setIcon(icon_hovered_sign_in)
            self.arrow_button.setIconSize(QtCore.QSize(34, 31))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.arrow_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/przycisk_strzałka.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.arrow_button.setIcon(icon_sign_in)
            self.arrow_button.setIconSize(QtCore.QSize(34, 31))

        return super(VProfileWin, self).eventFilter(source, event)

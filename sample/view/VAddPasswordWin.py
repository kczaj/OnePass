#######################################################
# 
# VAddPasswordWin.py
# Python implementation of the Class VAddPasswordWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:09:35
# Original author: KUBA
# 
#######################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from sample.controller.PAddPasswordWin import PAddPasswordWin
from sample.view.VGenerateWinBefore import VGenerateWinBefore
from sample.view.VWindow import VWindow


class VAddPasswordWin(VWindow):

    def __init__(self, main_window, password_list_window):
        super().__init__()
        self.controller = PAddPasswordWin(main_window, password_list_window, self)

    def generate_button_pressed(self):
        self.controller.generate_button_handle()

    def save_button_pressed(self):
        pass

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
                                 "}\n"
                                 "QComboBox{\n"
                                 "    font: 12pt \"Rubik\";\n"
                                 "    color:white;\n"
                                 "    background: rgb(119,119,119);\n"
                                 "    border-radius: 10px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 512, 600))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("view/img/o_app_tlo.png"))
        self.bg.setObjectName("bg")
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
        self.login_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 3, 0, 1, 1)
        self.url_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.url_label.setAlignment(QtCore.Qt.AlignCenter)
        self.url_label.setObjectName("url_label")
        self.gridLayout.addWidget(self.url_label, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.surname_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.surname_frame.setReadOnly(False)
        self.surname_frame.setObjectName("surname_frame")
        self.gridLayout.addWidget(self.surname_frame, 3, 1, 1, 1)
        self.category_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.category_label.setAlignment(QtCore.Qt.AlignCenter)
        self.category_label.setObjectName("category_label")
        self.gridLayout.addWidget(self.category_label, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.password_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_frame.setReadOnly(False)
        self.password_frame.setObjectName("password_frame")
        self.gridLayout.addWidget(self.password_frame, 9, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.email_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_frame.setReadOnly(False)
        self.email_frame.setObjectName("email_frame")
        self.gridLayout.addWidget(self.email_frame, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 5, 0, 1, 1)
        self.name_frame = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_frame.setReadOnly(False)
        self.name_frame.setObjectName("name_frame")
        self.gridLayout.addWidget(self.name_frame, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['mail', 'rozrywka'])
        self.gridLayout.addWidget(self.comboBox, 7, 1, 1, 1)
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(60, 490, 161, 34))
        self.generate_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/img/new_pass/generuj_przycisk.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.generate_button.setIcon(icon1)
        self.generate_button.setIconSize(QtCore.QSize(161, 34))
        self.generate_button.setAutoDefault(False)
        self.generate_button.setDefault(False)
        self.generate_button.setObjectName("generate_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(290, 490, 161, 34))
        self.save_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view/img/new_pass/zapisz_przycisk.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setIconSize(QtCore.QSize(161, 34))
        self.save_button.setAutoDefault(False)
        self.save_button.setDefault(False)
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.arrow_button.clicked.connect(self.arrow_button_pressed)
        self.generate_button.clicked.connect(self.generate_button_pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NOWE HASŁO"))
        self.about_app_label.setText(_translate("MainWindow", "NOWE HASŁO"))
        self.name_label.setText(_translate("MainWindow", "NAZWA"))
        self.login_label.setText(_translate("MainWindow", "LOGIN"))
        self.url_label.setText(_translate("MainWindow", "ADRES"))
        self.category_label.setText(_translate("MainWindow", "KATEGORIA"))
        self.password_label.setText(_translate("MainWindow", "HASŁO"))
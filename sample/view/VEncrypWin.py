#######################################################
# 
# VEncrypWin.py
# Python implementation of the Class VEncrypWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:01:57
# Original author: KUBA
# 
#######################################################
from sample.controller.PEncrypWin import PEncrypWin
from sample.view.VMainWin import VMainWin
from PyQt5 import QtCore, QtGui, QtWidgets


class VEncrypWin(VMainWin):

    def __init__(self, main_window):
        super().__init__()
        self.controller = PEncrypWin(main_window)

    def decrypt_button_pressed(self):
        pass

    def encrypt_button_pressed(self):
        pass

    # Nadpisać show(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QPushButton{\n"
                                 "    backgroung-color:transparent;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton{\n"
                                         "    background-color:transparent;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bg.setMinimumSize(QtCore.QSize(800, 600))
        self.bg.setMaximumSize(QtCore.QSize(800, 600))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("view/img/tło.png"))
        self.bg.setScaledContents(False)
        self.bg.setObjectName("bg")
        self.greeting_label = QtWidgets.QLabel(self.centralwidget)
        self.greeting_label.setGeometry(QtCore.QRect(90, 20, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(22)
        self.greeting_label.setFont(font)
        self.greeting_label.setStyleSheet("color: white")
        self.greeting_label.setObjectName("greeting_label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 9, 61, 581))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.note_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.note_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_notatki.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.note_button.setIcon(icon)
        self.note_button.setIconSize(QtCore.QSize(41, 46))
        self.note_button.setObjectName("note_button")
        self.gridLayout_2.addWidget(self.note_button, 3, 0, 1, 1)
        self.logo = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("view/img/logo_male.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)
        self.option_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.option_button.setEnabled(False)
        self.option_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/img/przycisk_opcje.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.option_button.setIcon(icon1)
        self.option_button.setIconSize(QtCore.QSize(32, 34))
        self.option_button.setObjectName("option_button")
        self.gridLayout_2.addWidget(self.option_button, 7, 0, 1, 1)
        self.password_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.password_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_hasla.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.password_button.setIcon(icon2)
        self.password_button.setIconSize(QtCore.QSize(34, 46))
        self.password_button.setObjectName("password_button")
        self.gridLayout_2.addWidget(self.password_button, 2, 0, 1, 1)
        self.home_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.home_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_home.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.home_button.setIcon(icon3)
        self.home_button.setIconSize(QtCore.QSize(32, 46))
        self.home_button.setObjectName("home_button")
        self.gridLayout_2.addWidget(self.home_button, 1, 0, 1, 1)
        self.generate_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.generate_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_generuj_maly.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generate_button.setIcon(icon4)
        self.generate_button.setIconSize(QtCore.QSize(45, 52))
        self.generate_button.setObjectName("generate_button")
        self.gridLayout_2.addWidget(self.generate_button, 4, 0, 1, 1)
        self.encrypt_file_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.encrypt_file_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_szyfruj.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encrypt_file_button.setIcon(icon5)
        self.encrypt_file_button.setIconSize(QtCore.QSize(42, 52))
        self.encrypt_file_button.setObjectName("encrypt_file_button")
        self.gridLayout_2.addWidget(self.encrypt_file_button, 5, 0, 1, 1)
        self.file_list = QtWidgets.QListView(self.centralwidget)
        self.file_list.setGeometry(QtCore.QRect(105, 101, 631, 361))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        self.file_list.setFont(font)
        self.file_list.setStyleSheet("background:transparent")
        self.file_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.file_list.setViewMode(QtWidgets.QListView.ListMode)
        self.file_list.setObjectName("file_list")
        self.encryp_button = QtWidgets.QPushButton(self.centralwidget)
        self.encryp_button.setGeometry(QtCore.QRect(600, 540, 132, 28))
        self.encryp_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("view/img/encryp_file_win/szyfruj_button.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encryp_button.setIcon(icon6)
        self.encryp_button.setIconSize(QtCore.QSize(132, 28))
        self.encryp_button.setObjectName("encryp_button")
        self.decryp_button = QtWidgets.QPushButton(self.centralwidget)
        self.decryp_button.setGeometry(QtCore.QRect(600, 490, 132, 28))
        self.decryp_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("view/img/encryp_file_win/deszyfruj_button.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decryp_button.setIcon(icon7)
        self.decryp_button.setIconSize(QtCore.QSize(132, 28))
        self.decryp_button.setObjectName("decryp_button")
        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setGeometry(QtCore.QRect(130, 545, 411, 19))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        self.file_label.setFont(font)
        self.file_label.setStyleSheet("background:rgb(119,119,119);\n"
                                      "color:white;\n"
                                      "")
        self.file_label.setText("")
        self.file_label.setObjectName("file_label")
        self.file_choose_button = QtWidgets.QPushButton(self.centralwidget)
        self.file_choose_button.setGeometry(QtCore.QRect(539, 544, 31, 21))
        self.file_choose_button.setStyleSheet("background:transparent")
        self.file_choose_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("view/img/encryp_file_win/trzykropek_button.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_choose_button.setIcon(icon8)
        self.file_choose_button.setIconSize(QtCore.QSize(27, 19))
        self.file_choose_button.setAutoDefault(False)
        self.file_choose_button.setDefault(False)
        self.file_choose_button.setFlat(False)
        self.file_choose_button.setObjectName("file_choose_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_button_action(self.home_button, self.password_button, self.note_button, self.generate_button,
                               self.encrypt_file_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TWOJE PLIKI"))
        self.greeting_label.setText(_translate("MainWindow", "TWOJE PLIKI"))
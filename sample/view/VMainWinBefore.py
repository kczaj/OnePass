#######################################################
# 
# VMainWinBefore.py
# Python implementation of the Class VMainWinBefore
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:25
# Original author: KUBA
# 
#######################################################
from PyQt5 import QtCore, QtGui, QtWidgets

from sample.controller.PMainWinBefore import PMainWinBefore
from sample.view.VWindow import VWindow


class VMainWinBefore(VWindow):

    def __init__(self, main_window, hasher):
        super().__init__()
        self.controller = PMainWinBefore(self, main_window,hasher)

    def __about_app_button_pressed(self):
        self.controller.about_app_button_handle()

    def __generate_button_pressed(self):
        self.controller.generate_button_handle()

    def _sign_in_button_pressed(self):
        self.controller.sign_in_button_handle()

    def __sign_up_button_pressed(self):
        self.controller.sign_up_button_handle()

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
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 115, 611, 468))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.generate_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.generate_button.setStyleSheet("background-color:transparent")
        self.generate_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_generuj.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.generate_button.setIcon(icon)
        self.generate_button.setIconSize(QtCore.QSize(202, 199))
        self.generate_button.setObjectName("generate_button")
        self.gridLayout.addWidget(self.generate_button, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.sign_up_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sign_up_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_zarejestruj.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.sign_up_button.setIcon(icon1)
        self.sign_up_button.setIconSize(QtCore.QSize(202, 199))
        self.sign_up_button.setObjectName("sign_up_button")
        self.gridLayout.addWidget(self.sign_up_button, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.about_app_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.about_app_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_oapp.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.about_app_button.setIcon(icon2)
        self.about_app_button.setIconSize(QtCore.QSize(202, 199))
        self.about_app_button.setObjectName("about_app_button")
        self.gridLayout.addWidget(self.about_app_button, 1, 3, 1, 1)
        self.sign_in_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sign_in_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_zaloguj.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.sign_in_button.setIcon(icon3)
        self.sign_in_button.setIconSize(QtCore.QSize(202, 199))
        self.sign_in_button.setObjectName("sign_in_button")
        self.gridLayout.addWidget(self.sign_in_button, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 9, 61, 581))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logo = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("view/img/logo_male.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)
        self.option_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.option_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("view/img/przycisk_opcje.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.option_button.setIcon(icon4)
        self.option_button.setIconSize(QtCore.QSize(32, 34))
        self.option_button.setObjectName("option_button")
        self.gridLayout_2.addWidget(self.option_button, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sign_in_button.clicked.connect(self._sign_in_button_pressed)
        self.sign_up_button.clicked.connect(self.__sign_up_button_pressed)
        self.generate_button.clicked.connect(self.__generate_button_pressed)
        self.about_app_button.clicked.connect(self.__about_app_button_pressed)

        self.sign_in_button.installEventFilter(self)
        self.sign_up_button.installEventFilter(self)
        self.about_app_button.installEventFilter(self)
        self.generate_button.installEventFilter(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ONEPASS"))
        self.greeting_label.setText(_translate("MainWindow", "WITAJ W ONEPASS"))

    def eventFilter(self, source, event) -> bool:
        if event.type() == QtCore.QEvent.HoverEnter and source is self.sign_in_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_zaloguj_hovered.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.sign_in_button.setIcon(icon_hovered_sign_in)
            self.sign_in_button.setIconSize(QtCore.QSize(202, 199))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.sign_in_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_zaloguj.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.sign_in_button.setIcon(icon_sign_in)
            self.sign_in_button.setIconSize(QtCore.QSize(202, 199))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.sign_up_button:
            icon_hovered_sign_up = QtGui.QIcon()
            icon_hovered_sign_up.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_zarejestruj_hovered.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.sign_up_button.setIcon(icon_hovered_sign_up)
            self.sign_up_button.setIconSize(QtCore.QSize(202, 199))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.sign_up_button:
            icon_sign_up = QtGui.QIcon()
            icon_sign_up.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_zarejestruj.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.sign_up_button.setIcon(icon_sign_up)
            self.sign_up_button.setIconSize(QtCore.QSize(202, 199))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.generate_button:
            icon_hovered_generate = QtGui.QIcon()
            icon_hovered_generate.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_generuj_hovered.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.generate_button.setIcon(icon_hovered_generate)
            self.generate_button.setIconSize(QtCore.QSize(202, 199))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.generate_button:
            icon_generate = QtGui.QIcon()
            icon_generate.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_generuj.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.generate_button.setIcon(icon_generate)
            self.generate_button.setIconSize(QtCore.QSize(202, 199))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.about_app_button:
            icon_hovered_about_app = QtGui.QIcon()
            icon_hovered_about_app.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_oapp_hovered.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.about_app_button.setIcon(icon_hovered_about_app)
            self.about_app_button.setIconSize(QtCore.QSize(202, 199))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.about_app_button:
            icon_about_app = QtGui.QIcon()
            icon_about_app.addPixmap(QtGui.QPixmap("view/img/main_win_before/przycisk_oapp.png"), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.about_app_button.setIcon(icon_about_app)
            self.about_app_button.setIconSize(QtCore.QSize(202, 199))


        return super(VMainWinBefore, self).eventFilter(source, event)
#######################################################
#
# VGenerateWinBefore.py
# Python implementation of the Class VGenerateWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:18
# Original author: KUBA
#
#######################################################
from sample.controller.PGenerateWinAfter import PGenerateWinAfter
from PyQt5 import QtCore, QtGui, QtWidgets

from sample.view.VMainWin import VMainWin


class VGenerateWinAfter(VMainWin):

    def __init__(self, main_window, main_win_before):
        super().__init__()
        self.controller = PGenerateWinAfter(self, main_window, main_win_before)

    def generate_button_pressed(self):
        self.controller.generate_button_handle()

    def copy_button_pressed(self):
        self.controller.copy_button_handle()

    def case_pressed(self):
        self.controller.case_handle()

    def dig_pressed(self):
        self.controller.dig_handle()

    def spec_pressed(self):
        self.controller.spec_handle()

    def static_pressed(self):
        self.controller.static_handle()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 720)
        MainWindow.setMinimumSize(QtCore.QSize(618, 720))
        MainWindow.setMaximumSize(QtCore.QSize(618, 720))
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
                                 "QSpinBox{\n"
                                 "    font: 12pt \"Rubik\";\n"
                                 "    color:white;\n"
                                 "    background: rgb(119,119,119);\n"
                                 "    border-radius: 10px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 620, 720))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("view/img/generate_win/tlo_generuj.png"))
        self.bg.setObjectName("bg")
        self.password_frame = QtWidgets.QLineEdit(self.centralwidget)
        self.password_frame.setGeometry(QtCore.QRect(40, 130, 531, 25))
        self.password_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.password_frame.setFrame(False)
        self.password_frame.setReadOnly(True)
        self.password_frame.setObjectName("password_frame")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.arrow_button.setGeometry(QtCore.QRect(15, 15, 41, 41))
        self.arrow_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/img/przycisk_strzałka.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.arrow_button.setIcon(icon)
        self.arrow_button.setIconSize(QtCore.QSize(34, 31))
        self.arrow_button.setObjectName("arrow_button")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 190, 471, 301))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.static_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.static_label.setAlignment(QtCore.Qt.AlignCenter)
        self.static_label.setObjectName("static_label")
        self.gridLayout_2.addWidget(self.static_label, 9, 0, 1, 1)
        self.case_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.case_label.setAlignment(QtCore.Qt.AlignCenter)
        self.case_label.setObjectName("case_label")
        self.gridLayout_2.addWidget(self.case_label, 3, 0, 1, 1)
        self.small_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.small_label.setObjectName("small_label")
        self.gridLayout_2.addWidget(self.small_label, 3, 3, 1, 1)
        self.static_yes_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.static_yes_label.setObjectName("static_yes_label")
        self.gridLayout_2.addWidget(self.static_yes_label, 9, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.spec_yes_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.spec_yes_label.setObjectName("spec_yes_label")
        self.gridLayout_2.addWidget(self.spec_yes_label, 7, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 10, 1, 1)
        self.dig_yes_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.dig_yes_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/img/generate_win/nie_zaznaczone_button.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("view/img/generate_win/zaznaczone_button.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dig_yes_button.setIcon(icon1)
        self.dig_yes_button.setIconSize(QtCore.QSize(31, 31))
        self.dig_yes_button.setCheckable(True)
        self.dig_yes_button.setObjectName("dig_yes_button")
        self.gridLayout_2.addWidget(self.dig_yes_button, 5, 5, 1, 1)
        self.mix_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.mix_label.setObjectName("mix_label")
        self.gridLayout_2.addWidget(self.mix_label, 3, 9, 1, 1)
        self.static_no_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.static_no_label.setObjectName("static_no_label")
        self.gridLayout_2.addWidget(self.static_no_label, 9, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        self.spin_box = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spin_box.setObjectName("spin_box")
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(25)
        self.gridLayout_2.addWidget(self.spin_box, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 4, 1, 1)
        self.spec_no_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.spec_no_label.setObjectName("spec_no_label")
        self.gridLayout_2.addWidget(self.spec_no_label, 7, 3, 1, 1)
        self.spec_no_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.spec_no_button.setText("")
        self.spec_no_button.setIcon(icon1)
        self.spec_no_button.setIconSize(QtCore.QSize(31, 31))
        self.spec_no_button.setCheckable(True)
        self.spec_no_button.setObjectName("spec_no_button")
        self.gridLayout_2.addWidget(self.spec_no_button, 7, 2, 1, 1)
        self.spec_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.spec_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spec_label.setObjectName("spec_label")
        self.gridLayout_2.addWidget(self.spec_label, 7, 0, 1, 1)
        self.dig_no_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.dig_no_button.setText("")
        self.dig_no_button.setIcon(icon1)
        self.dig_no_button.setIconSize(QtCore.QSize(31, 31))
        self.dig_no_button.setCheckable(True)
        self.dig_no_button.setObjectName("dig_no_button")
        self.gridLayout_2.addWidget(self.dig_no_button, 5, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 8, 0, 1, 1)
        self.static_yes_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.static_yes_button.setText("")
        self.static_yes_button.setIcon(icon1)
        self.static_yes_button.setIconSize(QtCore.QSize(31, 31))
        self.static_yes_button.setCheckable(True)
        self.static_yes_button.setObjectName("static_yes_button")
        self.gridLayout_2.addWidget(self.static_yes_button, 9, 5, 1, 1)
        self.case_big_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.case_big_button.setText("")
        self.case_big_button.setIcon(icon1)
        self.case_big_button.setIconSize(QtCore.QSize(31, 31))
        self.case_big_button.setCheckable(True)
        self.case_big_button.setObjectName("case_big_button")
        self.gridLayout_2.addWidget(self.case_big_button, 3, 5, 1, 1)
        self.dig_no_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.dig_no_label.setObjectName("dig_no_label")
        self.gridLayout_2.addWidget(self.dig_no_label, 5, 3, 1, 1)
        self.static_no_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.static_no_button.setText("")
        self.static_no_button.setIcon(icon1)
        self.static_no_button.setIconSize(QtCore.QSize(31, 31))
        self.static_no_button.setCheckable(True)
        self.static_no_button.setObjectName("static_no_button")
        self.gridLayout_2.addWidget(self.static_no_button, 9, 2, 1, 1)
        self.spec_yes_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.spec_yes_button.setText("")
        self.spec_yes_button.setIcon(icon1)
        self.spec_yes_button.setIconSize(QtCore.QSize(31, 31))
        self.spec_yes_button.setCheckable(True)
        self.spec_yes_button.setObjectName("spec_yes_button")
        self.gridLayout_2.addWidget(self.spec_yes_button, 7, 5, 1, 1)
        self.length_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.length_label.setAlignment(QtCore.Qt.AlignCenter)
        self.length_label.setObjectName("length_label")
        self.gridLayout_2.addWidget(self.length_label, 1, 0, 1, 1)
        self.dig_yes_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.dig_yes_label.setObjectName("dig_yes_label")
        self.gridLayout_2.addWidget(self.dig_yes_label, 5, 6, 1, 1)
        self.dig_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.dig_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dig_label.setObjectName("dig_label")
        self.gridLayout_2.addWidget(self.dig_label, 5, 0, 1, 1)
        self.big_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.big_label.setObjectName("big_label")
        self.gridLayout_2.addWidget(self.big_label, 3, 6, 1, 1)
        self.case_small_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.case_small_button.setText("")
        self.case_small_button.setIcon(icon1)
        self.case_small_button.setIconSize(QtCore.QSize(31, 31))
        self.case_small_button.setCheckable(True)
        self.case_small_button.setObjectName("case_small_button")
        self.gridLayout_2.addWidget(self.case_small_button, 3, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 0, 0, 1, 1)
        self.case_mix_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.case_mix_button.setText("")
        self.case_mix_button.setIcon(icon1)
        self.case_mix_button.setIconSize(QtCore.QSize(31, 31))
        self.case_mix_button.setCheckable(True)
        self.case_mix_button.setObjectName("case_mix_button")
        self.gridLayout_2.addWidget(self.case_mix_button, 3, 8, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 4, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 10, 0, 1, 1)
        self.static_frame = QtWidgets.QLineEdit(self.centralwidget)
        self.static_frame.setGeometry(QtCore.QRect(190, 510, 211, 21))
        self.static_frame.setObjectName("static_frame")
        self.static_frame.setMaxLength(25)
        self.static_frame.setReadOnly(True)
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(80, 560, 171, 41))
        self.generate_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view/img/generate_win/generuj_button.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.generate_button.setIcon(icon2)
        self.generate_button.setIconSize(QtCore.QSize(164, 35))
        self.generate_button.setObjectName("generate_button")
        self.copy_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_button.setGeometry(QtCore.QRect(350, 560, 171, 41))
        self.copy_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("view/img/generate_win/kopiuj.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.copy_button.setIcon(icon3)
        self.copy_button.setIconSize(QtCore.QSize(164, 35))
        self.copy_button.setObjectName("copy_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # setting default values of buttons
        self.case_small_button.setChecked(True)
        self.dig_no_button.setChecked(True)
        self.spec_no_button.setChecked(True)
        self.static_no_button.setChecked(True)

        # connecting buttons to methods
        self.generate_button.clicked.connect(self.generate_button_pressed)
        self.copy_button.clicked.connect(self.copy_button_pressed)
        self.arrow_button.clicked.connect(self.arrow_button_pressed)
        self.case_small_button.clicked.connect(self.case_pressed)
        self.case_big_button.clicked.connect(self.case_pressed)
        self.case_mix_button.clicked.connect(self.case_pressed)
        self.dig_no_button.clicked.connect(self.dig_pressed)
        self.dig_yes_button.clicked.connect(self.dig_pressed)
        self.spec_no_button.clicked.connect(self.spec_pressed)
        self.spec_yes_button.clicked.connect(self.spec_pressed)
        self.static_no_button.clicked.connect(self.static_pressed)
        self.static_yes_button.clicked.connect(self.static_pressed)

        self.arrow_button.installEventFilter(self)
        self.copy_button.installEventFilter(self)
        self.generate_button.installEventFilter(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GENEROWANIE"))
        self.static_label.setText(_translate("MainWindow", "CZĘŚĆ \n"
                                                           " STAŁA"))
        self.case_label.setText(_translate("MainWindow", "WIELKOŚĆ \n"
                                                         " LITER"))
        self.small_label.setText(_translate("MainWindow", "MAŁE"))
        self.static_yes_label.setText(_translate("MainWindow", "TAK"))
        self.spec_yes_label.setText(_translate("MainWindow", "TAK"))
        self.mix_label.setText(_translate("MainWindow", "MIX"))
        self.static_no_label.setText(_translate("MainWindow", "NIE"))
        self.spec_no_label.setText(_translate("MainWindow", "NIE"))
        self.spec_label.setText(_translate("MainWindow", "ZNAKI \n"
                                                         " SPECJALNE"))
        self.dig_no_label.setText(_translate("MainWindow", "NIE"))
        self.length_label.setText(_translate("MainWindow", "DŁUGOŚĆ"))
        self.dig_yes_label.setText(_translate("MainWindow", "TAK"))
        self.dig_label.setText(_translate("MainWindow", "CYFRY"))
        self.big_label.setText(_translate("MainWindow", "DUŻE"))

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

        if event.type() == QtCore.QEvent.HoverEnter and source is self.generate_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/generate_win/generuj_button_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.generate_button.setIcon(icon_hovered_sign_in)
            self.generate_button.setGeometry(QtCore.QRect(72, 559, 180, 38))
            self.generate_button.setIconSize(QtCore.QSize(180, 38))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.generate_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/generate_win/generuj_button.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.generate_button.setIcon(icon_sign_in)
            self.generate_button.setGeometry((QtCore.QRect(80, 560, 171, 41)))
            self.generate_button.setIconSize(QtCore.QSize(164, 35))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.copy_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/generate_win/kopiuj_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.copy_button.setIcon(icon_hovered_sign_in)
            self.copy_button.setGeometry(QtCore.QRect(342, 559, 180, 38))
            self.copy_button.setIconSize(QtCore.QSize(180, 38))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.copy_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/generate_win/kopiuj.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.copy_button.setIcon(icon_sign_in)
            self.copy_button.setGeometry(QtCore.QRect(350, 560, 171, 41))
            self.copy_button.setIconSize(QtCore.QSize(164, 35))

        return super(VGenerateWinAfter, self).eventFilter(source, event)
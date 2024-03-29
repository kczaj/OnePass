#######################################################
# 
# VAboutAppWinBefore.py
# Python implementation of the Class VAboutAppWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:04
# Original author: KUBA
# 
#######################################################
from sample.controller.PAboutAppWinBefore import PAboutAppWinBefore
from sample.view.VWindow import VWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class VAboutAppWinBefore(VWindow):

    def __init__(self, main_window, main_win_before):
        super().__init__()
        self.controller = PAboutAppWinBefore(main_window, main_win_before)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 600)
        MainWindow.setStyleSheet("QLabel{\n"
                                 "    font: 12pt \"Rubik\";\n"
                                 "    color:white;\n"
                                 "}\n"
                                 "QPushButton{\n"
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
        self.about_app_label.setGeometry(QtCore.QRect(56, 60, 381, 31))
        self.about_app_label.setStyleSheet("    font: 22pt \"Rubik\";\n"
                                           "    color:white;")
        self.about_app_label.setObjectName("about_app_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(56, 110, 400, 441))
        self.textBrowser.setStyleSheet("font: 12pt \"Rubik\";\n"
                                       "    color:white;\n"
                                       "    background: transparent;\n"
                                       "    border-radius: 10px;")
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.arrow_button.clicked.connect(self.arrow_button_pressed)
        self.arrow_button.installEventFilter(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "O APLIKACJI"))
        self.about_app_label.setText(_translate("MainWindow", "O APLIKACJI"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Rubik\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><p>One Pass jest aplikacja realizującą usługę menadżera haseł. W aplikacji jesteśmy w stanie przechowywać nasze hasła i szyfrowane notatki, zaszyfrować pliki oraz wygenerować hasło.</p> <p>Używanie aplikacji należy zacząć od zarejestrowaniu się do niej. Rejestracja wymaga od nas utworzenie trudnego hasła (minimalnie 9 znaków, wielka i mała litera, cyfra i znak specjalny). Należy to hasło zapamiętać, ponieważ odzyskanie hasła jest niemozliwe. Po zalogowaniu mamy możliwość na korzystanie z aplikacji w pełni. Po zakończeniu pracy należy przycisnąć przycisk wyloguj, który szyfruje wszystkie pliki.</p><p>Aplikacja stworzona w ramach realizacji przedmiotu Projekt Indywidualny na Politechnice Warszawskiej, której autorem jest Jakub Czajka.</p></body></html>"))

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

        return super(VAboutAppWinBefore, self).eventFilter(source, event)

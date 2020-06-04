from sample.controller.PAboutAppWinAfter import PAboutAppWinAfter
from sample.view.VMainWin import VMainWin
from PyQt5 import QtCore, QtGui, QtWidgets


class VAboutAppWinAfter(VMainWin):

    def __init__(self, main_window):
        super().__init__()
        self.controller = PAboutAppWinAfter(main_window)

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
        icon.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_notatki.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("view/img/przycisk_opcje.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.option_button.setIcon(icon1)
        self.option_button.setIconSize(QtCore.QSize(32, 34))
        self.option_button.setObjectName("option_button")
        self.gridLayout_2.addWidget(self.option_button, 7, 0, 1, 1)
        self.password_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.password_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_hasla.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
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
        icon5.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_szyfruj.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
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
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(105, 101, 611, 361))
        self.textBrowser.setStyleSheet("font: 12pt \"Rubik\";\n"
                                       "    color:white;\n"
                                       "    background: transparent;\n"
                                       "    border-radius: 10px;")
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_button_action(self.home_button, self.password_button, self.note_button, self.generate_button,
                               self.encrypt_file_button)

        self.home_button.installEventFilter(self)
        self.password_button.installEventFilter(self)
        self.note_button.installEventFilter(self)
        self.generate_button.installEventFilter(self)
        self.encrypt_file_button.installEventFilter(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "O APLIKACJI"))
        self.greeting_label.setText(_translate("MainWindow", "O APLIKACJI"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Rubik\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><p>One Pass jest aplikacja realizującą usługę menadżera haseł. W aplikacji jesteśmy w stanie przechowywać nasze hasła i szyfrowane notatki, zaszyfrować pliki oraz wygenerować hasło.</p> <p>Używanie aplikacji należy zacząć od zarejestrowaniu się do niej. Rejestracja wymaga od nas utworzenie trudnego hasła (minimalnie 9 znaków, wielka i mała litera, cyfra i znak specjalny). Należy to hasło zapamiętać, ponieważ odzyskanie hasła jest niemozliwe. Po zalogowaniu mamy możliwość na korzystanie z aplikacji w pełni. Po zakończeniu pracy należy przycisnąć przycisk wyloguj, który szyfruje wszystkie pliki.</p><p>Aplikacja stworzona w ramach realizacji przedmiotu Projekt Indywidualny na Politechnice Warszawskiej, której autorem jest Jakub Czajka.</p></body></html>"))

    def eventFilter(self, source, event) -> bool:
        if event.type() == QtCore.QEvent.HoverEnter and source is self.home_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_home_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.home_button.setIcon(icon_hovered_sign_in)
            self.home_button.setIconSize(QtCore.QSize(32, 46))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.home_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_home.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.home_button.setIcon(icon_sign_in)
            self.home_button.setIconSize(QtCore.QSize(32, 46))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.password_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_hasla_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.password_button.setIcon(icon_hovered_sign_in)
            self.password_button.setIconSize(QtCore.QSize(34, 46))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.password_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_hasla.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.password_button.setIcon(icon_sign_in)
            self.password_button.setIconSize(QtCore.QSize(34, 46))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.note_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_notatki_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.note_button.setIcon(icon_hovered_sign_in)
            self.note_button.setIconSize(QtCore.QSize(41, 46))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.note_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_notatki.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.note_button.setIcon(icon_sign_in)
            self.note_button.setIconSize(QtCore.QSize(41, 46))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.generate_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_generuj_maly_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.generate_button.setIcon(icon_hovered_sign_in)
            self.generate_button.setIconSize(QtCore.QSize(45, 52))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.generate_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_generuj_maly.png"),
                                   QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.generate_button.setIcon(icon_sign_in)
            self.generate_button.setIconSize(QtCore.QSize(45, 52))

        if event.type() == QtCore.QEvent.HoverEnter and source is self.encrypt_file_button:
            icon_hovered_sign_in = QtGui.QIcon()
            icon_hovered_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_szyfruj_hovered.png"),
                                           QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
            self.encrypt_file_button.setIcon(icon_hovered_sign_in)
            self.encrypt_file_button.setIconSize(QtCore.QSize(42, 52))
        if event.type() == QtCore.QEvent.HoverLeave and source is self.encrypt_file_button:
            icon_sign_in = QtGui.QIcon()
            icon_sign_in.addPixmap(QtGui.QPixmap("view/img/main_win_after/przycisk_szyfruj.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.encrypt_file_button.setIcon(icon_sign_in)
            self.encrypt_file_button.setIconSize(QtCore.QSize(42, 52))

        return super(VAboutAppWinAfter, self).eventFilter(source, event)
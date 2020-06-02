from abc import ABC
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class PController(ABC):

    def __init__(self, main_win, main_win_before=None):
        self.main_window = main_win
        self.main_win_before = main_win_before

    def set_main_window(self, main_win):
        self.main_window = main_win

    def arrow_button_handle(self):
        self.change_window(self.main_win_before)

    def change_window(self, window):
        self.main_window.close()
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.setWindowIcon(QtGui.QIcon('view/img/ikona.png'))
        window.update_main_window(self.main_window)
        window.show(self.main_window)
        self.main_window.show()
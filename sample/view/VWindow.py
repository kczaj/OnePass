from abc import ABC, abstractmethod

from PyQt5.QtCore import QObject


class VWindow(QObject):

    def __init__(self):
        super().__init__()
        self.controller = None

    def update_main_window(self, main_win):
        self.controller.set_main_window(main_win)

    def arrow_button_pressed(self):
        self.controller.arrow_button_handle()

    def show(self, where):
        self.setupUi(where)

    '''@abstractmethod
    def setupUi(self, where):
        pass'''

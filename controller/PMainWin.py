#######################################################
# 
# PMainWin.py
# Python implementation of the Class PMainWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:02:02
# Original author: KUBA
# 
#######################################################
from controller.PController import PController
from PyQt5 import QtWidgets


class PMainWin(PController):

    def __init__(self, main_window):
        super().__init__(main_window)
        self.window_list = None

    def encrypt_file_button_handle(self):
        self.main_window.close()
        self.main_window = QtWidgets.QMainWindow()
        self.window_list[4].update_main_window(self.main_window)
        self.window_list[4].show(self.main_window)
        self.main_window.show()
        pass

    def generate_button_handle(self):
        self.main_window.close()
        self.main_window = QtWidgets.QMainWindow()
        self.window_list[3].update_main_window(self.main_window)
        self.window_list[3].show(self.main_window)
        self.main_window.show()
        pass

    def home_button_handle(self):
        self.main_window.close()
        self.main_window = QtWidgets.QMainWindow()
        self.window_list[0].update_main_window(self.main_window)
        self.window_list[0].show(self.main_window)
        self.main_window.show()

    def note_button_handle(self):
        self.main_window.close()
        self.main_window = QtWidgets.QMainWindow()
        self.window_list[2].update_main_window(self.main_window)
        self.window_list[2].show(self.main_window)
        self.main_window.show()
        pass

    def password_button_handle(self):
        self.main_window.close()
        self.main_window = QtWidgets.QMainWindow()
        self.window_list[1].update_main_window(self.main_window)
        self.window_list[1].show(self.main_window)
        self.main_window.show()

    # [0] -- main_win_after
    # [1] -- password_list_win
    # [2] -- note_list_win
    # [3] -- generate_win
    # [4] -- encryp_win
    def set_window_list(self, win_list):
        self.window_list = win_list

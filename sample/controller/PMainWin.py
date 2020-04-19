#######################################################
# 
# PMainWin.py
# Python implementation of the Class PMainWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:02:02
# Original author: KUBA
# 
#######################################################
from sample.controller.PController import PController
from PyQt5 import QtWidgets


class PMainWin(PController):

    def __init__(self, main_window, window_before=None):
        super().__init__(main_window, window_before)
        self.window_list = None

    # Pamiętać by zmienić na 4 gdy dodam generate_win działające
    def encrypt_file_button_handle(self):
        self.change_window(self.window_list[3])

    def generate_button_handle(self):
        self.change_window(self.window_list[4])

    def home_button_handle(self):
        self.change_window(self.window_list[0])

    def note_button_handle(self):
        self.change_window(self.window_list[2])

    def password_button_handle(self):
        self.change_window(self.window_list[1])

    # [0] -- main_win_after
    # [1] -- password_list_win
    # [2] -- note_list_win
    # [3] -- generate_win
    # [4] -- encryp_win
    def set_window_list(self, win_list):
        self.window_list = win_list

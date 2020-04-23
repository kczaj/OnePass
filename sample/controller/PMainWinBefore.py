#######################################################
# 
# PMainWinBefore.py
# Python implementation of the Class PMainWinBefore
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:23
# Original author: KUBA
# 
#######################################################

from PyQt5 import QtWidgets

from sample.controller.PController import PController
from sample.view.VSignInWin import VSignInWin
from sample.view.VSignUpWin import VSignUpWin
from sample.view.VGenerateWinBefore import VGenerateWinBefore
from sample.view.VAboutAppWinBefore import VAboutAppWinBefore
from sample.model.MLoader import MLoader


class PMainWinBefore(PController):

    def __init__(self, main_win_before, main_window, hasher):
        super().__init__(main_window, main_win_before)

        self._loader = MLoader()
        self._loader.load_logins()
        self._about_app_win = VAboutAppWinBefore(main_window, self.main_win_before)
        self._generate_win = VGenerateWinBefore(main_window, self.main_win_before)
        self._sign_up_win = VSignUpWin(main_window, self.main_win_before, self._generate_win)
        self._sign_in_win = VSignInWin(main_window, self._loader, self._sign_up_win, self.main_win_before,
                                       self._generate_win, hasher)
        self.main_win_before.show(self.main_window)
        self.main_window.show()

    def about_app_button_handle(self):
        self.change_window(self._about_app_win)

    def generate_button_handle(self):
        self.change_window(self._generate_win)

    def __load_logins(self):
        pass

    def sign_in_button_handle(self):
        self.change_window(self._sign_in_win)

    def sign_up_button_handle(self):
        self.change_window(self._sign_up_win)

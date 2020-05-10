#######################################################
# 
# PSignInWin.py
# Python implementation of the Class PSignInWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:17
# Original author: KUBA
# 
#######################################################
# from view.VMainWinAfter import VMainWinAfter
from sample.controller.PController import PController
from sample.model.MChecker import MChecker
from sample.model.MEncryptor import MEncryptor
from PyQt5 import QtWidgets
from sample.view.VEncrypWin import VEncrypWin
from sample.view.VGenerateWinAfter import VGenerateWinAfter
from sample.view.VMainWinAfter import VMainWinAfter
from sample.view.VNoteListWin import VNoteListWin
from sample.view.VPasswordsListWin import VPasswordsListWin


class PSignInWin(PController):

    # remember about MainWinAfter

    def __init__(self, main_window, loader, sign_up_win, main_win_before, generate_win, hasher):
        super().__init__(main_window, main_win_before)
        self._generate_win = generate_win
        self._loader = loader
        self._checker = MChecker(self._loader, hasher)
        self._encryptor = MEncryptor()
        self._sign_up_window = sign_up_win

    def forget_button_handle(self):
        pass

    def _load_profile(self, login, password):
        return self._loader.load_profile(login, password)

    def sign_in_button_handle(self, login, password):
        if self.__validate_data((login, password)):
            profile = self._load_profile(login, password)
            main_win_after = VMainWinAfter(self.main_window, self.main_win_before)
            win_list = [main_win_after, VPasswordsListWin(self.main_window),
                        VNoteListWin(self.main_window), VEncrypWin(self.main_window),
                        VGenerateWinAfter(self.main_window, main_win_after)]
            for i in range(len(win_list)):
                win_list[i].set_window_list(win_list)
                win_list[i].set_profile(profile)
            win_list[0].set_window_list_in_subwindow()
            self.change_window(win_list[0])
        else:
            print("Error. Wrong login or passoword")

    def sign_up_button_handle(self):
        self.change_window(self._sign_up_window)

    def __validate_data(self, data):
        return self._checker.verify_data(data)

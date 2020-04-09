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
from controller.PController import PController
from model.MChecker import MChecker
from model.MEncryptor import MEncryptor
from PyQt5 import QtWidgets


class PSignInWin(PController):

    # remember about MainWinAfter

    def __init__(self, main_window, loader, sign_up_win, main_win_before):
        super().__init__(main_window,main_win_before)
        self._loader = loader
        self._checker = MChecker()
        self._encryptor = MEncryptor()
        self._sign_up_window = sign_up_win

    def forget_button_handle(self):
        pass

    def __load_profile(self, login):
        pass

    def sign_in_button_handle(self):
        pass

    def sign_up_button_handle(self):
        pass

    def __validate_data(self, data):
        pass

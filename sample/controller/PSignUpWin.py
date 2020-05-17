#######################################################
# 
# PSignUpWin.py
# Python implementation of the Class PSignUpWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:15
# Original author: KUBA
# 
#######################################################

# from view.VMainWinAfter import VMainWinAfter

from sample.controller.PController import PController
from sample.model.MProfileMaker import MProfileMaker
import string

# remember about MainWinAfter
from sample.view.VEncrypWin import VEncrypWin
from sample.view.VGenerateWinAfter import VGenerateWinAfter
from sample.view.VMainWinAfter import VMainWinAfter
from sample.view.VNoteListWin import VNoteListWin
from sample.view.VPasswordsListWin import VPasswordsListWin


class PSignUpWin(PController):
    NOT_ALL_GAPS_FILLED_ERROR = 'Wypełnij wszystkie pola'
    NAME_ERROR = 'Podane imię jest niepoprawne'
    SURNAME_ERROR = 'Podane nazwisko jest niepoprawne'
    EMAIL_ERROR = 'Podany mail jest niepoprawny'
    LOGIN_ERROR = 'Podany login jest niepoprawny'
    PASSWORD_ERROR = 'Podane hasło nie spełnia wymogów'

    def __init__(self, sign_up_win, main_window, _loader, main_win_before, generate_win, hasher):
        super().__init__(main_window, main_win_before)
        self._loader = _loader
        self._profile_maker = MProfileMaker()
        self._sign_up_win = sign_up_win
        self._generate_win = generate_win
        self._hasher = hasher

    def sign_up_button_handle(self, name, surname, email, login, password):
        status = self.__validate_data(name, surname, email, login, password)
        if status == '1':
            profile = self._profile_maker.make_profile(name, surname, email, login, password)
            logins = self._loader.get_logins()
            logins[login] = self._hasher.hash(password)
            main_win_after = VMainWinAfter(self.main_window, self.main_win_before)
            win_list = [main_win_after, VPasswordsListWin(self.main_window),
                        VNoteListWin(self.main_window), VEncrypWin(self.main_window),
                        VGenerateWinAfter(self.main_window, main_win_after)]
            for i in range(len(win_list)):
                win_list[i].set_window_list(win_list)
                win_list[i].set_profile(profile)
            win_list[0].set_window_list_in_subwindow()
            self.change_window(win_list[0])
            return '1'
        else:
            return status

    def __validate_data(self, name, surname, email, login, password):
        special_symols = '!@#$%^&*()_-+={[}]\:;<,>.?/'
        digits = string.digits
        if name != '' and surname != '' and email != '' and login != '' and password != '':
            for c in special_symols + digits:
                if c in name:
                    return self.NAME_ERROR
                if c in surname:
                    return self.SURNAME_ERROR
            for c in special_symols:
                if c in login:
                    return self.LOGIN_ERROR
            return '1'
        else:
            return self.NOT_ALL_GAPS_FILLED_ERROR

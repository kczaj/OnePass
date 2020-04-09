#######################################################
# 
# PMainWin.py
# Python implementation of the Class PMainWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:02:02
# Original author: KUBA
# 
#######################################################
from view.VEncrypWin import VEncrypWin
from view.VMainWinAfter import VMainWinAfter
from view.VNoteListWin import VNoteListWin
from view.VPasswordsListWin import VPasswordsListWin
from view.VGenerateWinBefore import VGenerateWinBefore

class PMainWin:
    m_VEncrypWin= VEncrypWin()

    m_VMainWinAfter= VMainWinAfter()

    m_VNoteListWin= VNoteListWin()

    m_VPasswordsListWin= VPasswordsListWin()

    m_VGenerateWin= VGenerateWinBefore()

    def encrypt_file_button_handle(self):
        pass

    def generate_button_handle(self):
        pass

    def home_button_handle(self):
        pass

    def note_button_handle(self):
        pass

    def password_button_handle(self):
        pass
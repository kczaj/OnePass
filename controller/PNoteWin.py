#######################################################
# 
# PNoteWin.py
# Python implementation of the Class PNoteWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:14:38
# Original author: KUBA
# 
#######################################################
from view.VGenerateWin import VGenerateWin
from view.VEncrypWin import VEncrypWin
from view.VPasswordsListWin import VPasswordsListWin
from view.VMainWinAfter import VMainWinAfter
from view.VAddNoteWin import VAddNoteWin
from model.MProfile import MProfile
from controller.PMainWin import PMainWin

class PNoteWin(PMainWin):
    m_VGenerateWin= VGenerateWin()

    m_VEncrypWin= VEncrypWin()

    m_VPasswordsListWin= VPasswordsListWin()

    m_VMainWinAfter= VMainWinAfter()

    m_VAddNoteWin= VAddNoteWin()

    m_MProfile= MProfile()

    def add_button_handle(self):
        pass

    def delete_button_handle(self, note):
        pass

    def edit_button_handle(self):
        pass

    def save_button_handle(self, note):
        pass

    def __update(self, notes):
        pass
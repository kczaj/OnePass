#######################################################
# 
# PPasswordsListWin.py
# Python implementation of the Class PPasswordsListWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:09:37
# Original author: KUBA
# 
#######################################################
'''from view.VPasswordWin import VPasswordWin
from view.VEncrypWin import VEncrypWin
'''
from PyQt5.QtWidgets import QListWidgetItem

from sample.controller.PMainWin import PMainWin
from sample.view.VAddPasswordWin import VAddPasswordWin
from PyQt5 import QtGui, QtCore


class PPasswordsListWin(PMainWin):

    def __init__(self, main_window, password_list_win):
        super().__init__(main_window)
        self.password_list_win = password_list_win
        self.add_password_window = VAddPasswordWin(self.main_window, self.password_list_win)

    def add_button_handle(self):
        self.change_window(self.add_password_window)

    def choose_button_handle(self):
        pass

    def add_item_to_list(self, password_list):
        icon_names = ['view/img/icons/mail.png', 'view/img/icons/rozrywka.png']
        icons = []
        for name in icon_names:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(name), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
            icon.actualSize(QtCore.QSize(99, 98))
            icons.append(icon)

        passwords = self.profile.get_passwords()
        favourites = []
        not_favourites = []
        for password in passwords.values():
            isFavourite = password.get_isFavourite()
            if isFavourite:
                favourites.append(password)
            else:
                not_favourites.append(password)
        types = []
        types.append(favourites)
        types.append(not_favourites)

        for type in types:
            for password in type:
                type = password.get_type()
                index = -1
                if type == 'mail':
                    index = 0
                elif type == 'rozrywka':
                    index = 1
                else:
                    raise Exception("Type not supported")

                item = QListWidgetItem()
                item.setSizeHint(QtCore.QSize(150,150))
                item.setIcon(icons[index])
                item.setText(password.get_name())
                password_list.addItem(item)

        self.add_password_window.set_profile(self.profile)


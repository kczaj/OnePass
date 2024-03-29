#######################################################
# 
# PNoteWin.py
# Python implementation of the Class PNoteWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 12:14:38
# Original author: KUBA
# 
#######################################################
from sample.controller.PMainWin import PMainWin
from sample.model.MEncryptor import MEncryptor
from sample.model.MNote import MNote
from sample.view.VAddNoteWin import VAddNoteWin
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QListWidgetItem
from Crypto.Random import get_random_bytes


class PNoteWin(PMainWin):

    def __init__(self, main_window, note_list_win):
        super().__init__(main_window)
        self._note_list_win = note_list_win
        self._add_note_window = VAddNoteWin(self)
        self._encryptor = MEncryptor()

    def add_button_handle(self):
        self._note = None
        self.change_window(self._add_note_window)
        self._add_note_window.new_note_settings()

    def delete_button_handle(self, name):
        notes = self.profile.get_notes()
        notes.pop(name.lower())
        self.change_window(self._note_list_win)

    def save_button_handle(self, note):
        name = note[0]
        msg = note[1]
        if self._note is None:
            notes = self.profile.get_notes()
            if name in notes:
                return
            path = 'data/' + self.profile.get_login() + '/note/' + name.lower() + '_b'
            note_instance = MNote(name, path)
            notes[name.lower()] = note_instance
            salt = get_random_bytes(32)
            self._encryptor.encrypt(path, msg, salt, self.profile.get_password())
            self.change_window(self._note_list_win)
        else:
            path = self._note.get_path()
            salt = get_random_bytes(32)
            self._encryptor.encrypt(path, msg, salt, self.profile.get_password())
            self.change_window(self._note_list_win)

    def edit_button_handle(self, name):
        if name == '':
            return
        notes = self.profile.get_notes()
        self._note = notes[name.lower()]
        msg = self.get_msg(self._note)
        self.change_window(self._add_note_window)
        self._add_note_window.set_note(self._note, msg)

    def get_msg(self, note):
        path = note.get_path()
        msg = self._encryptor.decrypt(path, self.profile.get_password())
        return msg

    def add_notes(self, note_list):
        notes = self.profile.get_notes()

        for note in notes.values():
            item = QListWidgetItem()
            item.setSizeHint(QtCore.QSize(150, 150))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('view/img/icons/notatki.png'), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            icon.actualSize(QtCore.QSize(99, 98))
            item.setIcon(icon)
            item.setText(note.get_name())
            note_list.addItem(item)

#######################################################
# 
# MLoader.py
# Python implementation of the Class MLoader
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:33
# Original author: KUBA
# 
#######################################################
from sample.model.MEncryptor import MEncryptor
from sample.model.MNote import MNote
from sample.model.MPassword import MPassword
from sample.model.MProfileMaker import MProfileMaker


class MLoader:
    login_file = 'data/logins'
    key = b'\xcf>\'E\x9f\x9e\xe78\x07"\xad\xee\xb0%\x88\xb69\xc4\xe5P-\x95\xf6\xe7\x0b\n\x14\xa1j\xbb!\x92'

    def __init__(self):
        self._logins = {}
        self._profile_maker = MProfileMaker()
        self._encryptor = MEncryptor()

    def load_logins(self):
        logins = self._encryptor.decrypt('data/log')
        lines = logins.split('\n')
        for line in lines:
            words = line.split(';')
            password = words[1]
            if password[-1] == '\n':
                password = password[:-1]
            self._logins[words[0]] = password

    def load_profile(self, login_instance, password):
        info = 'data/' + login_instance + '/infob'
        passwords = 'data/' + login_instance + '/passwords'
        notes = 'data/' + login_instance + '/notes'

        info_str = self._encryptor.decrypt(info, password)
        words = info_str.split(';')
        name_instance = words[0]
        surname_instance = words[1]
        email_instance = words[2]
        login_instance = words[3]

        passwords_list = {}

        with open(passwords, 'r') as f:
            data = f.readlines()
            for line in data:
                words = line.split(';')
                name = words[0]
                login = words[1]
                password = words[2]
                type = words[3]
                isFavourite = True if words[4] == '1' else False
                password = MPassword(name, login, password, type, isFavourite)
                passwords_list[name] = password

        notes_list = {}

        with open(notes, 'r') as f:
            data = f.readlines()
            for line in data:
                word = line.split('\\n')
                path = 'data/' + login_instance + 'note' + word[0]
                note = MNote(word[0], path)
                notes_list[word[0]] = note

        return self._profile_maker.make_profile(name_instance, surname_instance, email_instance, login_instance,
                                                passwords_list, notes_list)

    def get_logins(self):
        return self._logins

    def set_logins(self, logins):
        self._logins = logins

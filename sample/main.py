import sys
from PyQt5 import QtWidgets

from sample.model.MEncryptor import MEncryptor
from sample.model.MHasher import MHasher
from sample.view.VMainWinBefore import VMainWinBefore
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

if __name__ == '__main__':
    hasher = MHasher()
    encryptor = MEncryptor()
    '''salt = get_random_bytes(32)
    file = open('data/admin/encrypteds', 'r')
    msg = file.read()
    encryptor.encrypt('data/admin/encryptedsb', msg, salt, 'passwrd12')'''

    '''salt = get_random_bytes(32)
    msg = encryptor.decrypt('data/admin/encrypted/jezyki.txt.ope', 'passwrd1')
    encryptor.encrypt('data/admin/encrypted/jezyki.txt.ope', msg, salt, 'passwrd12')
    msg = encryptor.decrypt('data/admin/note/notatka_1_b', 'passwrd1')
    encryptor.encrypt('data/admin/note/notatka_1_b', msg, salt, 'passwrd12')
    msg = encryptor.decrypt('data/admin/note/notatka_2_b', 'passwrd1')
    encryptor.encrypt('data/admin/note/notatka_2_b', msg, salt, 'passwrd12')
    msg = encryptor.decrypt('data/admin/note/notatka_3_b', 'passwrd1')
    encryptor.encrypt('data/admin/note/notatka_3_b', msg, salt, 'passwrd12')'''
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    w = VMainWinBefore(main_window, hasher)
    sys.exit(app.exec_())

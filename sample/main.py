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
    encryptor.encrypt('data/admin/encryptedsb', msg, salt, 'passwrd1')'''
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    w = VMainWinBefore(main_window, hasher)
    sys.exit(app.exec_())

#######################################################
# 
# MEncryptor.py
# Python implementation of the Class MEncryptor
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:37
# Original author: KUBA
# 
#######################################################
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
import sys


class MEncryptor:
    password = b'ZobaczmyCzyToZadziala'

    def decrypt(self, file, password=None):
        if password is None:
            password = self.password
        try:
            file_in = open(file, 'rb')
            salt = file_in.read(32)
            iv = file_in.read(16)
            msg = file_in.read()
            file_in.close()

            key = PBKDF2(password, salt, dkLen=32)
            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            og_data = unpad(cipher.decrypt(msg), AES.block_size)
            return og_data.decode('utf-8')
        except FileNotFoundError:
            print('Nie znaleziono pliku ' + file)
            sys.exit()

    def encrypt(self, file, data, salt, password=None):
        if password is None:
            password = self.password
        msg = data.encode()
        key = PBKDF2(password, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(msg, AES.block_size))
        output_file = open(file, 'wb')
        output_file.write(salt)
        output_file.write(cipher.iv)
        output_file.write(ciphered_data)
        output_file.close()

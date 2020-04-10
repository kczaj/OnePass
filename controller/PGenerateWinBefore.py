#######################################################
# 
# PGenerateWinBefore.py
# Python implementation of the Class PGenerateWin
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:13
# Original author: KUBA
# 
#######################################################
from controller.PController import PController
from model.MGenerator import MGenerator
from PyQt5 import QtWidgets


class PGenerateWinBefore(PController):

    def __init__(self, generate_win, main_window, main_win_before):
        super().__init__(main_window, main_win_before)
        self._generate_win = generate_win
        self._generator = MGenerator()
        self.setting = [10, 1, 1, 1, 1, ""]

    def case_handle(self):
        sender = self.main_window.sender()
        if sender == self._generate_win.case_small_button:
            if not self._generate_win.case_small_button.isChecked():
                self._generate_win.case_small_button.setChecked(False)
                self._generate_win.case_big_button.setChecked(True)
                self._generate_win.case_mix_button.setChecked(False)
                self.setting[1] = 2
            else:
                self._generate_win.case_small_button.setChecked(True)
                self._generate_win.case_big_button.setChecked(False)
                self._generate_win.case_mix_button.setChecked(False)
                self.setting[1] = 1
        elif sender == self._generate_win.case_big_button:
            if not self._generate_win.case_big_button.isChecked():
                self._generate_win.case_small_button.setChecked(False)
                self._generate_win.case_big_button.setChecked(False)
                self._generate_win.case_mix_button.setChecked(True)
                self.setting[1] = 3
            else:
                self._generate_win.case_small_button.setChecked(False)
                self._generate_win.case_big_button.setChecked(True)
                self._generate_win.case_mix_button.setChecked(False)
                self.setting[1] = 2
        else:
            if not self._generate_win.case_mix_button.isChecked():
                self._generate_win.case_small_button.setChecked(True)
                self._generate_win.case_big_button.setChecked(False)
                self._generate_win.case_mix_button.setChecked(False)
                self.setting[1] = 1
            else:
                self._generate_win.case_small_button.setChecked(False)
                self._generate_win.case_big_button.setChecked(False)
                self._generate_win.case_mix_button.setChecked(True)
                self.setting[1] = 3

    def dig_handle(self):
        sender = self.main_window.sender()
        if sender == self._generate_win.dig_no_button:
            if not self._generate_win.dig_no_button.isChecked():
                self._generate_win.dig_no_button.setChecked(False)
                self._generate_win.dig_yes_button.setChecked(True)
                self.setting[2] = 2
            else:
                self._generate_win.dig_no_button.setChecked(True)
                self._generate_win.dig_yes_button.setChecked(False)
                self.setting[2] = 1
        else:
            if not self._generate_win.dig_yes_button.isChecked():
                self._generate_win.dig_no_button.setChecked(True)
                self._generate_win.dig_yes_button.setChecked(False)
                self.setting[2] = 1
            else:
                self._generate_win.dig_no_button.setChecked(False)
                self._generate_win.dig_yes_button.setChecked(True)
                self.setting[2] = 2

    def spec_handle(self):
        sender = self.main_window.sender()
        if sender == self._generate_win.spec_no_button:
            if not self._generate_win.spec_no_button.isChecked():
                self._generate_win.spec_no_button.setChecked(False)
                self._generate_win.spec_yes_button.setChecked(True)
                self.setting[3] = 2
            else:
                self._generate_win.spec_no_button.setChecked(True)
                self._generate_win.spec_yes_button.setChecked(False)
                self.setting[3] = 1
        else:
            if not self._generate_win.spec_yes_button.isChecked():
                self._generate_win.spec_no_button.setChecked(True)
                self._generate_win.spec_yes_button.setChecked(False)
                self.setting[3] = 1
            else:
                self._generate_win.spec_no_button.setChecked(False)
                self._generate_win.spec_yes_button.setChecked(True)
                self.setting[3] = 2

    def static_handle(self):
        sender = self.main_window.sender()
        if sender == self._generate_win.static_no_button:
            if not self._generate_win.static_no_button.isChecked():
                self._generate_win.static_no_button.setChecked(False)
                self._generate_win.static_yes_button.setChecked(True)
                self.setting[4] = 2
            else:
                self._generate_win.static_no_button.setChecked(True)
                self._generate_win.static_yes_button.setChecked(False)
                self.setting[4] = 1
        else:
            if not self._generate_win.static_yes_button.isChecked():
                self._generate_win.static_no_button.setChecked(True)
                self._generate_win.static_yes_button.setChecked(False)
                self.setting[4] = 1
            else:
                self._generate_win.static_no_button.setChecked(False)
                self._generate_win.static_yes_button.setChecked(True)
                self.setting[4] = 2

        if self._generate_win.static_no_button.isChecked():
            self._generate_win.static_frame.clear()
            self._generate_win.static_frame.setReadOnly(True)
        else:
            self._generate_win.static_frame.setReadOnly(False)

    def generate_button_handle(self):
        self.setting[5] = self._generate_win.static_frame.text()
        if self.setting[4] == 2:
            self._generate_win.spin_box.setValue(self._generate_win.spin_box.value() + len(self.setting[5]))
        self.setting[0] = self._generate_win.spin_box.value()
        password = self._generator.generate(self.setting)
        self._generate_win.password_frame.setText(password)

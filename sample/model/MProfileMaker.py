#######################################################
# 
# MProfileMaker.py
# Python implementation of the Class MProfileMaker
# Generated by Enterprise Architect
# Created on:      04-kwi-2020 11:43:07
# Original author: KUBA
# 
#######################################################
from sample.model.MProfile import MProfile


class MProfileMaker():

    def make_profile(self, name, surname, email, login, password):
        return  MProfile(name, surname, email, login, password)

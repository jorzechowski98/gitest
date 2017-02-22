#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wersja funkcyjna, zmienna lokalna

#DEFINICJA KLASY
class Samochod(object):
    def __init__(self, marka='', model='', ileOsob=0):
        self.marka = ileOsob
        self.model = ileOsob

    def laduj(self, ileOsob):
        self.model += ileOsob
        return self.model

    def wyladuj(self, ileOsob):
        self.model -= ile
        return self.model

car1= Samochod()
car2= Samochod()

ileOsob = int(raw_input("Ładuj 1: "))
print "Wolne miejsca:", car1.laduj(ileOsob)

ileOsob = int(raw_input("Ładuj 2: "))
print "Wolne miejsca:", car2.laduj(ileOsob)

ileOsob = int(raw_input("Wyładuj 1: "))
print "Wolne miejsca:", car1.(ileOsob)

ileOsob = int(raw_input("Wyładuj 2: "))
print "Wolne miejsca:", car2.wyladuj(ileOsob)


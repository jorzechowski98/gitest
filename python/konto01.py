#!/usr/bin/env python
# -*- coding: utf-8 -*-

bilans = 0
ile = int(raw_input("Wpłata: "))
bilans += ile
print "Stan konta:", bilans

ile = int(raw_input("Stojek: "))
bilans -= ile
print "Stan konta:", bilans

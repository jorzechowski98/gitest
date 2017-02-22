#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class Konwerter(QWidget):
    def __init__(self, parent=None):
        super(Konwerter, self).__init__(parent)

        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta1 = QLabel("Chcę przeliczyć: ")
        etykieta2 = QLabel("Wynik: ")

        # pola edycyjne
        self.liczba = QLineEdit()
        self.wynik = QLineEdit()


        # układ tabelaryczny
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 3, 0)
        ukladT.addWidget(self.liczba, 0, 1)
        ukladT.addWidget(self.wynik, 3, 1)

        # przyciski
        mcmBtn = QPushButton("&m na cm", self)
        cmmBtn = QPushButton("&cm na m", self)
        calmBtn = QPushButton("&cal na m", self)
        mcalBtn = QPushButton("&m na cal", self)
        ftmBtn = QPushButton("&ft na m", self)
        mftBtn = QPushButton("&m na ft", self)
        ydmBtn = QPushButton("&yd na m", self)
        mydBtn = QPushButton("&m na yd", self)
        ukladH = QHBoxLayout()
        ukladH.addWidget(mcmBtn)
        ukladH.addWidget(cmmBtn)
        ukladH.addWidget(calmBtn)
        ukladH.addWidget(mcalBtn)
        ukladH.addWidget(ftmBtn)
        ukladH.addWidget(mftBtn)
        ukladH.addWidget(ydmBtn)
        ukladH.addWidget(mydBtn)



        ukladT.addLayout(ukladH, 2, 0, 1, 3)

        koniecBtn = QPushButton("&Koniec", self)
        ukladT.addWidget(koniecBtn, 4, 0, 1, 3)

        self.setLayout(ukladT)

        #obsługa zdarzeń
        koniecBtn.clicked.connect(self.koniec)
        mcmBtn.clicked.connect(self.dzialanie)
        cmmBtn.clicked.connect(self.dzialanie)
        calmBtn.clicked.connect(self.dzialanie)
        mcalBtn.clicked.connect(self.dzialanie)
        ftmBtn.clicked.connect(self.dzialanie)
        mftBtn.clicked.connect(self.dzialanie)
        ydmBtn.clicked.connect(self.dzialanie)
        mydBtn.clicked.connect(self.dzialanie)
        self.resize(500, 200)
        self.setWindowTitle("Konwerter jednostek długośći")
        self.show()


    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def koniec(self):
        self.close()

    def dzialanie(self):
        nadawca = self.sender()

        try:

            liczba = float(self.liczba.text())
            if liczba <0:
                ujemne = QMessageBox.question(
                self, 'Komunikat',
                "Wprowadź poprawną wartość.",QMessageBox.Ok)
                liczba = 0

            if nadawca.text() == "&m na cm":
                wynik = liczba*100
            elif nadawca.text() == "&cm na m":
                wynik = liczba*0.01
            elif nadawca.text() == "&cal na m":
                wynik = liczba*0.0254
            elif nadawca.text() == "&m na cal":
                wynik = liczba*39.370079
            elif nadawca.text() == "&ft na m":
                wynik = liczba*0.3048
            elif nadawca.text() == "&m na ft":
                wynik = liczba*3.28084
            elif nadawca.text() == "&yd na m":
                wynik = liczba*0.914400
            elif nadawca.text() == "&m na yd":
                wynik = liczba*1.093613





            self.wynik.setText(str(wynik))



        except (ValueError, ZeroDivisionError):
            QMessageBox.warning(self, "Błąd", "Błędne dane!", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Konwerter()
    sys.exit(app.exec_())

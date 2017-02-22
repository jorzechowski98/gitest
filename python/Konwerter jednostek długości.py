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
        ukladT.addWidget(etykieta1, 2, 0)
        ukladT.addWidget(etykieta2, 3, 0)
        ukladT.addWidget(self.liczba, 1, 1)
        ukladT.addWidget(self.wynik, 3, 1)

        # przyciski
        mcmBtn = QPushButton("&m na cm", self)
        cmmBtn = QPushButton("&cm na m", self)
        ukladH = QHBoxLayout()
        ukladH.addWidget(mcmBtn)
        ukladH.addWidget(cmmBtn)


        ukladT.addLayout(ukladH, 2, 0, 1, 3)

        koniecBtn = QPushButton("&Koniec", self)
        ukladT.addWidget(koniecBtn, 4, 0, 1, 3)

        self.setLayout(ukladT)

        #obsługa zdarzeń
        koniecBtn.clicked.connect(self.koniec)
        mcmBtn.clicked.connect(self.dzialanie)
        cmmBtn.clicked.connect(self.dzialanie)

        self.resize(300, 100)
        self.setWindowTitle("Konwerter jednostek")
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

            if nadawca.text() == "&m na cm":
                wynik = liczba*100
            elif nadawca.text() == "&cm na m":
                wynik = liczba*0.01



            self.wynik.setText(str(wynik))

        except (ValueError, ZeroDivisionError):
            QMessageBox.warning(self, "Błąd", "Błędne dane!", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Konwerter()
    sys.exit(app.exec_())

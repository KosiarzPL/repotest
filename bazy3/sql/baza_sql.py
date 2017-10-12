#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#  dane.py
# 

import sqlite3
from dane import *


def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor()   # utworzenie kursora
    
    with open('pracownicy.sql', 'r') as plik:
        cur.executescript(plik.read())
        
    premia = dane_z_pliku('premia.txt')
    premia = wyczysc_dane(premia, 1)
    
    pracownicy = dane_z_pliku('pracownicy.txt')
    pracownicy = wyczysc_dane(pracownicy, 5)
    
    dzial = dane_z_pliku('dział.txt')
    
    cur.executemany('INSERT INTO dzial VALUES (?, ?, ?)',dzial)
    cur.executemany('INSERT INTO premia VALUES (?, ?)',premia)
    
    cur.executemany('INSERT INTO pracownicy (id, nazwisko, imie, stanowisko,data_zatr, placa, id_dzial) VALUES (?, ?, ?, ?, ?, ?, ?)',pracownicy)
    
    con.commit()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

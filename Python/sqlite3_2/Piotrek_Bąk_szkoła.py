#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#zapytania.py

import sqlite3


def kw_a(cur):
    cur.execute('''
        SELECT imie, nazwisko, tbklasy.klasa
        FROM tbuczniowie, tbklasy
        WHERE tbuczniowie.klasaID = tbklasy.IDklasy
         AND klasa like '1A'
        ''')
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_b(cur):
    cur.execute('''
        SELECT MAX(EgzHum)
         FROM tbuczniowie
        ''')
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))



def kw_c(cur):
    cur.execute("""
        SELECT AVG(EgzMat)
        FROM tbuczniowie, tbklasy
        WHERE tbuczniowie.klasaID=tbklasy.IDklasy
        AND klasa LIKE '1A'
        """)
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_d(cur):
    cur.execute("""
        SELECT imie, nazwisko, tboceny.ocena
        FROM tbuczniowie, tboceny
        WHERE tboceny.uczenID = tbuczniowie.IDucznia
        AND nazwisko LIKE 'Nowak'
        AND imie LIKE 'Dorota' 
        """)
        
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))
        

def kw_e(cur):
    cur.execute("""
        SELECT AVG(ocena)
        FROM tboceny, tbprzedmioty
        WHERE strftime('%m', datad) LIKE '10'
        AND tboceny.przedmiotID = tbprzedmioty.IDprzedmiotu
        AND przedmiot LIKE 'fizyka'
       """)
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))
 

def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor() #utworzenie kursora
    con.row_factory = sqlite3.Row
    
    kw_c(cur)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

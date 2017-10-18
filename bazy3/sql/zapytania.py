#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#  dane.py
# 

import sqlite3



def kw_c(cur):
    cur.execute("""
        SELECT SUM(placa) FROM pracownicy
    """)
    
    wyniki = cur.fetchall()
    for rekord in wyniki:
        print(tuple(rekord))



def kw_d(cur):
    parametr = input('Podaj nazwę działu:')
    # parametr2 = input('Kobiety czy mężczyźni')
    cur.execute("""
        SELECT dzial.id, dzial.nazwa,nazwisko,imie 
        FROM dzial, pracownicy
        WHERE dzial.id = pracownicy.id_dzial
        AND dzial.nazwa = ?
        AND imie NOT LIKE '%a'
    """,(parametr,))
    
    wyniki = cur.fetchall()
    for rekord in wyniki:
        print(tuple(rekord))

def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor()   # utworzenie kursora
    
    kw_d(cur)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

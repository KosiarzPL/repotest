#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dane.py
#  
#  

import csv

def dane_z_pliku(plik):
    dane=[]
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter='\t')
        for rekord in tresc:
            dane.append(rekord)
            
    return dane
    
def wyczysc_dane(dane, pole):
    for i, rekord in enumerate(dane):
        element = rekord[pole]
        element = element.replace(" ", "")
        element = element.replace(",", ".")
        element = element.replace("zł", "")
        rekord[pole] = element
        dane[i] = rekord
    return dane
    

def main(args):
    premia = dane_z_pliku('premia.txt')
    premia = wyczysc_dane(premia, 1)
    
    pracownicy = dane_z_pliku('pracownicy.txt')
    pracownicy = wyczysc_dane(pracownicy, 5)
    
    dzial = dane_z_pliku('dzial.txt')
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

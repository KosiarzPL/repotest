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
    

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

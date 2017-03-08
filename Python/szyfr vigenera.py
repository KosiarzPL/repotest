#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj_vigenere(tekst, klucz):
    szyfrogram = ''
    i = 0
    for l1 in tekst:
        wartosc1 = ord(l1.upper()) - 64
        # print wartosc1
        if i > len(klucz) - 1:
            i = 0
        wartosc2 = ord(klucz[i].upper()) - 64
        # print wartosc2
        i += 1
        wartosc3 = wartosc1 + wartosc2
        if wartosc3 > 26:
            wartosc3 -= 26
        szyfrogram += chr(wartosc3 + 64)
    return szyfrogram


def main(args):
    tekst = raw_input("Podaj tekst")
    klucz = raw_input("Podaj klucz")
    szyfruj_vigenere(tekst, klucz)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

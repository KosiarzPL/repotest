#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pracownicy_orm.py
#  


from peewee import *

baza_plik = SqliteDatabase(':memory:')


class BaseModel(Model):
    class Meta:
        baza = baza_plik
 
class Premia(BaseModel):
     id = CharField(primary_key = True)
     premia = DecimalField()
     
class Dzial(BaseModel):
     id = Integer(primary_key = True)
     nazwa = CharField()
     siedziba = CharField()
        
class Pracownik(BaseModel):
    id = CharField(primary_key = True)
    nazwisko = CharField()
    imie = CharField()
    stanowisko = ForeignKeyField(Premia)
    data_zatr = DataField()
    placa = DecimalField()
    premia = DecimalField()
    id_dzial = ForeignKeyField(Dzial)

baza_plik.connect() #polaczenie z baza
baza_plik.create_tables([Premia, Dzial, Pracownik], True)
    
def main(args):
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

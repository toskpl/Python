# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:28:13 2017

Zadanie domowe
1. Wczytaj zestaw danych z pliku "mieszkania.csv". Plik zawiera informacje o mieszkaniach na sprzedaż na terenie Poznania.
2. Ilu pokojowe mieszkania są najczęstsze?
3. Wyświetl 5 najdroższych i 5 najtańszych mieszkań, które są usytuowane na I piętrze.
4. Dodaj kolumnę Borough, która będzie zawierać informacje o dzielnicach i powstanie z kolumny Localization. Rozpatrz tylko następujące dzielnice: Stare Miasto, Wilda, Jeżyce, Rataje, Piątkowo, Winogrady, Miłostowo, Dębiec. Jeżeli ogłoszenie nie zawiera się w żadnym w powyższych, ustal jego wartość na Inne.
5. Narysuj wykres słupkowy pokazujący ile jest ogłoszeń mieszkań z podziałem na dzielnice.
6. Jaka jest średnia cena mieszkania na Wildzie? Jaka jest średnia cena mieszkania 3-pokojowego?
7. W której dzielnicy znajduje się mieszkanie na 13-piętrze?
8. Wyświetl wszystkie ogłoszenia mieszkań, które znajdują się na Winogradach, mają 3 pokoje i są położone na 1 piętrze.

"""

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

#import matplotlib
#matplotlib.style.use('ggplot')

#zad1
mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')

#zad2
mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')
dane = pd.Series(mieszkania_data["Rooms"])
print(dane.value_counts())

#zad3
mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')
dm = DataFrame(mieszkania_data [mieszkania_data["Floor"] == 1])
dm2 = dm.sort_values(by='Expected', ascending=0).head()[:5]
print(dm2)

mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')
dm = DataFrame(mieszkania_data [mieszkania_data["Floor"] == 1])
dm2 = dm.sort_values(by='Expected', ascending=1).head()[:5]
print(dm2)
#zad4

#zad5

#zad6

mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')
mask=  mieszkania_data [mieszkania_data["Location"]]
#dm = DataFrame('Expected':mieszkania_data['Expected'],'Floor':mieszkania_data['Floor'])
dm = DataFrame(mieszkania_data [mieszkania_data.Location.str.contains('Wilda')])
dm2 = dm[dm.Location.str.contains('Wilda')]
print(dm['Expected'].mean())

mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')
dm = DataFrame(mieszkania_data [mieszkania_data['Rooms'] == 3])
print(dm['Expected'].mean())

dm3 = DataFrame(mieszkania_data [mieszkania_data.Location.str.contains('Wilda') & mieszkania_data['Rooms'] == 3])
print(dm3)

#zad7

mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')
dm = DataFrame(mieszkania_data [mieszkania_data['Floor'] == 13])
print(dm['Location'])

#zad8

mieszkania_data = pd.read_csv('C:\\Users\\toskpl\\Desktop\\BIG_DATA\\mieszkania.csv')
dm = DataFrame(mieszkania_data [mieszkania_data.Location.str.contains('Winogrady')])
dm2 = dm[dm['Floor'] == 1]
dm3 = dm2[dm2['Rooms'] == 3]
print(dm3)
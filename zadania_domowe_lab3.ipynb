# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:35:13 2017


Zadania
1. Napisz funckję is_numeric, która sprawdzi, czy każdy element z przekazanej listy jest typu int lub float. 
   Wykorzystaj funcję isinstance().

2. Stwórz klasę Point, która będzie reprezentować punkt w przestrzeni wielowymiarowej :
   Konstruktor ma przyjąc tylko 1 parametr: listę współrzednych. Wykorzystaj funckję z pierwszego zadania, żeby sprawdzić, czy lista zawiera wyłącznie liczby.
   Napisz metodę add, która pozwoli na dodanie dwóch punktów do siebie i zwróci wynik jako nowy obiekt. Co jeżeli punkty mają różną liczbę współrzędnych?
   Napisz metodę to_string, która zwróci łancuch znakowy, który w czytelny sposób przedstawi punkt.
   Napisz metodę __len__, która zwróci liczbę współrzędnych punktu. Zobacz, czy możesz teraz wywołać funkcję len na obiekcie typy punkt.
   Napisz metodę __str__, która bedzie działać dokładnie tak samo jak metoda to_string. Wyświetl obiekt typy Point korzystając z funkcji print.

3. Zainstaluj bibliotekę sqlachemy na komputerze, na którym pracujesz.

4  Korzystając z sqlalchemy stwórz prostą bazę danych, która będzie operować na 3 obiektach. 
   Możesz wykorzystać przykłady z zajęć z SQLa.
"""

#zad 1
def is_numeric(li):
    if len (li) == 0:
        return False
    for i in li:
        var = isinstance(i,int) 
        var2 = isinstance(i,float) 
# print('var', var)
# print('var2',var2)
        
        if var == False and var2 == False:
            temp = False
            break
        else:
            temp = True
    return temp
        
print (is_numeric([1,1,333,"zzz"]) )
print (is_numeric([1,1,333,4.5]) )
print (is_numeric([1,1,333,4.5,1,21,2]) )
print (is_numeric([] ))


#zad 2
class Point:
    def __init__(self,text):
            self.text = text
            
    def add(p1, p2):
        print (len(p1.text))
        print (p2.text)
        len_p1 = len(p1.text)
        len_p2 = len(p2.text)
        if len_p1 != len_p2:
           print("punkty nie maja takiej smamej ilosci wspolrzednych")
           return
        p3 = list()
        for i in range(len_p1):
            p3.append(p1.text[i] + p2.text[i])
        return Point(p3)
    
    def to_string(self):
        return print(self.text)
    
    def __str__(self):
        return print( "{0}".format(self.text))
    
    def __len__(self):
        return len(self.text)
    
    def introduce(self):
        if len (self.text) == 0:
               return False
        for i in self.text:
            var = isinstance(i,int) 
            var2 = isinstance(i,float) 
            print('var', var)
            print('var2',var2)
        
            if var == False and var2 == False:
                temp = False
                break
            else:
                temp = True
        if temp:
           return print(self.text)
        else:
            print("Cos nie tak")
            
pointA = Point([1,100,"x"])
pointB = Point([9,8])
pointA.__len__()
pointA.to_string()
pointA.__str__()
pointA.introduce()
pointB.to_string()
pointB.__str__()
pointC = Point.add(pointA,pointB)
pointC.to_string()
print (pointA.introduce())
print (pointA.to_string())


#zad 3

import sqlalchemy

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#zad 4
Base = declarative_base()
 
class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    mark = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    address_id = Column(Integer, ForeignKey('address.id'))
    person = relationship(Person)
    addres = relationship(Address)
    
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)

session = DBSession()
 
new_person = Person(name='new person')
session.add(new_person)
session.commit()
 
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()

new_cars = Cars(model='cabrio',mark='polonez', person=new_person,addres=new_address)
session.add(new_cars)
session.commit()

session = DBSession()
print(session.query(Person).all())

person = session.query(Person).first()

session.query(Address).filter(Address.person == person).one().post_code
             
session.query(Cars).filter(Cars.person == person).one().mark
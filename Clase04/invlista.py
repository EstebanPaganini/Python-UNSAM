# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:10:47 2021

@author: Esteb
"""
#EJERCICIO 4.8
from pprint import pprint
def invertir_lista(lista):
    invertida = []
    i= len(lista)
    for e in lista:
        i = i-1
        invertida.append(lista[i])
        
    return invertida

l = [10, 23, 35, 74, 95]    
uno = [1, 2, 3, 4, 5]
dos = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
m = invertir_lista(l)
pprint(f'Entrada {dos}, Salida: {m}')

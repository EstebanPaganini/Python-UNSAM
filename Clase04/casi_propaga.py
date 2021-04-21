# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:13:43 2021

@author: Esteb
"""

def propagar(lista):
    i = len(lista)
    for e in range(i-1):
        if (lista[i] == 1) and (lista[i+1] == 0):
            lista[i+1] = 1
    
    return lista
        


lista = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
print(propagar(lista))
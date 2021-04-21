# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:29:05 2021

@author: Esteb
"""

def propagar(lista):
    n = len(lista)
    for i in range(n-1):
        if (lista[i]==1) and (lista[i+1]==0):
            lista[i+1]=1
    for i in lista:
        n = n-1
        if (lista[n]==1) and (lista[n-1]==0):
            lista[n-1]=1
    
    return lista

fosforos1 = [ 0, 0, 0, -1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
fosforos2 = [ 1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0]
fosforos3 = []
print(propagar(fosforos3))
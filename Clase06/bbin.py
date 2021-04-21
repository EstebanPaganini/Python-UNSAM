# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 10:32:48 2021

@author: Esteb
"""
##########################
#EJERCICIO 6.14

def donde_insertar(lista, x):
    pos = -1
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda                
    if x not in lista:
        lista.append(x)
        lista.sort()
        return (f' El elemento "{x}" no se encuentra en la lista, pero podria insertarse en la posicion N° {lista.index(x)}')
    return pos
#print(donde_insertar([0,5,10,15,20,25,30],45))
#%%
##########################
#EJERCICIO 6.15
def donde_insertar(lista, x):
    pos = -1
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda                
    if x not in lista:
        lista.append(x)
        lista.sort()
        return (f' El elemento "{x}" fue insertado en la posicion N° {lista.index(x)}, {lista}')
    return (f' el elemento "{x}" se encuentra en la posicion N° {pos}')
#print(donde_insertar([0,5,10,15,20,25,30],-1))
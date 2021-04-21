# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:35:13 2021

@author: Esteb
"""
#EJERCICIO 2.14
cadena = ['banana', 'manzana', 'mandarina']

def cadena_geringoso(cadena):
    cadena_2 = ''
    for letra in cadena:
        if letra in 'aeiou':
            cadena_2 += letra+'p'+letra
        else:
            cadena_2 += letra
    
    return cadena_2

dic = {}    

for e in cadena:
    gering = cadena_geringoso(e)
    dic[e] = gering

print (dic)


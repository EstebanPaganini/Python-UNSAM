# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:10:12 2021

@author: Esteb
"""
#EJERCICIO 2.7

def buscar_precios(fruta):
    f = open('C:/ejercicios_python/data/precios.csv')
    
    for linea in f:
        fila = linea.strip('\n')
        fila = linea.split(',')
        if fruta in fila[0]:
            precio_fruta = float(fila[1])
            break
        else:
            precio_fruta = 0
    f.close()
    return precio_fruta

nombre_fruta = input('Ingrese el nombre de la fruta o verdura (con la primer letra mayuscula):')
precio = buscar_precios(nombre_fruta)
if precio == 0:
    print ('Disculpa maestre, no me quedo', nombre_fruta)
else:
    print('El precio del cajon de ', nombre_fruta, 'es de: $',precio)

    

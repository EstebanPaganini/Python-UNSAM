# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:35:13 2021

@author: Esteb
"""
#EJERCICIO 2.10
import csv
import sys


def costo_camion(nombre_archivo):
    f = open(nombre_archivo)    
    costo_final = 0
    fila = csv.reader(f)
    titulo = next(fila)
    for linea in f:
        linea = linea.strip('\n')
        fila = linea.split(',')
        cajon = int(fila[1])
        precio = float(fila[2])
        costo_fruta = cajon * precio
        costo_final = costo_final + costo_fruta
    f.close()
    return costo_final

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'C:/Users/Esteb/ejercicios_python/data/missing.csv'

costo = costo_camion('C:/Users/Esteb/ejercicios_python/data/missing.csv')
print('El costo final es de: $', costo)

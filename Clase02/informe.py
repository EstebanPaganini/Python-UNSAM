# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:44:32 2021

@author: Esteb
"""
#EJERCICIOS 2.16/2.17/2.18
###########################################
import csv

def leer_camion(nombre_archivo):
    camion = []
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
       filas = csv.reader(f)
       encabezados = next(filas)
       for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            camion.append(record)
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                total += ncajones*precio
            except ValueError:
                print(f'Fila{n_fila}:No pude interpretar: {fila}')
    return camion
      

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        precio = {}
        for row in rows:
            try:
                precio[row[0]] = float(row[1])
            except:
                pass
    return precio

dic_camion = leer_camion('C:/Users/Esteb/ejercicios_python/data/camion.csv')
dic_precios = leer_precios('C:/Users/Esteb/ejercicios_python/data/precios.csv')
costo_camion = 0
for e in dic_camion:
    costo_camion += int(e['cajones'])*float(e['precio'])   
print (f'costo camion: {costo_camion}')

recaudado = 0
for e in dic_camion:
    lista_frutas = (e['nombre'])
    lista_precios = dic_precios[lista_frutas]
    recaudado += lista_precios * int(e['cajones'])
print (f'recaudado: {recaudado}')
print (f'la diferencia {recaudado-costo_camion:0.2f}')

        



        



#%%
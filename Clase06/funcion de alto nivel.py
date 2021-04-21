# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:38:49 2021

@author: Esteb
"""
import csv

def leer_camion(nombre_archivo):
    camion = []
    total = 0.0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {'nombre':row[0],'cajones':int(row[1]),'precio':float(row[2])}
            camion.append(lote)
    for s in camion:
        total += s['cajones']*s['precio']
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

def hacer_informe(dic_camion, dic_precios):
    dic_camion = leer_camion(dic_camion)
    dic_precios = leer_precios(dic_precios)
    valores = []
    lista_final = (valores)
    for s in dic_camion:
        valores = list(s.values())   
        for i in dic_precios:
            if s['nombre']==i:
                precio_venta = float(dic_precios[i])
                cambio = round(precio_venta - s['precio'],2)
                valores.append(cambio)  
                lista_final.append(valores)  
    titulos = ('Nombre', 'Cajones', 'Precio', 'Cambio')  
    print(f'{titulos[0]:>10s} {titulos[1]:>10s} {titulos[2]:>10s} {titulos[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in lista_final:
        print(f"{nombre:>10s} {cajones:>10d} {f'${precio:.2f}':>10} {f'${cambio:.2f}':>10}")
    
    


files=['C:/ejercicios_python/data/camion.csv','C:/ejercicios_python/data/camion2.csv']
for name in files:
        print(f'{name:-^43s}')
        hacer_informe(name, 'C:/ejercicios_python/data/precios.csv')
        print('-------------------------------------------')

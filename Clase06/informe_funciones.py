# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:42:11 2021

@author: Esteb
"""
###############################
#EJERCICIO 6.11
    
from fileparse import parse_csv

def leer_camion(nombre_archivo):
    camion = parse_csv(nombre_archivo, select=['nombre', 'cajones', 'precio'], types=[str, int, float])
    return camion  

def leer_precios(nombre_archivo):
    precio = parse_csv(nombre_archivo, types =[str,float], encabezados = False)
    return precio



def informe_funciones(camion, precios):
    camion = leer_camion(camion)
    precios = leer_precios(precios)
    valores= []
    lista_final = (valores)
    for e in camion:
        valores = list(e.values()) 
        for i in precios:
            if e['nombre']==i[0]:
                precio_venta= i[1]
                cambio = round(precio_venta - e['precio'],2)
                valores.append(cambio)
                lista_final.append(valores)
                
    titulos = ('Nombre', 'Cajones', 'Precio', 'Cambio')  
    print(f'{titulos[0]:>10s} {titulos[1]:>10s} {titulos[2]:>10s} {titulos[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in lista_final:
        print(f"{nombre:>10s} {cajones:>10d} {f'${precio:.2f}':>10} {f'${cambio:.2f}':>10}")
    

#informe_funciones('C:/ejercicios_python/data/camion.csv', 'C:/ejercicios_python/data/precios.csv')
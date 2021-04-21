# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:17:11 2021

@author: Esteb
"""
###############################
#EJERCICIO 6.12 

import informe_funciones

def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    total = 0
    for i in camion:
        ncajones= i['cajones']
        precio = i['precio']
        total += (ncajones*precio)
    return (total)

costo_camion('C:/ejercicios_python/data/camion.csv')
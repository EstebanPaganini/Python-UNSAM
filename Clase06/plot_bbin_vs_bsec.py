# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:32:46 2021

@author: Esteb
"""

import random
import matplotlib.pyplot as plt
import numpy as np
#####################################
def busqueda_secuencial(lista, x):
    comps = 0 
    pos = -1
    for i,z in enumerate(lista):
        comps += 1
        if z == x:
            pos = i
            break
    return pos, comps
#####################################
def busqueda_binaria(lista, x):
    comps = 0
    pos = -1 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
    return pos, comps
#####################################
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l
#####################################
def generar_elemento(m):
    return random.randint(0, m-1)
#####################################
m = 10000
n = 100
lista = generar_lista(n, m)


x = generar_elemento(m)
comps = busqueda_secuencial(lista, x)[1]
#####################################
m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
#####################################
m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
#####################################

def experimento_binario_promedio(lista, m, k):
     comps_tot = 0
     for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

     comps_prom = comps_tot / k
     return comps_prom

m = 10000
k = 1000

largos = np.arange(256) + 1 
comps_promedio = np.zeros(256) 

for i, n in enumerate(largos):
    lista = generar_lista(n, m) 
    comps_promedio[i] = experimento_binario_promedio(lista, m, k)
    
plt.plot(largos,comps_promedio,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.xscale('symlog')
plt.yscale('symlog')
plt.legend()



#'linear', 'log', 'symlog', 'logit', 'function', 'functionlog'

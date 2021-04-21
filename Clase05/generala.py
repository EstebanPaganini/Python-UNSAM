# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:35:52 2021

@author: Esteb
"""

import random

def tirada():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada


def es_generala(tirada):
    return max(tirada)==min(tirada)

'''        
N=1000000
hay_generala_servida = [es_generala(tirada()) for i in range(N)]
G = sum([es_generala(tirada()) for i in range(N)])
prob = G/N
print(f' Tire los dados {N} de veces y me saque {G} generalas servidas.')
print(f' la probabilodad de sacarme generala servida es de {prob}')
'''
#%%
#EJERCICIO 5.2

def generala_no_servida():
    G = sum([es_generala(tirada()) for i in range(3)])
    if G > 0:
       H = True
    else: 
       H = False
    return H 

N = 100000
generala_con_3_tiros =[generala_no_servida() for i in range(N)]
G = sum(generala_con_3_tiros)
prob = G/N

print(f' Tire {N} veces los dados y me saque {G} generalas.')
print(f' Podemos decir que la probabilidad de sacarme generala con tres tiros es de: {prob:.4f}')
#%%


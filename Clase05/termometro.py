# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:15:43 2021

@author: Esteb
"""
#EJERCICIO 5.5
import random
n = 999
g =[]
for i in range(n):
    h = (random.normalvariate(37.5,0.2))
    g.append(round(h,2))


print (max(g))
print (min(g))
print ((sum(g)/n))
g.sort()
print (g[50])
#%%
########################
#EJERCICIO 5.7
import numpy as np

np.save('Temperaturas.npy', g)
a = np.load('temperaturas.npy')

print (a)
#%%
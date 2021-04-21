# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:23:21 2021

@author: Esteb
"""

import matplotlib.pyplot as plt
import random
n = 999
g =[]
for i in range(n):
    h = (random.normalvariate(37.5,0.2))
    g.append(round(h,2))
    
plt.hist(g,bins=155)
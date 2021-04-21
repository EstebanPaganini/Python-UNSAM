# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:28:03 2021

@author: Esteb
"""

t = []
for e in range(0,10):
    t.append(e)



print(f'    {t[0]:>4d} {t[1]:>4d} {t[2]:>4d} {t[3]:>4d} {t[4]:>4d} {t[5]:>4d} {t[6]:>4d} {t[7]:>4d} {t[8]:>4d} {t[9]:>4d}')
print(f'{"------------------------------------------------------"}')
for i,row in enumerate(t, start=0):
    print(f'{i}:  {row:>4d} ')

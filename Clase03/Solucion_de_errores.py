# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:56:14 2021

@author: Esteb
"""
#Ejercicios de errores en el código
#%%
##EJERCICIO 3.1. Función tiene_a()

#TIENE UN ERROR DE TIPO SEMANTICO YA QUE SI LA A NO ES LA PRIMER LETRA 
#NO LA RECONOCE POR LO TANTO RETORNA COMO FALSE.
#LO CORREGI PRIMERO PASANDO LA EXPRESION A MINUSCULA,SACANDOLE EL ELSE:, YA QUE EL RETURN FALSE
#TENDRIA QUE SER NECESARIO UNA VEZ QUE RECORRE TODA LA EXPRESION Y NO ENCUNTRA NINGUNA 'a' Y 
#SUBIENDO EL I += 1 A LA ALTURA DEL IF, PARA QUE EL CONTADOR SUME CADA VEZ QUE CORRE UNA 
#LETRA
def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%
#EJERCICIO 3.2 funcion tiene_a()

#TIENE VARIOS ERRORES DE SINTAXIS Y ESTAN UBICADOS EN LA PRIMER LINEA DEL CODIGO AL NO TENER
#LOS ':' QUE LLEVA UNA VEZ DEFINIDA LA FUNCION, TMB FALTAN LOS ':' DSP DEL WHILE I<N Y EN LA
#LINEA DEL IF FALTA UN = PARA QUE SEA 'IGUAL A' SINO SOLO ES UNA ASIGNACION, TMB FALTAN LOS ':'
#LUEGO DEL IF, POR ULTIMO EL RETURN DICE 'Falso' CUANDO DEVERIA DECIR 'False'.

#EL CODIGO VA A SEGUIR SIN FUNCIONAR EN EL PRIMER CASO DE PRUEBA, YA QUE NO ESTAN CONTEMPLADAS
#LAS MAYUSCULAS, PARA CORREGIR EL CODIGO HAY QUE MODIFICAR LA EXPRESION A MINUSCULA.
def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%%
#EJERCICIO 3.3 funcion tiene_1()
#EL ERROR ES DE TIPO YA QUE LOS ENTEROS NO TIENEN LEN() Y LO SOLUCIONE PASANDO LA EXPRESION
#A STR PRIMERO ANTES DE BUSCAR SU LEN()

#CODIGO CORREGIDO:
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
#%%
#EJERCICIO 3.4 funcion suma()
#EL ERROR ES DE TIPO SEMANTICO Y ESTA UBICADO DENTRO DE LA FUNCION, YA QUE SIN EL RETURN, NO VA
# A RETORNAR NINGUN VALOR Y LA SUMA DE LOS PARAMETROS DEVUELVE UN NONE, AL PONERLE UN RETURN C,  
#QUE ES LA VARIABLE EN LA CUAL SE SUMAN LOS PARAMETROS QUE LE PASAMOS A LA FUNCION QUEDA SOLUCIONADO
#EL ERROR
#CODIGO CORREGIDO:
def suma(a,b):
    c = a + b 
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%

import csv
from pprint import pprint
def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion
camion = leer_camion('C:/Users/Esteb/ejercicios_python/data/camion.csv')
pprint(camion)
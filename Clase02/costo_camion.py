# -*- coding: utf-8 -*-
#EJERCICIO 2.2
import csv

f = open('C:/Users/Esteb/ejercicios_python/data/camion.csv')
fila = csv.reader(f)
titulo = next(fila)

costo_final = 0
for linea in f:
    linea = linea.strip('\n')
    fila = linea.split(',')
    cajon = int(fila[1])
    precio = float(fila[2])
    costo_fruta = cajon * precio
    costo_final = costo_final + costo_fruta
   
print('El costo final es de: $', costo_final)

f.close()

#%%

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, 'rt') as f:
        fila = csv.reader(f)
        encabezados = next(fila)
    for n_fila, fila in enumerate(fila, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')




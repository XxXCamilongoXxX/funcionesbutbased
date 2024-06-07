import os
import time
import msvcrt
import csv
from funcionesses import*
nombresitos=[]

with open('nombresitos.csv','w',newline='') as archivo:
    escritor = csv.writer(archivo)
    for ciclo in range(3):
        nombresito=input("Ingrese nombre: ")
        nombresitos.append(nombresito)
    escritor.writerow(nombresitos)

nombre_mas_largo(nombresitos)
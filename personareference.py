import csv
from funcionesses import *
personas = []

for vuelta in range(3):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    persona = [nombre,apellido]
    personas.append(persona)
almacenar_datos(personas)
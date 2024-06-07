import csv

from funcionesses import *
personas=[]

while True:
    nombre=input("Ingrese nombre: ")
    apellido=input("Ingrese apellido: ")
    edad=int(input("Ingrese edad:"))
    persona=[nombre,apellido,edad]
    personas.append(persona)
    pap=input("Quiere agregar otra persona?: ").lower()
    if pap =='no':
        print("Chao papu :,v")
        break
personas_edades(personas)

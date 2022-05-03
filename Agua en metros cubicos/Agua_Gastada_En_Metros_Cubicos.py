"""Programa para determinar el precio de agua para cobrar a una vivienda, segun los mts^3 gastados"""

#Input
x = int(input("Ingresa los mts^3 de agua gastados: "))

#Processing
if x <= 50:
    gasto = 0
elif x > 50 and x < 200:
    gasto = 2000 * (x-50)
else:
    gasto = (3000 * (x-250)) + (2000 * (x-50))
precio = gasto + 10000

#Output
print("Su precio a pagar es: $" + str(precio))
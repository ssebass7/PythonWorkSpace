



'''Ejercicio2'''

from random import randint


enteros=[[randint(1,100) for j in range(50)] for i in range(50)]
print("enteros:",enteros)
print("Longitud:",enteros.__len__())
repetidos = []
sinRepetir = []
multiplos37 = []

for valor in multiplos37:
    if valor not in sinRepetir:
        sinRepetir.append(valor)
    else:
        if valor not in repetidos:
            repetidos.append(valor)
 
print ("valores repetidos:",repetidos)

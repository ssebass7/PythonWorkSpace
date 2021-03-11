
'''
Created on 26 nov. 2020

@author: sseba
'''

mares = ["mediterraneo", "cantabrico", "baltico", "adriatico", "tirreno", "egeo", "rojo", "muerto", "caspio", "negro", "arabigo", "sulu"]

mares1 = ["mediterraneo", "cantabrico", "baltico", "adriatico", "tirreno", "egeo"]

mares2 = ["rojo","muerto", "caspio", "negro", "arabigo", "sulu"]

print(mares)

"""1. Cambia a la vez los valores de los elementos undecimo y duodecimo de la lista mares por los
valores 'del norte' y 'alboran'"""

mares[mares.index("arabigo")] = "norte"
mares[mares.index("sulu")] = "alboran"

"""2. Comprueba el cambio del valor de dichos elementos"""

print(mares)


"""3. Inserta en la lista mares una posicion con el valor 'baltico'"""
mares.insert(12, "baltico")
print(mares)


"""4. Borra el quinto elemento de la lista mares
"""
mares.pop(4)


"""5. Comprueba el cambio realizado"""
print("elemento 5 eliminado", mares)


"""
6. Muestra la longitud de la lista mares
"""
print("longitud de la lista 'mares':", mares.__len__(), "\n")


"""
7. Cuenta los valores repetidos en la lista mares
"""
i = 0
for i in range(0, 12):
    print("Valor:", "'", mares[i], "'", "repeticion:", mares.count(mares[i]))
    pass


"""8. Elimina el elemento de la tercera posicion de la lista mares y guardalo en la variable mar1"""
mar1 = mares.pop(2)
print(mares)


"""9. Elimina el ultimo elemento de la lista mares y guardalo en la variable mar2"""
mar2 = mares.pop(-1)
print(mares)


"""10. Guarda el valor de la novena posicion en la variable mar3"""
mar3 = mares.pop(8)
print(mares)


"""11. Muestra los valores de las variables mar1, mar2 y mar3"""
print("mar1 =", mar1, "mar 2=", mar2, "mar3 =", mar3)


"""12. Elimina el primer elemento de la lista mares con valor 'baltico'"""
mares = ["mediterraneo", "cantabrico", "baltico", "adriatico", "tirreno", "egeo", "rojo", "muerto", "caspio", "negro", "arabigo", "sulu","baltico"]
mares.remove("baltico")
print(mares)
"""13. Elimina todos los elementos de la lista mares"""
mares.clear()
print(mares)


"""14. Ordena por orden alfabetico de 'a' a 'z' los elementos de la lista mares1"""
mares1.sort()
print(mares1)
mares2.sort()


"""15. Ordena por orden alfabetico de 'z' a 'a' los elementos de la lista mares2"""
mares2.reverse()
print(mares2)

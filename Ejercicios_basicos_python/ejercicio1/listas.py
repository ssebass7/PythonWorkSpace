
'''
Created on 26 nov. 2020

@author: sseba
'''

mares1 = ["mediterraneo", "cantabrico", "baltico", "adriatico", "tirreno", "egeo"]

mares2 = ["rojo","muerto", "caspio", "negro", "arabigo", "sulu"]

mares=[]

i = 0
cont = 0;
for i in range(0,12):
    
    if i <= 5:
        mares.append(mares1[i])
        pass 
    
    if i >= 6:
        mares.append(mares2[cont])
        cont += 1
        pass 
    
       
    i += 1
    pass

print("1. Longitud de lista 'mares1':",mares1.__len__())

print("2. valores lista 'mares1':",mares1[:],"\n")

print("3. Longitud de lista 'mares2':",mares2.__len__())

print("4 valores lista 'mares2':",mares2[:],"\n")

print("5. Longitud de lista 'mares':",mares.__len__())

print("6. valores lista 'mares':",mares[:],"\n")

print("7. valores posicion 1, 2 y 3 lista 'mares1':",mares1[0],",",mares1[1],",",mares1[2])

print("8. posicion mar egeo en 'mares1':", mares1.index("egeo"),"\n")

print("9. valores posicion 4, 5 y 6 lista 'mares2':",mares2[3],",",mares2[4],",",mares2[5])

print("10. posicion mar caspio en 'mares2':", mares2.index("caspio"),"\n")

print("11. posicion mar caspio en 'mares2':", mares.index("caspio"))

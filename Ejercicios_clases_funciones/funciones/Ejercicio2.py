'''
Created on 29 ene. 2021

@author: sseba
'''
def generar_n_caracteres(num = int,caracterEntrada = str):
    caract = caracterEntrada 
    if num != 0: 
        for i in range(1,num):  
            caracterEntrada = caracterEntrada + caract
    else:
        caracterEntrada = "Introduce un numero distinto de 0"
    return caracterEntrada

print(generar_n_caracteres(20,"x"))
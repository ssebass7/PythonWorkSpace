'''
Created on 29 ene. 2021

@author: sseba
'''
def palabraLongitud(frase):
    numLetras = 0;
    diccionarioFrase = {}
    lista = frase.split(" ")
    for i in range(0,len(lista)):
        lista[i]
        numLetras = len(lista[i])
        diccionarioFrase[lista[i]] = numLetras    
   
    return print(diccionarioFrase)
   
palabraLongitud("Hola y adios")
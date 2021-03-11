'''
Created on 29 ene. 2021

@author: sseba

'''

def fnlista(n):
    return n
    
def funcionLista(funcion,lista):
    listaModificada = []
    for i in range(0,len(lista)):
        valor = lista[i]**funcion
        listaModificada.append(valor)
    return listaModificada

print(funcionLista(fnlista(3),[1,2,3,4,5]))
    
    
    
   


    
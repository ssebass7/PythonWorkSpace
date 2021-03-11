'''
Created on 29 ene. 2021

@author: sseba
'''


def histograma(lista_numeros):
    printCaracter = ""
    for i in range(0,len(lista_numeros)):
        for j in range(0,lista_numeros[i]):
            printCaracter = printCaracter + "*"
        pass
        print(printCaracter)
        printCaracter = ""
    pass
    return "terminado"

print(histograma([1,2,3]))
'''
Created on 29 ene. 2021

@author: sseba
'''



def calificaPalabras(dicc):
    dicc2 = {}
    for key in dicc:
        valorKey = key.upper() 
        if dicc[key] < 5:
            dicc2[valorKey] = "Suspenso"
        if  5 <= dicc[key] < 6 :
            dicc2[valorKey] = "Suficiente"
        if  6 <= dicc[key] < 7:
            dicc2[valorKey] = "Bien"
        if  7 <= dicc[key] < 9:
            dicc2[valorKey] = "Notable"
        if  9 <= dicc[key] < 10:
            dicc2[valorKey] = "Sobresaliente"
        if  dicc[key] == 10:
            dicc2[valorKey] = "Sobresaliente"
        if  dicc[key] > 10:
            dicc2[valorKey] = "La nota no puede sobrepasar 10"
    print(dicc2)
dicc = {"android" : 8.2,"hilos" : 5.6 ,"python": 9.3, "interfaces" : 4.4}
    
calificaPalabras(dicc)

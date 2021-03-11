'''
Created on 29 ene. 2021

@author: sseba
'''
def vocal(caracter):
    condicion = True
    
    if caracter == 'a' or  caracter == 'e' or  caracter == 'i' or caracter == 'o' or caracter == 'u':
        
        condicion=True
    else: 
        condicion = False
        
    return condicion

print(vocal("e"))
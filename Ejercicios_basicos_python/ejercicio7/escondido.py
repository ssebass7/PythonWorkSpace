'''
Created on 26 nov. 2020

@author: sseba
'''
numSecreto = 6
numUsuario = input("Averigua el numero escondido:\n")
intentos = 0
while int(numUsuario) != numSecreto:
    
    if int(numUsuario) < numSecreto:
        print("El 'numero introducido' debe ser mayor\n")
        
        if intentos >= 3:
            diferencia = int(numSecreto) - int(numUsuario)
            print("PISTA:",diferencia,"numeros mas")
           
            pass
        
        pass
    else:
        print("El 'numero introducido' debe ser menor\n")
        
        if intentos >= 3:
           diferencia = int(numUsuario) - int(numSecreto)
           print("PISTA:",diferencia,"numeros menos")
           pass
       
        pass
    
    intentos += 1
    numUsuario = input("Averigua el numero escondido:\n")
    pass
print("Enhorabuena lo has averiguado")
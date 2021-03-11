'''
Created on 26 nov. 2020

@author: sseba
'''
condicion = False
while condicion != True:
    num = input("Dame un numero\n")

    num2 = input("Dame otro numero\n")

    suma = int(num) + int(num2)

    if suma > 100:
        print("La suma supera la centena y es:", suma)
        pass
    else:
        print("El resultado de la suma no supera la centena")
        pass
    
    pass
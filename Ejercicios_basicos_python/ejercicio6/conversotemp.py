'''
Created on 26 nov. 2020

@author: sseba
'''
tempFaC = input("grados Fahrenheit a grados Celsius:\n")

tempCaF = input("grados Celsisus a grados Fahrenheit:\n")

formulaFaC = float((float(tempFaC) - 32) * 5 / 9)

formulaCaF = float(( float(tempCaF) * 9 / 5) + 32)
                   
print("grados Fahrenheit:",tempFaC, "grados Celsius:",formulaFaC)
print("grados Celsius:",tempCaF,"grados Fahrenheit:",formulaCaF)
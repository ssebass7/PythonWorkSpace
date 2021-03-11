'''
Created on 28 ene. 2021

@author: sseba
'''
_version_ = '1.0'


def dame(texto):
    for caracter in texto:
        print('Dame una', caracter, end="")
        print("'"+caracter+"'")


def medio(texto):
    print('El caracter de en medio es:', texto[len(texto)//2])


def a_mayusc(texto):
    mayusc = ''
    for caracter in texto:

        if 'a' <= caracter <= 'z':
            location = ord(caracter) - ord('a')
            new_ascii = location + ord('A')
            caracter = chr(new_ascii)

        mayusc = mayusc + caracter
    return mayusc


print(a_mayusc('Piratas del caribe'))


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try:
        
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


print(4*5/0)

try:
    raise ZeroDivisionError('4*5/0')
except ZeroDivisionError:
    print("Has intentado dividir por 0")
    raise

def dividir(n1, n2):
    try:
        resultado = n1/n2
    except ZeroDivisionError:
        print("AVISO: Has dividido entre 0. El valor de n2 es:", n2)

    else:
        print("Cla�sula else. el resultado es:", resultado)
    finally:
        print("Ejecutando la cl�usula finally. \ Operaci�n finalizada")


dividir(4, 2)
dividir(5, 0)

print(8+var2/5+10)


def operacion():
    try:
        valor = 8+var2/5+10
    except NameError:
        print("Aviso: has usado la operaci�n con una variable inexistente!")


operacion()


def operacion():
    try:
        valor = 8+var2/5+10
    except NameError:
        print("Aviso: Has usado en la operaci�n una variable inexistente!",valor)
    else:
        print("El resultado es:",valor)
    finally:
        print("Ejecutando c�usula Finally. Operaci�n finalizada")

operacion()

raise NameError('Hola DAM')


try:
    raise NameError("Hola DAM")
except NameError:
    print('La excepci�n NameError se ha lanzado!')
    raise

# TypeError

print(10-'5')

def oper1():
    try:
        print(int('5')+8)
    except TypeError:
        print("Aviso: has usado argumentos num�ricos \ y cadenasde caracteres en la operaci�n")
oper1()

num = int(input("Dame un n�mero entero: "))
print(num)


while True:
    try:
        x = int(input("Por favor, introduce un n�mero entero"))
    except ValueError:
        print("Vaya! Este no es un n�mero entero v�lido. Prueba de nuevo...")
    else:
        print("El valor introducido",x,"es un n�mero entero")
        break

class MiExcepcion(Exception):
    def _init_(self,valor):
        self.valor=valor
    def _str_(self):
        return repr(self.valor)

#raise MiExcepcion(5+8)


try:
    raise MiExcepcion(5+23)
except MiExcepcion as e:
    print("Se ha generado mi excepci�n con valor:",e.valor)
    raise
    
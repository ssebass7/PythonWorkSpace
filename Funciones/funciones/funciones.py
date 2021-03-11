'''
Created on 11 dic. 2020

@author: sseba
'''
from lib2to3.pgen2.token import OP

'''
decimal = int(input("Introduce un numero decimal, base 10, para convertirlo a binario\n"))
binario = ""

while decimal // 2 != 0:
    binario = str(decimal % 2) + binario 
    decimal = decimal // 2
print("El numero binario correspondiente es",str(decimal) + binario)

for letra in "python" :
    if letra == "o":
        break
    pass
    print("Letra obtenida en paso: ",letra)
pass

for letra in "python" :
    if letra == "h":
        continue
    pass
    print("Letra obtenida en paso: ",letra)
pass

  
var = 10

while var > 0:
    print("Valor de la variable en este paso: ",var)
    var = var -1
    if var == 5:
        break
   
   
  

var = 10

while var > 0:
    var = var -1
    if var == 5:
        continue
    print("Valor de la variable en este paso: ",var)
    

 
print("Encuentra un numero PAR")
for num in range(2, 15):
     if num % 2 == 0:
         print("Numero par encontrado", num)
         continue
     print("Numero", num)


for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d es igual a %d * %d" % (num, i, j))
            break
    else:
        print(num, "es un numero primo")
 
numero = 0
while numero < 100:
    if numero == 90:
        break
    if numero % 2 == 0:
        print("El numero ", numero, "es par.")
    else:
        print("El numero",numero,"es impar.")
    numero = numero + 1
    continue
    print("Esto nunca se ejecuta")
else:
    print("Se sale del bucle... cuando numero sea 100")
    

colores = ["negro","blanco","rojo","verde","azul","amarillo"]
for color in colores:
    print("El",color, "es un color.")
else:
    print("La lista se ha terminado") 
    
while True:
    pass

for letra in "Python":
    if letra == "h":
        pass
        print("Este es el bloque pass")
    print("Letra obtenida:", letra)
    


def obtener_info(*args):
    pass
    print('Este es el bloque pass')
obtener_info()
obtener_info(5)


def obtener_info():
    pass

obtener_info()
obtener_info(5)


class ClaseVacia:
    pass


def imprime(cadena):
    print(cadena)
    return cadena

var = imprime("Primera cadena")
imprime("Segunda cadena")
imprime(cadena = "Tercera cadena")
print(var)

def muestrainfo(nombre,edad):
    print("Nombre:", nombre)
    print("Edad:", edad)
    
muestrainfo(edad = 20, nombre="Arturo")
muestrainfo("Javi",25)


def suma(num1,num2):
    resultado = num1 + num2


def muestrainfo(arg1,*valores):
    print("La salida es: ")
    print(arg1)
    for val in valores:
        print(val)

muestrainfo(100)
muestrainfo(90,48,36,78)


def actualizame(milista):
    milista.append([1,2,3,4])
    print("Muestra los valores dentro de la funcion", milista)
    
milista=[10,20,30,40]
actualizame(milista)
print("Muestra los valores fuera de la funcion:",milista)


def actualizame(milista):
    milista = ([1,2,3,4])
    print("Muestra los valores dentro de la funcion", milista)
    
milista=[10,20,30,40]
actualizame(milista)
print("Muestra los valores fuera de la funcion:",milista)


def f(n,L=[]):
    L.append(n)
    return L
lista = [1,3,6]
print(f(1,lista))
print(f(2))
print(f(3))


def f(n,L=None):
    if L is None:
        L = []
    L.append(n)
    return L
print(f(1))
print(f(2))
print(f(3))

def preguntar(mensaje, intentos=4, aviso="Opcion no valida. Prueba otra cosa"):
    while True:
        opcion = input(mensaje)
        if opcion in ("s","si","S","SI"):
            return True
        if opcion in ("n","no","N","NO"):
            return False
        intentos -= 1
        print("Te quedan", intentos,"intentos")
        if intentos == 0:
            raise ValueError("respuesta invalida")
        print(aviso)
preguntar("quieres sobrescribir el archivo",2,'Solo debes contestar si o no')
'''
def loro(voltaje,estado="tieso",accion="explotaria",tipo="Azul Noruego"):
    print("--Este loro no",accion,end="")
    print(" si haces pasar",voltaje,"voltios a traves de el.")
    print("--con un plumaje maravilloso de tipo",tipo)
    print("--Se quedaria",estado,":)")
    
loro(20)
loro(accion="HABLARIA",voltaje=10000)
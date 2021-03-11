
# -*- coding: utf-8 -*-

print('hola mundo python!!!!')
print("hola mundo python!!!!")
print(5 + 9, 5 * 6, 2 ** 3, 5 / 2)
print('hola', 'adios')
print('hola' + 'adios')

print('pruebas', 5)
print('pruebas ' * 5)
print(4 * 'HO' + 2 * 'LA')

var1 = 5
var2 = 8.4
var3 = var1 + var2
print(var3)

print(5 == 5)
print(5 == 6)
print(5 == 5 and 8 == 4)
print(5 == 5 or 8 == 4)
print(8 == 4 or 5 == 5)

print('7', 'a' == ('a' or'b'))

print('la suma de 5 y 4 es ', 5 + 4)

num1 = input('Dame un numero\n')
print(num1)

num1 = int(input('Dame un numero\n'))
print(num1)

num1 = float(input('Dame un numero\n'))
print(type(num1))

num2 = int(input('Dame un numero\n'))
print(type(num2))

num3 = input('Dame un numero\n')
print(type(num3))

# print(num3+6)

num2 = float(input('Dame un numero\n'))
num4 = repr(num2)
print(type(num4))

v = eval('123')
print(v, type(v))

v1 = eval('123.88')
print(v1, type(v1))

# esto da error
v2 = eval('hola')
print(v2, type(v2))

v3 = eval('[4,8,24]')
print(v3, type(v3))
'''
'''
# lista protegida se escribe con parentesis(), tambien llamada tupla
mi_tupla = (2, 4.5, 'hola', 'prueba', 8.54)
# lista desprotegida, similar al arraylist, se escribe corchetes[] 
mi_lista = ['tarara', 45.5, 'adios', 'testeo', 88.88]

print(mi_tupla)
print(mi_lista)
print(mi_lista[0])
# la ultima posicion no te la coge, la primera que pongas si esta incluida
print(mi_lista[1:4])
# de esta manera va hasta el final automaticamente
print(mi_lista[3:])
# de esta manera va desde la primera poscion hasta la posicion anterior al valos indicado
print(mi_lista[:3])
print(len(mi_lista))

mi_lista.append("añadido")
print(mi_lista)
# mi_tupla.append("añademe esta")

del mi_lista[1]
print(mi_lista)
mi_lista._delitem_(1)
print(mi_lista)
mi_lista.remove(88.88)
print(mi_lista)

ultimo = mi_lista.pop()
print(ultimo)
'''
'''
mi_lista = [2, 'valle', 4.77, 'valle', 1, 'montaña', 2, 'arbol']
print(mi_lista)
print(type(mi_lista))
mi_tupla = (2, 'valle', 4.77, 'valle', 1, 'montaña', 2, 'arbol')
print(mi_tupla)
print(type(mi_tupla))

print('valle esta ', mi_lista.count('valle') , 'veces')
print('montaña esta ', mi_lista.count('montaña') , 'veces')

mi_lista.insert(1, 'sendero')
print(mi_lista)

# mi_tupla.insert(1, 'sendero')

mi_lista.append(7)
print(mi_lista)

del mi_lista[1]
print(mi_lista)

mi_lista.remove('valle')
print(mi_lista)

var = mi_lista.pop()
print(mi_lista)
print(var)
var = mi_lista.pop(3)
print(mi_lista)
print(var)

mi_lista[2:4] = ["verde", "blanco"]
print(mi_lista)
'''
'''
lista = [2, 14, 5, 12, 7, 3, 8, 10]
lista.sort()
print(lista)

lista.reverse()
print(lista)
'''
'''
lista = [2, 14, 5, 12, 7, 3, 8, 10]
lista.reverse()
print(lista)
lista.sort()
lista.reverse()
print(lista)
'''
'''
stack = [1, 2, 3, 4]
print(stack)
stack.append(5)
print(stack)
stack.append(6)
print(stack)
stack.append(8)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
'''
'''
c = 0
while c < 10:
    print(c)
    c += 1
    pass  # no es obligatorio pero sirve para indicar el limite
print('FIN')
'''
'''
año = 2001
while año <= 2012:
    print('Informes del año: ', str(año))
    año += 1
    pass
'''
'''
while True:
     nombre = input('Dame tu nombre\n')
     print('Hola', nombre)
     if nombre:
        break
'''
'''
n1 = int(input('Primer numero\n'))
n2 = int(input('Segundo numero\n'))
suma = n1 + n2

if suma < 10:
    print('la suma es:', str(suma))
    pass
else:
    print('los numero son muy grandes')
    pass
'''
'''
n1 = int(input('Primer numero\n'))
suma = n1
while True:
     n1 = int(input('Nuevo numero\n'))
     if n1 == -1:
         break
     suma += n1
     print('la suma es', str(suma))
     pass
print('la suma es', str(suma))
print('FIN')
'''
'''
fin_prog = ''
while fin_prog != 's' and fin_prog != 'S' :
    print('estas dentro del while')
    fin_prog = input('pulsa s para salir\n')
    pass
'''
'''
semaforo = input('esta el semaforo en verde y/N\n')
if semaforo == 'y' or semaforo == 'Y' :
    print('puede pasar')
    pass
else:
    print('Espere por favor')
    pass
'''
'''
n = int(input('introdudca valor cualquiera\n'))
if n < 0:
    n = -n
    pass
print('el valor absoluto es', str(n))
'''
'''
fijo = 5
var = int(input('numero a comparar\n'))
if var < fijo:
    print('es menor que', fijo)
    pass
elif var > fijo:
    print('es mayor que', fijo)
    pass
else:
    print('es igual que', fijo)
    pass

x = 8
y = 10
print(x == y)
'''

'''
lista = ['geranio', 'rosa', 'clavel', 'tulipan', 'amapola']
if 'geranio' in lista:
    print('geranio esta en la lista')
    pass
else:
    print('geranio no esta en la lista')
    pass

if 'lavanda' not in lista:
    lista.append('lavanda')
    pass

print(lista)

for e in lista:
    print(e)
    pass

'''
'''
# sentido normal
i = 0
for i in range(1, 10):
    print(i)
    i += 1
    pass
# sentido invertido
i = 0
for i in range(10, 1, -1):
    print(i)
    i += 1
    pass


lista = ['geranio', 'rosa', 'clavel', 'tulipan', 'amapola']
for i in range(len(lista)):
    print(lista[i])
    pass
print('\nFIN\n')
for i in range(2,len(lista),2):
    print(lista[i])
    pass 

print("---------------------------------------------------")
milista2 = [0 for i in range(12)]
milista2[1] = 25 
print ("milista2:", milista2)
print("posiciones 1 y 2:", milista2[1:3])
print("posiciones 0, 1 y 2:",milista2[:3])
print("posiciones desde la 5 en adelante:",milista2[5:])


milista4 = [i**2 for i in range(12)]
print("milista4:",milista4)

matrizdim2 = [[1,3],[4,6]]
print("matrizdim2",matrizdim2)

for i in range(len(matrizdim2)):
    for j in range(len(matrizdim2[i])):
        print("El valor de la posicon es", matrizdim2[i][j])
        
        pass
    pass

matriz=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(matriz)

matriz1=[[0 for j in range(3)] for i in range(3)]
print(matriz1)

matriz2 = [[i*j for j in range(3)] for i in range(3)]
print(matriz2)


columna0 = [c[0] for c in matriz2]
print(columna0, end= ' ')
print()
for e in matriz2: 
    print(e, end=' ')
    print()

matriz3 = [(1,2,3),(4,5,6),(7,8,9)]
print("matriz3:",matriz3)
columna0 = [c[0] for c in matriz3]
print("columna 0", columna0, end=' ')
columna1 = [c[1] for c in matriz3]
print("columna 1", columna1, end=' ')
columna2 = [c[2] for c in matriz3]
print("columna 2", columna2, end=' ')


matriz4 = [[i+j for j in range(3)] for i in range(3)]

print("matriz4",matriz4)
print("numero de elementos",len(matriz4))

columna0=[c[0]for c in matriz4]
print(columna0)

matriz5 = [(x,y,z) for x in [1,2,3] for y in [3,1,4] for z in [5,7,4] if x!= y]
print(matriz5)
print(matriz5.__len__())

#DICCIONARIOS
contactos = {}
nombre = "Isaac Asimov"
numero = 8288222992
contactos[nombre]=numero

contactos = {}
nombre = "Albert Einstein"
numero = 828824554222
contactos[nombre]=numero

print('El telefono es:', contactos["Isaac Asimov"])
print(contactos.keys())

for x in contactos:
    print("Nombre:",x,"\tNumero:",contactos[x])
    pass

if nombre in contactos:
    del contactos[nombre]
    pass

for x in contactos:
    print("Nombre:",x,"\tNumero:",contactos[x])
    pass


diccionario = {"nombre" : "Carlos", "edad" : 22,
               "cursos" : ["Python", "Django", "Javascript"]}


print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["cursos"])

print(diccionario["cursos"][0])
print(diccionario["cursos"][1])
print(diccionario["cursos"][2])

for key in diccionario:
    print(key, ":", diccionario[key])

dic = dict(zip("abcd",[1,2,3,4]))
print(dict)
print(dic)

print(dic.keys())

items = dic.items()

print(items)

keys = dic.keys()
print(keys)

print(dic.values())

valor = dic.get("b")
print(valor)

dic1 = dic.copy()
print(dic1)

valor = dic.pop("b")
print(valor)
print(dic)

valor = dic.setdefault("a")
print(valor)

valor = dic.setdefault("e",5)
print(valor)
print(dic)

dic = dict.fromkeys(["a", "b", "c", "d"],1)
print(dic)

dic1 = {"a" : 1, "b" : 2, "c" : 3, "d" : 4 }
dic2 = {"c" :6, "b" : 5, "e" : 9, "f" : 10}

dic1.update(dic2)
print(dic1)

dic1.clear()
print(dic1)


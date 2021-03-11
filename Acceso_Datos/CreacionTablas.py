
# -*- coding: utf-8 -*-

'''
Created on 5 feb. 2021

@author: sseba
'''
import psycopg2
import psycopg2.extras
import sys
import pprint #Para mostrar los valores de las tuplas recibidas
from test.support import catch_threading_exception
#Conexi�n a la base de datos en Postgresql
print()
print("PRUEBA DE CREACION DE TABLAS EN POSTGRES Y REALIZACION DE CONSULTAS")
print()
conx = None #Para destruir cualquier conexi�n conx existente
print("Conexion a la Base de Datos Postgres")
#Se usa try para poder capturar las excepciones producidas durante la conexi�n
try:
# Se realiza la conexi�n con la base de datos postgres
    conx = psycopg2.connect("dbname=postgres user=openpg password=openpgpwd")
    print("Estableciendo conexion a la base de datos ...")
    #conx.cursor devuelve un objeto cursor necesario para realizar las consultas SQL
    cur = conx.cursor()
    print ("Conectado!\n")
    #Se ejecutan una serie de consultas o queries
    #Si existe la tabla prueba se borrar� para evitar excepciones al ejecutar el c�digo de nuevo
    cur.execute("DROP TABLE IF EXISTS prueba")
    print("La tabla prueba se ha eliminado")
    #Se crea una tabla nueva llamada prueba con un campo que ser� clave primaria
    cur.execute("CREATE TABLE prueba (id serial PRIMARY KEY, nombre varchar, sueldo integer)")
    #Se insertan algunas tuplas en la tabla. La �ltima se inserta de otra forma
    cur.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Miguel Sanchez", 1500))
    cur.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Clara Munoz", 1600))
    cur.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Paco Lopez", 1580))
    cur.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Nerea Montalban", 1570))
    cur.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Luis Bermudez", 1650))
    cur.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Ana Palomo", 1590))
    #Se inserta una tupla más de otra manera
    cur.execute("""INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s);""", ("Lola Otero", 1700))
    print("Tabla PRUEBA creada")
except:
    print("Ocurrio un error")

 
 #####################################################################################################3
#Se realiza una consulta para comprobar si se han introducido dichas tuplas
cur.execute("SELECT * FROM prueba")
tuplas=cur.fetchall()
print()
print("Se muestran todas las tuplas con un bucle for")
for row in tuplas:
    print (row)
#Se muestran las tuplas mediante pprint
print()
print("Se muestran todas las tuplas usando pprint")
pprint.pprint(tuplas)
#Se ven las tuplas una a una y se muestran los campos deseados de las mismas
cur.execute("SELECT * FROM prueba")
print()
print("Se muestran todos los campos de la fila:")
while True:
    fila = cur.fetchone() #Sólo se extrae una tupla del cursor
    if fila == None: #Si no hay más filas se sale del bucle while
        break
print (fila[0], fila[1], fila[2]) #para la fila, se muestran los valores de los campos 0, 1 y 2
print()
print()
#Se muestra la tupla que cumple una condición
print("Se muestra sólo la tupla que cumpla la condición - nombre = Luis")
sql = "select * from prueba where nombre like 'Luis%'"
cur.execute(sql)
fila = cur.fetchone()
print (fila)
#Se añade un campo nuevo a la tabla
cur.execute("alter table prueba add column telefono integer")
#Se introducen los valores en el nuevo campo
cur.execute("update prueba set telefono=911111111 where id=1")
cur.execute("update prueba set telefono=912222222 where id=2")
cur.execute("update prueba set telefono=913333333 where id=3")
#Comienzo del C�digo
# -*- coding: utf-8 -*-
import psycopg2 # Adaptador Python - Postgres
import psycopg2.extras
import sys
import pprint #Para mostrar los valores de las tuplas recibidas
#Conexi�n a la base de datos en Postgresql
print()
print("PRUEBA DE CONEXION A POSTGRES Y VERSI�N DE LA BASE DE DATOS")
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
#Se muestra la versi�n de Postgresql
    cur.execute('select version()')
    version = cur.fetchone()
    print ("version de PostgreSQL\n", version)
except:
    print ("No se puede conectar con la Base de Datos")
#Fin del c�digo

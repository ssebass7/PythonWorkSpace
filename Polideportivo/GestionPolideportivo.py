'''
Created on 5 feb. 2021

@author: sseba
'''
import psycopg2
import psycopg2.extras
import sys
import pprint 
import time




def menu(cur):
    
    condicion = True

    print()
    print("MENU:\n", 
            "1. Dar de alta un cliente con sus datos personales\n", 
            "2. Dar de baja un cliente\n", 
            "3. Mostrar los datos personales de un cliente o de todos\n",
            "4. Matricular a un cliente en un deporte\n",
            "5. Desmatricular a un cliente en un deporte\n",
            "6. Mostrar los deportes de un cliente\n",
            "7. Salir\n")
    
    opcion = int(input("Introduce una Opcion(solo numero):\n"))
    

    #OPCION 1 
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente:")
        fecha = input("Introduce la fecha del cliente:")
        telefono = input("Introduce el telefono del cliente:")
        c = clientes()
        c.__datos__(nombre, fecha, telefono,cur)
        time.sleep(2)
        pass
    
    
    #OPCION 2
    elif opcion == 2:
        
        try:
            print("ENTRANDO EN OPCION 2")
            nombre = input("Introduce el nombre del cliente que desea borrar:")
             
            cur.execute("DELETE FROM clientes where nombreCompleto = %s",(nombre.title(),))
            print("Cliente: '" + nombre.upper() + "' dado de baja")
            
            time.sleep(2)
            pass
        except:
            print("ERROR en opcion 2")
            
            time.sleep(2)
        pass
    
    
    #OPCION 3 
    elif opcion == 3:
        
        print("ENTRANDO EN OPCION 3")
        print("")
        print("  - Opcion 1: Mostrar datos personales de un cliente")
        print("  - Opcion 2: Mostrar datos personales de todos los cliente")
        print("")
        opcionImprimir = int(input("Introduzca una opcion (SOLO NUMERO):"))
        print(opcionImprimir)
        try:
            if opcionImprimir == 1:
                nombreCompleto = input("Introduce el nombre del cliente que desea visualizar:")
                cur.execute("SELECT nombreCompleto, fechaNaci, telefono from clientes where nombreCompleto = %s;",(nombreCompleto.title(),))
        
                nombreTabla = "CLIENTES"
                mostrarTabla(cur,nombreTabla)
                
                time.sleep(2)
                
                pass
            elif opcionImprimir == 2:
                cur.execute("SELECT * FROM clientes")
                nombreTabla = "CLIENTES"
                mostrarTabla(cur, nombreTabla)
                
                time.sleep(2)
                pass
            pass
        
        except:
            print("ERROR en opcion 3")
            
            time.sleep(2)
            pass 
        
        pass
    
    
    #OPCION 4 
    elif opcion == 4:
        
        try:
            print("ENTRANDO EN OPCION 4")
            
            cur.execute("SELECT * FROM deportes")
            nombreTabla = "DEPORTES"
            mostrarTabla(cur, nombreTabla)
            print()
            nombreCliente = input("Introduce nombre de un cliente:\n")
            nombreDeporte = input("Introduce nombre del deporte:\n")
            
            cur.execute("SELECT * FROM deportes")
            tuplasDeportes=cur.fetchall() 
            print()
            aviso = ""
            contador = 0
            deporteExistente = False
            
            for nombreDeporteSQL in tuplasDeportes:
                contador += 1
                
                if nombreDeporte.lower() == nombreDeporteSQL[0].lower():
                    aviso = "El deporte '"+ nombreDeporte.upper() +"' esta en la tabla"
                    deporteExistente = True
                    pass
                elif contador == (len(tuplasDeportes)-1) and deporteExistente == False:
                    aviso = "No se ha encontrado el deporte"
                    pass
                
                pass
            
            print(aviso)
            
            #SI SE INTRODUCE EL NOMBRE DE CLIENTE CORRECTAMENTE
            if deporteExistente == True:   
                
                try:
                    cur.execute("SELECT nombreCompleto FROM clientes where nombreCompleto = %s;",(nombreCliente.title(),))
                    fila = cur.fetchone()
                    nombreClienteSQL =  fila[0]
                    print("El nombre '"+ nombreCliente.upper() + "' esta en la tabla")
                    if nombreCliente.lower() == nombreClienteSQL.lower():
                        try:
                            horario = input("Elija hora para el horario (p.e 9:00-10:00):")
                            cur.execute("INSERT INTO matriculacion (nombreCliente, nombreDeporte,horario) VALUES (%s, %s, %s)",(nombreCliente.title(),nombreDeporte.title(),horario.title()))
                            cur.execute("SELECT * FROM matriculacion")
                            nombreTabla = "MATRICULACION"
                            mostrarTabla(cur, nombreTabla)
                            
                            time.sleep(2)
                            pass
                        except:
                            print("Error en insertar datos en tabla ''MATRICULACION''")
                            
                            pass
                        pass
                    
                    pass
                
                
                except:
                    print("El nombre de cliente introducido no existe en la BBDD") 
                    
                    time.sleep(2)
                    pass
           
                pass
            
            else:
                print("No se puede matricular al cliente.'NOMBRE DEPORTE' no existente")
                
                time.sleep(2)
                pass
            
           
            pass 
        
        except:
            print("ERROR en opcion 4")  
            
            time.sleep(2)
            pass 
        
        contador = 0; 
        pass
    
    
    #OPCION 5
    elif opcion == 5:
        try:
           
            print("ENTRANDO EN OPCION 5")
            nombreCliente = input("Introduce el nombre del cliente que desea borrar:")
            nombreDeporte = input("Introduce el nombre del deporte que desea borrar:")
            
            cur.execute("DELETE from matriculacion where nombreCliente = %s",(nombreCliente.title(),))
            ''' "AND nombreDeporte = %s",(nombreDeporte.title(),))'''
           
            cur.execute("SELECT * FROM matriculacion")
            
            nombreTabla = "MATRICULACION"
            mostrarTabla(cur,nombreTabla)
            
            time.sleep(2)
            pass
        except:
            print("ERROR EN OPCION 5")
            
            time.sleep(2)
            pass
      
        
    #OPCION 6
    elif opcion == 6:
        try:
            print("ENTRANDO EN OPCION 6")
            nombreCliente = input("Introduce el nombre del cliente que desea visualizar:")
            cur.execute("SELECT nombreDeporte, horario from matriculacion where nombreCliente = %s;",(nombreCliente.title(),))
        
            nombreTabla = "MATRICULACION"
            mostrarTabla(cur,nombreTabla)
        
            time.sleep(2)
            pass
        
        except:
            print("ERROR en opcion 6")
            
            time.sleep(2)
            pass
        
        pass
    
    
    #OPCION 7
    elif opcion == 7:
        print("ENTRANDO EN OPCION 7")
        
        print("Saliendo del sistema...")
        time.sleep(2)
        condicion = False
        pass
    else: 
        print("Debes introducir un numero del 1 al 7")
        pass
    return condicion
#FINAL METODO MENU
    pass


#CLASE CLIENTE
class clientes():
    
    #METODO DATOS DEL CLIENTE
    def __datos__(self,nombreCompleto,fechaNaci,telefono, cur):
        
        try:
       
            cur.execute("INSERT INTO clientes (nombreCompleto, fechaNaci,telefono) VALUES (%s, %s, %s)",(nombreCompleto.title(), fechaNaci,telefono))
            print("Cliente '" +nombreCompleto.upper() +"' dado de alta")
            
            pass
        
        except:
            print("ERROR en opcion 1")    
            
            time.sleep(2)
            pass  

    #METODO DATOS DEPORTE
    def __deportes__(self,cur):
        
        tenis = ['Tenis','10euros/hora']
        natacion = ["Natacion","12euros/hora"]
        atletismo = ["Atletismo","7euros/hora"]
        baloncesto = ["Baloncesto","8euros/hora"]    
        futbol = ["Futbol","11euros/hora"]
      
        try:
            cur.execute("INSERT INTO deportes (nombre, precio) VALUES (%s, %s)",(tenis[0].title(),tenis[1].title()))
            cur.execute("INSERT INTO deportes (nombre, precio) VALUES (%s, %s)",(natacion[0].title(),natacion[1].title()))
            cur.execute("INSERT INTO deportes (nombre, precio) VALUES (%s, %s)",(atletismo[0].title(),atletismo[1].title()))
            cur.execute("INSERT INTO deportes (nombre, precio) VALUES (%s, %s)",(baloncesto[0].title(),baloncesto[1].title()))
            cur.execute("INSERT INTO deportes (nombre, precio) VALUES (%s, %s)",(futbol[0].title(),futbol[1].title()))
            
            cur.execute("SELECT * FROM deportes")
            nombreTabla = "DEPORTES"
            mostrarTabla(cur, nombreTabla)
            
            time.sleep(1)
            pass
        except:
            print("ERROR en insercion en tabla 'DEPORTES'")
            
            time.sleep(1)
            pass
       
        pass
    pass



#METODO PARA MOSTRAR TABLA 
def mostrarTabla(cur,nombreTabla):
    
    tuplas=cur.fetchall()
    print()
    print("tabla '" + nombreTabla +"'")
    pprint.pprint(tuplas)
    pass


condicion = True

#CONEXION A LA BASE DE DATOS
try:
    conx = psycopg2.connect("dbname=postgres user=openpg password=openpgpwd")
    print("Estableciendo conexion a la base de datos ...")
    time.sleep(0.5)
    print ("Conectado!\n")
    time.sleep(0.5)
    cur = conx.cursor()
    cur.execute("DROP TABLE IF EXISTS clientes")
    cur.execute("DROP TABLE IF EXISTS deportes")
    cur.execute("DROP TABLE IF EXISTS matriculacion")
    print("Tablas clientes, deportes, matriculacion eliminadas")
    cur.execute("CREATE TABLE clientes (nombreCompleto varchar PRIMARY KEY, fechaNaci varchar, telefono integer)")
    cur.execute("CREATE TABLE deportes (nombre varchar PRIMARY KEY, precio varchar)")
    cur.execute("CREATE TABLE matriculacion (nombreCliente varchar PRIMARY KEY, nombreDeporte varchar, horario varchar)")
    print("Tablas clientes, deportes, matriculacion creadas")
except:
    print("ERROR en 'CONEXION A LA BASE DE DATOS POSTGRESQL' ")
time.sleep(0.5)
c = clientes()
c.__deportes__(cur)

#BUCLE WHILE PARA REALIZAR METODO MENU
while condicion == True:
    condicion = menu(cur)
    pass

#FINALIZAR CONEXION A BASE DE DATOS
conx.commit() 
print("Guardando datos...")
time.sleep(2)
cur.close() 
conx.close() 
print ("La conexión con la base de datos se ha cerrado")
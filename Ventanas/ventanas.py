#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 19 feb. 2021

@author: sseba
'''
from psycopg2._psycopg import cursor

'''
#CREACION VENTANA 
import tkinter
from tkinter import * 
 
ventana = tkinter.Tk()
ventana.mainloop()


#CREACION VENTANA modificaciones
import tkinter
import time
from tkinter import messagebox
bg = 1
ventana = tkinter.Tk()
ventana.mainloop(bg)

# messagebox --> showinfo(), showwarning(), asquestion(), askyesno()
# askokcancel(), showerror(), askokcancel(), askyesnocancel(),
# askretrycancel()


messagebox.showinfo(message= time.localtime(), title= "Fecha y hora")

var=messagebox.askyesno(message="¿vas a venir a la fiesta?", title = "Pregunta")

if var:
    print("Voy a la fiesta")
else:
    print("No voy a la fiesta")
    
ventana.mainloop()

#CREACIION DE VENTNA_2 - VENTANA QUE HEREDA

import tkinter
from tkinter import * 

ventana = tkinter.Tk()
ventana.title("Primera Ventana")
ventana.config(bg="coral")
ventana1 = tkinter.Toplevel(ventana)

ventana.mainloop()

#TAMANIOS VENTANA
import tkinter
from tkinter import * 

ventana = tkinter.Tk()
ventana.title("Primera Ventana")
ventana.geometry("3000x300+0+0")

#VENTANA HIJA
ventana1 = tkinter.Toplevel(ventana)
ventana1.title("Segunda ventana")
ventana1.geometry("400x500+300+300")

#BLOQUEA LA OPCION DE AMPLIAR LA VENTANA HIJA
ventana1.transient(ventana)
ventana.mainloop()


import tkinter
from tkinter import * 

ventana = tkinter.Tk()
ventana.title("Primera Ventana")
ventana.geometry("3000x300+0+0")

#TAMAÑO MAXIMO ANCHO - ALTO O EN OTRO ORDEN INDICANDO WIDTH Y HEIGHT
ventana.maxsize(400, 500)
ventana.maxsize(height=500, width=400)
ventana.mainloop()




import tkinter
from tkinter import * 

ventana = tkinter.Tk()
ventana.title("Primera Ventana")
ventana.geometry("300x300+0+0")

#TAMAÑO MINIMO ANCHO - ALTO O EN OTRO ORDEN INDICANDO WIDTH Y HEIGHT
ventana.minsize(300, 300)
ventana.minsize(height=300, width=300)
ventana.mainloop()




import tkinter
from tkinter import * 

ventana = tkinter.Tk()
ventana.title("Primera Ventana")
ventana.geometry("200x200+0+0")

#Permitir o restringir la redimension de la ventana
ventana.resizable(width=True, height=False)

ventana.mainloop()



#OCULTAR VENTANA

import tkinter
import time 

ventana = tkinter.Tk()
ventana.title("Primera Ventana")
ventana.geometry("300x300+0+0")

ventana.withdraw()     #Se oculta la ventana
time.sleep(10)         #tiempo de espera
ventana.deiconify()    #mostrar ventana

ventana.mainloop()

#INTRODUCIR UNA ETIQUETA EN EJE CENTRAL

import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Prueba de etiquetas")
ventana.geometry("400x200")

etiqueta = tkinter.Label(ventana,text = "Primera Etiqueta")
buttonPantalla = tkinter.Button(ventana,text = "adios")
etiqueta.pack()
buttonPantalla.pack()

ventana.mainloop()

'''

#PROPIEDADES DE ETIQUETAS

import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Prueba de etiquetas")
ventana.geometry("400x700")

etiqueta1 = tkinter.Label(ventana, text="Hola Mundo Python!!!", borderwidth=15, bg ="cyan")
etiqueta1.pack()
etiqueta1_2 = tkinter.Label(ventana, text="Hola DAM!!!", bd=80,background ="coral") 
etiqueta1_2.pack()


'''
etiqueta2 = tkinter.Label(ventana, text="¿Qué te parece la parte gráfica?", cursor="hand1")
etiqueta2.pack()
etiqueta2_1 = tkinter.Label(ventana, text="¿Qué te parece la parte gráfica?", cursor="hand2")
etiqueta2_1.pack()
etiqueta2_2 = tkinter.Label(ventana, text="¿Qué te parece la parte gráfica?", cursor="dot")
etiqueta2_2.pack()


etiqueta3 = tkinter.Label(ventana, text="Hola Mundo Python muy alto!!!", height=10)
etiqueta3.pack()
etiqueta3_1 = tkinter.Label(ventana, text="Hola Mundo Python!!!", width=30)
etiqueta3_1.pack()



etiqueta4 = tkinter.Label(ventana, text="Hola\n Mundo!!!", justify="right")
etiqueta4.pack()
etiqueta4_1 = tkinter.Label(ventana, text="Hola\n Mundo!!!", justify="center")
etiqueta4_1.pack()
etiqueta4_2 = tkinter.Label(ventana, text="Hola\n Mundo!!!", justify="left")
etiqueta4_2.pack()



etiqueta5 = tkinter.Label(ventana, text="Hola Mundo!!!", relief="sunken", borderwidth=5)
etiqueta5.pack()
etiqueta5_1 = tkinter.Label(ventana, text="Hola Mundo!!!", relief="raised", borderwidth=5)
etiqueta5_1.pack()
etiqueta5_2 = tkinter.Label(ventana, text="Hola Mundo!!!", relief="groove", borderwidth=5)
etiqueta5_2.pack()
etiqueta5_3 = tkinter.Label(ventana, text="Hola Mundo!!!", relief="ridge", borderwidth=5)
etiqueta5_3.pack()
etiqueta5_4 = tkinter.Label(ventana, text="Hola Mundo!!!", relief="flat", borderwidth=5)
etiqueta5_4.pack()

'''

var = StringVar()
etiqueta5_5 = Label( ventana, textvariable=var, relief=RAISED )
var.set("¿Para qué haces todo esto?")
etiqueta5_5.pack()

texto = "Código Python"
etiqueta6 = tkinter.Label(ventana, text=texto)
etiqueta6.pack()



etiqueta7 = tkinter.Label(ventana, text="Hola \n a todos")
etiqueta7.pack()
etiqueta7_1 = tkinter.Label(ventana, text="Hola \t a todos")
etiqueta7_1.pack()




etiqueta8 = tkinter.Label(ventana, text="Hola Mundo Python!!!", underline=3)
etiqueta8.pack()
etiqueta8_1 = tkinter.Label(ventana, text="Hola Mundo Python!!!", underline=8)
etiqueta8_1.pack()

etiqueta9 = tkinter.Label(ventana, text="Hola Mundo Python!!!", font="HELVETICA")
etiqueta9.pack()
etiqueta9_1 = tkinter.Label(ventana, text="Hola Mundo Python!!!", font="calibri")
etiqueta9_1.pack()


etiqueta10 = tkinter.Label(ventana, text="Hola Mundo Python!!!", fg="green")
etiqueta10.pack()
etiqueta10_1 = tkinter.Label(ventana, text="Hola Mundo Python!!!", fg="#38EB5C")
etiqueta10_1.pack()
etiqueta10_2 = tkinter.Label(ventana, text="Hola Mundo Python!!!", bg="#F24149")
etiqueta10_2.pack()
etiqueta10_3 = tkinter.Label(ventana, text="Hola Mundo Python!!!", background="yellow")
etiqueta10_3.pack()


etiqueta11 = tkinter.Label(ventana, text="Hola Mundo Python!!!", bitmap="hourglass")
etiqueta11.pack()
etiqueta11_1 = tkinter.Label(ventana, text="Hola Mundo Python!!!", bitmap="questhead")
etiqueta11_1.pack()
etiqueta11_2 = tkinter.Label(ventana, text="Hola Mundo Python!!!", bitmap="warning")
etiqueta11_2.pack()


ventana.mainloop()





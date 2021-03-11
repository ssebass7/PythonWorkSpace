'''
Created on 5 mar. 2021

@author: sseba
'''
'''
from ventanas import ventana

#CUADRO DE TEXTO
import tkinter
from tkinter import *


ventana = tkinter.Tk()
ventana.title("Prueba de cuadro de texto")
ventana.config(bg="#00FF00")
ventana.geometry("500x300")

ctexto = Entry(ventana, fg="red3", width=50)
ctexto.insert(END, "ESCRIBE LO QUE QUIERAS")
print(ctexto.get())
ctexto.pack(pady=5)

ctexto1 = tkinter.Entry(ventana,bg="white",fg="black",justify=RIGHT)
ctexto1.insert(0, "codigo PYTHON")
print(ctexto1.get())
ctexto1.pack(pady=15)

ctexto2 = tkinter.Entry(ventana, show="", justify=CENTER)
ctexto2.insert(0, "Código oculto")
print(ctexto2.get())
ctexto2.pack(pady=25)

def comando():
    print(ctexto.get())
    print(ctexto.get())
    print(ctexto2.get())
    
display = tkinter.Button(ventana, text="Muestra texto", command=comando, bg="blue", fg="white").pack(pady=30)

ventana.mainloop()    

'''

'''

import tkinter

from tkinter import *



ventana = Tk()

ventana.title('PRUEBA DE TEXTOS')

ventana.geometry("900x1200") 



texto1 = Text(ventana)

texto1.insert(INSERT, "BUENAS TARDES DAM.....")

texto1.insert(INSERT, "SIGUE PRACTICANDO CON PYTHON.....")

texto1.insert(INSERT, "PRACTICANDO.....")

texto1.insert(INSERT, "CON MUCHOS.....")

texto1.insert(END, "TEXTOS.....")

texto1.pack(padx=20, pady=5)


texto1.tag_add("T1", "1.0", "1.6")

texto1.tag_add("T2", "1.7", "1.13")

texto1.tag_add("T3", "1.14", "1.17")

texto1.tag_add("T4", "1.55", "1.63")

texto1.tag_add("T5", "1.71", "1.74")

texto1.tag_add("T6", "1.86", "1.92")



texto1.tag_config("T1", background="cyan", foreground="black")

texto1.tag_config("T2", background="black", foreground="yellow")

texto1.tag_config("T3", background="red3", foreground="white")

texto1.tag_config("T4", background="coral", foreground="blue")

texto1.tag_config("T5", background="maroon", foreground="yellow")

texto1.tag_config("T6", background="orange", foreground="black")





texto2 = Text(ventana)

texto2.insert(INSERT, "HOLA, HELLO.....")

texto2.insert(END, "ADIOS, Bye Bye.....")

texto2.pack(pady=80)



texto2.tag_add("T1", "1.0", "1.11")

texto2.tag_add("T2", "1.16", "1.30")

texto2.tag_config("T1", background="yellow", foreground="blue")

texto2.tag_config("T2", background="blue", foreground="white")


ventana.mainloop()


'''


#IMAGENES


#Imagen1

from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Imagen")
ventana.geometry("600x600")

imagen1 = PhotoImage(file="python.png")
display = Label(ventana, imagen=imagen1).place(x=10, y=5)

ventana.mainloop()

'''
#Imagen2
from tkinter import * 
ventana = Tk()

ventana.title("Vista de imágenes")
ventana.configure(bg="AntiquWhite1")
ventana.geometry("300x300")

canvas = Canvas(ventana, width = 200, height = 200)
canvas.pack()

img = PhotoImage(file="baddie1.png")
canvas.create_image(10,10,anchor=NW,image=img)

ventana.mainloop()

'''

'''
#Prueba botones

import tkinter

from tkinter import *



ventana = Tk()

ventana.title("Prueba de Botones")

ventana.geometry("400x600")



etiqueta = Label(ventana, text="Ejemplos de Botones", bg = 'yellow', bd = 20, width = 40)

etiqueta.pack()



def imprimir():

   print("Comprueba que el caracter 3 está subrayado")

boton1 = Button(ventana, text="Hola Mundo Python!!!", command=imprimir, underline=3).pack()



def funcion():

   print ("Excelente")



boton2 = Button(ventana, text="Que te parece la guía?", command=funcion).pack()

boton3 = Button(ventana, text="botón 3!!!", command=funcion, height=5, activebackground="#F50743").pack()

boton4 = Button(ventana, text="botón 4!!!", command=funcion, height=5, activeforeground="#F50743").pack()

boton5 = Button(ventana, text="botón 5!!!", command=funcion, height=5, bg="#38EB5C").pack()

boton6 = Button(ventana, text="botón 6!!!", command=funcion, height=5, fg="#38EB5C").pack()



ventana.mainloop()


#Prueba botones2 

import tkinter

from tkinter import messagebox

from tkinter import *



ventana = Tk()

ventana.title("Prueba de Botones")

ventana.geometry("400x200")



etiqueta = Label(ventana, text="Prueba de Botones", font=("Courier", 18, "italic"), bg = 'coral', fg='blue', bd = 20)

etiqueta.pack()



def hola():

  messagebox.showinfo( "Título: Mensaje escondido", "Hola Mundo Python")



display = Button(ventana, text ="Mensaje", command = hola, bg="yellow").pack(pady=10)

display = Button(ventana, text ="SALIR", command = exit, bg="blue",fg="white" ).pack(pady=20)



ventana.mainloop()



#CHECKBUTTON 

import tkinter

from tkinter import *



ventana = Tk()



etiqueta = Label(ventana, text="Prueba de Checkbutton", font=("arial", 16, "bold"), bg = 'green', fg='white', bd = 20)

etiqueta.pack()





etiqueta = Label(ventana, text="Elige una opción").pack()



CheckVar1 = IntVar()

CheckVar2 = IntVar()

CheckVar3 = IntVar()



C1 = Checkbutton(ventana, text = "Música", variable = CheckVar1, \

                onvalue = 1, offvalue = 0, height=5, \

                width = 10)

C2 = Checkbutton(ventana, text = "Video", variable = CheckVar2, \

                onvalue = 1, offvalue = 0, height=5, \

                width = 10)

C3 = Checkbutton(ventana, text = "Audio", variable = CheckVar3, \

                onvalue = 1, offvalue = 0, height=5, \

                width = 10)

C1.pack()

C2.pack()

C3.pack()

#Ver estado de checkbutton: marcado / no marcado

print(CheckVar1.get())

print(CheckVar2.get())

print(CheckVar3.get())

#Ver el texto del Checkbutton

print(C1.cget("text"))

print(C2.cget("text"))

print(C3.cget("text"))



ventana.mainloop()







#OTRO CHECKBOX 

from tkinter import *

ventana = Tk()



def var_states():

  print("Estudiante: %d,\nTrabajador: %d" % (var1.get(), var2.get()))



Label(ventana, text="Tu ocupación:").grid(row=0, sticky=W)

var1 = IntVar()

Checkbutton(ventana, text="Estudiante", variable=var1).grid(row=1, sticky=W)

var2 = IntVar()

Checkbutton(ventana, text="Trabajador", variable=var2).grid(row=2, sticky=W)

Button(ventana, text='Salir', command=ventana.quit).grid(row=3, sticky=W, pady=4)

Button(ventana, text='Mostrar', command=var_states).grid(row=4, sticky=W, pady=4)

ventana.mainloop()




#OTRO TIPO RADIOBUTTON

import tkinter as tk



ventana = tk.Tk()

ventana.configure(bg="ORCHID1")



v = tk.IntVar()

tk.Label(ventana, 

       text="Elige tus vacaciones:""",

       justify = tk.LEFT, padx = 20).pack()



tk.Radiobutton(ventana, text="Playa", padx = 20, variable=v, 

             value=1).pack(anchor=tk.W)

tk.Radiobutton(ventana, text="Montaña", padx = 20, variable=v, 

             value=2).pack(anchor=tk.W)

tk.Radiobutton(ventana, text="Viajar por paises", padx = 20, variable=v, 

             value=3).pack(anchor=tk.W)
             
             
             
ventana.mainloop()




#DESPLEGABLE


import tkinter

from tkinter import *

from tkinter import ttk



ventana = Tk()

ventana.title("Prueba de Combobox")

ventana.geometry("400x400")



Label(ventana, text= 'Elige tu lenguaje de programación favorito:', bg='yellow', justify = LEFT, padx = 20).pack(anchor= W)



def seleccion(ventana, event):

   print("Nuevo elemento seleccionado:", combo.get())



combo = ttk.Combobox(ventana)

combo.place(x=10, y=30)

combo["values"] = ["Python", "Java", "Perl", "C", "C++", "C#"]

combo.set("Selecciona un lenguaje")

combo.bind("<<ComboboxSeleccionado>>", seleccion)



ventana.mainloop()





#LISTA 


import tkinter

from tkinter import *



ventana = Tk()

ventana.title("Prueba de Listbox")

ventana.geometry("400x400")





Lb1 = Listbox(ventana)

Lb1.insert(1, "Python")

Lb1.insert(2, "Perl")

Lb1.insert(3, "Visual C++")

Lb1.insert(4, "PHP")

Lb1.insert(5, "C#")

Lb1.insert(5, "R")

Lb1.insert(6, "Cobol")

Lb1.pack()



print(Lb1.size())



ventana.mainloop()
'''

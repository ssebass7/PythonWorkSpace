'''
Created on 10 mar. 2021

@author: sseba
'''


import tkinter
from tkinter import *
from tkinter import ttk

'''class Aplicacion():'''
ventana = tkinter.Tk()
ventana.title("Agencia de Viajes")
ventana.config(bg="white")
ventana.geometry("700x750")

scrollbar = Scrollbar(ventana)
scrollbar.pack( side = RIGHT, fill = Y)
display = tkinter.Label(ventana,text = "VIAJES DE SENDERISMO",font=("arial", 8, "bold"), bd = 2, width = 65).pack(side=TOP, expand = True)





#RADIOBUTTON

radioValue = IntVar()

listaExcuriones = []

tkinter.Label(ventana, text="Elige tus excursiones:",justify = tkinter.LEFT,font=("arial",8,"underline"), padx = 20).pack(side=TOP, expand=True)



rdioOne = tkinter.Radiobutton(ventana, text="Monte Abantos", padx = 20, variable= radioValue, value=1, bg="white",).pack(side=TOP, expand=True)

rdioTwo = tkinter.Radiobutton(ventana, text="La Pedriza", padx = 20, variable= radioValue, value=2, bg="white",).pack(side=TOP, expand=True)
    
rdioThree = tkinter.Radiobutton(ventana, text="Las dehesas de Cercedilla", padx = 20, variable= radioValue,value=3, bg="white",).pack(side=TOP, expand=True)

rdioFour = tkinter.Radiobutton(ventana, text="La Cabrera-Pico de la Miel", padx = 20, variable= radioValue,value=4, bg="white",).pack(side=TOP, expand=True)



listaExcuriones.append(rdioOne)
listaExcuriones.append(rdioTwo)
listaExcuriones.append(rdioThree)
listaExcuriones.append(rdioFour)
#CHECKBOX
etiqueta = tkinter.Label(ventana, text="Elige tus accesorios:",padx = 60,font=("arial",8,"underline")).pack(side=TOP,expand=True)


CheckVar1 = IntVar()

CheckVar2 = IntVar()

CheckVar3 = IntVar()

CheckVar4 = IntVar()

CheckVar5 = IntVar()

CheckVar6 = IntVar()

CheckVar7 = IntVar()
    
CheckVar8 = IntVar()



C1 = Checkbutton(ventana, text = "Mochila", variable = CheckVar1, padx = 60,bg="white",\
                 
                 onvalue = 1, offvalue = 0, height=0, \

                width = 10)

C2 = Checkbutton(ventana, text = "Linterna",variable = CheckVar2, padx = 60,bg="white",\

                onvalue = 1, offvalue = 0, height=0, \

                width = 10)

C3 = Checkbutton(ventana, text = "GPS", variable = CheckVar3,padx = 60,bg="white", \

                onvalue = 1, offvalue = 0, height=0, \

                width = 10)

C4 = Checkbutton(ventana, text = "Mapa", variable = CheckVar4,padx = 60,bg="white", \

                onvalue = 1, offvalue = 0, height=0, \

                width = 10)


C5 = Checkbutton(ventana, text = "Prismáticos", variable = CheckVar5,padx = 60,bg="white", \
                 
                onvalue = 1, offvalue = 0, height=0, \

                width = 10)



C6 = Checkbutton(ventana, text = "Cantimplora", variable = CheckVar6,padx = 60,bg="white", \

                onvalue = 1, offvalue = 0, height=0, \

                width = 10)



C7 = Checkbutton(ventana, text = "Botiquín", variable = CheckVar7,padx = 60,bg="white", \

                onvalue = 1, offvalue = 0, height=0, \

                width = 10)



C8 = Checkbutton(ventana, text = "Crema_Solar", variable = CheckVar8,padx = 60,bg="white", \

                onvalue = 1, offvalue = 0, height=0, \

                width = 10)



C1.pack(side=TOP, expand = True)

C2.pack(side=TOP, expand = True)

C3.pack(side=TOP, expand = True)
    
C4.pack(side=TOP, expand = True)

C5.pack(side=TOP, expand = True)

C6.pack(side=TOP, expand = True)

C7.pack(side=TOP, expand = True)

C8.pack(side=TOP, expand = True)

#Ver estado de checkbutton: marcado / no marcado

print(CheckVar1.get())

print(CheckVar2.get())

print(CheckVar3.get())

#Ver el texto del Checkbutton

print(C1.cget("text"))

print(C2.cget("text"))

print(C3.cget("text"))



#DATOS PERSONALES

etiqueta = tkinter.Label(ventana, text="Datos Personales:",padx = 60,font=("arial",8,"underline")).pack(side=TOP,expand=True)


campoNombre = Entry(ventana, fg="grey", width=50)
campoNombre.insert(END,"Nombre")
print(campoNombre.get())
campoNombre.pack(side=TOP,pady=10)


campoApellido = Entry(ventana, fg="grey", width=50)
campoApellido.insert(END,"Apellido")
print(campoApellido.get())
campoApellido.pack(side=TOP,pady=10)


campoDireccion = Entry(ventana, fg="grey", width=50)
campoDireccion.insert(END,"Direccion")
print(campoDireccion.get())
campoDireccion.pack(side=TOP,pady=10)
    

campoTeléfono = Entry(ventana, fg="grey", width=50)
campoTeléfono.insert(END,"Teléfono")
print(campoTeléfono.get())
campoTeléfono.pack(side=TOP,pady=10)


#COMBOX

etiqueta = tkinter.Label(ventana, text="Elige tu POBLACION:",padx = 60,font=("arial",8,"underline")).pack(side=TOP,expand=True)





combo = ttk.Combobox(ventana)

combo.pack(side=TOP,pady=5,expand=True)

combo["values"] = ["Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas","Majadahonda","Móstoles","Alcorcón","Boadilla del Monte","Villaviciosa de Odón"]

combo.set("Selecciona un lenguaje")


'''
 #LISTA
 etiqueta = tkinter.Label(ventana, text="Lista:",padx = 60,font=("arial",8,"underline")).pack(side=TOP,expand=True)

Lb1 = Listbox(ventana)

Lb1.insert(0, "Introduce un comentario")



Lb1.pack()
'''

#BOTON

def aceptar():
        
    radioValue.get()
    pass
    
  
botonAceptar = tkinter.Button(ventana, text="Aceptar", command=aceptar).pack(side=TOP,expand=True)


ventana.mainloop()
    
    


    



'''
Created on 29 ene. 2021

@author: sseba
'''
class Poligono():

    listaLados = []
    def __init__(self,numLados = 4):
        self.numLados = numLados
        pass
    
    def darLados(self):
        
        for i in range(0,int(self.numLados)):
            valorLado = input("introduce lado \n")
            self.listaLados.append(valorLado)
            pass
        pass

    def verLados(self):
        print("La lista de lados es: \n",self.listaLados)
        self.listaLados.clear()
        pass
    
class Triangulo(Poligono):
    
    def Imprimir(self):
        Poligono.__init__(self, numLados = 3)
        Poligono.darLados(self)
        Poligono.verLados(self)
        self.area()
        self.perimetro()
        pass
    def area(self):
        base = input("Introduce la base del triangulo: \n")
        altura = input("Introduce la altura del triangulo: \n")
        a = int(base) * int(altura) / 2
        return print("El area del triangulo es:",a)
    pass

    def perimetro(self):
        self.sumaLados = 0
        for i in range(0,len(Poligono.listaLados)):
            self.sumaLados += int(Poligono.listaLados[i])
            pass
        pass
        return print("El perimetro del triangulo es:",self.sumaLados)
    pass
t1 = Triangulo()
t2 = Triangulo()
t1.Imprimir()
t2.Imprimir()

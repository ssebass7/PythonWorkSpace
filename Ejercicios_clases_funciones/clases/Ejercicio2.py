'''
Created on 29 ene. 2021

@author: sseba
'''
from operator import __add__
class Punto():
    
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y
    pass    
        
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
        pass
    pass
    def __suma__(self,p2,p3):
        sumax = self.x + p2.x + p3.x
        sumay = self.y + p2.y + p3.y

        return sumax , sumay
        pass
p1 = Punto(5,6)
p2 = Punto(2,4)
p3 = Punto(3,7)

print(p1.__str__())
print(p2.__str__())
print(p3.__str__())
print(p1.__suma__(p2,p3))



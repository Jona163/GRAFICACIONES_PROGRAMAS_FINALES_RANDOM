#Ecuacion Cuadratica
import math as m
import numpy as np
from matplotlib import pyplot

a=float(input("ingrese el valor de (a):\n"))
b=float(input("ingrese el valor de (b):\n"))
c=float(input("ingrese el valor de (c):\n"))

disc=(b**2)-(4*a*c)
raiz=(disc)**(0.5)

if(disc>0):
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("x1= ",x1)
    print("x2= ",x2)

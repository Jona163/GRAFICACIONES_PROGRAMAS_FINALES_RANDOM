#POLINOMIAL XD
import numpy as np
import animatplot as amp
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
########## PREPARAR LA DATA ##########
#Importamos los datos de la misma librería de scikit-learn
boston = datasets.load_boston()
print(boston)
print()
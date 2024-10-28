import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Coeficientes de la función objetivo
c = [-25, -30]  # Coeficientes de x y y en la función objetivo (se multiplican por -1 para convertir en maximización)

# Coeficientes de las restricciones (lado izquierdo de las desigualdades)
A = [[1, 1.5], [1.5, 1]]  # Coeficientes de x y y en las restricciones
b = [750, 750]  # Lado derecho de las restricciones (disponibilidad de oro y plata)

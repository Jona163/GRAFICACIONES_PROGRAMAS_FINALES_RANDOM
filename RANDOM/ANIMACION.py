import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.optimize import linprog

# Coeficientes de la función objetivo
c = [-25, -30]

# Coeficientes de las restricciones
A = [[1, 1.5], [1.5, 1]]
b = [750, 750]

# Límites de las variables
x_bounds = (0, None)
y_bounds = (0, None)

# Resolución del problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# Valores iniciales de las variables
x_initial = 320  # Cantidad de joyas de tipo A
y_initial = 320  # Cantidad de joyas de tipo B

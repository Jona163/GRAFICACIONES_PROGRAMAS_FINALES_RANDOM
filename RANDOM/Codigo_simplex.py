import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Coeficientes de la función objetivo
c = [-25, -30]  # Coeficientes de x y y en la función objetivo (se multiplican por -1 para convertir en maximización)

# Coeficientes de las restricciones (lado izquierdo de las desigualdades)
A = [[1, 1.5], [1.5, 1]]  # Coeficientes de x y y en las restricciones
b = [750, 750]  # Lado derecho de las restricciones (disponibilidad de oro y plata)

# Límites de las variables
x_bounds = (0, None)  # x >= 0
y_bounds = (0, None)  # y >= 0

# Resolución del problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# Extraer los resultados
x = result.x[0]  # Cantidad de joyas de tipo A
y = result.x[1]  # Cantidad de joyas de tipo B
max_beneficio = -result.fun  # Máximo beneficio

# Imprimir resultados
print("Cantidad de joyas de tipo A:", x)
print("Cantidad de joyas de tipo B:", y)
print("Máximo beneficio:", max_beneficio)

# Graficar las restricciones y la solución óptima
x_vals = np.linspace(0, 500, 100)
y1_vals = (750 - x_vals) / 1.5
y2_vals = 750 - 1.5 * x_vals

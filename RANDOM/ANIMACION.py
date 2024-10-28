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

# Valores objetivo óptimos
x_optimal = result.x[0]  # Cantidad óptima de joyas de tipo A
y_optimal = result.x[1]  # Cantidad óptima de joyas de tipo B

# Configuración de la gráfica de barras
fig, ax = plt.subplots()
bar_labels = ['Joyas A', 'Joyas B']
bar_values = [x_initial, y_initial]
bars = ax.bar(bar_labels, bar_values)
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de joyas de cada tipo')

# Función de actualización de la animación
def update_bars(i):
    # Actualizar los valores de las barras con los valores óptimos en el último fotograma
    if i == len(frames) - 1:
        bars[0].set_height(x_optimal)
        bars[1].set_height(y_optimal)
    else:
        # Interpolación lineal entre los valores iniciales y óptimos en los fotogramas intermedios
        t = i / (len(frames) - 1)  # Tiempo normalizado entre 0 y 1
        x_interpolated = x_initial + (x_optimal - x_initial) * t
        y_interpolated = y_initial + (y_optimal - y_initial) * t
        bars[0].set_height(x_interpolated)
        bars[1].set_height(y_interpolated)

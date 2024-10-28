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

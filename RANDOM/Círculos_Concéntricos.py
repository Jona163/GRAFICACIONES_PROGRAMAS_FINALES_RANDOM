import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de parámetro t para la circunferencia exterior
t = np.linspace(0, 2 * np.pi, 1000)

# Definir las funciones paramétricas para x(t) y y(t) - circunferencia exterior
x_exterior = np.cos(t)
y_exterior = np.sin(t)

# Definir el rango de parámetro t para los círculos interiores
t_interior = np.linspace(0, 2 * np.pi, 1000)

# Definir las funciones paramétricas para x(t) y y(t) - círculo interior 1
x_interior1 = 0.5 * np.cos(t_interior)  # Radio 0.5
y_interior1 = 0.5 * np.sin(t_interior)

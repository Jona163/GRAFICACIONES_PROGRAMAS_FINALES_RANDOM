import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de parámetro t para la circunferencia exterior
t = np.linspace(0, 2 * np.pi, 1000)

# Definir las funciones paramétricas para x(t) y y(t) - circunferencia exterior
x_exterior = np.cos(t)
y_exterior = np.sin(t)

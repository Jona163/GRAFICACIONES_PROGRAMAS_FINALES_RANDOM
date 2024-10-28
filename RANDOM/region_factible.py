import matplotlib.pyplot as plt
import numpy as np

# Definir las restricciones
x = np.linspace(0, 10, 100)  # Valores de A en el rango [0, 10]
y1 = (12 - x) / 2  # Restricción 1: A + 2B > 12
y2 = 10 - 2*x  # Restricción 2: 2A + B > 10

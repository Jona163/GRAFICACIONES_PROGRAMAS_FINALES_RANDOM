import matplotlib.pyplot as plt
import numpy as np

# Definir las restricciones
x = np.linspace(0, 10, 100)  # Valores de A en el rango [0, 10]
y1 = (12 - x) / 2  # Restricción 1: A + 2B > 12
y2 = 10 - 2*x  # Restricción 2: 2A + B > 10

# Graficar las restricciones
plt.plot(x, y1, label='A + 2B > 12')
plt.plot(x, y2, label='2A + B > 10')

# Rellenar la región factible
plt.fill_between(x, np.maximum(y1, 0), y2, where=(y1 < y2), color='gray', alpha=0.5)

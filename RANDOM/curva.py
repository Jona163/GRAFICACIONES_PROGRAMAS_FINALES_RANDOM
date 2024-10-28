# Importar librerias
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango del parametro t
t=np.linspace(0, 2 * np.pi, 1000)

# Definir las funciones de x y y
x = np.cos(t)
y = np.sin(t)

# Crear Grafica
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Circunferencia Parametrica')
plt.axis('equal')

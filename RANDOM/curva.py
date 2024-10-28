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

#Opciones adicionales para la grafica
plt.title('Curva Parametrica')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

#Mostrar la grafica
plt.show()

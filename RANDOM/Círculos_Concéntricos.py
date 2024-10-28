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

# Definir las funciones paramétricas para x(t) y y(t) - círculo interior 2
x_interior2 = 0.3 * np.cos(t_interior)  # Radio 0.3
y_interior2 = 0.3 * np.sin(t_interior)

# Crear la gráfica
plt.figure(figsize=(6, 6))  # Ajusta el tamaño de la figura

# Dibujar las curvas paramétricas
plt.plot(x_exterior, y_exterior, label='Circunferencia exterior')
plt.plot(x_interior1, y_interior1, label='Círculo interior 1')
plt.plot(x_interior2, y_interior2, label='Círculo interior 2')

plt.axis('equal')  # Ajusta la relación de aspecto para que la figura sea una circunferencia

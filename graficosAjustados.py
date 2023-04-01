import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tabla1=pd.read_csv("C:\\Users\\PATRICIA PARODI\\Desktop\\Codigos\\pyy\\python\Fiuna\\Tdatos1.csv", sep=r'\s*,\s*',
                           header=0, encoding='ascii', engine='python')

# Eliminar valores duplicados de x
x_unique, index = np.unique(tabla1['x'], return_index=True)
y_unique = tabla1['y'][index]

# Crear una función de interpolación para suavizar la curva
window_len = 11
window = np.hanning(window_len)
y_smooth = np.convolve(window/window.sum(), y_unique, mode='valid')

# Graficar los datos suavizados
x_new = np.linspace(x_unique.min(), x_unique.max(), len(y_smooth))
plt.plot(x_new, y_smooth)
plt.xlabel('Def.Unitaria')
plt.ylabel('Tension (N/ mm^2)')
plt.title('Fragil')
# Obtener el valor máximo y su posición
max_value = np.max(y_smooth)
max_index = np.where(y_smooth == max_value)[0][0]

# Obtener las coordenadas (x,y) del punto máximo
x_max = x_new[max_index]
y_max = max_value

# Resaltar el valor máximo con una flecha que diga "Tensión máxima"
plt.annotate('Tensión máxima', xy=(x_max, y_max), xytext=(x_max+0.02, y_max+0.1),
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=12, color='green')


plt.show()

tabla2 = pd.read_csv("C:\\Users\\PATRICIA PARODI\\Desktop\\Codigos\\pyy\\python\Fiuna\\Tdatos2.csv", sep=r'\s*,\s*',
                           header=0, encoding='ascii', engine='python')

# Eliminar valores duplicados de x
x_unique, index = np.unique(tabla2['x'], return_index=True)
y_unique = tabla2['y'][index]

# Crear una función de interpolación para suavizar la curva
window_len = 9
window = np.hanning(window_len)
y_smooth = np.convolve(window/window.sum(), y_unique, mode='valid')

# Graficar los datos suavizados
x_new = np.linspace(x_unique.min(), x_unique.max(), len(y_smooth))
plt.plot(x_new, y_smooth)
plt.xlabel('Def.Unitaria')
plt.ylabel('Tension (N/ mm^2)')
plt.title('Ductil')

# Obtener el valor máximo y su posición
max_value = np.max(y_smooth)
max_index = np.where(y_smooth == max_value)[0][0]

# Obtener las coordenadas (x,y) del punto máximo
x_max = x_new[max_index]
y_max = max_value

# Resaltar el valor máximo con una flecha que diga "Tensión máxima"
plt.annotate('Tensión máxima', xy=(x_max, y_max), xytext=(x_max+0.02, y_max+0.1),
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=12, color='green')


plt.show()

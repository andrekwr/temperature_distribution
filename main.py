from math import *
import matplotlib.pyplot as plt
import numpy as np

def calcula_temperatura(x):
    h = 15
    k = 200
    L = 0.3
    p = 0.03*4
    A = 0.03 ** 2 
    t_inf = 300
    t_base = 350
    teta_b = t_base - t_inf
    m = sqrt((h*p) / (k*A))
    teta_tetab = (cosh(m * (L - x)) + (h / (m*k)) * sinh(m * (L -x))) / (cosh(m*L) + (h / (m*k)) * sinh(m*L) )
    return teta_tetab * teta_b + t_inf

print("Temperatura em L/2: ", calcula_temperatura(0.15))
print("Temperatura em L: ", calcula_temperatura(0.3))

lista_x = np.arange(0, 0.3, 0.01)
results = [calcula_temperatura(x) for x in lista_x]

plt.plot(lista_x, results, 'red')
plt.plot(0.15, calcula_temperatura(0.15), 'bo')
plt.xlabel('Distância (m)')
plt.ylabel('Temperatura (K)')
plt.grid(True)
plt.show()

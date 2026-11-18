import numpy as np

"y = H_k*x_k + n_k"

k = int(input(" Ingrese los 2 ultimos digitos de su cedula: "))

# Fase_1

""" Calcular los valores de H_k, X_k, Y_k, n_k 
    En funcion de k definir ...
"""

a = 1 + 0.1*((k % 3) + 1)
b = 0.2 + 0.1*((k % 4))
c = 0.1 + 0.1*((k + 1) % 4)
d = 1 + 0.1*((k + 2) % 3)

# prueba para valores - print (a,b,c,d)

H_k = np.array([[a, b], [c, d]])
X_k = np.array([[1 + (k%3)],[2 + (k%2)]])
n_k = np.array([[0.01*(k%5)],[-0.01*((k+2)%5)]])
Y_k = (H_k @ X_k) + n_k

# prueba para ver las matrices
"""
print(H_k)
print()
print(X_k)
print()
print(n_k)
print()
print(Y_k)

"""

# Fase_2


# Fase_3
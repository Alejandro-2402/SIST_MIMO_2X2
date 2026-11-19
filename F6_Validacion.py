import numpy as np

"y = H_k*x_k + n_k"

k = int(input(" Ingrese los 2 ultimos digitos de su cedula: "))

# Fase_1: Construccion

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
print("H_k: ",H_k)
print()
print("X_k: ",X_k)
print()
print("n_k: ",n_k)
print()
print("Y_k: ",Y_k)
print()


# Fase_2: Recuperacion de señal

# X_k2 = H_k^-1 (Y_k)

X_k2 = np.linalg.inv(H_k) @ Y_k

H_k_inv = np.linalg.inv(H_k)


n_K_2 = X_k2 - X_k      # n_k_2 = Error al momento de recuperar la señal

print("H_k_inv: ",H_k_inv)
print()
print("X_k2: ",X_k2)
print()
print("n_K_2: ",n_K_2)


# Fase_3: Determinante e Invertibilidad

det_H_k = np.linalg.det(H_k)

print("Determinante de H_k: ",det_H_k)

if det_H_k != 0:
  print("La matriz H_k es invertible")
else:
  print("La matriz H_k no es invertible")
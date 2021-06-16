import numpy as np

v1 = np.array([1,2])
v2 = np.array([2,2])

suma = v1 + v2

print(v1)
print (type(v1))

print (suma)

v1a = np.array([3,9])
v2b = np.array([2,2])

suma2= v1a + v2b
print(suma2)

# escalar
producto_escalar = 3* v1a
print(producto_escalar)

lista = [x**2 for x in range(5)]
print (lista)
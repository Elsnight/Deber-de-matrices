import numpy as np

def new_matriz(m,n):
    return [[i*j for j in range(n)] for i in range (m)]

filas =int(input("Introduce numero de filas: "))
columnas=int(input("Introduce numero de columnas: "))

matriz = new_matriz(filas,columnas)
print(matriz)

A=np.array([[1,2],[3,4],[5,6]])
B=np.array([[1,2,3],[3,4,5]])
print(A)
print(B)
print(np.dot(A,B))
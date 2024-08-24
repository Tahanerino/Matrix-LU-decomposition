import numpy as np

def decomposition_lu(matrix):
    n = len(matrix)
    L = np.identity(n)
    U = np.zeros((n, n))

    for k in range(n):
        U[k, k:] = matrix[k, k:]
        L[k+1:, k] = matrix[k+1:, k] / U[k, k]
        U[k+1:, k+1:] = matrix[k+1:, k+1:] - np.outer(L[k+1:, k], U[k, k+1:])

    return L, U

# Saisie de la matrice
n = int(input("Enter the size of the square matrix : "))
mx = []
for i in range(n):
    row = [float(input(f"Enter the coefficient of line {i+1} and column {j+1}: ")) for j in range(n)]
    mx.append(row)

# Décomposition LU
L, U = decomposition_lu(np.array(mx))

print("L is :\n", L)
print("U is :\n", U)

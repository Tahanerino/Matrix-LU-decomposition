import numpy as np

def decomposition_lu(matrix):
    n = len(matrix)
    L = np.identity(n)
    U = np.copy(matrix)

    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]

    return L, U

n = int(input("Entrez l'ordre de la matrice carrée : "))
mx = []
for i in range(n):
    row = [float(input(f"Entrer le coefficient de la ligne {i+1} colonne {j+1}: ")) for j in range(n)]
    mx.append(row)

L, U = decomposition_lu(np.array(mx))

print("L est :\n", L)
print("U est :\n", U)

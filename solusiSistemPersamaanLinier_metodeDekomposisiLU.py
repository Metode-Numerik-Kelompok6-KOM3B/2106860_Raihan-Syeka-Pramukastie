
# Fungsi Algoritma Dekomposisi LU
def lu_decomposition(A, b):
    # Ukuran matrik A
    n = len(A)
    # Inisialisasi matrik L dan U dengan ukuran sama dengan A
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    # Lakukan dekomposisi LU
    for k in range(n):
        # Tentukan nilai elemen matrik U di diagonal
        U[k][k] = 1
        for i in range(k, n):
            # Tentukan nilai elemen matrik L di kolom k
            L[i][k] = A[i][k] - sum(L[i][j] * U[j][k] for j in range(k))
        for j in range(k+1, n):
            # Tentukan nilai elemen matrik U di baris k
            U[k][j] = (A[k][j] - sum(L[k][i] * U[i][j]
                       for i in range(k))) / L[k][k]
    # Tentukan vektor solusi y dengan metode sustituisi maju (forward substitution)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    # Tentukan vektor solusi x dengan metode sustituisi mundur (back substitution)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
    return x


A = [[2, 1], [1, -2]]
b = [8, -2]

x = lu_decomposition(A, b)
print(
    f"Solusi sistem persamaan linier tersebut adalah x = {x[0]} dan y = {x[1]}")

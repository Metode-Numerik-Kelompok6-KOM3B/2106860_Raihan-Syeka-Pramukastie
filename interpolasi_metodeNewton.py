def newton_interpolation(x, y):
    # Ukuran vektor x dan y
    n = len(x)
    # Inisialisasi matrik koefisien dengan ukuran n x n
    a = [[0.0] * n for _ in range(n)]
    # Tentukan nilai elemen matrik koefisien di diagonal pertama
    for i in range(n):
        a[i][0] = y[i]
    # Tentukan nilai elemen matrik koefisien lainnya dengan menggunakan rumus
    # a[i][j] = (a[i][j-1] - a[i-1][j-1]) / (x[i] - x[i-j])
    for j in range(1, n):
        for i in range(j, n):
            a[i][j] = (a[i][j-1] - a[i-1][j-1]) / (x[i] - x[i-j])
    # Kembalikan matrik koefisien
    return a


def evaluate_polynomial(a, x, r):
    # Inisialisasi nilai polinomial dengan nilai elemen matrik koefisien terakhir
    value = a[-1][-1]
    # Hitung nilai polinomial dengan menggunakan rumus
    # value = a[n-1][n-1] + (x - x[n-1]) * (a[n-1][n-2] + (x - x[n-2]) * (a[n-2][n-3] + ... + (x - x[1]) * (a[1][0] + (x - x[0]) * a[0][0])))
    for i in range(len(a)-2, -1, -1):
        value = a[i][i] + (r - x[i]) * value
    return value


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Tentukan matrik koefisien
a = newton_interpolation(x, y)

# Tentukan nilai y untuk suatu nilai x
r = 2.5
y_r = evaluate_polynomial(a, x, r)
print(f"Nilai y untuk x = {r} adalah {y_r}")

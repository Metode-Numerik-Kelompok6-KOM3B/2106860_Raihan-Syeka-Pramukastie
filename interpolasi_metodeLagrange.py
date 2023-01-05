def lagrange_interpolation(x, y, r):
    # Inisialisasi nilai polinomial dengan 0
    value = 0
    # Tentukan nilai polinomial dengan menggunakan rumus
    # value = sum(y[i] * l[i] for i in range(n))
    # dengan l[i] adalah fungsi Lagrange
    # l[i] = product(r - x[j] for j in range(n) if i != j) / product(x[i] - x[j] for j in range(n) if i != j)
    for i in range(len(x)):
        l = 1
        for j in range(len(x)):
            if i != j:
                l *= (r - x[j]) / (x[i] - x[j])
        value += y[i] * l
    return value


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Tentukan nilai y untuk suatu nilai x
r = 2.5
y_r = lagrange_interpolation(x, y, r)
print(f"Nilai y untuk x = {r} adalah {y_r}")

from math import sqrt

# Fungsi Akar


def f(x):
    return x**2 - 2

# Fungsi Turunan


def df(x):
    return 2*x

# Fungsi Algoritman Newton Raphson


def newton_raphson(f, df, x0, epsilon=1e-5):
    # Selama toleransi error belum terpenuhi, lanjutkan iterasi
    while True:
        # Hitung nilai f(x0) dan f'(x0)
        f_x0 = f(x0)
        df_x0 = df(x0)
        # Jika f'(x0) bernilai 0, maka tidak dapat dilakukan iterasi lagi. Kembalikan nilai x0
        if df_x0 == 0:
            return x0
        # Tentukan x1 dengan rumus x1 = x0 - f(x0)/f'(x0)
        x1 = x0 - f_x0/df_x0
        # Jika toleransi error sudah terpenuhi, maka kembalikan nilai x1
        if abs(x1 - x0) < epsilon:
            return x1
        # Set x0 dengan x1, lalu lakukan iterasi lagi
        x0 = x1


root = newton_raphson(f, df, 1)
print(f"Akar dari persamaan x^2 - 2 = 0 adalah {root}")

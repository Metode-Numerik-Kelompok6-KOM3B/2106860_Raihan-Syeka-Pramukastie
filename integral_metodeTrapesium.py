def f(x):
    # Fungsi yang akan diintegrasi
    return x**2


def trapezoidal_rule(a, b, n):
    # Tentukan h
    h = (b - a) / n
    # Inisialisasi nilai integral dengan 0
    integral = 0
    # Tentukan nilai integral dengan menggunakan rumus
    # integral = (h / 2) * (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n)))
    integral += (h / 2) * (f(a) + f(b))
    for i in range(1, n):
        integral += h * f(a + i * h)
    return integral


# Tentukan batas integral dan jumlah subinterval
a = 0
b = 1
n = 100

# Tentukan nilai integral dengan menggunakan metode Trapesium
integral = trapezoidal_rule(a, b, n)
print(f"Nilai integral dari f(x) dari {a} sampai {b} adalah {integral}")

from math import sqrt

# Fungsi Akar


def f(x):
    return x**2 - 2

############


# Fungsi Algorima metode bagiDua

def bagiDua(f, a, b, epsilon=1e-5):
    # Selama batas atas dan batas bawah interval masih lebih besar dari toleransi error,
    # maka lanjutkan iterasi
    while (b-a) > epsilon:
        # Tentukan nilai tengah dari interval
        c = (a+b) / 2
        # Jika nilai fungsi di titik tengah sama dengan 0, maka titik tengah adalah akar
        if f(c) == 0:
            return c
        # Jika nilai fungsi di batas bawah dan titik tengah bernilai negatif, maka akar terletak
        # di sebelah kiri titik tengah. Sebaliknya, jika bernilai positif, maka akar terletak di
        # sebelah kanan titik tengah.
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    # Setelah iterasi selesai, kembalikan nilai tengah dari interval akhir
    return (a+b) / 2

############


root = bagiDua(f, 0, 2)
print(f"Akar dari persamaan x^2 - 2 = 0 adalah {root}")

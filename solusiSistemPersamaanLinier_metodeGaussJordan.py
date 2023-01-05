
# Fungsi Algoritma Metode Gauss Jordan
def gauss_jordan(A, b):
    # Gabungkan matrik A dan vektor b menjadi matrik augmented [A|b]
    augmented = [row + [right] for row, right in zip(A, b)]
    # Ukuran matrik augmented
    n = len(augmented)
    # Iterasi setiap baris matrik
    for i in range(n):
        # Tentukan elemen pivot
        pivot = augmented[i][i]
        # Jika pivot bernilai 0, tukar baris dengan baris di bawahnya yang pivot-nya tidak 0
        if pivot == 0:
            for j in range(i+1, n):
                if augmented[j][i] != 0:
                    augmented[i], augmented[j] = augmented[j], augmented[i]
                    pivot = augmented[i][i]
                    break
        # Normalisasi baris tersebut dengan membagi setiap elemennya dengan pivot
        for j in range(i, n+1):
            augmented[i][j] /= pivot
        # Eliminasi elemen di bawah pivot
        for j in range(n):
            if i != j:
                # Tentukan faktor eliminasi
                factor = augmented[j][i]
                # Eliminasi elemen di bawah pivot dengan cara mengurangi baris yang tepat dengan
                # baris pivot yang dikalikan dengan faktor eliminasi
                for k in range(i, n+1):
                    augmented[j][k] -= factor * augmented[i][k]
    # Kembalikan solusi dari matrik augmented
    return [row[-1] for row in augmented]


A = [[2, 1], [1, -2]]
b = [8, -2]

x = gauss_jordan(A, b)
print(
    f"Solusi sistem persamaan linier tersebut adalah x = {x[0]} dan y = {x[1]}")

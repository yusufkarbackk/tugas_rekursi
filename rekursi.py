def pangkat_iterasi(a, b):
    hasil = a
    for i in range(1, b):
        hasil *= a

    return hasil


def pangkat_rekursif(a, b):
    if b <= 1:
        print(f"akhir dari rekursif {b}")
        return a
    else:
        print(f"rekursif {a} x {b}")
        return a * pangkat_rekursif(a, (b-1))


a = int(input("angka: "))
b = int(input("pangkat: "))

#print(f'hasil iterasi = {pangkat_iterasi(a, b)}')
print(f'hasil rekursi = {pangkat_rekursif(a, b)}')

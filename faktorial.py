def faktorial(n):
    if n <= 1:
        print(n)
        return n
    else:
        print(f'{n} * ', end="")
        return n * faktorial(n - 1)


angka = int(input('menghitung faktorial dari: '))

hasil = faktorial(angka)

print(f'nilai faktorialnya adalah: {hasil}')

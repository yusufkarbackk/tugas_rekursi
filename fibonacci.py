def fibonacci(n):
    print(f'fibonacci ke {n}')
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


angka = int(input('menghitung fibonacci ke: '))
hasil = fibonacci(angka)

print(f'nilainya adalah: {hasil}')

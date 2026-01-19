# Segitiga Siku-siku Dasar (Menggunakan while Loop)

## Cara 1: Menggunakan perulangan while dengan penggandaan string
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
count = 1
i = 0
while i < tinggi:
    print('*' * count)
    count += 1
    i += 1

## Cara 2: Menggunakan perulangan while dengan kondisi True dan break
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
count = 1
while True:
    print('*' * count)
    count += 1
    if count > tinggi:
        break

## Cara 3: Menggunakan perulangan while dengan nested loop
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
i = 1
while i <= tinggi:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1

## Cara 4: Menggunakan perulangan while dengan format string
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
i = 1
while i <= tinggi:
    print(f"{'*' * i}")
    i += 1

## Cara 5: Menggunakan perulangan while dengan join
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
i = 1
while i <= tinggi:
    print(''.join(['*' for _ in range(i)]))
    i += 1

## Cara 6: Menggunakan perulangan while dengan format method
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
i = 1
while i <= tinggi:
    print("{}".format('*' * i))
    i += 1

## Cara 7: Menggunakan perulangan while dengan print multiple arguments
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
i = 1
while i <= tinggi:
    print(*(['*'] * i), sep='')
    i += 1

## Cara 8: Menggunakan perulangan while dengan list comprehension
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
i = 1
while i <= tinggi:
    print(''.join([ '*' for _ in range(i)]))
    i += 1
# Segitiga Siku-siku Dasar (Menggunakan for Loop)

## Cara 1: Menggunakan perulangan for dengan penggandaan string
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
count = 1
for i in range(tinggi):
    print('*' * count)
    count += 1

## Cara 2: Menggunakan perulangan for dengan nested loop
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
for i in range(1, tinggi + 1):
    for j in range(i):
        print('*', end='')
    print()

## Cara 3: Menggunakan perulangan for dengan format string
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
for i in range(1, tinggi + 1):
    print(f"{'*' * i}")

## Cara 4: Menggunakan perulangan for dengan join
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
for i in range(1, tinggi + 1):
    print(''.join(['*' for _ in range(i)]))

## Cara 5: Menggunakan perulangan for dengan unpacking
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
for i in range(1, tinggi + 1):
    print(*['*'] * i, sep='')

## Cara 6: Menggunakan perulangan for dengan format method
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
for i in range(1, tinggi + 1):
    print("{}".format('*' * i))

## Cara 7: Menggunakan perulangan for dengan print multiple arguments
tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
for i in range(1, tinggi + 1):
    print(*(['*'] * i), sep='')
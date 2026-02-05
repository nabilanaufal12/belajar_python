# Segitiga dengan Baris Ganjil Saja (Menggunakan while Loop dengan continue)

# Cara 1: Menggunakan perulangan while dengan continue untuk melewati baris genap
tinggi = int(input("Masukkan tinggi segitiga (hanya baris ganjil yang ditampilkan): "))
count = 1
while True:
    if count % 2:
        print('*' * count)
        count += 1
    else:
        count += 1
        continue

    if count > tinggi:
        break

# Cara 2: Menggunakan perulangan while dengan nested loop dan continue
tinggi = int(input("Masukkan tinggi segitiga (hanya baris ganjil yang ditampilkan): "))
i = 1
while i <= tinggi:
    if i % 2 == 0:
        i += 1
        continue
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1

# Cara 3: Menggunakan perulangan while dengan format string dan continue
tinggi = int(input("Masukkan tinggi segitiga (hanya baris ganjil yang ditampilkan): "))
i = 1
while i <= tinggi:
    if i % 2 == 0:
        i += 1
        continue
    print(f"{'*' * i}")
    i += 1

# Cara 4: Menggunakan perulangan while dengan join dan continue
tinggi = int(input("Masukkan tinggi segitiga (hanya baris ganjil yang ditampilkan): "))
i = 1
while i <= tinggi:
    if i % 2 == 0:
        i += 1
        continue
    print(''.join(['*' for _ in range(i)]))
    i += 1

# Cara 5: Menggunakan perulangan while dengan format method dan continue
tinggi = int(input("Masukkan tinggi segitiga (hanya baris ganjil yang ditampilkan): "))
i = 1
while i <= tinggi:
    if i % 2 == 0:
        i += 1
        continue
    print("{}".format('*' * i))
    i += 1

# Cara 6: Menggunakan perulangan while dengan print multiple arguments dan continue
tinggi = int(input("Masukkan tinggi segitiga (hanya baris ganjil yang ditampilkan): "))
i = 1
while i <= tinggi:
    if i % 2 == 0:
        i += 1
        continue
    print(*(['*'] * i), sep='')
    i += 1

# Cara 7: Menggunakan perulangan while dengan list comprehension dan continue
tinggi = int(input("Masukkan tinggi segitiga (hanya baris ganjil yang ditampilkan): "))
while True:
    for i in range(1, tinggi + 1):
        if i % 2 == 0:
            continue
        print('*' * i)
    break
# Segitiga Sama Kaki (Piramida)

tinggi = int(input("Masukkan tinggi segitiga sama kaki: "))
# Cara 1: Menggunakan perulangan for dengan penggandaan string dan spasi
for i in range(1, tinggi + 1):
    spasi = ' ' * (tinggi - i)
    bintang = '*' * (2 * i - 1)
    print(spasi + bintang)
print()

# Cara 2: Menggunakan perulangan for dengan nested loop
for i in range(1, tinggi + 1):
    for j in range(tinggi - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
print()

# Cara 3: Menggunakan perulangan for dengan format string
for i in range(1, tinggi + 1):
    print(f"{' ' * (tinggi - i)}{'*' * (2 * i - 1)}")
print()

# Cara 4: Menggunakan perulangan for dengan join
for i in range(1, tinggi + 1):
    spasi = ''.join([' ' for _ in range(tinggi - i)])
    bintang = ''.join(['*' for _ in range(2 * i - 1)])
    print(spasi + bintang)
print()

# Cara 5: Menggunakan perulangan for dengan format method
for i in range(1, tinggi + 1):
    spasi = " " * (tinggi - i)
    bintang = "*" * (2 * i - 1)
    print("{}{}".format(spasi, bintang))
print()

# Cara 6: Menggunakan perulangan for dengan print multiple arguments
for i in range(1, tinggi + 1):
    print(*([' '] * (tinggi - i)), end='')
    print(*(['*'] * (2 * i - 1)), sep='')
print()
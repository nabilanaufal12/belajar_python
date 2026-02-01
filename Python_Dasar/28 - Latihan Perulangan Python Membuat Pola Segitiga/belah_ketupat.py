# Belah Ketupat 

# Cara 1: Menggunakan perulangan for dengan penggandaan string dan spasi
tinggi = int(input("Masukkan tinggi belah ketupat (harus ganjil): "))
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    for i in range(1, (tinggi // 2) + 2):
        spasi = ' ' * ((tinggi // 2) + 1 - i)
        bintang = '*' * (2 * i - 1)
        print(spasi + bintang)
    
    # Bagian bawah belah ketupat
    for i in range((tinggi // 2), 0, -1):
        spasi = ' ' * ((tinggi // 2) + 1 - i)
        bintang = '*' * (2 * i - 1)
        print(spasi + bintang)
print()

# Cara 2: Menggunakan perulangan for dengan nested loop
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    for i in range(1, (tinggi // 2) + 2):
        for j in range((tinggi // 2) + 1 - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()
    
    # Bagian bawah belah ketupat
    for i in range((tinggi // 2), 0, -1):
        for j in range((tinggi // 2) + 1 - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()
print()

# Cara 3: Menggunakan perulangan for dengan format string
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    for i in range(1, (tinggi // 2) + 2):
        print(f"{' ' * ((tinggi // 2) + 1 - i)}{'*' * (2 * i - 1)}")
    
    # Bagian bawah belah ketupat
    for i in range((tinggi // 2), 0, -1):
        print(f"{' ' * ((tinggi // 2) + 1 - i)}{'*' * (2 * i - 1)}")
print()

# Cara 4: Menggunakan perulangan for dengan join
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    for i in range(1, (tinggi // 2) + 2):
        spasi = ''.join([' ' for _ in range((tinggi // 2) + 1 - i)])
        bintang = ''.join(['*' for _ in range(2 * i - 1)])
        print(spasi + bintang)
    
    # Bagian bawah belah ketupat
    for i in range((tinggi // 2), 0, -1):
        spasi = ''.join([' ' for _ in range((tinggi // 2) + 1 - i)])
        bintang = ''.join(['*' for _ in range(2 * i - 1)])
        print(spasi + bintang)
print()

# Cara 5: Menggunakan perulangan for dengan format method
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    for i in range(1, (tinggi // 2) + 2):
        spasi = " " * ((tinggi // 2) + 1 - i)
        bintang = "*" * (2 * i - 1)
        print("{}{}".format(spasi, bintang))
    
    # Bagian bawah belah ketupat
    for i in range((tinggi // 2), 0, -1):
        spasi = " " * ((tinggi // 2) + 1 - i)
        bintang = "*" * (2 * i - 1)
        print("{}{}".format(spasi, bintang))
print()

# Cara 6: Menggunakan perulangan for dengan print multiple arguments
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    for i in range(1, (tinggi // 2) + 2):
        print(*([' '] * ((tinggi // 2) + 1 - i)), end='')
        print(*(['*'] * (2 * i - 1)), sep='')
    
    # Bagian bawah belah ketupat
    for i in range((tinggi // 2), 0, -1):
        print(*([' '] * ((tinggi // 2) + 1 - i)), end='')
        print(*(['*'] * (2 * i - 1)), sep='')
print()

# Cara 7: Menggunakan perulangan while dengan penggandaan string dan spasi
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    i = 1
    while i <= (tinggi // 2) + 1:
        spasi = ' ' * ((tinggi // 2) + 1 - i)
        bintang = '*' * (2 * i - 1)
        print(spasi + bintang)
        i += 1
    
    # Bagian bawah belah ketupat
    i = tinggi // 2
    while i >= 1:
        spasi = ' ' * ((tinggi // 2) + 1 - i)
        bintang = '*' * (2 * i - 1)
        print(spasi + bintang)
        i -= 1
print()

# Cara 8: Menggunakan perulangan while dengan nested loop
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    i = 1
    while i <= (tinggi // 2) + 1:
        j = 0
        while j < (tinggi // 2) + 1 - i:
            print(' ', end='')
            j += 1
        k = 0
        while k < 2 * i - 1:
            print('*', end='')
            k += 1
        print()
        i += 1
    
    # Bagian bawah belah ketupat
    i = tinggi // 2
    while i >= 1:
        j = 0
        while j < (tinggi // 2) + 1 - i:
            print(' ', end='')
            j += 1
        k = 0
        while k < 2 * i - 1:
            print('*', end='')
            k += 1
        print()
        i -= 1
print()

# Cara 9: Menggunakan perulangan while dengan format string
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    i = 1
    while i <= (tinggi // 2) + 1:
        print(f"{' ' * ((tinggi // 2) + 1 - i)}{'*' * (2 * i - 1)}")
        i += 1
    
    # Bagian bawah belah ketupat
    i = tinggi // 2
    while i >= 1:
        print(f"{' ' * ((tinggi // 2) + 1 - i)}{'*' * (2 * i - 1)}")
        i -= 1
print()

# Cara 10: Menggunakan perulangan while dengan join
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    i = 1
    while i <= (tinggi // 2) + 1:
        spasi = ''.join([' ' for _ in range((tinggi // 2) + 1 - i)])
        bintang = ''.join(['*' for _ in range(2 * i - 1)])
        print(spasi + bintang)
        i += 1
    
    # Bagian bawah belah ketupat
    i = tinggi // 2
    while i >= 1:
        spasi = ''.join([' ' for _ in range((tinggi // 2) + 1 - i)])
        bintang = ''.join(['*' for _ in range(2 * i - 1)])
        print(spasi + bintang)
        i -= 1
print()

# Cara 11: Menggunakan perulangan while dengan format method
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    i = 1
    while i <= (tinggi // 2) + 1:
        spasi = " " * ((tinggi // 2) + 1 - i)
        bintang = "*" * (2 * i - 1)
        print("{}{}".format(spasi, bintang))
        i += 1
    
    # Bagian bawah belah ketupat
    i = tinggi // 2
    while i >= 1:
        spasi = " " * ((tinggi // 2) + 1 - i)
        bintang = "*" * (2 * i - 1)
        print("{}{}".format(spasi, bintang))
        i -= 1
print()

# Cara 12: Menggunakan perulangan while dengan print multiple arguments
if tinggi % 2 == 0:
    print("Tinggi harus berupa bilangan ganjil.")
else:
    # Bagian atas belah ketupat
    i = 1
    while i <= (tinggi // 2) + 1:
        print(*([' '] * ((tinggi // 2) + 1 - i)), end='')
        print(*(['*'] * (2 * i - 1)), sep='')
        i += 1
    
    # Bagian bawah belah ketupat
    i = tinggi // 2
    while i >= 1:
        print(*([' '] * ((tinggi // 2) + 1 - i)), end='')
        print(*(['*'] * (2 * i - 1)), sep='')
        i -= 1
print()
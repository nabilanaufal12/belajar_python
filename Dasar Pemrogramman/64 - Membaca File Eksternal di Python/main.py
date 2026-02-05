# Konsep __main__ dan Penanganan File Eksternal di Python

# Membuka File dengan open()
file = open("data.txt", mode="r")
print(f"Status Readable: {file.readable()}")
print(f"Status Writable: {file.writable()}")

# Membaca Isi File
## Membaca Seluruh File (file.read())
content = file.read()
print(content)

## Membaca Baris per Baris (file.readline())
file = open("data.txt", mode="r")
line1 = file.readline()
line2 = file.readline()
print(line1, end='') # Menghilangkan double enter
print(line2)

## Membaca Semua Baris sebagai List (file.readlines())
file = open("data.txt", mode="r")
all_lines = file.readlines()
print(all_lines)

# Menutup File dengan file.close()
print(f"Apakah file sudah ditutup? {file.closed}")
file.close()
print(f"Apakah file sudah ditutup? {file.closed}")

# Pendekatan Terbaik: Menggunakan with Statement
with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end='')
    print(f"Apakah file sudah ditutup (dalam with)? {file.closed}")

print(f"Apakah file sudah ditutup (dalam with)? {file.closed}")
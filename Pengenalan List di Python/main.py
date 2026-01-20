# Cara Membuat List di Python

# 1. Membuat List Secara Manual (Menggunakan Kurung Siku [])

## Kumpulan Angka (Number)
angka_favorit = [1, 2, 3, 4, 5]
print("Angka Favorit:", angka_favorit)

## Kumpulan String (Text)
buah_favorit = ['apel', 'pisang', 'jeruk', 'mangga']
print("Buah Favorit:", buah_favorit)

## Kumpulan Boolean (True/False)
status_hari = [True, False, True, True]
print("Status Hari:", status_hari)

## Kumpulan Campuran (Mixed Types)
campuran = [1, 'apel', True, 3.14, 'pisang']
print("List Campuran:", campuran)


# 2. Membuat List Menggunakan Fungsi list() dan range()

## List dari range angka 0 sampai 9
angka_range = list(range(10))
print("Angka dari 0 sampai 9:", angka_range)

## List dari range angka 2 sampai 9
angka_range_custom = list(range(2, 10))
print("Angka dari 2 sampai 9:", angka_range_custom)

## List dari range angka dengan langkah tertentu
angka_range_step = list(range(0, 10, 2))  # Angka genap dari 0 sampai 8
print("Angka Genap dari 0 sampai 18:", angka_range_step)


# 3. Membuat List Kosong dan Menambahkan Elemen

## Membuat List Kosong
list_kosong = []
print("List Kosong:", list_kosong)

## Menambahkan Elemen ke List Kosong
list_kosong.append('elemen pertama')
list_kosong.append(42)
print("List Setelah Menambahkan Elemen:", list_kosong)

# 4. Membuat List Menggunakan List Comprehension

## List Comprehension Dasar (dengan for loop)
list_for = [x for x in range(0, 5)]
print("List Comprehension dengan for loop:", list_for)

## List Comprehension dengan Operasi Matematika
list_squared = [x**2 for x in range(0, 5)]
print("List Comprehension dengan kuadrat:", list_squared)

## List Comprehension dengan Kondisi if (Filter)

### Menghilangkan Elemen Tertentu
list_tanpa_angka_lima = [x for x in range(0, 10) if x != 5]
print("List tanpa angka 5:", list_tanpa_angka_lima)

### Mengambil Hanya Angka Genap
list_angka_genap = [x for x in range(0, 10) if x % 2 == 0]
print("List Angka Genap:", list_angka_genap)

### Membuat List Bilangan Ganjil (dan Operasi Kuadrat)
list_bilangan_ganjil_kuadrat = [x**2 for x in range(0, 10) if x % 2 != 0]
print("List Bilangan Ganjil Kuadrat:", list_bilangan_ganjil_kuadrat)
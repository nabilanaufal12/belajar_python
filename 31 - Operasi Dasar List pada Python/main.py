# Operasi Dasar List pada Python

# Contoh list untuk demonstrasi
data_angka = [1, 2, 3, 4, 5, 1, 2, 1]
data_buah = ['apel', 'pisang', 'jeruk', 'mangga', 'pisang']
print("Data Angka:", data_angka)
print("Data Buah:", data_buah)

# 1. Menghitung Kemunculan Elemen (.count())
jumlah_satu = data_angka.count(1)
jumlah_dua = data_angka.count(2)
print(f"Jumlah kemunculan angka 1: {jumlah_satu}")
print(f"Jumlah kemunculan angka 2: {jumlah_dua}")

# 2. Mencari Indeks Elemen (.index())
indeks_pisang_pertama = data_buah.index('pisang')
indeks_pisang_kedua = data_buah.index('pisang', indeks_pisang_pertama + 1)
print(f"Indeks kemunculan pertama 'pisang': {indeks_pisang_pertama}")
print(f"Indeks kemunculan kedua 'pisang': {indeks_pisang_kedua}")

# 3. Mengurutkan List (.sort())

## Mengurutkan data angka secara ascending
data_angka.sort()
print("Data Angka setelah diurutkan (ascending):", data_angka)

## Mengurutkan data buah secara ascending
data_buah.sort()
print("Data Buah setelah diurutkan (ascending):", data_buah)

# 4. Membalik Urutan List (.reverse())

## Membalik urutan data angka
data_angka.reverse()
print("Data Angka setelah dibalik urutan:", data_angka)

## Membalik urutan data buah
data_buah.reverse()
print("Data Buah setelah dibalik urutan:", data_buah)
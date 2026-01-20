# Konsep Perulangan (Looping)
"""
Tujuan Utama: 
Menghindari penulisan kode yang berulang-ulang untuk tugas yang sama. 
Misalnya, jika Anda perlu menambahkan angka 3 ke sebuah variabel sebanyak 100 kali, 
perulangan akan melakukannya secara otomatis tanpa perlu menulis 100 baris kode.

Contoh Aksi Berulang:
- Menambahkan nilai ke sebuah angka secara bertahap.
- Meminta login berulang kali jika password salah.
- Mencetak "Saya Keren" berkali-kali.
"""

# Sintaks Dasar for Loop di Python
# for variabel in iterable:
    # aksi yang akan diulang
    # Blok kode ini akan dieksekusi untuk setiap item dalam iterable

# Penggunaan for Loop dengan Berbagai Tipe Data
## Iterasi dengan List
print("Iterasi dengan List:")
angka = [1, 2, 3, 4, 5]
for nilai in angka:
    print(f"Nilai saat ini: {nilai}")
print("Selesai iterasi dengan list.\n")

## Iterasi dengan String
print("Iterasi dengan String:")
kata = "Python"
for huruf in kata:
    print(f"Huruf saat ini: {huruf}")
print("Selesai iterasi dengan string.\n")

## Iterasi dengan Range
print("Iterasi dengan Range:")
for i in range(5):  # Menghasilkan angka dari 0 hingga 4
    print(f"Angka saat ini: {i}")
print("Selesai iterasi dengan range.\n")

# Perbedaan dengan while Loop (Sekilas)
"""
while kondisi:
    aksi yang akan diulang
    # Blok kode ini akan dieksekusi selama kondisi bernilai True
"""
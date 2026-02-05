# Logika Dasar Kalkulator Sederhana dengan Percabangan di Python
"""
Untuk membuat kalkulator sederhana, kita membutuhkan beberapa komponen utama:
1. Angka 1: Bilangan pertama yang akan dioperasikan.
2. Operator: Simbol operasi matematika (+, -, *, /).
3. Angka 2: Bilangan kedua yang akan dioperasikan.
4. Hasil: Output dari operasi yang dilakukan.

Alur program secara umum adalah sebagai berikut:
1. Ambil data input dari pengguna, yaitu angka 1, operator, dan angka 2 .
2. Lakukan percabangan (if-elif-else) untuk mengecek operator yang dimasukkan.
3. Berdasarkan operator, lakukan perhitungan yang sesuai.
4. Tampilkan hasil perhitungan kepada pengguna.
"""

# Implementasi Python: Mengambil Input User

# Tampilan Awal
print("\n" + 20*"=")
print("Kalkulator Sederhana")
print(20*"-")

# Mengambil Angka dan Operator dari User
angka1 = float(input("Masukkan Angka Pertama: "))
operator = input("Masukkan Operator (+, -, *, /): ")
angka2 = float(input("Masukkan Angka Kedua: "))

# Implementasi Python: Logika Percabangan (IF-ELIF-ELSE)
# Penjumlahan
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
# Pengurangan
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
# Perkalian
elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
# Pembagian
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
# Operator Tidak Valid
else:
    print("Error: Operator tidak valid. Gunakan salah satu dari (+, -, *, /).")

# Penutup
print(20*"=")
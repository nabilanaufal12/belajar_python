# Pernyataan import di Python: Mengelola Kode dan Data Eksternal

# 1. Fungsi Dasar import: Menjalankan Kode Eksternal
import program_print

# 2. Mengimpor Data (Variabel) dengan Konsep Namespace
import program_var

print(f"Hi, {program_var.data[0]}")
print(f"Helo, {program_var.data[1]}")

# 3. Mengimpor Fungsi
import program_math

hasil = program_math.tambah(2, 4)

print(f"2 + 4 = {hasil}")
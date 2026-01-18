# Format Angka dengan f-string pada Python

# Bilangan Bulat (Integer)
nilai_integer = 42
print(f"Nilai integer: {nilai_integer:d}")

# Bilangan Desimal (Float)
nilai_float = 3.14159
print(f"Nilai float: {nilai_float:.2f}")  # Format dengan 2 angka di belakang koma

# Bilangan dengan Pemisah Ribuan
nilai_besar = 1000000
print(f"Nilai dengan pemisah ribuan: {nilai_besar:,}")

# Bilangan dalam Format Persentase
nilai_persen = 0.85
print(f"Nilai dalam format persentase: {nilai_persen:.2%}")

# Bilangan dalam Notasi Ilmiah
nilai_ilmiah = 123456789
print(f"Nilai dalam notasi ilmiah: {nilai_ilmiah:.2e}")

# Bilangan dengan Lebar Minimum dan Perataan
nilai_lebar = 75
print(f"Nilai dengan lebar minimum 10 karakter, rata kanan: {nilai_lebar:>10d}")
print(f"Nilai dengan lebar minimum 10 karakter, rata kiri: {nilai_lebar:<10d}")
print(f"Nilai dengan lebar minimum 10 karakter, rata tengah: {nilai_lebar:^10d}")

# Bilangan dengan Padding Nol
nilai_padding = 7
print(f"Nilai dengan padding nol hingga 5 digit: {nilai_padding:05d}")

# Bilangan Negatif dengan Tanda Plus
nilai_negatif = -42
print(f"Nilai negatif dengan tanda plus: {nilai_negatif:+d}")

# Bilangan Positif dengan Tanda Plus
nilai_positif = 42
print(f"Nilai positif dengan tanda plus: {nilai_positif:+d}")

# Bilangan dalam Format Biner, Oktal, dan Heksadesimal
nilai_bilangan = 255
print(f"Nilai dalam format biner: {nilai_bilangan:b}")
print(f"Nilai dalam format oktal: {nilai_bilangan:o}")
print(f"Nilai dalam format heksadesimal (huruf kecil): {nilai_bilangan:x}")
print(f"Nilai dalam format heksadesimal (huruf besar): {nilai_bilangan:X}")

# Kombinasi Beberapa Format
nilai_kombinasi = 12345.6789
print(f"Nilai kombinasi: {nilai_kombinasi:,.2f}")  # Pemisah ribuan dan 2 angka di belakang koma

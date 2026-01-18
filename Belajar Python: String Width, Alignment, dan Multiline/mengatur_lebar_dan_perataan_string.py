# Mengatur Lebar (Width) dan Perataan (Alignment) String

""" Konsep Dasar
Dalam Python, kita dapat mengatur lebar dan perataan string menggunakan f-string dengan format khusus.
rikut adalah beberapa opsi yang umum digunakan:
Lebar (Width): Menentukan lebar minimum dari string.
Perataan Kiri (<): Meratakan string ke kiri.
- Perataan Kanan (>): Meratakan string ke kanan.
- Perataan Tengah (^): Meratakan string di tengah.

Sintaksnya adalah {nilai:alignment_symbol lebar} di dalam f-string.
"""

# Contoh Data
data_nama = "Alice"
data_umur = 30
data_tinggi = 165.5
data_nomor_telepon = "081234567890"

# Perataan Kanan (:>)
data_string_rata_kanan = f"""
Nama          : {data_nama:>15}
Umur          : {data_umur:>15} tahun
Tinggi        : {data_tinggi:>15} cm
Nomor Telepon : {data_nomor_telepon:>15}
"""
print(5*"=" + " Perataan Kanan " + 5*"=")
print(data_string_rata_kanan)

# Perataan Kiri (:<)
data_string_rata_kiri = f"""
Nama          : {data_nama:<15}
Umur          : {data_umur:<15} tahun
Tinggi        : {data_tinggi:<15} cm
Nomor Telepon : {data_nomor_telepon:<15}
"""
print(5*"=" + " Perataan Kiri " + 5*"=")
print(data_string_rata_kiri)

# Perataan Tengah (:^)
data_string_rata_tengah = f"""
Nama          : {data_nama:^15}
Umur          : {data_umur:^15} tahun
Tinggi        : {data_tinggi:^15} cm
Nomor Telepon : {data_nomor_telepon:^15}
"""
print(5*"=" + " Perataan Tengah " + 5*"=")
print(data_string_rata_tengah)
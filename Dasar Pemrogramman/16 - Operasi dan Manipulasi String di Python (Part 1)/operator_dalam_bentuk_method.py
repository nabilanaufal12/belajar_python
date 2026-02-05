# Operator dalam Bentuk Method di Python
nama_belakang = "Santoso"
nama_tengah = "D"
nama_depan = "Bell"

print("Nama belakang :", nama_belakang)
print("Nama tengah  :", nama_tengah)
print("Nama depan   :", nama_depan)

# Menyambung string menggunakan operator +
nama_lengkap = nama_belakang + " " + nama_tengah + "'" + nama_depan
print("Nama lengkap menggunakan + :", nama_lengkap)

# Menggunakan method string untuk operasi tertentu
upper_nama = nama_lengkap.upper()
print("Nama lengkap dalam huruf kapital :", upper_nama)
lower_nama = nama_lengkap.lower()
print("Nama lengkap dalam huruf kecil   :", lower_nama)
title_nama = nama_lengkap.title()
print("Nama lengkap dalam format title  :", title_nama)
jumlah_a = nama_lengkap.count('a')
print("Jumlah kemunculan huruf 'a' dalam nama lengkap :", str(jumlah_a))
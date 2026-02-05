# Menghitung Panjang String (Length of String) di Python

nama_belakang = "Santoso"
nama_tengah = "D"
nama_depan = "Bell"

print("Nama belakang :", nama_belakang)
print("Nama tengah  :", nama_tengah)
print("Nama depan   :", nama_depan)

# Menyambung string menggunakan operator +
nama_lengkap = nama_belakang + " " + nama_tengah + "'" + nama_depan
print("Nama lengkap menggunakan + :", nama_lengkap)

# Menghitung panjang string menggunakan fungsi len()
panjang_nama = len(nama_lengkap)
print("Panjang nama lengkap adalah :", str(panjang_nama))
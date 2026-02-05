# Item Paling Kecil dan Paling Besar (Arguments min() dan max()) di Python

nama_belakang = "Santoso"
nama_tengah = "D"
nama_depan = "Bell"

print("Nama belakang :", nama_belakang)
print("Nama tengah  :", nama_tengah)
print("Nama depan   :", nama_depan)

# Menyambung string menggunakan operator +
nama_lengkap = nama_belakang + " " + nama_tengah + "'" + nama_depan
print("Nama lengkap menggunakan + :", nama_lengkap)

# Mencari item paling kecil dan paling besar dalam string menggunakan fungsi min() dan max()
item_terkecil = min(nama_lengkap)
item_terbesar = max(nama_lengkap)
print("Item paling kecil dalam nama lengkap adalah :", item_terkecil)
print("Item paling besar dalam nama lengkap adalah  :", item_terbesar)

ascii_terkecil = ord(item_terkecil)
ascii_terbesar = ord(item_terbesar)
print("Nilai ASCII dari item paling kecil ('" + item_terkecil + "') adalah :", str(ascii_terkecil))
print("Nilai ASCII dari item paling besar ('" + item_terbesar + "') adalah  :", str(ascii_terbesar))
# Indexing dan Slicing di Python

nama_belakang = "Santoso"
nama_tengah = "D"
nama_depan = "Bell"

print("Nama belakang :", nama_belakang)
print("Nama tengah  :", nama_tengah)
print("Nama depan   :", nama_depan)

# Menyambung string menggunakan operator +
nama_lengkap = nama_belakang + " " + nama_tengah + "'" + nama_depan
print("Nama lengkap menggunakan + :", nama_lengkap)

# Indexing
print("Karakter pertama nama lengkap :", nama_lengkap[0])
print("Karakter kedua nama lengkap   :", nama_lengkap[6])
print("Karakter terakhir nama lengkap :", nama_lengkap[-1])
print("Karakter kedua dari belakang nama lengkap :", nama_lengkap[-2])

# Slicing
print("Slicing nama belakang :", nama_lengkap[0:7])
print("Slicing nama tengah   :", nama_lengkap[8:9])
print("Slicing nama depan    :", nama_lengkap[10:14])
print("Slicing nama lengkap dari karakter ke-0 sampai ke-4 :", nama_lengkap[0:5])
print("Slicing nama lengkap dari karakter ke-5 sampai akhir   :", nama_lengkap[5:])
print("Slicing nama dengan indeks negatif dari -5 sampai akhir :", nama_lengkap[-5:])
print("Slicing nama dengan indeks negatif dari awal sampai -5   :", nama_lengkap[:-5])
print("Slicing nama lengkap seluruhnya :", nama_lengkap[:])
print("Slicing nama lengkap dengan step 2 :", nama_lengkap[::2])
print("Slicing nama lengkap dengan step 3 :", nama_lengkap[::3])
print("Slicing nama lengkap terbalik :", nama_lengkap[::-1])
print("Slicing nama lengkap terbalik dengan step 2 :", nama_lengkap[::-2])
print("Slicing nama indeks ganjil :", nama_lengkap[1::2])
print("Slicing nama indeks genap  :", nama_lengkap[0::2])
print("Slicing nama indeks ganjil :", nama_lengkap[1:5:2])
print("Slicing nama indeks genap  :", nama_lengkap[0:3:2])
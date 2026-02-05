# Penggabungan dan Pemisahan String (Concatenation and Splitting Strings) di Python

data1 = "Halo"
data2 = "Dunia"
data_list = ["Python", "adalah", "bahasa", "pemrograman"]

print("Data 1:", data1)
print("Data 2:", data2)
print("Data List:", data_list)

# Penggabungan String (.join())
gabungan = " ".join([data1, data2])
print("\nHasil penggabungan string menggunakan .join():", gabungan)
print("Hasil penggabungan string dari list menggunakan .join():", " ".join(data_list))

# Pemisahan String (.split())
kalimat = "Python adalah bahasa pemrograman yang menyenangkan"
pemisahan = kalimat.split(" ")
print("\nKalimat asli:", kalimat)
print("Hasil pemisahan string menggunakan .split():", pemisahan)
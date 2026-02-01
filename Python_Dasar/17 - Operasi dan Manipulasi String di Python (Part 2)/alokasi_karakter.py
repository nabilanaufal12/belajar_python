# Alokasi Karakter (Rata Kanan/Kiri/Tengah) di String Python

data = "Halo Dunia"
print("Data asli:", data)
print("Rata kiri 20 karakter  :", data.ljust(20, '-'))
print("Rata kanan 20 karakter :", data.rjust(20, '-'))
print("Rata tengah 20 karakter:", data.center(20, '-'))
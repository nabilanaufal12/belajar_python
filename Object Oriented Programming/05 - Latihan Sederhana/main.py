class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        print(f"Objek Mahasiswa '{self.nama}' berhasil dibuat.")

    def tampilkan_info(self):
        print(f"Nama\t: {self.nama}")
        print(f"NIM\t: {self.nim}")
        print(f"Jurusan\t: {self.jurusan}")
        print("-" * 20)

# Membuat objek mahasiswa pertama
mahasiswa1 = Mahasiswa("Mizu", "220244", "Teknik Informatika")

# Membuat objek mahasiswa kedua
mahasiswa2 = Mahasiswa("Miwa", "220145", "Teknik Industri")

# Mengakses atribut objek
print(f"Nama mahasiswa 1: {mahasiswa1.nama}")
print(f"Jurusan mahasiswa 2: {mahasiswa2.jurusan}")

# Memanggil metode objek
print("\nInformasi Mahasiswa 1:")
mahasiswa1.tampilkan_info()

print("Informasi Mahasiswa 2:")
mahasiswa2.tampilkan_info()

# Memodifikasi atribut mahasiswa1
mahasiswa1.jurusan = "Teknik Nuklir"
print("\nInformasi Mahasiswa 1 setelah diubah:")
mahasiswa1.tampilkan_info()
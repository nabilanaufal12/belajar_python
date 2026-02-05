class Mahasiswa:
    def __init__(self, nama, nim):
        # 'self.nama' dan 'self.nim' adalah atribut objek
        # 'nama' dan 'nim' adalah parameter yang diterima oleh konstruktor
        self.nama = nama
        self.nim = nim
        print(f"Objek Mahasiswa {self.nama} dengan NIM {self.nim} telah dibuat.")

# Membuat objek (instance) dari kelas Mahasiswa
# Saat objek dibuat, metode __init__() akan dipanggil secara otomatis
mhs1 = Mahasiswa("Mizu", "223456")
mhs2 = Mahasiswa("Mika", "220987")

# Mengakses atribut objek
print(f"Nama Mahasiswa 1: {mhs1.nama}")
print(f"NIM Mahasiswa 2: {mhs2.nim}")
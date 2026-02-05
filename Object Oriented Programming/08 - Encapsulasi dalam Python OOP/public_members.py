class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama # Atribut public
        self.gaji = gaji # Atribut public

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

k = Karyawan("Mizu", 500000000)
print(k.nama) # Akses langsung atribut publik
k.gaji = 600000000 # Modifikasi langsung atribut publik
k.tampilkan_info()
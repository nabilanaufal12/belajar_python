class Kucing:
    spesies = "Felis catus" # Variabel kelas

    def __init__(self, nama, warna):
        self.nama = nama # Variabel instance
        self.warna = warna # Variabel instance

kucing1 = Kucing("Miko", "Putih")
kucing2 = Kucing("Miwa", "Hitam")

print(Kucing.spesies)
print(kucing1.spesies)
print(kucing2.spesies)

Kucing.spesies = "Kucing Domestik" # Mengubah variabel kelas melalui kelas
print(kucing1.spesies)
print(kucing2.spesies)
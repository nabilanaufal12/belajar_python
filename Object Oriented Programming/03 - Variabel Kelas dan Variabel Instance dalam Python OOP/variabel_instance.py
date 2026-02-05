class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama # Variabel instance
        self.warna = warna # Variabel instance

kucing1 = Kucing("Miko", "Putih")
kucing2 = Kucing("Miwa", "Hitam")

print(kucing1.nama)
print(kucing2.nama)

kucing1.warna = "Coklat" # Mengubah variabel instance untuk kucing1 saja
print(kucing1.warna)
print(kucing2.warna)
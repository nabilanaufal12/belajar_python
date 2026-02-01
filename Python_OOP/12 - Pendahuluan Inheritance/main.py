# Kelas Induk (Superclass)
class Hewan:
    def __init__(self, nama):
        self.nama = nama
        print(f"{self.nama} adalah hewan.")

    def bersuara(self):
        print("Hewan ini bersuara.")

# Kelas Anak (Subclass) yang mewarisi dari Hewan
class Anjing(Hewan):
    def __init__(self, nama, ras):
        # Memanggil konstruktor kelas induk menggunakan super()
        super().__init__(nama)
        self.ras = ras
        print(f"{self.nama} adalah anjing ras {self.ras}.")

    # Mengganti (override) metode bersuara dari kelas induk
    def bersuara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# Kelas Anak lain
class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna
        print(f"{self.nama} adalah kucing berwarna {self.warna}.")

    # Mengganti (override) metode bersuara dari kelas induk
    def bersuara(self):
        print(f"{self.nama} mengeong: Meong meong!")

# Membuat objek
hewan_umum = Hewan("Binatang")
hewan_umum.bersuara()

anjing_saya = Anjing("Miko", "Golden Retriever")
anjing_saya.bersuara()

kucing_saya = Kucing("Niko", "Pink")
kucing_saya.bersuara()
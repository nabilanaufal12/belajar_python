class Hewan:
    def bersuara(self):
        print("Hewan bersuara")

class Anjing(Hewan):
    def bersuara(self): # Meng-override metode bersuara() dari Hewan
        print("Guk guk!")

class Kucing(Hewan):
    def bersuara(self): # Meng-override metode bersuara() dari Hewan
        print("Meong!")

hewan_umum = Hewan()
anjing_peliharaan = Anjing()
kucing_peliharaan = Kucing()

hewan_umum.bersuara()
anjing_peliharaan.bersuara()
kucing_peliharaan.bersuara()


class Kendaraan:
    def bergerak(self):
        print("Kendaraan bergerak maju.")

class Mobil(Kendaraan):
    def bergerak(self): # Overide
        super().bergerak() # Memanggil metode bergerak() dari kelas induk
        print("Mobil bergerak dengan empat roda.")

mobil_saya = Mobil()
mobil_saya.bergerak()
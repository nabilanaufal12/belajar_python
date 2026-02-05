class Mobil:
    roda = 4 # Atribut kelas

    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def ganti_jumlah_roda(cls, jumlah_baru): # Class method
        cls.roda = jumlah_baru
        return f"Jumlah roda semua mobil sekarang {cls.roda}"
    
    @classmethod
    def buat_mobil_listrik(cls, merek): # Factory method
        return cls(f"Listrik {merek}")
    
print(Mobil.ganti_jumlah_roda(6)) # Memanggil class method melalui kelas
mobil_baru = Mobil.buat_mobil_listrik("Tesla")
print(mobil_baru.merek)
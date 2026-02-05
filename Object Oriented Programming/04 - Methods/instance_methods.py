class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self): # Instance method
        return f"{self.nama} mengeong."
    
    def tambah_umur(self, tahun): # Instance method
        self.umur += tahun
        return f"Umur {self.nama} sekarang {self.umur} tahun."
    
kucing_saya = Kucing("Milo", 3)
print(kucing_saya.bersuara()) # Memanggil instance method
print(kucing_saya.tambah_umur(1))
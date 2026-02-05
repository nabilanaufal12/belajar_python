from abc import ABC, abstractmethod

class Bentuk(ABC): # Kelas Bentuk adalah abstrak
    @abstractmethod
    def hitung_luas(self):
        pass # Metode abstrak tidak memiliki implementasi

    @abstractmethod
    def hitung_keliling(self):
        pass

class Lingkaran(Bentuk):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def hitung_luas(self):
        return 3.14 * self.radius * self.radius
    
    def hitung_keliling(self):
        return 2 * 3.14 * self.radius
    
class Persegi(Bentuk): # Jika tidak mengimplementasikan semua metode abstrak, ini juga menjadi abstrak
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi
    
    def hitung_keliling(self):
        return 4 * self.sisi
    
# bentuk = Bentuk() # Ini akan menghasilkan TypeError karena Bentuk adalah kelas abstrak
lingkaran = Lingkaran(5)
print(f"Luas Lingkaran: {lingkaran.hitung_luas()}")
print(f"Keliling Lingkaran: {lingkaran.hitung_keliling()}")

persegi = Persegi(3)
print(f"Luas Persegi: {persegi.hitung_luas()}")
print(f"Keliling Persegi: {persegi.hitung_keliling()}")
from abc import ABC, abstractmethod

# Mendefinisikan kelas abstract 'Bentuk'
class Bentuk(ABC):
    def __init__(self, nama):
        self.nama = nama

    # Metode abstract: harus diimplementasikan oleh subclass
    @abstractmethod
    def hitung_luas(self):
        pass # Tidak ada implementasi di sini

    # Metode konkret: bisa memiliki implementasi di kelas abstract
    def tampilkan_nama(self):
        print(f"Ini adalah bentuk: {self.nama}")

# Subclass konkret 'Lingkaran'
class Lingkaran(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self.radius = radius

    # Implementasi metode abstract hitung_luas()
    def hitung_luas(self):
        return 3.14 * self.radius * self.radius
    
# Subclass Konkret 'Persegi'
class Persegi(Bentuk):
    def __init__(self, nama, sisi):
        super().__init__(nama)
        self.sisi = sisi

    # Implementasi metode abstract hitung_luas()
    def hitung_luas(self):
        return self.sisi * self.sisi
    
# Penggunaan
# Mencoba menginstansiasi kelas abstract akan menghasilkan error
try:
    Bentuk_umum = Bentuk("Bentuk Umum")
except TypeError as e:
    print(f"Error: {e}")

# Menginstansiasi subclass konkret
lingkaran1 = Lingkaran("Lingkaran A", 5)
persegi1 = Persegi("Persegi", 4)

print(f"{lingkaran1.nama} memiliki luas: {lingkaran1.hitung_luas()}")
print(f"{persegi1.nama} memiliki luas: {persegi1.hitung_luas()}")

lingkaran1.tampilkan_nama()
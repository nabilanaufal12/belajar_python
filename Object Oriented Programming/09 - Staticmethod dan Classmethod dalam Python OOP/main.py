## Staticmethod
class Matematika:
    @staticmethod
    def hitung_luas_lingkaran(radius):
        return 3.14159 * radius * radius
    
# Memanggil staticmethod
luas = Matematika.hitung_luas_lingkaran(5)
print(luas)

## Classmethod
class Orang:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    @classmethod
    def dari_string(cls, data_string):
        nama, usia = data_string.split('-')
        return cls(nama, int(usia)) # cls() akan memanggil konstruktor kelas
    
# Memanggil classmethod
orang1 = Orang.dari_string("Budi-30")
print(f"{orang1.nama}, {orang1.usia}")
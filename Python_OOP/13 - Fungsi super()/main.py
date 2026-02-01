## Penggunaan `super()` dalam `__init__`
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
        print(f"Kendaraan {self.merek} tahun {self.tahun} dibuat.")

class Mobil(Kendaraan):
    def __init__(self, merek, tahun, model):
        super().__init__(merek, tahun) # Memanggil konstruktor Kendaraan
        self.model = model
        print(f"Mobil {self.merek} model {self.model} dibuat.")

# Contoh penggunaan
mobil_saya = Mobil("Toyota", 2020, "Camry")


## Penggunaan `super()` untuk Metode Lain
class Bentuk:
    def info(self):
        return "Ini adalah sebuah bentuk."
    
class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def info(self):
        # Memanggil metode info() dari kelas Bentuk
        pesan_induk = super().info()
        return f"{pesan_induk} Ini adalah lingkaran dengan radius {self.radius}."
    
# Contoh penggunaan
lingkaran_kecil = Lingkaran(5)
print(lingkaran_kecil.info())


## `super()` dan Method Resolution Order (MRO)
class A:
    def method(self):
        print("Method dari A")

class B(A):
    def method(self):
        print("Method dari B")
        super().method() # Memanggil method dari A

class C(A):
    def method(self):
        print("Method dari C")
        super().method() # Memanggil method dari A

class D(B, C):
    def method(self):
        print("Method dari D")
        super().method() # Memanggil method dari B (sesuai MRO)

# Contoh penggunaan
d_obj = D()
d_obj.method()

print(D.__mro__)
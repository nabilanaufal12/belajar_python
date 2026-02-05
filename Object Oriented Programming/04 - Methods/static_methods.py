class Kalkulator:
    @staticmethod
    def tambah(a, b):
        return a + b
    
    @staticmethod
    def kurang(a, b):
        return a - b
    
hasil_tambah = Kalkulator.tambah(5, 3) # Memanggil static method melalui kelas
print(f"Hasil tambah: {hasil_tambah}")
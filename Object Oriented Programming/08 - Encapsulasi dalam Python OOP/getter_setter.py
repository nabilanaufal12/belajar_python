class Karyawan:
    def __init__(self, nama, gaji):
        self._nama = nama
        self._gaji = gaji # Menggunakan _ untuk menunjukkan bahwa ini harus diakses melalui properti

    @property # Getter untuk nama
    def nama(self):
        return self._nama
    
    @nama.setter # Setter untuk nama
    def nama(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Nama harus berupa string non-kosong.")
        self._nama = value
        
    @property # Getter untuk gaji
    def gaji(self):
        return self._gaji
    
    @gaji.setter # Setter untuk gaji
    def gaji(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            self._gaji = value

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

k = Karyawan("Mizu", 900000000)
print(k.nama) # Memanggil getter nama
print(k.gaji) # Memanggil getter gaji

k.gaji = 950000000 # Memanggil setter gaji
k.tampilkan_info()

try:
    k.gaji = -100 # Akan memicu ValueError dari setter
except ValueError as e:
    print(f"Error: {e}")

try:
    k.nama = "" # Akan memicu ValueError dari setter
except ValueError as e:
    print(f"Error: {e}")
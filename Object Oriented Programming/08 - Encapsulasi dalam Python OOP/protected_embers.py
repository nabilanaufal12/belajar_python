class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self._gaji = gaji # Atribut terlindungi (konvensi)

    def _hitung_pajak(self): # Metode terlindungi (konvensi)
        return self._gaji * 0.10

    def tampilkan_info(self):
        pajak = self._hitung_pajak()
        print(f"Nama: {self.nama}, Gaji: {self._gaji}, Pajak: {pajak}")

k = Karyawan("Mizu", 700000000)
print(k._gaji) # Masih bisa diakses, tapi tidak disarankan
pajak_manual = k._hitung_pajak() # Masih bisa dipanggil, tapi tidak disarankan
k.tampilkan_info()
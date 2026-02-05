class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.__gaji_pokok = gaji # Atribut privat (name mangling)

    def __hitung_bonus(self): # Metode privat (name mangling)
        return self.__gaji_pokok * 0.05

    def tampilkan_info(self):
        bonus = self.__hitung_bonus()
        print(f"Nama: {self.nama}, Gaji Pokok: {self.__gaji_pokok}, Bonus: {bonus}")

k = Karyawan("Mizu", 800000000)
# print(k.__gaji_pokok) # Ini akan menyebabkan AttributeError
# print(k.__hitung_bonus()) # Ini akan menyebabkan AttributeError

# Akses melalui name mangling (tidak disarankan)
print(k._Karyawan__gaji_pokok)
bonus_manual = k._Karyawan__hitung_bonus()
print(f"Bonus manual: {bonus_manual}")

k.tampilkan_info()
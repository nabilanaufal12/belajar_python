# Membangun dan Menggunakan Modul Python

import module_math as mm

hasil_penjumlahan = mm.penjumlahan(1, 2, 3, 4)
print(f"Hasil penjumlahan: {hasil_penjumlahan}")

hasil_perkalian = mm.perkalian(1, 2, 3, 4)
print(f"Hasil perkalian: {hasil_perkalian}")

pangkat_3_f = mm.pangkat(3)
hasil_pangkat = pangkat_3_f(2)
print(f"Hasil pengkat: {hasil_pangkat}")

from module_math import penjumlahan as tambah
from module_math import perkalian as kali
from module_math import pangkat as pkt

hasil_penjumlahan = tambah(1, 2, 3, 4)
print(f"Hasil penjumlahan: {hasil_penjumlahan}")

hasil_perkalian = kali(1, 2, 3, 4)
print(f"Hasil perkalian: {hasil_perkalian}")

pangkat_3_f = pkt(3)
hasil_pangkat = pangkat_3_f(2)
print(f"Hasil pengkat: {hasil_pangkat}")
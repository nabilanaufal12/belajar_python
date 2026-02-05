# Memahami Package dan Modul di Python

## a. Import Langsung Package dan Modul
import sains.module_math

hasil_penjumlahan = sains.module_math.penjumlahan(1, 2, 3, 4)
print(f"Hasil penjumlahan dari package: {hasil_penjumlahan}")

## b. Import Modul dari Package
from sains import module_physic

hasil_gaya = module_physic.gaya(90, 10)
print(f"Gaya (fisika.gaya): {hasil_gaya}")

## c. Import Fungsi Spesifik dengan Alias
from sains.module_physic import gaya as force

hasil_force = force(90, 10)
print(f"Gaya (fisika.gaya): {hasil_force}")

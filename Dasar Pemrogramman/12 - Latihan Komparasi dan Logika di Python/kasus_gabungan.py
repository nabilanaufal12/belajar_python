# KASUS 1: Gabungan Komparasi dan Logika
# Angka < 3 atau Angka > 7

inputUser = float(input("Masukkan angka: "))

isKurangDari = inputUser < 3
isLebihDari = inputUser > 7

print("Kurang dari 3:", isKurangDari)
print("Lebih dari 7:", isLebihDari)

hasil = isKurangDari or isLebihDari

print(f"Hasil komparasi {isKurangDari} or {isLebihDari}: {hasil}")

# KASUS 2: Irisan Komparasi dan Logika
# Angka > 3 dan Angka < 7

inputUser = float(input("Masukkan angka: "))

isKurangDari = inputUser > 3
isLebihDari = inputUser < 7

print("Kurang dari 3:", isKurangDari)
print("Lebih dari 7:", isLebihDari)

hasil = isKurangDari and isLebihDari

print(f"Hasil komparasi {isKurangDari} and {isLebihDari}: {hasil}")
# 2.  Soal 2: Buat logika untuk rentang `+++++ 0 ----- 5 +++++ 8 ----- 11 +++++`.
#     Angka harus: (`< 0`) ATAU (`> 5` DAN `< 8`) ATAU (`> 11`).

print("Soal 2")
print("------- Rentang +++++ 0 ----- 5 +++++ 8 ----- 11 +++++")
print(55*"=")

inputUser = float(input("Masukkan angka: "))

isKurangDariNol = inputUser < 0
isLebihDariLima = inputUser > 5
isKurangDariDelapan = inputUser < 8
isLebihDariSebelas = inputUser > 11

print("Kurang dari 0:", isKurangDariNol)
print("Lebih dari 5:", isLebihDariLima)
print("Kurang dari 8:", isKurangDariDelapan)
print("Lebih dari 11:", isLebihDariSebelas)

hasilSoal2 = (isKurangDariNol or (isLebihDariLima and isKurangDariDelapan)) or isLebihDariSebelas

print(f"Hasil komparasi ({isKurangDariNol} or ({isLebihDariLima} and {isKurangDariDelapan})) or {isLebihDariSebelas}: {hasilSoal2}")
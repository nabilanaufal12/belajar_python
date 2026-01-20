# 1.  Soal 1: Buat logika untuk rentang `----- 0 +++++ 5 ----- 8 +++++ 11 -----`.
#     Angka harus: (`> 0` DAN `< 5`) ATAU (`> 8` DAN `< 11`).

print("Soal 1")
print("------- Rentang ----- 0 +++++ 5 ----- 8 +++++ 11 -----")
print(55*"=")

inputUser = float(input("Masukkan angka: "))

isLebihDariNol = inputUser > 0
isKurangDariLima = inputUser < 5
isLebihDariDelapan = inputUser > 8
isKurangDariSebelas = inputUser < 11

print("Lebih dari 0:", isLebihDariNol)
print("Kurang dari 5:", isKurangDariLima)
print("Lebih dari 8:", isLebihDariDelapan)
print("Kurang dari 11:", isKurangDariSebelas)

hasilSoal1 = (isLebihDariNol and isKurangDariLima) or (isLebihDariDelapan and isKurangDariSebelas)

print(f"Hasil komparasi ({isLebihDariNol} and {isKurangDariLima}) or ({isLebihDariDelapan} and {isKurangDariSebelas}): {hasilSoal1}")
# Fungsi Lambda dan Anonymous Function di Python

# Perbandingan dengan Fungsi def Biasa
def kuadrat(angka):
    return angka ** 2
print(kuadrat(5))

kuadrat = lambda angka: angka ** 2
print(kuadrat(4))

# Contoh dengan Banyak Argumen
pangkat = lambda num, pow: num ** pow
print(pangkat(3, 3))

# Kegunaan Fungsi Lambda
## 1. Sorting List
data_list = ["Miwaa", "Mika", "Mizuuu"]
data_list.sort(key=lambda nama: len(nama))
print(data_list)

## 2. Filtering List
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_kecil = list(filter(lambda x: x<5, data_angka))
print(data_kecil)

data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(data_genap)

data_ganjil = list(filter(lambda x: (x % 2 == 1) or (x % 2 != 0), data_angka))
print(data_ganjil)

data_kelipatan3 = list(filter(lambda x: (x % 3 == 0), data_angka))
print(data_kelipatan3)

## 3. Anonymous Function (Currying)
def pangkat(n):
    return lambda angka: angka ** n

pangkat2 = pangkat(2)
print(pangkat2(5))

pangkat2 = pangkat(4)
print(pangkat2(2))
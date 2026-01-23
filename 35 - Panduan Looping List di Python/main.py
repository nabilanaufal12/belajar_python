# Panduan Looping List di Python

# 1. For Loop Biasa (Standard)
kumpulan_angka = [1, 2, 3, 4, 5]
for num in kumpulan_angka:
    print(f"Angka: {num}")

peserta = ["Andi", "Budi", "Citra"]
for nama in peserta:
    print(f"Peserta: {nama}")

# 2. For Loop dengan range() dan len()
panjang_list = len(kumpulan_angka)
for i in range(panjang_list):
    print(f"Indeks {i} memiliki nilai {kumpulan_angka[i]}")

# 3. While Loop
index = 0
while index < len(peserta):
    print(f"Peserta ke-{index + 1}: {peserta[index]}")
    index += 1

# 4. List Comprehension
kuadrat_angka = [x**2 for x in kumpulan_angka]
print(f"Kuadrat Angka: {kuadrat_angka}")

data_list = ["Andi", 25, "Budi", 30, "Citra", 22]
[print(f"Data: {item}") for item in data_list]

# 5. enumerate()
for idx, data in enumerate(data_list):
    print(f"Indeks {idx}: {data}")
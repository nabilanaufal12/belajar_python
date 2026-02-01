# Tipe Koleksi Data Python: Tuples dan Sets

data_tuple = (1, 2, 3, 4, 5)
print("Tuple:", data_tuple)
print("Elemen pertama dari tuple:", data_tuple[0])
print("Panjang tuple:", len(data_tuple))

data_set = {1, 2, 3, 4, 5}
print("Set:", data_set)
data_set.add(6)
print("Set setelah menambahkan elemen 6:", data_set)
data_set.remove(3)
print("Set setelah menghapus elemen 3:", data_set)
print("Apakah 4 ada di set?", 4 in data_set)
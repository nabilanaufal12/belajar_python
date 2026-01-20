# Deep Copy untuk Nested List di Python

# Memahami Nested List
data_0 = [1, 2]
data_1 = [3, 4]

data_nested = [data_0, data_1, 5, 6]
print("Nested List Awal:", data_nested)

# Shallow Copy dengan .copy()

## Bukti Kegagalan Shallow Copy
data_shallow = data_nested.copy()
print("Shallow Copy dari Nested List:", data_shallow)
print()

print(f"ID Nested List Asli: {hex(id(data_nested))}")
print(f"ID Nested List Shallow Copy: {hex(id(data_shallow))}\n")

print(f"ID Elemen Pertama Nested List Asli: {hex(id(data_nested[0]))}")
print(f"ID Elemen Pertama Nested List Shallow Copy: {hex(id(data_shallow[0]))}\n")

## Konsekuensi Shallow Copy
data_shallow[0][0] = 999
print("Setelah Modifikasi pada Shallow Copy:")
print("Nested List Asli:", data_nested)
print("Nested List Shallow Copy:", data_shallow)
print()

# Deep Copy dengan deepcopy()

## Implementasi Deep Copy
from copy import deepcopy

data_deep = deepcopy(data_nested)
print(f"ID Nested List Deep Copy: {hex(id(data_deep))}\n")
print()

## Manfaat Deep Copy
data_deep[0][0] = 555
print("Setelah Modifikasi pada Deep Copy:")
print("Nested List Asli:", data_nested)
print("Nested List Deep Copy:", data_deep)
# Belajar Python: Copy & Pop Dictionary

# 1. Perbedaan Assignment (=) dan Method .copy()

## 1.1. Assignment Langsung (=)
data_asli = {
    'nama': 'Andi',
    'umur': 25,
    'kota': 'Jakarta'
}

data_copy = data_asli
data_copy['nama'] = 'Budi'

print("Data Asli:", data_asli)
print("Data Copy:", data_copy)

## 1.2. Method .copy()
data_asli = {
    'nama': 'Andi',
    'umur': 25,
    'kota': 'Jakarta'
}

data_copy = data_asli.copy()
data_copy['nama'] = 'Budi'

print("Data Asli:", data_asli)
print("Data Copy:", data_copy)

# 2. Method .pop() Dictionary
data = {
    'nama': 'Andi',
    'umur': 25,
    'kota': 'Jakarta'
}

nilai_dihapus = data.pop('umur')
print("Data setelah pop:", data)
print("Nilai yang dihapus:", nilai_dihapus)

# 3. Method .popitem() Dictionary
data = {
    'nama': 'Andi',
    'umur': 25,
    'kota': 'Jakarta'
}
item_dihapus = data.popitem()
print("Data setelah popitem:", data)
print("Item yang dihapus:", item_dihapus)
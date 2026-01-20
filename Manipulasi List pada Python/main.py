# Manipulasi List pada Python

# Membuat List
data = ["apel", "jeruk", "mangga"]
print(f"Data awal: {data}")

# 1. Pengambilan Data (Indexing)

print(f"data[0] = {data[0]}")  # Output: apel
print(f"data[1] = {data[1]}")  # Output: jeruk
print(f"data[-1] = {data[-1]}")  # Output: mangga

# 2. Mendapatkan Informasi List
print(f"Jumlah data dalam list: {len(data)}")  # Output: 3

# 3. Menambah Data ke List

## a. insert(posisi, item)
data.insert(1, "semangka")
print(f"Setelah insert: {data}")  # Output: ['apel', 'semangka', 'jeruk', 'mangga']

## b. append(item)
data.append("pisang")
print(f"Setelah append: {data}")  # Output: ['apel', 'semangka', 'jeruk', 'mangga', 'pisang']

## c. extend(iterable)
data.extend(["kiwi", "nanas"])
print(f"Setelah extend: {data}")  # Output: ['apel', 'semangka', 'jeruk', 'mangga', 'pisang', 'kiwi', 'nanas']

# 4. Mengubah Data dalam List
data[2] = "anggur"
print(f"Setelah mengubah data[2]: {data}")  # Output: ['apel', 'semangka', 'anggur', 'mangga', 'pisang', 'kiwi', 'nanas']

# 5. Menghapus Data dari List

## a. remove(item)
data.remove("semangka")
print(f"Setelah remove: {data}")  # Output: ['apel', 'anggur', 'mangga', 'pisang', 'kiwi', 'nanas']

## b. pop(index)
removed_item = data.pop(3)
print(f"Setelah pop: {data}, item yang dihapus: {removed_item}")  # Output: ['apel', 'anggur', 'mangga', 'kiwi', 'nanas']
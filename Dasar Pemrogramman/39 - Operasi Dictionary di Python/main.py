# Operasi Dictionary di Python

# 1. Mendapatkan Panjang Dictionary (len())
data_buah = {
    'apel': 10,
    'pisang': 20,
    'jeruk': 15
}
print("Data Buah:", data_buah)
panjang_dict = len(data_buah)
print(f"Panjang dictionary: {panjang_dict}")

# 2. Mengecek Keberadaan Kunci (in)
print("Apakah 'apel' ada dalam dictionary?", 'apel' in data_buah)  # True
print("Apakah 'mangga' ada dalam dictionary?", 'mangga' in data_buah)  # False

# 3. Mengakses Nilai (Value) Dictionary

## a. Akses Langsung (nama_dictionary['kunci'])
apel_count = data_buah['apel']
print(f"Jumlah apel: {apel_count}")

## b. Menggunakan Metode .get()
jeruk_count = data_buah.get('jeruk')
print(f"Jumlah jeruk: {jeruk_count}")

# 4. Memperbarui dan Menambah Data

## a. Penugasan Langsung (nama_dictionary['kunci'] = nilai)
data_buah['pisang'] = 25  # Memperbarui jumlah pisang
data_buah['mangga'] = 30   # Menambah data mangga
print("Data Buah setelah pembaruan dan penambahan:", data_buah)

## b. Menggunakan Metode .update()
data_buah.update({'kiwi': 12, 'apel': 15})  # Menambah kiwi dan memperbarui apel
print("Data Buah setelah update:", data_buah)

# 5. Menghapus Data (del)
del data_buah['jeruk']  # Menghapus jeruk dari dictionary
print("Data Buah setelah penghapusan jeruk:", data_buah)
# Summary Manipulasi List Pyth

> Generated: January 20th, 2026 12:20 PM
> Sources: Belajar Python [Dasar] - 30 - Manipulasi List.youtube, pasted-text-1.md

---

# Manipulasi List pada Python

List adalah salah satu struktur data fundamental di Python yang memungkinkan penyimpanan koleksi item. Operasi manipulasi list sangat penting untuk mengelola dan memproses data secara efisien.

## 1. Pengambilan Data (Indexing)

Pengambilan data dari list dilakukan menggunakan **indeks**, yang merupakan posisi item dalam list.
*   Indeks dimulai dari `0` untuk elemen pertama.
*   Indeks negatif dapat digunakan untuk mengakses elemen dari akhir list, di mana `-1` merujuk pada elemen terakhir, `-2` pada elemen kedua terakhir, dan seterusnya.

Untuk mengambil data, gunakan sintaks `data[index]`"].

```python
data = ["Ucup", "Otong", "Dudung"]

# Mengambil data pertama (indeks 0)
data_pertama = data[0]
print(f"Data pertama (index 0) adalah: {data_pertama}") # Output: Ucup

# Mengambil data terakhir (indeks -1)
data_terakhir = data[-1]
print(f"Data terakhir adalah: {data_terakhir}") # Output: Dudung

# Mengambil data kedua dari belakang (indeks -2)
data_kedua_terakhir = data[-2]
print(f"Data kedua terakhir adalah: {data_kedua_terakhir}") # Output: Otong
```

## 2. Mendapatkan Informasi List

Untuk mengetahui jumlah elemen atau panjang list, gunakan fungsi `len()`.

```python
data = ["Ucup", "Otong", "Dudung"]
panjang_data = len(data)
print(f"Panjang data adalah: {panjang_data}") # Output: 3
```

## 3. Menambah Data ke List

Ada beberapa cara untuk menambahkan item ke dalam list:

### a. `insert(posisi, item)`
Metode `.insert()` digunakan untuk menambahkan item pada posisi (indeks) tertentu dalam list. Item yang sudah ada di posisi tersebut dan setelahnya akan digeser ke kanan.

```python
data = ["Ucup", "Otong", "Dudung"]
print(f"Data sebelum insert: {data}") # Output: ['Ucup', 'Otong', 'Dudung']

data.insert(1, "Asep") # Masukkan "Asep" di indeks 1
print(f"Data sesudah insert(1, 'Asep'): {data}") # Output: ['Ucup', 'Asep', 'Otong', 'Dudung']
```

### b. `append(item)`
Metode `.append()` digunakan untuk menambahkan item baru di **akhir** list.

```python
data = ["Ucup", "Asep", "Otong", "Dudung"]
print(f"Data sebelum append: {data}")

data.append("Jajang") # Tambahkan "Jajang" di akhir list
print(f"Data sesudah append('Jajang'): {data}") # Output: ['Ucup', 'Asep', 'Otong', 'Dudung', 'Jajang']
```

### c. `extend(list_baru)`
Metode `.extend()` digunakan untuk menggabungkan item-item dari list lain ke dalam list yang sudah ada. Item-item dari `list_baru` akan ditambahkan di akhir list utama.

```python
data = ["Ucup", "Asep", "Otong", "Dudung", "Jajang"]
data_baru = ["Ujang", "Usep", "Dadang"]
print(f"Data sebelum extend: {data}")
print(f"List yang akan digabungkan: {data_baru}")

data.extend(data_baru) # Gabungkan data_baru ke data
print(f"Data sesudah extend: {data}") # Output: ['Ucup', 'Asep', 'Otong', 'Dudung', 'Jajang', 'Ujang', 'Usep', 'Dadang']
```

## 4. Mengubah Data dalam List

Untuk mengubah data yang sudah ada, akses item menggunakan indeksnya, lalu berikan nilai baru.

```python
data = ["Ucup", "Asep", "Otong", "Dudung", "Jajang", "Ujang", "Usep", "Dadang"]
print(f"Data sebelum diubah: {data}")

data[2] = "Michael" # Ubah item di indeks 2 (Otong) menjadi "Michael"
print(f"Data sesudah ubah index 2 jadi Michael: {data}") # Output: ['Ucup', 'Asep', 'Michael', 'Dudung', 'Jajang', 'Ujang', 'Usep', 'Dadang'] = \"Michael\""]
```

## 5. Menghapus Data dari List

Ada dua metode utama untuk menghapus item dari list:

### a. `remove(item)`
Metode `.remove()` menghapus item pertama yang ditemukan dengan nilai yang cocok dari list.
*   Jika item yang ingin dihapus tidak ada dalam list, Python akan mengeluarkan `ValueError`.
*   Metode ini bersifat *case-sensitive*, artinya harus sama persis (huruf besar/kecil) dengan nilai item di list.

```python
data = ["Ucup", "Asep", "Michael", "Dudung", "Jajang", "Ujang", "Usep", "Dadang"]
print(f"Data sebelum remove: {data}")

data.remove("Ujang") # Hapus item dengan nilai "Ujang"
print(f"Data sesudah remove('Ujang'): {data}") # Output: ['Ucup', 'Asep', 'Michael', 'Dudung', 'Jajang', 'Usep', 'Dadang']

# Contoh jika item tidak ada (akan error)
# data.remove("Yujeng") # Ini akan menyebabkan ValueError jika "Yujeng" tidak ada
```

### b. `pop()`
Metode `.pop()` menghapus dan mengembalikan item **terakhir** dari list secara *default*. Jika indeks diberikan sebagai argumen (misalnya `data.pop(index)`), maka item pada indeks tersebut yang akan dihapus dan dikembalikan.

```python
data = ["Ucup", "Asep", "Michael", "Dudung", "Jajang", "Usep", "Dadang"]
print(f"Data sebelum pop: {data}")

data_terhapus = data.pop() # Hapus dan ambil item terakhir
print(f"Data akhir yang dihapus (pop): {data_terhapus}") # Output: Dadang
print(f"Data akhir sekarang: {data}") # Output: ['Ucup', 'Asep', 'Michael', 'Dudung', 'Jajang', 'Usep']
```

## Contoh Kode Lengkap (Rangkuman)

Berikut adalah rangkuman semua operasi manipulasi list dalam satu blok kode:

```python
# 1. Operasi Dasar
data = ["Ucup", "Otong", "Dudung"]
print(f"Data Awal = \n{data}")

data_0 = data[0]
print(f"Data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"Data terakhir = {data_terakhir}")

panjang_data = len(data)
print(f"Panjang data = {panjang_data} \n")

# 2. Manipulasi Data List
print(f"Data Sebelum Ditambah = \n{data}")

# Insert (Menambah di posisi tertentu)
data.insert(1, "Asep")
print(f"Data sesudah insert(1, 'Asep') = \n{data}")

# Append (Menambah di akhir)
data.append("Jajang")
print(f"Data sesudah append('Jajang') = \n{data}")

# Extend (Menggabungkan List)
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"Data sesudah extend = \n{data}")

# Ubah Data
data[2] = "Michael"
print(f"Data sesudah ubah index 2 jadi Michael = \n{data}")

# Remove (Hapus berdasarkan nilai)
data.remove("Ujang")
print(f"Data sesudah remove('Ujang') = \n{data}")

# Pop (Hapus data paling akhir)
data_terakhir = data.pop()
print(f"Data akhir yang dihapus (pop) = {data_terakhir}")
print(f"Data akhir sekarang = \n{data}")
```
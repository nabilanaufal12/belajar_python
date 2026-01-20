# Deep Copy untuk Nested List di Python

## Pendahuluan

Dalam pemrograman Python, menyalin objek seperti list adalah operasi umum. Namun, ketika berhadapan dengan **nested list** (list di dalam list), metode penyalinan standar (`.copy()`) dapat menimbulkan perilaku yang tidak terduga. Tutorial ini akan menjelaskan perbedaan antara *shallow copy* dan *deep copy*, serta kapan harus menggunakan masing-masing, khususnya untuk struktur data list bersarang.

## Memahami Nested List

**Nested list** adalah list yang elemen-elemennya juga berupa list. Selain itu, sebuah nested list juga bisa berisi elemen non-list (misalnya, angka atau string).

Contoh nested list:
```python
data_0 = [1, 2]
data_1 = [3, 4]
data_2D = [data_0, data_1, 10]
# data_2D sekarang adalah [[1, 2], [3, 4], 10]
```
Untuk mengakses elemen dalam nested list, kita menggunakan indeks bertingkat. Misalnya, `data_2D[0]` akan mengembalikan `[1, 2]`, dan `data_2D[0][0]` akan mengembalikan `1`.

## Shallow Copy dengan `.copy()`

Metode `list.copy()` digunakan untuk membuat salinan list. Untuk list sederhana (yang hanya berisi elemen non-list), metode ini bekerja dengan baik, menghasilkan salinan independen.

Namun, untuk nested list, `list.copy()` hanya melakukan **shallow copy** (salinan dangkal). Ini berarti:
1.  **List Utama Disalin**: List terluar (`data_2D`) akan memiliki alamat memori yang berbeda dari salinannya (`data_2D_copy`).
2.  **List Bersarang Tidak Disalin**: Elemen-elemen yang berupa list di dalamnya (misalnya `data_0` dan `data_1` dalam `data_2D`) tidak disalin secara independen. Sebaliknya, `data_2D_copy` akan menyimpan *referensi* ke objek list yang sama dengan yang ada di `data_2D`.

### Bukti Kegagalan Shallow Copy

Kita dapat memverifikasi ini dengan memeriksa ID memori (`id()`) dari objek list:

```python
data_0 = [1, 2]
data_1 = [3, 4]
data_2D = [data_0, data_1, 10]

data_2D_copy = data_2D.copy()

print(f"ID data_2D: {hex(id(data_2D))}")
print(f"ID data_2D_copy: {hex(id(data_2D_copy))}")
# Output: ID berbeda untuk list utama

print(f"ID member pertama data_2D: {hex(id(data_2D[0]))}")
print(f"ID member pertama data_2D_copy: {hex(id(data_2D_copy[0]))}")
# Output: ID yang SAMA untuk list bersarang
```

### Konsekuensi Shallow Copy

Karena list bersarang dalam salinan dangkal masih merujuk ke objek yang sama dengan list aslinya, mengubah elemen dalam list bersarang pada salah satu versi akan memengaruhi versi lainnya.

```python
data_0 = [1, 2]
data_1 = [3, 4]
data_2D = [data_0, data_1, 10]
data_2D_copy = data_2D.copy() # Shallow Copy

print(f"Sebelum diubah:")
print(f"data asli = {data_2D}") # [[1, 2], [3, 4], 10]
print(f"data copy = {data_2D_copy}") # [[1, 2], [3, 4], 10]

# Mengubah elemen dalam list bersarang
data_2D[1][0] = 5

print(f"\nSetelah mengubah list bersarang:")
print(f"data asli = {data_2D}") # [[1, 2], [5, 4], 10]
print(f"data copy = {data_2D_copy}") # [[1, 2], [5, 4], 10] <-- Ikut berubah!

# Mengubah elemen non-list
data_2D[2] = 9

print(f"\nSetelah mengubah elemen non-list:")
print(f"data asli = {data_2D}") # [[1, 2], [5, 4], 9]
print(f"data copy = {data_2D_copy}") # [[1, 2], [5, 4], 10] <-- Tidak berubah!
```
Perhatikan bahwa perubahan pada elemen non-list (angka `10` menjadi `9`) hanya memengaruhi list asli, karena `10` adalah objek yang tidak dapat diubah (immutable) dan disalin nilainya, bukan referensinya.

## Deep Copy dengan `deepcopy()`

Untuk mengatasi masalah shallow copy pada nested list, kita perlu melakukan **deep copy** (salinan mendalam). Deep copy akan membuat salinan independen dari list utama *dan semua elemen bersarangnya secara rekursif*.

Untuk melakukan deep copy, kita harus mengimpor fungsi `deepcopy` dari modul `copy`.

### Implementasi Deep Copy

```python
from copy import deepcopy

data_0 = [1, 2]
data_1 = [3, 4]
data_2D = [data_0, data_1, 10]

data_2D_deepcopy = deepcopy(data_2D)

print(f"ID member pertama data_2D: {hex(id(data_2D[0]))}")
print(f"ID member pertama data_2D_deepcopy: {hex(id(data_2D_deepcopy[0]))}")
# Output: ID yang BERBEDA untuk list bersarang
```

### Manfaat Deep Copy

Dengan deep copy, perubahan pada list asli tidak akan memengaruhi salinannya, karena semua elemen, termasuk list bersarang, adalah objek yang sepenuhnya independen.

```python
from copy import deepcopy

data_0 = [1, 2]
data_1 = [3, 4]
data_2D = [data_0, data_1, 10] # Reset data untuk demonstrasi
data_2D_deepcopy = deepcopy(data_2D)

print(f"Sebelum diubah:")
print(f"data asli = {data_2D}") # [[1, 2], [3, 4], 10]
print(f"data deep = {data_2D_deepcopy}") # [[1, 2], [3, 4], 10]

# Mengubah elemen dalam list bersarang pada data asli
data_2D[1][0] = 30

print(f"\nSetelah mengubah list bersarang:")
print(f"data asli = {data_2D}") # [[1, 2], [30, 4], 10]
print(f"data deep = {data_2D_deepcopy}") # [[1, 2], [3, 4], 10] <-- Tetap aman!
```

## Kesimpulan

Penting untuk memahami perbedaan antara shallow copy dan deep copy saat bekerja dengan struktur data kompleks seperti nested list:
*   Gunakan `list.copy()` (shallow copy) jika list Anda hanya berisi elemen-elemen non-list (misalnya, angka, string) atau jika Anda memang ingin salinan berbagi referensi ke objek bersarang yang sama.
*   Gunakan `copy.deepcopy()` (deep copy) jika list Anda adalah **nested list** dan Anda ingin salinan yang sepenuhnya independen, di mana perubahan pada list asli tidak akan memengaruhi salinannya, dan sebaliknya.

Dengan menggunakan `deepcopy`, Anda dapat menghindari efek samping yang tidak diinginkan saat memanipulasi salinan nested list.
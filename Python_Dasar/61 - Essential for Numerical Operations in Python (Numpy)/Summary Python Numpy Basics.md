# Numpy: Fondasi untuk Operasi Matematika dan Matriks di Python

## Pendahuluan
**Numpy** (Numerical Python) adalah salah satu *package* paling populer dan berjasa di Python, khususnya untuk operasi matematika dan matriks. Ia menjadi fondasi penting dalam bidang *Data Science* dan *Machine Learning* karena kemampuannya dalam melakukan komputasi numerik yang efisien.

## Instalasi dan Importasi

### Instalasi Numpy
Sebelum menggunakan Numpy, pastikan `pip` sudah terinstal di sistem Anda. Instalasi dilakukan melalui terminal dengan perintah berikut:
```bash
pip install numpy
```
Anda dapat memverifikasi instalasi *package* yang ada dengan `pip list` atau `pip3 list`.

### Importasi Numpy
Setelah terinstal, Numpy dapat diimpor ke dalam kode Python Anda. Standar praktik adalah mengimpornya dengan alias `np` untuk memudahkan penulisan kode.
```python
import numpy as np
```

## Membuat Array (Vektor dan Matriks)

Numpy memperkenalkan struktur data **Array**, yang merupakan fondasi untuk representasi vektor dan matriks.

### Membuat Vektor (Array 1D)
Vektor atau *Array 1 Dimensi* dapat dibuat menggunakan fungsi `np.array()`, dengan memasukkan *list* Python sebagai argumen.)"]
```python
vector_a = np.array([1, 2, 3, 4])
print(f"Vector A : {vector_a}")
# Output: Vector A : [1 2 3 4]
```

#### Perbedaan Numpy Array dengan List Python
Meskipun sama-sama menampung koleksi data, Numpy Array memiliki beberapa perbedaan fundamental dengan *list* Python biasa:
*   **Tampilan**: Saat dicetak, Numpy Array terlihat lebih rapi tanpa koma antar elemen, menyerupai representasi vektor matematis.
*   **Operasi Matematika**: Ini adalah keunggulan utama Numpy. Numpy Array memungkinkan operasi matematika dilakukan secara **element-wise** (per elemen) secara langsung.
    *   **Pengkuadratan**: Mengkuadratkan Numpy Array akan mengkuadratkan setiap elemennya. Sementara itu, mengkuadratkan *list* Python (`list**2`) akan menghasilkan *error*.
    *   **Perkalian Skalar**: Mengalikan Numpy Array dengan skalar akan mengalikan setiap elemennya dengan skalar tersebut. Mengalikan *list* Python dengan bilangan bulat akan menduplikasi isi *list* tersebut.

```python
list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

# Operasi pengkuadratan
# print(list_a ** 2) # Akan ERROR
print(f"Vector A kuadrat : {vector_a**2}") # Output: [ 1  4  9 16]

# Operasi perkalian skalar
print(f"List A * 2       : {list_a*2}") # Output: [1, 2, 3, 4, 1, 2, 3, 4]
print(f"Vector A * 5     : {vector_a*5}") # Output: [ 5 10 15 20]
```

### Membuat Matriks (Array 2D)
Matriks atau *Array 2 Dimensi* dapat dibuat dengan `np.array()` menggunakan *list* bersarang (nested list) sebagai argumen, di mana setiap *list* bagian dalam merepresentasikan satu baris matriks.)"]
```python
matrix_b = np.array([(1, 2), (3, 4)])
print(f"\nMatrix B:\n{matrix_b}")
# Output:
# Matrix B:
# [[1 2]
#  [3 4]]
```
Operasi matematika *element-wise* juga berlaku untuk matriks.
```python
print(f"Matrix B kuadrat:\n{matrix_b**2}")
# Output:
# Matrix B kuadrat:
# [[ 1  4]
#  [ 9 16]]
```

## Fungsi Pembantu untuk Membuat Matriks Khusus

Numpy menyediakan fungsi-fungsi praktis untuk membuat matriks dengan nilai-nilai spesifik:

*   `np.zeros((dimensi))`: Membuat matriks yang semua elemennya bernilai nol. Dimensi matriks diberikan dalam bentuk *tuple* (baris, kolom).
    ```python
    zeros_c = np.zeros((2, 2))
    print(f"\nZeros C:\n{zeros_c}")
    # Output:
    # Zeros C:
    # [[0. 0.]
    #  [0. 0.]]
    ```
*   `np.ones((dimensi))`: Membuat matriks yang semua elemennya bernilai satu.
    ```python
    ones_d = np.ones((2, 2))
    print(f"\nOnes D:\n{ones_d}")
    # Output:
    # Ones D:
    # [[1. 1.]
    #  [1. 1.]]
    ```

## Operasi Aritmatika Matriks

Numpy menyederhanakan operasi aritmatika antar matriks. Penjumlahan, pengurangan, perkalian, dan pembagian matriks dilakukan secara *element-wise* jika dimensinya sesuai.
```python
# Contoh penjumlahan matriks
jumlah = matrix_b + matrix_b**2 + ones_d
print(f"\nHasil Penjumlahan Matrix:\n{jumlah}")
# Output:
# Hasil Penjumlahan Matrix:
# [[ 3.  7.]
#  [13. 21.]]
```
Kemudahan dalam melakukan operasi matriks ini menjadikan Numpy sangat berguna untuk tugas-tugas komputasi numerik yang kompleks, terutama dalam pengembangan model *Data Science* dan *Machine Learning*.
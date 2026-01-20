# Summary Python List Dasar

> Generated: January 20th, 2026 11:48 AM
> Sources: Belajar Python [Dasar] - 29 - List.youtube, pasted-text-1.md

---

# Pengenalan List di Python

List adalah salah satu struktur data fundamental di Python yang berfungsi sebagai **kumpulan data** atau koleksi elemen. Berbeda dengan beberapa bahasa pemrograman lain yang mengenal istilah *array*, Python secara bawaan menggunakan List untuk tujuan serupa. List sangat fleksibel karena dapat menampung berbagai tipe data sekaligus dalam satu koleksi.

## Cara Membuat List

Ada beberapa metode untuk membuat List di Python, mulai dari cara manual hingga yang lebih canggih menggunakan *list comprehension*.

### 1. Membuat List Secara Manual (Menggunakan Kurung Siku `[]`)

List dibuat dengan menempatkan elemen-elemen di dalam **kurung siku `[]`**, dipisahkan oleh koma.

*   **Kumpulan Angka (Numbers)**: List dapat berisi angka integer atau float.
    ```python
    data_angka = [1, 2, 3, 5]
    print(data_angka) # Output: [1, 2, 3, 5]
    ```

*   **Kumpulan String**: List juga dapat berisi teks atau string.
    ```python
    data_string = ["Ucok", "Otong", "Odah"]
    print(data_string) # Output: ['Ucok', 'Otong', 'Odah']
    ```

*   **Kumpulan Boolean**: List bisa menampung nilai boolean (`True` atau `False`).
    ```python
    data_boolean = [True, False, True, True]
    print(data_boolean) # Output: [True, False, True, True]
    ```

*   **Kumpulan Campuran (Mixed Data Types)**: Salah satu keunggulan List Python adalah kemampuannya menampung berbagai tipe data (angka, string, boolean, dll.) dalam satu List yang sama.
    ```python
    data_campuran = [1, "bala-bala", 2, "cireng", "Ucup", True, False]
    print(data_campuran) # Output: [1, 'bala-bala', 2, 'cireng', 'Ucup', True, False]
    ```

### 2. Membuat List Menggunakan Fungsi `range()`

Fungsi `range()` digunakan untuk menghasilkan urutan angka. Secara default, `range()` akan menghasilkan objek `range`, bukan List secara langsung. Untuk mengubahnya menjadi List, kita perlu mengkonversinya menggunakan fungsi `list()`.

Sintaks `range()` adalah `range(start, stop, step)`:
*   `start`: Angka awal (inklusif, default 0).
*   `stop`: Angka akhir (eksklusif).
*   `step`: Selisih antar angka (default 1).

Contoh:
```python
data_range_obj = range(0, 10) # range dari 0 sampai sebelum 10 (0-9)
print(data_range_obj) # Output: range(0, 10) - masih objek range

data_list_dari_range = list(data_range_obj)
print(data_list_dari_range) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dengan step
data_range_step = range(0, 10, 2) # range dari 0 sampai sebelum 10, dengan step 2
data_list_step = list(data_range_step)
print(data_list_step) # Output: [0, 2, 4, 6, 8]
```

### 3. Membuat List Menggunakan List Comprehension

**List Comprehension** adalah cara yang ringkas dan efisien untuk membuat List baru dari List atau *iterable* lainnya. Ini memungkinkan kita untuk membuat List menggunakan *for loop* dalam satu baris kode.

*   **List Comprehension Dasar (dengan `for` loop)**
    Sintaks umumnya adalah `[ekspresi for item in iterable]`.
    ```python
    list_pake_for = [i for i in range(0, 10)] # Membuat list dari 0-9
    print(list_pake_for) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

*   **List Comprehension dengan Operasi**
    Kita bisa menerapkan operasi matematika atau fungsi pada setiap elemen saat membuat List.
    ```python
    # Membuat list kuadrat dari angka 0-9
    list_kuadrat = [i**2 for i in range(0, 10)]
    print(list_kuadrat) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # Membuat list pangkat tiga dari angka 0-9
    list_pangkat_tiga = [i**3 for i in range(0, 10)]
    print(list_pangkat_tiga) # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
    ```

*   **List Comprehension dengan Kondisi `if` (Filter)**
    List comprehension juga dapat menyertakan kondisi `if` untuk memfilter elemen yang akan dimasukkan ke dalam List baru. Sintaksnya menjadi `[ekspresi for item in iterable if kondisi]`.

    *   **Menghilangkan Elemen Tertentu**:
        ```python
        # Membuat list dari 0-9, kecuali angka 5
        list_tanpa_lima = [i for i in range(0, 10) if i != 5]
        print(list_tanpa_lima) # Output: [0, 1, 2, 3, 4, 6, 7, 8, 9]
        ```

    *   **Membuat List Bilangan Genap**:
        ```python
        # Membuat list bilangan genap dari 0-9
        list_genap = [i for i in range(0, 10) if i % 2 == 0]
        print(list_genap) # Output: [0, 2, 4, 6, 8]
        ```

    *   **Membuat List Bilangan Ganjil (dan Operasi Kuadrat)**:
        ```python
        # Membuat list bilangan ganjil dari 0-9
        list_ganjil = [i for i in range(0, 10) if i % 2 != 0]
        print(list_ganjil) # Output: [1, 3, 5, 7, 9]

        # Membuat list kuadrat dari bilangan ganjil 0-9
        list_ganjil_kuadrat = [i**2 for i in range(0, 10) if i % 2 != 0]
        print(list_ganjil_kuadrat) # Output: [1, 9, 25, 49, 81]
        ```

## Kesimpulan

List adalah struktur data yang sangat penting di Python untuk mengelola koleksi data. Kita dapat membuat List dengan berbagai cara:
*   Secara manual menggunakan kurung siku `[]` untuk data angka, string, boolean, atau campuran.
*   Menggunakan fungsi `range()` yang kemudian dikonversi menjadi List dengan `list()`.
*   Menggunakan **List Comprehension** yang powerful untuk membuat List secara ringkas, termasuk dengan operasi dan kondisi `if` untuk filtering.

## Materi Selanjutnya

Setelah memahami cara membuat List, langkah selanjutnya adalah mempelajari **manipulasi List**, seperti menambah, menghapus, atau mengubah elemen di dalamnya.
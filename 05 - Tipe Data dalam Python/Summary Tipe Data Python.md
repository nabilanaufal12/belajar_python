# Tipe Data dalam Python

Python adalah bahasa pemrograman yang secara otomatis mendeteksi dan mengelola tipe data, sehingga tidak memerlukan deklarasi eksplisit seperti bahasa pemrograman lain. **Tipe data** adalah klasifikasi yang menentukan jenis nilai yang dapat disimpan oleh suatu variabel, serta operasi apa saja yang dapat dilakukan padanya.

Berikut adalah berbagai tipe data yang tersedia di Python:

## Tipe Data Standar

### Integer (Bilangan Bulat)
**Integer** adalah tipe data untuk angka satuan atau bilangan bulat yang tidak memiliki bagian desimal atau koma.
*   **Contoh**: `1`, `10`, `145`, `1000000`.
*   Python secara otomatis mengenali angka tanpa koma sebagai integer.
*   Untuk memeriksa tipe data, gunakan fungsi `type()`:
    ```python
    data_integer = 1
    print("data : ", data_integer)
    print("- bertipe : ", type(data_integer))
    # Output: <class 'int'>
    ```

### Float (Angka Desimal)
**Float** adalah tipe data untuk angka dengan koma atau bilangan desimal.
*   **Contoh**: `1.5`, `1.23`.
*   Di Python, semua angka desimal secara *default* dianggap sebagai float; tidak ada tipe data `double` terpisah seperti di beberapa bahasa lain.
*   Untuk memeriksa tipe data:
    ```python
    data_float = 1.5
    print("data : ", data_float)
    print("- bertipe : ", type(data_float))
    # Output: <class 'float'>
    ```

### String (Kumpulan Karakter)
**String** adalah tipe data yang merepresentasikan kumpulan karakter.
*   String didefinisikan menggunakan tanda kutip tunggal (`'`) atau ganda (`"`).
*   **Contoh**: `"Ucup"`, `"Ini adalah string"`.
*   Penting untuk diingat bahwa angka yang diapit tanda kutip (misalnya `"10"`) akan diperlakukan sebagai string, bukan sebagai nilai numerik.
*   Untuk memeriksa tipe data:
    ```python
    data_string = "Ucup"
    print("data : ", data_string)
    print("- bertipe : ", type(data_string))
    # Output: <class 'str'>
    ```

### Boolean (Biner)
**Boolean** adalah tipe data biner yang hanya memiliki dua nilai: `True` (benar) atau `False` (salah). Ini setara dengan 1 atau 0.
*   **Penulisan**: `True` dan `False` harus diawali dengan huruf kapital.
*   Jangan menggunakan tanda kutip pada nilai boolean, karena akan mengubahnya menjadi string.
*   Untuk memeriksa tipe data:
    ```python
    data_bool = True
    print("data : ", data_bool)
    print("- bertipe : ", type(data_bool))
    # Output: <class 'bool'>
    ```

## Tipe Data Khusus

### Bilangan Kompleks
Untuk kebutuhan matematika, Python mendukung tipe data **Bilangan Kompleks**.
*   Bilangan kompleks terdiri dari bagian real dan bagian imajiner, di mana bagian imajiner ditandai dengan `j`.
*   **Contoh**: `5 + 6j`.
*   Dapat dibuat menggunakan fungsi `complex(real, imaginary)`.
*   Untuk memeriksa tipe data:
    ```python
    data_complex = complex(5, 6)
    print("data : ", data_complex)
    print("- bertipe : ", type(data_complex))
    # Output: <class 'complex'>
    ```

### Tipe Data dari Bahasa C (ctypes)
Karena Python dibangun menggunakan bahasa C, dimungkinkan untuk mengimpor dan menggunakan tipe data dari bahasa C melalui modul `ctypes`.
*   Ini berguna ketika tipe data standar Python tidak cukup untuk mengakomodasi perhitungan atau kebutuhan yang sangat spesifik, seperti `double`, `char`, atau `long` dari C.
*   Membutuhkan impor eksplisit dari modul `ctypes`.
*   **Contoh**: Menggunakan `c_double` untuk representasi angka *double precision*.
    ```python
    from ctypes import c_double

    data_c_double = c_double(10.5)
    print("data : ", data_c_double)
    print("- bertipe : ", type(data_c_double))
    # Output: <class 'c_double'>
    ```

Setelah memahami berbagai tipe data ini, langkah selanjutnya adalah mempelajari **konversi tipe data** atau *casting*, yang memungkinkan perubahan satu tipe data ke tipe data lain.
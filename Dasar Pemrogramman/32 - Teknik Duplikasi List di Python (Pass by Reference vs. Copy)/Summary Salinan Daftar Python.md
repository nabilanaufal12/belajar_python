# Teknik Duplikasi List di Python: Pass by Reference vs. Copy

Catatan ini membahas berbagai metode untuk menduplikasi `list` di Python, menyoroti perbedaan krusial antara **assignment** langsung (`b = a`) dan penggunaan metode `.copy()` untuk menghindari perilaku yang tidak diinginkan saat memanipulasi data. Pemahaman ini penting untuk mengelola struktur data secara efektif dan mencegah modifikasi data yang tidak disengaja.

## 1. Assignment List (`b = a`) - Perilaku Pass by Reference

Ketika sebuah `list` di-assign ke variabel lain menggunakan operator `=`, kedua variabel tersebut tidak membuat salinan independen dari `list` tersebut. Sebaliknya, mereka akan **merujuk ke objek `list` yang sama** di memori.

*   **Contoh Awal**:
    Misalkan kita memiliki `list` `a` yang berisi `["Ucup", "Otong", "Dudung"]`. Jika kita membuat `b = a`, pada pandangan pertama, `a` dan `b` akan terlihat identik.

*   **Masalah**:
    Jika salah satu `list` (misalnya `a`) dimodifikasi, perubahan tersebut juga akan **tercermin pada `list` yang lain** (dalam hal ini `b`). Ini berlaku untuk operasi seperti mengubah elemen (`a[1] = "Michael"`) atau mengurutkan (`b.sort()`).

*   **Penjelasan (Pass by Reference)**:
    Perilaku ini terjadi karena `b = a` tidak membuat `list` baru. Sebaliknya, `b` hanya menjadi **nama lain (alias)** yang menunjuk ke **alamat memori yang sama** dengan `a`. Oleh karena itu, setiap perubahan yang dilakukan melalui `a` atau `b` akan memengaruhi objek `list` tunggal yang mereka referensikan.

*   **Pembuktian Alamat Memori**:
    Untuk memverifikasi bahwa kedua variabel merujuk ke lokasi memori yang sama, kita dapat menggunakan fungsi `id()` di Python, yang mengembalikan identitas unik dari sebuah objek (seringkali alamat memorinya).
    ```python
    a = ["Ucup", "Otong", "Dudung"]
    b = a # Pass by Reference

    print(f"address a = {hex(id(a))}")
    print(f"address b = {hex(id(b))}")
    ```
    Hasilnya akan menunjukkan bahwa `address a` dan `address b` **sama persis**, mengonfirmasi bahwa mereka adalah referensi ke objek yang sama.

## 2. Duplikasi List dengan `.copy()` - Full Duplicate (Shallow Copy)

Untuk membuat salinan `list` yang benar-benar independen, sehingga modifikasi pada satu `list` tidak memengaruhi yang lain, kita harus menggunakan metode `.copy()`.

*   **Solusi (`.copy()` Method)**:
    Metode `.copy()` adalah cara yang disarankan untuk menduplikasi `list` agar menghasilkan objek `list` baru yang terpisah di memori.
    ```python
    c = a.copy() # Membuat list baru c dengan data dari a
    ```
    Ini disebut **Full Duplicate** atau **Shallow Copy**.

*   **Mekanisme**:
    Ketika `c = a.copy()` dieksekusi, Python akan membuat objek `list` baru di lokasi memori yang berbeda. `list` baru ini akan berisi salinan elemen-elemen dari `list` asli `a`.

*   **Pembuktian Alamat Memori**:
    Setelah menggunakan `.copy()`, `list` baru (`c`) akan memiliki alamat memori yang berbeda dari `list` aslinya (`a` atau `b`).
    ```python
    print(f"address a = {hex(id(a))}")
    print(f"address b = {hex(id(b))}") # Masih sama dengan a
    print(f"address c = {hex(id(c))}") # Akan berbeda!
    ```
    `address c` akan berbeda dari `address a` dan `address b`.

*   **Demonstrasi**:
    Jika kita mengubah elemen di `list` yang disalin (`c`), perubahan tersebut **hanya akan memengaruhi `c`** dan tidak akan memengaruhi `a` atau `b` (yang masih merujuk ke objek asli).
    ```python
    # Misalkan a = ["Ucup", "Michael", "Dudung"] dan b = a
    # c = a.copy()
    # c akan berisi ["Ucup", "Michael", "Dudung"]

    c[0] = "Dadang" # Ubah index 0 di c

    # Hasil:
    # a = ["Ucup", "Michael", "Dudung"]
    # b = ["Ucup", "Michael", "Dudung"]
    # c = ["Dadang", "Michael", "Dudung"]
    ```
    Hanya `c` yang berubah menjadi 'Dadang', sementara `a` dan `b` tetap 'Ucup'.

## Kesimpulan

*   **Assignment (`b = a`)**: Hanya membuat alias atau referensi ke objek `list` yang sama. Perubahan pada satu variabel akan memengaruhi semua variabel yang merujuk ke objek tersebut (**Pass by Reference**).
*   **Metode `.copy()`**: Membuat objek `list` baru yang independen dengan alamat memori yang berbeda. Perubahan pada `list` yang disalin tidak akan memengaruhi `list` asli (**Full Duplicate** atau **Shallow Copy**).

Penting untuk selalu menggunakan `.copy()` jika Anda ingin memanipulasi `list` tanpa memengaruhi versi aslinya.

## Topik Selanjutnya

Pembahasan selanjutnya akan mengenai **Nested List** (List di dalam List), yang menghadirkan kompleksitas tambahan dalam hal duplikasi.
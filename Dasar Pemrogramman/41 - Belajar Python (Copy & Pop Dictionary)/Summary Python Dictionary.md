# Belajar Python: Copy & Pop Dictionary

Catatan ini membahas cara menyalin (copy) dictionary di Python dan dua metode untuk menghapus serta mengambil elemen dari dictionary: `.pop()` dan `.popitem()`. Pemahaman ini penting untuk mengelola struktur data dictionary secara efektif, terutama saat menghindari referensi yang tidak diinginkan dan memanipulasi data.

## 1. Perbedaan Assignment (`=`) dan Method `.copy()`

Saat bekerja dengan dictionary, penting untuk memahami perbedaan antara meng-assign dictionary ke variabel baru menggunakan operator `=` dan menyalinnya menggunakan method `.copy()`.

### 1.1. Assignment Langsung (`=`)

Jika sebuah dictionary di-assign langsung ke variabel lain menggunakan operator `=`, variabel baru tersebut tidak akan membuat salinan independen. Sebaliknya, kedua variabel akan **mereferensi objek dictionary yang sama** di memori.

*   **Implikasi**: Setiap perubahan yang dilakukan pada dictionary melalui salah satu variabel akan memengaruhi dictionary yang direferensi oleh variabel lainnya JUGA IKUT BERUBAH."].
*   **Contoh**:
    ```python
    teman_teman = {
        "cup": "ucup surucup",
        "tong": "otong surotong"
    }
    friends = teman_teman # friends dan teman_teman mereferensi objek yang sama
    friends["cup"] = "ucup si keren"
    # Sekarang, teman_teman["cup"] juga akan menjadi "ucup si keren"
    ```

### 1.2. Method `.copy()`

Untuk membuat salinan dictionary yang benar-benar independen, gunakan method `.copy()`. Method ini akan membuat objek dictionary baru di memori dengan semua pasangan *key-value* dari dictionary asli.

*   **Implikasi**: Perubahan pada dictionary hasil salinan tidak akan memengaruhi dictionary asli, dan sebaliknya TIDAK akan berubah."].
*   **Contoh**:
    ```python
    teman_teman = {
        "cup": "ucup surucup",
        "tong": "otong surotong"
    }
    friends = teman_teman.copy() # friends adalah salinan independen dari teman_teman
    friends["cup"] = "ucup si keren"
    # teman_teman["cup"] akan tetap "ucup surucup"
    # friends["cup"] akan menjadi "ucup si keren"
    ```

## 2. Method `.pop()` Dictionary

Method `.pop(key)` digunakan untuk mengambil nilai (value) yang terkait dengan kunci (key) tertentu dari dictionary, dan secara bersamaan **menghapus** pasangan *key-value* tersebut dari dictionary.

*   **Fungsi**: Seperti operasi "cut & paste" di mana data dipindahkan dari dictionary ke variabel lain.
*   **Argumen**: Membutuhkan satu argumen wajib, yaitu `key` dari elemen yang ingin diambil dan dihapus.
*   **Nilai Kembali**: Mengembalikan *value* yang terkait dengan `key` yang diberikan.
*   **Efek Samping**: Setelah `.pop()` dijalankan, `key` yang bersangkutan tidak akan lagi ada di dalam dictionary.
*   **Contoh**:
    ```python
    friends = {
        "cup": "ucup surucup",
        "sep": "asep si kasyep",
        "cuy": "ucuy surucuy"
    }
    data_asep = friends.pop("sep")
    # data_asep akan berisi "asep si kasyep"
    # friends sekarang akan menjadi {"cup": "ucup surucup", "cuy": "ucuy surucuy"}
    ```

## 3. Method `.popitem()` Dictionary

Method `.popitem()` digunakan untuk mengambil dan menghapus pasangan *key-value* **yang paling terakhir dimasukkan** ke dalam dictionary.

*   **Fungsi**: Berguna ketika ingin memproses elemen dictionary secara berurutan dari yang terakhir ditambahkan, tanpa perlu mengetahui kuncinya.
*   **Argumen**: Tidak menerima argumen apa pun.
*   **Nilai Kembali**: Mengembalikan pasangan *key-value* yang dihapus sebagai sebuah **tuple** `(key, value)`.
*   **Efek Samping**: Pasangan *key-value* terakhir akan dihapus dari dictionary.
*   **Contoh**:
    ```python
    friends = {
        "cup": "ucup surucup",
        "sep": "asep si kasyep",
        "cuy": "ucuy surucuy" # Ini adalah elemen terakhir
    }
    data_terakhir = friends.popitem()
    # data_terakhir akan berisi ('cuy', 'ucuy surucuy')
    # friends sekarang akan menjadi {"cup": "ucup surucup", "sep": "asep si kasyep"}
    ```

## 4. Topik Lanjutan

Setelah memahami dasar-dasar `copy()`, `pop()`, dan `popitem()`, langkah selanjutnya adalah mempelajari **Nesting Dictionary** atau **Multi-keys**. Ini melibatkan pembuatan dictionary di dalam dictionary, yang memungkinkan pembentukan struktur data yang lebih kompleks dan terorganisir. Struktur seperti ini sangat berguna untuk merepresentasikan data yang kompleks, seperti struktur database atau konfigurasi aplikasi.
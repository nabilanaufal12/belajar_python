# Metode Ajaib (Magic Method) di Python OOP

Magic methods, atau sering disebut juga dunder methods (karena penggunaan *double underscore* atau `__`), adalah metode khusus di Python yang memungkinkan kita untuk mendefinisikan perilaku khusus untuk objek kelas. Metode ini memiliki nama yang diawali dan diakhiri dengan dua garis bawah (`__`). Dengan magic methods, kita dapat meng-override perilaku bawaan Python dan membuat objek kelas kita lebih fungsional dan bermakna.

## Apa itu Magic Method?

*   **Definisi**: Magic method adalah metode yang sudah memiliki kata kunci (`keywords`) di Python dan dapat kita gunakan kembali untuk tujuan tertentu.
*   **Tujuan**: Untuk mendefinisikan bagaimana objek kelas kita berinteraksi dengan operasi bawaan Python, seperti inisialisasi, representasi string, operasi aritmatika, dan akses atribut.
*   **Manfaat**:
    *   Membuat objek lebih fungsional dan berperilaku sesuai keinginan.
    *   Mengganti output objek yang tidak informatif (misalnya, `<__main__.Mangga object at 0x...>`) dengan representasi yang lebih mudah dibaca dan dimengerti.
    *   Memungkinkan operasi kustom (misalnya, penjumlahan) pada objek kustom.

## Magic Method Umum

Berikut adalah beberapa magic method yang sering digunakan:

### `__init__`

*   **Fungsi**: Metode inisialisasi yang secara otomatis dipanggil saat objek dari suatu kelas dibuat (instansiasi).
*   **Penggunaan**: Digunakan untuk mengatur atribut awal objek, seperti `nama` dan `jumlah`.
*   **Perilaku**: Dieksekusi secara otomatis saat pembuatan objek kelas.

### `__repr__`

*   **Fungsi**: Mengembalikan representasi "resmi" (official) dari suatu objek, biasanya string yang bisa digunakan untuk membuat ulang objek tersebut.
*   **Kasus Penggunaan**: Umumnya digunakan untuk **debugging** karena memberikan representasi yang lebih informatif daripada representasi objek bawaan Python (`<__main__.Mangga object at 0x...>`).
*   **Contoh**: Mengembalikan string seperti "Debug: Mangga arom manis dengan jumlah 10".
*   **Perilaku Default**: Jika tidak didefinisikan, `print()` objek akan menampilkan representasi objek bawaan yang kurang informatif.

### `__str__`

*   **Fungsi**: Mengembalikan representasi "tidak resmi" (informal) atau "ramah pengguna" (user-friendly) dari suatu objek.
*   **Kasus Penggunaan**: Umumnya digunakan untuk **produksi** atau saat program sudah jadi, untuk output yang lebih mudah dibaca oleh pengguna akhir.
*   **Perbedaan dengan `__repr__`**:
    *   `__str__` ditujukan untuk output yang mudah dibaca oleh pengguna.
    *   `__repr__` ditujukan untuk output yang jelas dan tidak ambigu, seringkali untuk debugging atau inspeksi developer.
    *   Jika `__str__` tidak didefinisikan, Python akan mencoba menggunakan `__repr__`. Jika `__repr__` juga tidak ada, akan kembali ke representasi objek bawaan.
*   **Preferensi**: Pembicara cenderung hanya menggunakan `__str__` jika tidak ada kebutuhan spesifik untuk `__repr__` dalam debugging.

### `__add__`

*   **Fungsi**: Mendefinisikan perilaku operator penjumlahan (`+`) untuk objek kelas.
*   **Masalah Tanpa `__add__`**: Objek tidak dapat dijumlahkan secara langsung dan akan menghasilkan `TypeError`.
*   **Implementasi**: Menerima objek lain sebagai argumen (`object`) dan mengembalikan hasil penjumlahan atribut yang diinginkan (misalnya, `self.jumlah + object.jumlah`).
*   **Contoh**: Menjumlahkan atribut `jumlah` dari dua objek `Mangga`, menghasilkan `15` dari `10 + 5`.
*   **Magic Method Aritmatika Lain**: Ada juga `__mul__` (perkalian), `__sub__` (pengurangan), `__truediv__` (pembagian), dan lainnya.

### `__dict__`

*   **Fungsi**: Mengakses kamus atribut dari suatu objek.
*   **Perilaku Default**: Mengeluarkan semua atribut objek dalam bentuk kamus.
*   **Meng-override `__dict__`**:
    *   Dapat di-override untuk mengembalikan representasi kustom dari atribut objek.
    *   Membutuhkan dekorator `@property` di atas definisi metode `__dict__` agar berfungsi dengan benar.
    *   **Contoh**: Mengembalikan string "Objek ini mempunyai nama dan jumlah" sebagai pengganti kamus atribut.

## Eksplorasi Lebih Lanjut

Ada banyak magic method lain yang tersedia di Python untuk berbagai operasi dan perilaku. Untuk daftar lengkap dan penggunaannya, disarankan untuk mencari di dokumentasi Python.
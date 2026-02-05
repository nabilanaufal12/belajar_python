# Belajar Python OOP: Class Abstract

## Overview

Catatan ini membahas konsep **Class Abstract** dalam Pemrograman Berorientasi Objek (OOP) di Python, termasuk definisi, tujuan, implementasi menggunakan modul `abc`, dan contoh penggunaannya. Class abstract berfungsi sebagai kerangka kerja atau kontrak yang harus dipatuhi oleh kelas turunannya.

## Konsep Class Abstract

**Class Abstract** adalah kelas yang tidak dapat diinstansiasi secara langsung (tidak bisa dibuat objeknya). Kelas ini dirancang untuk menjadi kelas dasar bagi kelas-kelas lain, mendefinisikan antarmuka umum atau "kontrak" yang harus diimplementasikan oleh kelas turunannya.

*   Kelas abstract seringkali mengandung satu atau lebih **metode abstract**.
*   **Metode abstract** adalah metode yang dideklarasikan tetapi tidak memiliki implementasi (badan) di kelas abstract itu sendiri. Implementasi metode ini diserahkan sepenuhnya kepada kelas-kelas turunan (subclass).

## Mengapa Menggunakan Class Abstract?

Penggunaan class abstract memiliki beberapa tujuan utama dalam desain OOP:

*   **Mendefinisikan Antarmuka (Interface):** Class abstract memungkinkan Anda untuk mendefinisikan serangkaian metode yang *harus* diimplementasikan oleh semua subclass. Ini memastikan bahwa semua kelas turunan memiliki fungsionalitas dasar yang sama, meskipun implementasinya mungkin berbeda.
*   **Menerapkan Struktur (Enforcing Structure):** Ini memaksa pengembang untuk mengikuti pola desain tertentu, sehingga meningkatkan konsistensi dan pemeliharaan kode.
*   **Mencegah Instansiasi Kelas Dasar yang Tidak Lengkap:** Karena kelas abstract tidak dapat diinstansiasi, ini mencegah pembuatan objek dari kelas yang belum sepenuhnya mendefinisikan semua perilakunya.
*   **Polimorfisme:** Memungkinkan objek dari berbagai kelas turunan untuk diperlakukan secara seragam melalui referensi ke kelas abstract dasar mereka, selama mereka mengimplementasikan metode abstract yang sama.

## Implementasi Class Abstract di Python

Berbeda dengan beberapa bahasa lain (seperti Java atau C++) yang memiliki kata kunci `abstract` bawaan, Python menggunakan modul `abc` (Abstract Base Classes) untuk mendukung class abstract.

Untuk membuat class abstract di Python, Anda perlu:

1.  **Mengimpor `ABC` dan `abstractmethod`** dari modul `abc`.
2.  **Mewarisi (inherit) dari `ABC`** di kelas yang ingin Anda jadikan abstract.
3.  **Mendekorasi metode** yang ingin Anda jadikan abstract dengan `@abstractmethod`.

### Aturan Penting:

*   Jika sebuah kelas mewarisi dari `ABC` dan memiliki metode yang didekorasi dengan `@abstractmethod`, maka kelas tersebut adalah **kelas abstract**.
*   Anda **tidak dapat membuat objek (instansiasi)** langsung dari kelas abstract.
*   Setiap **subclass konkret** (non-abstract) dari kelas abstract **harus mengimplementasikan semua metode abstract** dari kelas induknya. Jika tidak, subclass tersebut juga akan dianggap abstract dan tidak dapat diinstansiasi.
*   Kelas abstract **dapat memiliki metode konkret** (metode dengan implementasi) selain metode abstract.

## Contoh Penggunaan

Mari kita lihat contoh di mana kita mendefinisikan kelas abstract `Bentuk` dengan metode abstract `hitung_luas()`. Kelas `Lingkaran` dan `Persegi` kemudian akan mewarisi dari `Bentuk` dan mengimplementasikan metode `hitung_luas()` mereka sendiri.

```python
from abc import ABC, abstractmethod

# Mendefinisikan kelas abstract 'Bentuk'
class Bentuk(ABC):
    def __init__(self, nama):
        self.nama = nama

    # Metode abstract: harus diimplementasikan oleh subclass
    @abstractmethod
    def hitung_luas(self):
        pass # Tidak ada implementasi di sini

    # Metode konkret: bisa memiliki implementasi di kelas abstract
    def tampilkan_nama(self):
        print(f"Ini adalah bentuk: {self.nama}")

# Subclass konkret 'Lingkaran'
class Lingkaran(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self.radius = radius

    # Implementasi metode abstract hitung_luas()
    def hitung_luas(self):
        return 3.14 * self.radius * self.radius

# Subclass konkret 'Persegi'
class Persegi(Bentuk):
    def __init__(self, nama, sisi):
        super().__init__(nama)
        self.sisi = sisi

    # Implementasi metode abstract hitung_luas()
    def hitung_luas(self):
        return self.sisi * self.sisi

# --- Penggunaan ---

# Mencoba menginstansiasi kelas abstract akan menghasilkan error
try:
    bentuk_umum = Bentuk("Bentuk Umum")
except TypeError as e:
    print(f"Error: {e}") # Output: Can't instantiate abstract class Bentuk with abstract method hitung_luas

# Menginstansiasi subclass konkret
lingkaran1 = Lingkaran("Lingkaran A", 5)
persegi1 = Persegi("Persegi B", 4)

print(f"{lingkaran1.nama} memiliki luas: {lingkaran1.hitung_luas()}") # Output: Lingkaran A memiliki luas: 78.5
print(f"{persegi1.nama} memiliki luas: {persegi1.hitung_luas()}")   # Output: Persegi B memiliki luas: 16

lingkaran1.tampilkan_nama() # Output: Ini adalah bentuk: Lingkaran A
```

Dalam contoh di atas:
*   `Bentuk` adalah kelas abstract karena mewarisi dari `ABC` dan memiliki `@abstractmethod` `hitung_luas()`.
*   `Lingkaran` dan `Persegi` adalah subclass konkret yang berhasil mengimplementasikan `hitung_luas()`.
*   Mencoba membuat objek `Bentuk` secara langsung akan menghasilkan `TypeError`.

## Keuntungan Menggunakan Class Abstract

*   **Standardisasi dan Konsistensi:** Memastikan bahwa semua kelas turunan mematuhi "kontrak" yang sama, membuat kode lebih mudah dipahami dan dikelola.
*   **Desain yang Lebih Baik:** Mendorong desain yang lebih modular dan terstruktur, di mana detail implementasi disembunyikan dari kelas dasar.
*   **Pengujian yang Lebih Mudah:** Karena antarmuka didefinisikan dengan jelas, pengujian unit untuk kelas turunan menjadi lebih terfokus.
*   **Fleksibilitas:** Memungkinkan penambahan kelas turunan baru di masa mendatang tanpa mengubah kode yang ada, selama mereka mematuhi antarmuka yang didefinisikan.
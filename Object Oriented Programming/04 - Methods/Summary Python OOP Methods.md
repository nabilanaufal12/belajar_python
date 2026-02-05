# Belajar Python OOP: Methods

Dalam pemrograman berorientasi objek (OOP) di Python, **methods** adalah fungsi yang terkait dengan objek. Methods mendefinisikan perilaku objek atau tindakan yang dapat dilakukan objek tersebut. Mereka adalah blok kode yang beroperasi pada data yang terkandung dalam objek (atribut) atau pada kelas itu sendiri.

## Pengertian Method

Method adalah fungsi yang didefinisikan di dalam sebuah kelas. Ketika sebuah objek (instance) dari kelas tersebut dibuat, method-method ini dapat dipanggil melalui objek tersebut untuk melakukan operasi tertentu. Method memungkinkan objek untuk berinteraksi dengan datanya sendiri dan dengan objek lain, sehingga menjadi inti dari konsep enkapsulasi dan perilaku objek dalam OOP.

## Jenis-jenis Method

Python mendukung beberapa jenis method, masing-masing dengan tujuan dan cara penggunaan yang berbeda:

### 1. Instance Methods

**Instance methods** adalah jenis method yang paling umum. Mereka beroperasi pada instance (objek) dari sebuah kelas. Method ini selalu menerima parameter pertama, secara konvensional dinamakan `self`, yang merujuk pada instance objek itu sendiri.

*   **Tujuan**: Untuk mengakses atau memodifikasi atribut instance.
*   **Deklarasi**: Didefinisikan tanpa dekorator khusus.
*   **Contoh**:
    ```python
    class Kucing:
        def __init__(self, nama, umur):
            self.nama = nama
            self.umur = umur

        def bersuara(self): # Instance method
            return f"{self.nama} mengeong."

        def tambah_umur(self, tahun): # Instance method
            self.umur += tahun
            return f"Umur {self.nama} sekarang {self.umur} tahun."
    ```
    Dalam contoh di atas, `bersuara` dan `tambah_umur` adalah instance methods.

### 2. Class Methods

**Class methods** beroperasi pada kelas itu sendiri, bukan pada instance objek. Mereka menerima parameter pertama, secara konvensional dinamakan `cls`, yang merujuk pada kelas. Class methods dideklarasikan menggunakan dekorator `@classmethod`.

*   **Tujuan**: Untuk beroperasi pada atribut kelas atau untuk membuat instance baru dari kelas (seperti *factory methods*).
*   **Deklarasi**: Menggunakan dekorator `@classmethod`.
*   **Contoh**:
    ```python
    class Mobil:
        roda = 4 # Atribut kelas

        def __init__(self, merek):
            self.merek = merek

        @classmethod
        def ganti_jumlah_roda(cls, jumlah_baru): # Class method
            cls.roda = jumlah_baru
            return f"Jumlah roda semua mobil sekarang {cls.roda}."

        @classmethod
        def buat_mobil_listrik(cls, merek): # Factory method
            return cls(f"Listrik {merek}")
    ```
    `ganti_jumlah_roda` dan `buat_mobil_listrik` adalah class methods.

### 3. Static Methods

**Static methods** adalah method yang tidak menerima parameter `self` (instance) maupun `cls` (kelas) secara implisit. Mereka adalah fungsi biasa yang ditempatkan di dalam sebuah kelas karena memiliki hubungan logis dengan kelas tersebut, tetapi tidak beroperasi pada data instance atau kelas. Static methods dideklarasikan menggunakan dekorator `@staticmethod`.

*   **Tujuan**: Untuk fungsi utilitas yang secara logis terkait dengan kelas tetapi tidak memerlukan akses ke instance atau data kelas.
*   **Deklarasi**: Menggunakan dekorator `@staticmethod`.
*   **Contoh**:
    ```python
    class Kalkulator:
        @staticmethod
        def tambah(a, b): # Static method
            return a + b

        @staticmethod
        def kurang(a, b): # Static method
            return a - b
    ```
    `tambah` dan `kurang` adalah static methods.

## Parameter `self`

Parameter `self` adalah konvensi dalam Python untuk merujuk pada instance objek itu sendiri dalam sebuah instance method. Meskipun bisa menggunakan nama lain, `self` sangat direkomendasikan untuk menjaga konsistensi dan keterbacaan kode. Ketika sebuah instance method dipanggil, Python secara otomatis meneruskan instance objek sebagai argumen pertama ke parameter `self`.

*   **Peran**: Memungkinkan method untuk mengakses dan memanipulasi atribut serta method lain dari instance yang sama.
*   **Wajib**: Harus menjadi parameter pertama dari setiap instance method.

## Memanggil Method

Methods dipanggil menggunakan sintaks *dot notation* pada objek atau kelas, tergantung jenis methodnya.

*   **Instance Methods**: Dipanggil melalui instance objek.
    ```python
    kucing_saya = Kucing("Milo", 3)
    print(kucing_saya.bersuara()) # Memanggil instance method
    print(kucing_saya.tambah_umur(1))
    ```
*   **Class Methods**: Dipanggil melalui kelas atau instance. Lebih umum dipanggil melalui kelas.
    ```python
    print(Mobil.ganti_jumlah_roda(6)) # Memanggil class method melalui kelas
    mobil_baru = Mobil.buat_mobil_listrik("Tesla")
    print(mobil_baru.merek)
    ```
*   **Static Methods**: Dipanggil melalui kelas atau instance. Lebih umum dipanggil melalui kelas.
    ```python
    hasil_tambah = Kalkulator.tambah(5, 3) # Memanggil static method melalui kelas
    print(f"Hasil tambah: {hasil_tambah}")
    ```
Memahami berbagai jenis method dan cara kerjanya sangat penting untuk membangun struktur kelas yang efektif dan modular dalam Python OOP.
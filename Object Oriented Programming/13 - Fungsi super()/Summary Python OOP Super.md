# Belajar Python OOP: Fungsi `super()`

## Gambaran Umum

Dalam pemrograman berorientasi objek (OOP) Python, fungsi `super()` adalah alat yang sangat penting untuk mengelola hierarki pewarisan (inheritance). Fungsi ini memungkinkan kita untuk memanggil metode dari kelas induk (parent class) atau kelas saudara (sibling class) dalam konteks pewarisan berganda (multiple inheritance) secara dinamis. Ini sangat berguna untuk memastikan bahwa inisialisasi dan perilaku kelas induk dipertahankan atau diperluas oleh kelas anak (child class).

## Apa itu `super()`?

Fungsi `super()` mengembalikan objek proxy sementara yang memungkinkan Anda untuk mendelegasikan panggilan metode ke kelas induk atau saudara. Ini memiliki dua tujuan utama:

1.  **Memanggil konstruktor kelas induk (`__init__`)**: Ini adalah penggunaan paling umum dari `super()`. Ketika sebuah kelas anak memiliki konstruktornya sendiri, seringkali perlu untuk memanggil konstruktor kelas induk untuk memastikan bahwa semua atribut yang didefinisikan di kelas induk juga diinisialisasi dengan benar.
2.  **Memanggil metode lain dari kelas induk**: Selain konstruktor, `super()` juga dapat digunakan untuk memanggil metode lain yang didefinisikan di kelas induk, memungkinkan kelas anak untuk memperluas atau memodifikasi perilaku metode tersebut tanpa menulis ulang seluruh kode.

### Sintaks Dasar

Secara umum, `super()` dapat dipanggil dalam dua bentuk:

*   `super().__init__(...)`: Digunakan di dalam metode `__init__` kelas anak untuk memanggil konstruktor kelas induk.
*   `super().nama_metode(...)`: Digunakan untuk memanggil metode lain dari kelas induk.

Sebelum Python 3, sintaksnya adalah `super(NamaKelas, self).nama_metode(...)`. Namun, di Python 3, `super()` tanpa argumen secara otomatis mengidentifikasi kelas saat ini dan instance `self`, membuatnya lebih ringkas dan mudah digunakan.

## Penggunaan `super()` dalam `__init__`

Ketika sebuah kelas anak mewarisi dari kelas induk dan ingin menambahkan atributnya sendiri sambil tetap mempertahankan atribut dari kelas induk, `super().__init__()` adalah solusinya.

```python
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
        print(f"Kendaraan {self.merek} tahun {self.tahun} dibuat.")

class Mobil(Kendaraan):
    def __init__(self, merek, tahun, model):
        super().__init__(merek, tahun) # Memanggil konstruktor Kendaraan
        self.model = model
        print(f"Mobil {self.merek} model {self.model} dibuat.")

# Contoh penggunaan
mobil_saya = Mobil("Toyota", 2020, "Camry")
# Output:
# Kendaraan Toyota tahun 2020 dibuat.
# Mobil Toyota model Camry dibuat.
```
Dalam contoh di atas, `Mobil` mewarisi dari `Kendaraan`. Konstruktor `Mobil` memanggil `super().__init__(merek, tahun)` untuk memastikan bahwa atribut `merek` dan `tahun` diinisialisasi oleh konstruktor `Kendaraan` sebelum `Mobil` menambahkan atribut `model` miliknya sendiri.

## Penggunaan `super()` untuk Metode Lain

`super()` tidak hanya terbatas pada konstruktor. Ini juga dapat digunakan untuk memanggil metode lain dari kelas induk.

```python
class Bentuk:
    def info(self):
        return "Ini adalah sebuah bentuk."

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def info(self):
        # Memanggil metode info() dari kelas Bentuk
        pesan_induk = super().info()
        return f"{pesan_induk} Ini adalah lingkaran dengan radius {self.radius}."

# Contoh penggunaan
lingkaran_kecil = Lingkaran(5)
print(lingkaran_kecil.info())
# Output: Ini adalah sebuah bentuk. Ini adalah lingkaran dengan radius 5.
```
Di sini, metode `info()` di kelas `Lingkaran` memanggil `super().info()` untuk mendapatkan pesan dari kelas `Bentuk` dan kemudian menambahkan informasi spesifik `Lingkaran`.

## `super()` dan Method Resolution Order (MRO)

`super()` bekerja berdasarkan **Method Resolution Order (MRO)**. MRO adalah urutan di mana Python mencari metode di hierarki pewarisan. Ini sangat penting dalam kasus pewarisan berganda. Anda dapat melihat MRO dari sebuah kelas menggunakan `NamaKelas.__mro__` atau `help(NamaKelas)`.

Ketika `super()` dipanggil, ia tidak hanya mencari metode di kelas induk langsung, tetapi mengikuti MRO untuk menemukan implementasi metode berikutnya dalam urutan pewarisan. Ini memastikan perilaku yang benar dan konsisten, terutama dalam skenario pewarisan yang kompleks seperti pewarisan berganda.

```python
class A:
    def method(self):
        print("Method dari A")

class B(A):
    def method(self):
        print("Method dari B")
        super().method() # Memanggil method dari A

class C(A):
    def method(self):
        print("Method dari C")
        super().method() # Memanggil method dari A

class D(B, C):
    def method(self):
        print("Method dari D")
        super().method() # Memanggil method dari B (sesuai MRO)

# Contoh penggunaan
d_obj = D()
d_obj.method()
# Output:
# Method dari D
# Method dari B
# Method dari C
# Method dari A

print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```
Dalam contoh `D(B, C)`, `super().method()` di `D` akan memanggil `B.method()`, kemudian `super().method()` di `B` akan memanggil `C.method()` (karena `C` adalah kelas berikutnya dalam MRO setelah `B`), dan seterusnya, hingga `A.method()`.

## Keuntungan Menggunakan `super()`

*   **Pemeliharaan Kode yang Lebih Baik**: Mengurangi duplikasi kode dan membuat kode lebih mudah dipelihara.
*   **Fleksibilitas**: Memungkinkan perubahan pada hierarki kelas tanpa perlu memodifikasi kode di kelas anak secara ekstensif.
*   **Dukungan Pewarisan Berganda**: Menangani pewarisan berganda dengan cara yang konsisten dan dapat diprediksi melalui MRO.
*   **Inisialisasi yang Benar**: Memastikan bahwa semua bagian dari hierarki pewarisan diinisialisasi dengan benar.
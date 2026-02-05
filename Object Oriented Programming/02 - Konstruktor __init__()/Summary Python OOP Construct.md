# Belajar Python OOP: Konstruktor `__init__()`

Video ini membahas tentang konsep konstruktor dalam pemrograman berorientasi objek (OOP) di Python, dengan fokus pada metode khusus `__init__()`.

## Apa itu Konstruktor?

Dalam OOP, **konstruktor** adalah metode khusus yang secara otomatis dipanggil saat sebuah objek (instance) baru dari suatu kelas dibuat. Tujuan utamanya adalah untuk menginisialisasi atribut-atribut objek dengan nilai awal yang diperlukan. Konstruktor tidak secara eksplisit mengembalikan nilai apa pun.

## Metode `__init__()` di Python

Di Python, konstruktor diimplementasikan menggunakan metode khusus yang bernama `__init__()`.

*   Nama `__init__` diawali dan diakhiri dengan dua garis bawah (`__`), yang menandakan bahwa ini adalah "dunder method" (double underscore method) atau metode khusus yang memiliki makna tertentu bagi interpreter Python.
*   Metode ini akan dieksekusi setiap kali objek baru dari kelas tersebut dibuat.

### Tujuan dan Penggunaan

Metode `__init__()` digunakan untuk:
*   **Menginisialisasi atribut** objek dengan nilai awal yang diberikan saat objek dibuat.
*   Melakukan operasi *setup* atau persiapan lain yang diperlukan agar objek berada dalam keadaan yang valid segera setelah dibuat.

### Parameter `__init__()`

Metode `__init__()` dapat menerima parameter, yang memungkinkan kita untuk meneruskan data saat membuat objek.

*   **`self`**: Parameter pertama dari setiap metode instance (termasuk `__init__`) di Python haruslah `self`.
    *   `self` adalah referensi ke instance objek itu sendiri. Ini memungkinkan kita untuk mengakses atribut dan metode objek dari dalam kelas.
    *   Secara konseptual, `self` mirip dengan `this` di bahasa pemrograman lain seperti Java atau C++.
*   **Parameter Lain**: Setelah `self`, kita dapat mendefinisikan parameter lain yang akan digunakan untuk menginisialisasi atribut objek.

## Contoh Penggunaan `__init__()`

```python
class Mahasiswa:
    def __init__(self, nama, nim):
        # 'self.nama' dan 'self.nim' adalah atribut objek
        # 'nama' dan 'nim' adalah parameter yang diterima oleh konstruktor
        self.nama = nama
        self.nim = nim
        print(f"Objek Mahasiswa {self.nama} dengan NIM {self.nim} telah dibuat.") #

# Membuat objek (instance) dari kelas Mahasiswa
# Saat objek dibuat, metode __init__() akan dipanggil secara otomatis
mhs1 = Mahasiswa("Budi Santoso", "2022001") #
mhs2 = Mahasiswa("Siti Aminah", "2022002")

# Mengakses atribut objek
print(f"Nama Mahasiswa 1: {mhs1.nama}")
print(f"NIM Mahasiswa 2: {mhs2.nim}")
```

Dalam contoh di atas:
*   Ketika `mhs1 = Mahasiswa("Budi Santoso", "2022001")` dieksekusi, Python secara otomatis memanggil `__init__(mhs1, "Budi Santoso", "2022001")`.
*   Di dalam `__init__`, nilai `"Budi Santoso"` dan `"2022001"` digunakan untuk menginisialisasi atribut `self.nama` dan `self.nim` untuk objek `mhs1`.

Dengan menggunakan `__init__()`, kita memastikan bahwa setiap objek `Mahasiswa` yang dibuat akan selalu memiliki atribut `nama` dan `nim` yang terinisialisasi dengan benar.
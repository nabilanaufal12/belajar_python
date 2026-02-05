# Belajar Python OOP: Class Abstract dan Decorator

## Gambaran Umum

Catatan ini membahas dua konsep lanjutan dalam Pemrograman Berorientasi Objek (OOP) di Python: **Class Abstract** dan **Decorator**. Class Abstract digunakan untuk mendefinisikan antarmuka atau kontrak yang harus dipatuhi oleh subclass, sementara Decorator menyediakan cara yang fleksibel untuk menambahkan fungsionalitas ke fungsi atau metode yang ada tanpa memodifikasi strukturnya secara langsung.

## Class Abstract (Abstract Base Classes - ABCs)

**Class Abstract** adalah kelas yang tidak dapat diinstansiasi secara langsung dan dirancang untuk diwarisi oleh kelas lain. Tujuannya adalah untuk mendefinisikan antarmuka umum atau "kontrak" yang harus diimplementasikan oleh semua subclass konkretnya.

### Mengapa Menggunakan Class Abstract?

*   **Menerapkan Struktur:** Class Abstract memastikan bahwa subclass tertentu akan memiliki metode yang diperlukan, sehingga menjaga konsistensi dalam hierarki kelas. Ini mencegah pengembang lupa mengimplementasikan metode penting.
*   **Mendefinisikan Kontrak:** Mereka berfungsi sebagai cetak biru, mendikte apa yang harus dilakukan oleh subclass tanpa menentukan bagaimana melakukannya.

### Membuat Class Abstract di Python

Python tidak memiliki kata kunci `abstract` bawaan seperti beberapa bahasa lain. Sebaliknya, Python menyediakan modul `abc` (Abstract Base Classes) untuk bekerja dengan kelas abstrak.

1.  **Mewarisi dari `ABC`**: Untuk membuat kelas menjadi abstrak, kelas tersebut harus mewarisi dari `ABC` yang diimpor dari modul `abc`.
2.  **Menggunakan `@abstractmethod`**: Metode dalam kelas abstrak yang harus diimplementasikan oleh subclass ditandai dengan decorator `@abstractmethod`.

**Contoh Struktur:**

```python
from abc import ABC, abstractmethod

class Bentuk(ABC): # Kelas Bentuk adalah abstrak
    @abstractmethod
    def hitung_luas(self):
        pass # Metode abstrak tidak memiliki implementasi

    @abstractmethod
    def hitung_keliling(self):
        pass

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return 3.14 * self.radius * self.radius

    def hitung_keliling(self):
        return 2 * 3.14 * self.radius

# class Persegi(Bentuk): # Jika tidak mengimplementasikan semua metode abstrak, ini juga menjadi abstrak
#     def __init__(self, sisi):
#         self.sisi = sisi
#
#     def hitung_luas(self):
#         return self.sisi * self.sisi

# bentuk = Bentuk() # Ini akan menghasilkan TypeError karena Bentuk adalah kelas abstrak
lingkaran = Lingkaran(5)
print(f"Luas Lingkaran: {lingkaran.hitung_luas()}")
print(f"Keliling Lingkaran: {lingkaran.hitung_keliling()}")
```

### Aturan Class Abstract

*   **Tidak Dapat Diinstansiasi:** Anda tidak dapat membuat objek langsung dari kelas abstrak. Mencoba melakukannya akan menghasilkan `TypeError`.
*   **Subclass Harus Mengimplementasikan:** Subclass dari kelas abstrak *harus* mengimplementasikan semua metode abstrak yang didefinisikan di kelas induknya. Jika tidak, subclass tersebut juga akan dianggap abstrak dan tidak dapat diinstansiasi.

## Decorator

**Decorator** adalah pola desain yang memungkinkan Anda menambahkan fungsionalitas baru ke objek yang sudah ada tanpa memodifikasi strukturnya. Dalam Python, decorator biasanya adalah fungsi yang mengambil fungsi lain sebagai argumen, menambahkan beberapa fungsionalitas, dan kemudian mengembalikan fungsi baru.

### Mengapa Menggunakan Decorator?

*   **Reusabilitas Kode:** Terapkan logika "pembungkus" yang sama ke banyak fungsi yang berbeda.
*   **Pemisahan Kekhawatiran (Separation of Concerns):** Pisahkan logika inti dari kekhawatiran tambahan seperti *logging*, *timing*, validasi, atau otentikasi.
*   **Sintaksis yang Bersih:** Sintaks `@decorator_name` yang ringkas membuat kode lebih mudah dibaca dan dipahami.

### Cara Kerja Decorator

Decorator adalah fungsi yang menerima fungsi lain sebagai argumen. Di dalamnya, ia mendefinisikan fungsi *wrapper* yang akan menjalankan logika tambahan sebelum atau sesudah memanggil fungsi asli. Akhirnya, decorator mengembalikan fungsi *wrapper* ini.

**Sintaksis Dasar:**

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Sesuatu terjadi sebelum fungsi dipanggil.") # Logika tambahan
        result = func(*args, **kwargs) # Memanggil fungsi asli
        print("Sesuatu terjadi setelah fungsi dipanggil.") # Logika tambahan
        return result
    return wrapper # Mengembalikan fungsi wrapper

@my_decorator # Ini sama dengan 'say_hello = my_decorator(say_hello)'
def say_hello(name):
    print(f"Halo, {name}!")

@my_decorator
def add(a, b):
    print(f"Menambahkan {a} dan {b}")
    return a + b

say_hello("Dunia")
print(f"Hasil penambahan: {add(10, 20)}")
```

### Decorator dengan Argumen

Anda dapat membuat decorator yang menerima argumennya sendiri. Ini dilakukan dengan membuat fungsi luar yang menerima argumen decorator, yang kemudian mengembalikan fungsi decorator yang sebenarnya.

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3) # Decorator dengan argumen
def greet(name):
    print(f"Salam, {name}!")

greet("Python")
```

### `functools.wraps`

Saat menggunakan decorator, metadata fungsi asli (seperti `__name__` dan `__doc__`) dapat hilang karena fungsi *wrapper* yang dikembalikan. Modul `functools` menyediakan decorator `wraps` yang membantu mempertahankan metadata ini.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func) # Mempertahankan metadata fungsi asli
    def wrapper(*args, **kwargs):
        """Ini adalah docstring dari wrapper."""
        print("Sebelum fungsi.")
        result = func(*args, **kwargs)
        print("Setelah fungsi.")
        return result
    return wrapper

@my_decorator
def example_function():
    """Ini adalah fungsi contoh."""
    print("Fungsi contoh sedang berjalan.")

example_function()
print(f"Nama fungsi: {example_function.__name__}") # Akan mencetak 'example_function'
print(f"Docstring: {example_function.__doc__}") # Akan mencetak 'Ini adalah fungsi contoh.'
```

Class Abstract dan Decorator adalah alat yang ampuh dalam Python OOP untuk membangun kode yang lebih terstruktur, modular, dan mudah dipelihara.
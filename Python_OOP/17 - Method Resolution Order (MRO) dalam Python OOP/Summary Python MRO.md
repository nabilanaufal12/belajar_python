# Method Resolution Order (MRO) dalam Python OOP

## Gambaran Umum

Method Resolution Order (MRO) adalah mekanisme penting dalam pemrograman berorientasi objek (OOP) Python, terutama saat berhadapan dengan pewarisan berganda (multiple inheritance). MRO menentukan urutan di mana Python mencari metode atau atribut dalam hierarki kelas. Pemahaman MRO sangat krusial untuk memprediksi perilaku kode dalam struktur pewarisan yang kompleks dan untuk penggunaan fungsi `super()` yang benar.

## Apa itu Method Resolution Order (MRO)?

**Method Resolution Order (MRO)** adalah urutan di mana Python menelusuri hierarki pewarisan untuk menemukan metode atau atribut yang diminta. Ketika sebuah objek memanggil suatu metode, Python tidak hanya melihat kelas objek tersebut, tetapi juga semua kelas induknya dalam urutan tertentu hingga metode tersebut ditemukan.

### Mengapa MRO Penting?

MRO menjadi sangat penting dalam skenario **pewarisan berganda**, di mana sebuah kelas dapat mewarisi dari dua atau lebih kelas induk yang mungkin memiliki metode dengan nama yang sama. Tanpa aturan yang jelas, akan ada ambiguitas tentang metode mana yang harus dipanggil.

## Algoritma C3 Linearization

Python menggunakan algoritma **C3 Linearization** untuk menentukan MRO. Algoritma ini memastikan beberapa properti penting:
1.  **Konsistensi**: Urutan pewarisan tetap konsisten.
2.  **Monotonisitas**: Jika sebuah metode ditemukan di kelas `X` dalam MRO, maka metode tersebut tidak akan ditemukan di kelas yang lebih "jauh" dari `X` dalam hierarki yang sama.
3.  **Urutan Lokal**: Urutan kelas induk yang didefinisikan dalam tanda kurung saat deklarasi kelas anak dipertahankan.

## Cara Memeriksa MRO

Anda dapat memeriksa MRO dari sebuah kelas menggunakan salah satu dari dua cara berikut:
*   Menggunakan metode `.mro()` pada kelas: `ClassName.mro()`
*   Menggunakan fungsi `help()`: `help(ClassName)`

## Contoh MRO

### 1. Pewarisan Tunggal (Single Inheritance)

Dalam pewarisan tunggal, MRO cukup sederhana: kelas anak akan diperiksa terlebih dahulu, kemudian kelas induknya, dan seterusnya hingga `object` (kelas dasar dari semua kelas di Python).

```python
class A:
    def info(self):
        print("Ini kelas A")

class B(A):
    def info(self):
        print("Ini kelas B")

# MRO untuk kelas B
# B.mro() -> [B, A, object]
```
Ketika `B` memanggil `info()`, ia akan mencari di `B` terlebih dahulu. Jika tidak ditemukan, baru mencari di `A`.

### 2. Pewarisan Berganda Sederhana

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass

# MRO untuk kelas C
# C.mro() -> [C, A, B, object]
```
Dalam contoh ini, `C` mewarisi dari `A` dan `B`. Urutan `A` kemudian `B` dipertahankan karena `A` disebutkan sebelum `B` dalam definisi `C(A, B)`.

### 3. Masalah Berlian (Diamond Problem)

Ini adalah skenario klasik dalam pewarisan berganda yang diatasi oleh MRO.

```python
class A:
    def show(self):
        print("Ini dari A")

class B(A):
    def show(self):
        print("Ini dari B")

class C(A):
    def show(self):
        print("Ini dari C")

class D(B, C):
    def show(self):
        print("Ini dari D")

# MRO untuk kelas D
# D.mro() -> [D, B, C, A, object]
```
Penjelasan MRO `[D, B, C, A, object]`:
*   **D** adalah kelas pertama yang dicari.
*   **B** adalah induk pertama `D`, jadi dicari setelah `D`.
*   **C** adalah induk kedua `D`, jadi dicari setelah `B`.
*   **A** adalah induk dari `B` dan `C`. Meskipun `A` adalah induk dari keduanya, MRO memastikan `A` hanya muncul sekali dan ditempatkan setelah semua kelas anak yang mewarisinya (`B` dan `C`) telah diperiksa. Ini menjaga konsistensi dan menghindari pemanggilan metode `A` terlalu dini jika `B` atau `C` telah menimpanya.

## Fungsi `super()` dan MRO

Fungsi `super()` dalam Python tidak hanya memanggil metode dari kelas induk langsung, melainkan memanggil metode berikutnya dalam urutan MRO. Ini memungkinkan kolaborasi antar-metode dalam hierarki pewarisan yang kompleks.

### Contoh Penggunaan `super()` dengan MRO

```python
class A:
    def method(self):
        print("Method dari A")

class B(A):
    def method(self):
        print("Method dari B")
        super().method() # Memanggil method berikutnya di MRO

class C(A):
    def method(self):
        print("Method dari C")
        super().method() # Memanggil method berikutnya di MRO

class D(B, C):
    def method(self):
        print("Method dari D")
        super().method() # Memanggil method berikutnya di MRO

d_obj = D()
d_obj.method()
```
Output dari `d_obj.method()` akan menjadi:
```
Method dari D
Method dari B
Method dari C
Method dari A
```
Ini terjadi karena `super()` pada `D` memanggil `B.method()`. Kemudian `super()` pada `B` memanggil `C.method()` (sesuai MRO `[D, B, C, A, object]`). Akhirnya, `super()` pada `C` memanggil `A.method()`.

## Kesimpulan

MRO adalah konsep fundamental dalam Python OOP yang mengatur bagaimana metode dan atribut dicari dalam hierarki pewarisan. Dengan memahami MRO dan algoritma C3 Linearization, pengembang dapat menulis kode yang lebih dapat diprediksi dan memanfaatkan pewarisan berganda serta fungsi `super()` secara efektif.
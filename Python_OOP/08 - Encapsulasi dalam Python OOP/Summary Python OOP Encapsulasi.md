# Encapsulasi dalam Python OOP

## Apa itu Encapsulasi?

Encapsulasi adalah salah satu dari empat pilar utama dalam Pemrograman Berorientasi Objek (OOP), bersama dengan pewarisan (inheritance), polimorfisme (polymorphism), dan abstraksi (abstraction). Konsep utama enkapsulasi adalah **membungkus (bundling)** data (atribut) dan metode (fungsi) yang beroperasi pada data tersebut ke dalam satu unit, yaitu objek atau kelas. Selain itu, enkapsulasi juga berfokus pada **penyembunyian informasi (information hiding)**, di mana detail internal implementasi suatu objek disembunyikan dari dunia luar.

Tujuan utama dari enkapsulasi adalah untuk:
*   Melindungi integritas data dengan mencegah akses langsung dan modifikasi yang tidak sah dari luar objek.
*   Meningkatkan modularitas dan fleksibilitas kode, karena perubahan internal pada suatu kelas tidak akan memengaruhi bagian lain dari program yang menggunakan kelas tersebut, selama antarmuka publiknya tetap sama.

## Prinsip Encapsulasi

Prinsip dasar enkapsulasi adalah bahwa data dalam suatu objek harus diakses atau dimodifikasi hanya melalui metode yang disediakan oleh objek itu sendiri, bukan secara langsung. Ini menciptakan "kontrak" antara objek dan dunia luar, di mana objek menjamin bahwa datanya akan selalu berada dalam keadaan yang valid.

## Implementasi Encapsulasi di Python

Python tidak memiliki pengubah akses (access modifiers) `public`, `protected`, atau `private` yang ketat seperti bahasa lain (misalnya Java atau C++). Namun, Python menggunakan konvensi penamaan dan mekanisme khusus untuk mencapai tingkat enkapsulasi yang serupa.

### 1. Anggota Publik (Public Members)

Secara *default*, semua atribut dan metode dalam kelas Python bersifat publik. Ini berarti mereka dapat diakses dan dimodifikasi secara langsung dari luar kelas.

```python
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama  # Atribut publik
        self.gaji = gaji  # Atribut publik

    def tampilkan_info(self): # Metode publik
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

k = Karyawan("Budi", 5000000)
print(k.nama) # Akses langsung atribut publik
k.gaji = 6000000 # Modifikasi langsung atribut publik
k.tampilkan_info()
```

### 2. Anggota Terlindungi (Protected Members)

Anggota terlindungi di Python ditandai dengan awalan satu *underscore* (`_`). Ini adalah **konvensi** yang menunjukkan kepada pengembang bahwa atribut atau metode tersebut dimaksudkan untuk penggunaan internal dalam kelas atau subkelasnya, dan tidak boleh diakses secara langsung dari luar. Namun, secara teknis, mereka masih dapat diakses.

```python
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self._gaji = gaji # Atribut terlindungi (konvensi)

    def _hitung_pajak(self): # Metode terlindungi (konvensi)
        return self._gaji * 0.10

    def tampilkan_info(self):
        pajak = self._hitung_pajak()
        print(f"Nama: {self.nama}, Gaji: {self._gaji}, Pajak: {pajak}")

k = Karyawan("Citra", 7000000)
print(k._gaji) # Masih bisa diakses, tapi tidak disarankan
pajak_manual = k._hitung_pajak() # Masih bisa dipanggil, tapi tidak disarankan
k.tampilkan_info()
```

### 3. Anggota Privat (Private Members)

Anggota privat di Python ditandai dengan awalan dua *underscore* (`__`). Python mengimplementasikan "privat" melalui mekanisme yang disebut **name mangling**. Ketika sebuah atribut atau metode diawali dengan `__` (dan tidak diakhiri dengan `__`), Python akan mengubah namanya menjadi `_NamaKelas__nama_atribut`. Ini membuat akses langsung dari luar kelas menjadi lebih sulit, tetapi tidak sepenuhnya mustahil (masih bisa diakses dengan nama yang "dimangled").

```python
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.__gaji_pokok = gaji # Atribut privat (name mangling)

    def __hitung_bonus(self): # Metode privat (name mangling)
        return self.__gaji_pokok * 0.05

    def tampilkan_info(self):
        bonus = self.__hitung_bonus()
        print(f"Nama: {self.nama}, Gaji Pokok: {self.__gaji_pokok}, Bonus: {bonus}")

k = Karyawan("Dedi", 8000000)
# print(k.__gaji_pokok) # Ini akan menyebabkan AttributeError
# print(k.__hitung_bonus()) # Ini akan menyebabkan AttributeError

# Akses melalui name mangling (tidak disarankan)
print(k._Karyawan__gaji_pokok)
bonus_manual = k._Karyawan__hitung_bonus()
print(f"Bonus manual: {bonus_manual}")

k.tampilkan_info()
```

## Getter dan Setter (Accessors dan Mutators)

Meskipun Python memungkinkan akses langsung ke atribut publik, praktik terbaik enkapsulasi seringkali melibatkan penggunaan metode **getter** (untuk mendapatkan nilai atribut) dan **setter** (untuk mengatur nilai atribut). Ini memungkinkan kontrol lebih besar atas bagaimana data diakses dan dimodifikasi, memungkinkan validasi atau logika tambahan sebelum nilai diatur atau dikembalikan.

Python menyediakan dekorator `@property` untuk membuat getter dan setter dengan cara yang lebih "Pythonic", memungkinkan akses atribut seolah-olah itu adalah atribut publik, tetapi di balik layar memanggil metode.

```python
class Karyawan:
    def __init__(self, nama, gaji):
        self._nama = nama
        self._gaji = gaji # Menggunakan _ untuk menunjukkan bahwa ini harus diakses melalui properti

    @property # Getter untuk nama
    def nama(self):
        return self._nama

    @nama.setter # Setter untuk nama
    def nama(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Nama harus berupa string non-kosong.")
        self._nama = value

    @property # Getter untuk gaji
    def gaji(self):
        return self._gaji

    @gaji.setter # Setter untuk gaji
    def gaji(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Gaji harus berupa angka positif.")
        self._gaji = value

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

k = Karyawan("Eka", 9000000)
print(k.nama) # Memanggil getter nama
print(k.gaji) # Memanggil getter gaji

k.gaji = 9500000 # Memanggil setter gaji
k.tampilkan_info()

try:
    k.gaji = -100 # Akan memicu ValueError dari setter
except ValueError as e:
    print(f"Error: {e}")

try:
    k.nama = "" # Akan memicu ValueError dari setter
except ValueError as e:
    print(f"Error: {e}")
```

## Manfaat Encapsulasi

*   **Keamanan Data (Data Security)**: Melindungi data internal objek dari modifikasi yang tidak sah atau tidak disengaja dari luar.
*   **Validasi Data**: Memungkinkan implementasi logika validasi dalam metode setter, memastikan bahwa data selalu berada dalam keadaan yang valid.
*   **Fleksibilitas dan Pemeliharaan**: Memungkinkan perubahan implementasi internal suatu kelas tanpa memengaruhi kode eksternal yang menggunakannya, selama antarmuka publik tetap konsisten. Ini memudahkan pemeliharaan dan *refactoring*.
*   **Modularitas**: Memecah program menjadi unit-unit yang lebih kecil dan mandiri, meningkatkan keterbacaan dan pengelolaan kode.
*   **Kontrol Akses**: Memberikan kontrol granular atas bagaimana atribut dan metode diakses dan dimodifikasi.
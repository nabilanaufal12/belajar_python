# Variabel Privat dalam Python OOP

Dalam pemrograman berorientasi objek (OOP) Python, konsep **variabel privat** memiliki implementasi yang unik dibandingkan dengan bahasa pemrograman lain. Python tidak memiliki mekanisme "privat" yang ketat seperti Java atau C++, melainkan mengandalkan konvensi penamaan dan mekanisme **name mangling** untuk mengindikasikan dan mengelola aksesibilitas variabel.

## Konvensi Penamaan Variabel

Python menggunakan dua konvensi utama untuk mengindikasikan "privasi" variabel:

### 1. Variabel "Protected" (Satu Garis Bawah `_`)

Variabel yang diawali dengan satu garis bawah (`_`) dianggap sebagai **variabel protected** atau **internal use only**.
*   **Tujuan**: Ini adalah konvensi untuk memberi tahu pengembang lain bahwa variabel tersebut dimaksudkan untuk penggunaan internal dalam kelas atau modul, dan sebaiknya tidak diakses atau dimodifikasi secara langsung dari luar kelas.
*   **Aksesibilitas**: Meskipun ada konvensi, variabel ini **masih dapat diakses secara langsung** dari luar kelas. Python tidak mencegah akses tersebut; ini murni pedoman etika pemrograman.

**Contoh:**
```python
class Hero:
    def __init__(self, nama, health):
        self._nama = nama  # Variabel protected
        self.health = health

hero1 = Hero("Ucup", 100)
print(hero1._nama) # Output: Ucup (masih bisa diakses)
```

### 2. Variabel "Private" (Dua Garis Bawah `__`)

Variabel yang diawali dengan dua garis bawah (`__`) memicu mekanisme **name mangling** oleh interpreter Python.
*   **Tujuan**: Mekanisme ini **bukan untuk membuat variabel benar-benar privat** dalam arti keamanan data, melainkan untuk **mencegah konflik penamaan** (name clashes) ketika kelas diwarisi (inheritance).
*   **Name Mangling**: Python secara otomatis mengubah nama variabel `__variabel` menjadi `_NamaKelas__variabel`. Ini berarti variabel tersebut tidak dapat diakses secara langsung dengan nama aslinya dari luar kelas.
*   **Aksesibilitas**: Jika mencoba mengakses `hero.__variabel` secara langsung, akan terjadi `AttributeError`. Namun, variabel tersebut **masih bisa diakses secara tidak langsung** menggunakan nama yang sudah di-mangled: `hero._NamaKelas__variabel`.

**Contoh:**
```python
class Hero:
    def __init__(self, nama, health):
        self.__nama = nama  # Variabel yang akan di-mangled
        self.__health = health

hero2 = Hero("Otong", 200)
# print(hero2.__nama) # Ini akan menghasilkan AttributeError

# Mengakses menggunakan nama yang di-mangled
print(hero2._Hero__nama)   # Output: Otong
print(hero2._Hero__health) # Output: 200
```

## Peran Name Mangling dalam Pewarisan

Mekanisme name mangling pada variabel `__` sangat berguna dalam skenario pewarisan untuk menghindari konflik penamaan.

Misalnya, jika ada kelas `Hero` dengan variabel `__health` dan kelas `Hero_Intelligent` yang mewarisi `Hero` juga memiliki variabel `__health` sendiri:

```python
class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health # Variabel __health milik Hero

class Hero_Intelligent(Hero):
    def __init__(self, name, health, intelligence):
        super().__init__(name, health)
        self.__health = health # Variabel __health milik Hero_Intelligent
        self.intelligence = intelligence

hero1 = Hero("Ucup", 100)
hero2 = Hero_Intelligent("Otong", 200, 50)

# Mengakses health dari objek Hero
print(hero1._Hero__health) # Output: 100

# Mengakses health dari objek Hero_Intelligent
# Perhatikan bahwa ini adalah __health milik Hero_Intelligent, bukan Hero
print(hero2._Hero_Intelligent__health) # Output: 200

# Variabel __health dari kelas induk (Hero) masih ada di objek hero2
# dan dapat diakses dengan nama mangled kelas induknya
print(hero2._Hero__health) # Output: 200 (nilai yang diteruskan dari super().__init__)
```

Dalam contoh di atas, name mangling memastikan bahwa `__health` dari `Hero` dan `__health` dari `Hero_Intelligent` adalah dua variabel yang berbeda, sehingga tidak saling menimpa. Jika kita menggunakan `_health` (protected) alih-alih `__health`, maka `_health` di `Hero_Intelligent` akan menimpa `_health` dari `Hero`.

## Kesimpulan

*   **`_variabel` (Protected)**: Konvensi untuk penggunaan internal. Masih bisa diakses langsung.
*   **`__variabel` (Name Mangling)**: Mengubah nama variabel untuk mencegah konflik penamaan dalam pewarisan. Tidak benar-benar privat, karena masih bisa diakses dengan nama yang di-mangled (`_NamaKelas__variabel`).
*   **Python tidak memiliki "privat" sejati** seperti bahasa lain. Konsep ini lebih tentang konvensi dan mekanisme untuk mengelola kompleksitas dalam proyek besar atau pewarisan.

Untuk kontrol akses yang lebih ketat dan validasi data, Python biasanya menggunakan **getters dan setters** (metode khusus untuk mengakses dan memodifikasi variabel).
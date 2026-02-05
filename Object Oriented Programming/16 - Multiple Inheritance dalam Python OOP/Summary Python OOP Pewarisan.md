# Multiple Inheritance dalam Python OOP

## Pengantar
**Multiple inheritance** adalah sebuah konsep dalam pemrograman berorientasi objek (OOP) di mana sebuah kelas dapat mewarisi atribut dan metode dari lebih dari satu kelas induk (superclass) secara bersamaan. Ini memungkinkan kelas anak untuk menggabungkan fungsionalitas dari beberapa sumber yang berbeda.

## Apa itu Multiple Inheritance?
Secara sederhana, multiple inheritance berarti sebuah kelas dapat menjadi turunan dari dua atau lebih kelas induk. Sebagai contoh, jika ada `Class A` dan `Class B`, `Class C` dapat mewarisi dari `Class A` dan `Class B`. Ini berarti objek dari `Class C` akan memiliki akses ke metode dan atribut yang didefinisikan di `Class A` maupun `Class B`.

### Contoh Dasar
Misalkan kita memiliki dua kelas induk:
*   **Class A**: Memiliki metode `method_A`.
*   **Class B**: Memiliki metode `method_B`.

Jika `Class C` mewarisi dari `Class A` dan `Class B`, maka sebuah objek dari `Class C` dapat memanggil `method_A()` dan `method_B()`.

```python
class A:
    def method_A(self):
        print("Ini adalah method A")

class B:
    def method_B(self):
        print("Ini adalah method B")

class C(A, B): # C mewarisi dari A dan B
    pass

obj_c = C()
obj_c.method_A() # Output: Ini adalah method A
obj_c.method_B() # Output: Ini adalah method B
```

Dalam contoh ini, `obj_c` yang merupakan objek dari `Class C` dapat mengakses `method_A` dari `Class A` dan `method_B` dari `Class B`, menunjukkan kemampuan multiple inheritance.

## Contoh Penerapan Multiple Inheritance (Studi Kasus Hero)
Multiple inheritance dapat digunakan untuk menciptakan objek yang memiliki berbagai peran atau karakteristik dari beberapa kategori yang berbeda. Contohnya adalah dalam pengembangan game, di mana sebuah karakter `Hero` bisa memiliki karakteristik `Team` dan `TypeHero`.

### Kelas `Team`
Kelas ini bertanggung jawab untuk mengelola informasi tim dari sebuah hero.
```python
class Team:
    def set_team(self, team_name):
        self.team = team_name

    def show_team(self):
        print(f"Tim: {self.team}")
```
Metode `set_team` digunakan untuk mengatur nama tim, dan `show_team` untuk menampilkan nama tim.

### Kelas `TypeHero`
Kelas ini bertanggung jawab untuk mengelola tipe atau posisi dari sebuah hero.
```python
class TypeHero:
    def set_type(self, hero_type):
        self.type = hero_type

    def show_type(self):
        print(f"Tipe Hero: {self.type}")
```
Metode `set_type` digunakan untuk mengatur tipe hero, dan `show_type` untuk menampilkan tipe hero.

### Kelas `Hero`
Kelas `Hero` mewarisi dari `Team` dan `TypeHero`, serta memiliki atribut dasarnya sendiri seperti nama dan kesehatan.
```python
class Hero(Team, TypeHero): # Hero mewarisi dari Team dan TypeHero
    def __init__(self, name, health):
        self.name = name
        self.health = health
```
Dengan mewarisi dari `Team` dan `TypeHero`, objek `Hero` secara otomatis mendapatkan semua metode dari kedua kelas tersebut.

### Demonstrasi Penggunaan
Setelah mendefinisikan kelas-kelas di atas, kita dapat membuat objek `Hero` dan menggunakan metode dari semua kelas induknya:
```python
ucuk = Hero("Ucuk", 100)

# Menggunakan metode dari kelas Team
ucuk.set_team("Merah")
ucuk.show_team() # Output: Tim: Merah

# Menggunakan metode dari kelas TypeHero
ucuk.set_type("Cundang")
ucuk.show_type() # Output: Tipe Hero: Cundang
```
Dalam contoh ini, objek `ucuk` (dari `Class Hero`) dapat memanggil `set_team`, `show_team` (dari `Class Team`), serta `set_type`, dan `show_type` (dari `Class TypeHero`).

## Fleksibilitas dan Peran Objek
Salah satu keuntungan utama multiple inheritance adalah fleksibilitas yang diberikannya. Sebuah objek yang dibuat dari kelas turunan (misalnya `ucuk` dari `Hero`) dapat berperan sebagai berbagai jenis objek tergantung pada konteks metode yang dipanggil:
*   Saat memanggil `ucuk.set_team()`, `ucuk` berperan sebagai objek `Team`.
*   Saat memanggil `ucuk.set_type()`, `ucuk` berperan sebagai objek `TypeHero`.
*   Secara default, `ucuk` adalah objek `Hero` dengan atribut `name` dan `health`.

Ini memungkinkan satu objek untuk memiliki "banyak bentuk" atau perilaku yang berbeda, yang dapat sangat berguna dalam desain sistem yang kompleks.

## Dukungan Python
Python adalah salah satu bahasa pemrograman yang secara langsung mendukung multiple inheritance. Namun, tidak semua bahasa pemrograman mendukung fitur ini secara langsung; beberapa mungkin menggunakan mekanisme lain untuk mencapai fungsionalitas serupa.

## Topik Lanjutan: Konflik Nama Metode
Salah satu tantangan dalam multiple inheritance adalah ketika dua atau lebih kelas induk memiliki metode dengan nama yang sama. Ini dapat menyebabkan ambiguitas tentang metode mana yang harus dipanggil oleh kelas anak. Penanganan konflik nama metode ini akan dibahas lebih lanjut dalam topik berikutnya.
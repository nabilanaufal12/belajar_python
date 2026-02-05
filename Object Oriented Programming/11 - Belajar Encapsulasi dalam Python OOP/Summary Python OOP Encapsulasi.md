# Belajar Encapsulasi dalam Python OOP

## Pengantar Encapsulasi

**Encapsulasi** adalah salah satu prinsip dasar dalam Pemrograman Berorientasi Objek (OOP) yang mengacu pada pembundelan data (atribut) dan metode (fungsi) yang beroperasi pada data tersebut ke dalam satu unit tunggal, yaitu objek. Tujuan utama dari enkapsulasi adalah untuk menyembunyikan detail implementasi internal objek dan melindungi data dari akses atau modifikasi yang tidak sah dari luar objek.

Dalam Python, konsep enkapsulasi tidak diterapkan secara ketat menggunakan kata kunci `public`, `protected`, atau `private` seperti pada bahasa lain (misalnya Java atau C++). Sebaliknya, Python menggunakan konvensi penamaan untuk menunjukkan tingkat akses yang diharapkan.

## Tingkat Akses Atribut dalam Python

Python mengklasifikasikan atribut (dan metode) ke dalam tiga kategori berdasarkan konvensi penamaan:

### 1. Atribut Publik (Public Attributes)

*   **Definisi**: Atribut publik adalah atribut yang dapat diakses dan dimodifikasi secara langsung dari mana saja, baik dari dalam kelas maupun dari luar kelas.
*   **Konvensi Penamaan**: Tidak ada awalan khusus. Contoh: `nama_atribut`.
*   **Contoh Penggunaan**:
    ```python
    class Hero:
        def __init__(self, name):
            self.name = name # Atribut publik

    hero1 = Hero("Gatot Kaca")
    print(hero1.name) # Akses langsung
    hero1.name = "Bima"
    print(hero1.name)
    ```

### 2. Atribut Terlindungi (Protected Attributes)

*   **Definisi**: Atribut terlindungi dimaksudkan untuk diakses dari dalam kelas itu sendiri atau dari kelas turunannya (subclass). Meskipun dapat diakses secara teknis dari luar kelas, konvensi ini menyiratkan bahwa akses langsung dari luar harus dihindari.
*   **Konvensi Penamaan**: Diawali dengan satu garis bawah (`_`). Contoh: `_nama_atribut`.
*   **Contoh Penggunaan**:
    ```python
    class Hero:
        def __init__(self, name, health):
            self.name = name
            self._health = health # Atribut terlindungi

    hero1 = Hero("Gatot Kaca", 100)
    print(hero1._health) # Secara teknis bisa diakses, tapi tidak disarankan
    hero1._health = 90 # Bisa dimodifikasi, tapi melanggar konvensi
    print(hero1._health)
    ```

### 3. Atribut Privat (Private Attributes)

*   **Definisi**: Atribut privat dimaksudkan untuk tidak dapat diakses secara langsung dari luar kelas. Python menerapkan mekanisme "name mangling" untuk membuat akses langsung menjadi lebih sulit.
*   **Konvensi Penamaan**: Diawali dengan dua garis bawah (`__`). Contoh: `__nama_atribut`.
*   **Name Mangling**: Ketika sebuah atribut diawali dengan `__`, Python secara otomatis mengubah namanya menjadi `_NamaKelas__nama_atribut`. Ini membuat atribut tersebut tidak dapat diakses dengan nama aslinya dari luar kelas.
*   **Contoh Penggunaan**:
    ```python
    class Hero:
        def __init__(self, name, health, attack_power):
            self.name = name
            self._health = health
            self.__attack_power = attack_power # Atribut privat

    hero1 = Hero("Gatot Kaca", 100, 50)
    # print(hero1.__attack_power) # Akan menyebabkan AttributeError

    # Akses melalui name mangling (tidak disarankan, menunjukkan bahwa tidak sepenuhnya privat)
    print(hero1._Hero__attack_power) # Output: 50
    ```

## Getters dan Setters

Untuk mengontrol akses dan modifikasi atribut terlindungi atau privat secara aman dan terstruktur, praktik terbaik dalam OOP adalah menggunakan metode **getter** dan **setter**.

*   **Getter**: Metode yang digunakan untuk mendapatkan (membaca) nilai dari suatu atribut.
*   **Setter**: Metode yang digunakan untuk mengatur (mengubah) nilai dari suatu atribut, seringkali dengan validasi atau logika tambahan.

### Contoh Implementasi Getters dan Setters

```python
class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self._health = health
        self.__attack_power = attack_power

    # Getter untuk _health
    def getHealth(self):
        return self._health

    # Setter untuk _health dengan validasi
    def setHealth(self, new_health):
        if new_health < 0:
            print("Health tidak bisa kurang dari 0!")
        else:
            self._health = new_health

    # Getter untuk __attack_power
    def getAttackPower(self):
        return self.__attack_power

    # Setter untuk __attack_power dengan validasi
    def setAttackPower(self, new_power):
        if new_power < 0:
            print("Attack Power tidak bisa kurang dari 0!")
        else:
            self.__attack_power = new_power

# Membuat objek Hero
hero1 = Hero("Gatot Kaca", 100, 50)

# Mengakses atribut menggunakan getter
print(f"Nama: {hero1.name}")
print(f"Health: {hero1.getHealth()}")
print(f"Attack Power: {hero1.getAttackPower()}")

# Mengubah atribut menggunakan setter
hero1.setHealth(80)
hero1.setAttackPower(60)
print(f"Health baru: {hero1.getHealth()}")
print(f"Attack Power baru: {hero1.getAttackPower()}")

# Mencoba mengubah dengan nilai tidak valid
hero1.setHealth(-10) # Output: Health tidak bisa kurang dari 0!
hero1.setAttackPower(-5) # Output: Attack Power tidak bisa kurang dari 0!
```

## Manfaat Encapsulasi

*   **Kontrol Akses Data**: Memungkinkan pengembang untuk mengontrol bagaimana data di dalam objek diakses dan dimodifikasi, mencegah perubahan yang tidak diinginkan.
*   **Validasi Data**: Setter dapat menyertakan logika validasi untuk memastikan bahwa data yang dimasukkan memenuhi kriteria tertentu, menjaga integritas data.
*   **Penyembunyian Implementasi (Information Hiding)**: Detail internal objek dapat disembunyikan dari pengguna luar, yang hanya perlu berinteraksi melalui antarmuka publik (metode). Ini membuat kode lebih mudah dipelihara dan diubah tanpa memengaruhi bagian lain dari program.
*   **Fleksibilitas**: Memungkinkan perubahan pada implementasi internal kelas tanpa memengaruhi kode yang menggunakan kelas tersebut, selama antarmuka publik tetap sama.
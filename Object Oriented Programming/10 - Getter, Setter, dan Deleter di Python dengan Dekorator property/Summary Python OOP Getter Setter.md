# Getter, Setter, dan Deleter di Python dengan Dekorator `property`

Dalam pemrograman berorientasi objek (OOP), **enkapsulasi** adalah prinsip penting untuk menyembunyikan detail implementasi internal suatu objek dan mengontrol akses ke datanya. Python menawarkan cara yang elegan dan "Pythonic" untuk mencapai enkapsulasi menggunakan **dekorator `property`**, yang memungkinkan kita mendefinisikan getter, setter, dan deleter untuk atribut kelas.

## Pengantar Enkapsulasi Tradisional

Secara tradisional, dalam bahasa seperti Java atau C++, enkapsulasi sering dilakukan dengan membuat atribut kelas menjadi privat (misalnya, menggunakan `__` di Python untuk konvensi "name mangling") dan menyediakan metode publik (getter dan setter) untuk mengakses atau memodifikasi atribut tersebut.

Contoh enkapsulasi tradisional di Python:
```python
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health  # Atribut privat
        self.__armor = armor    # Atribut privat

    def get_health(self): # Metode getter
        return self.__health
```
Dengan pendekatan ini, untuk mendapatkan nilai `health`, kita harus memanggil `sniper.get_health()`.

## Masalah dengan Atribut Dinamis dan Akses Langsung

Ketika kita memiliki atribut yang nilainya seharusnya merupakan hasil komputasi atau bergantung pada atribut lain, mendeklarasikannya sebagai atribut biasa dapat menimbulkan masalah. Misalnya, jika kita memiliki atribut `info` yang menampilkan nama dan `health` hero:
```python
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # Atribut info diinisialisasi sekali
        self.info = f"Nama: {self.name}\n\tHealth: {self.__health}"

# ...
sniper = Hero("sniper", 100, 10)
print(sniper.info) # Output: Nama: sniper\n\tHealth: 100
```
Masalah muncul jika kita mencoba mengubah `info` secara langsung (`sniper.info = "adalah info"`). Ini memungkinkan klien untuk memodifikasi informasi yang seharusnya hanya bersifat tampilan atau turunan, padahal kita ingin `info` tetap konsisten dan tidak dapat diubah secara langsung. Selain itu, jika atribut dasar seperti `name` berubah, `info` tidak akan otomatis diperbarui.

## Dekorator `@property` untuk Getter

Python menyediakan **dekorator `@property`** untuk mengatasi masalah ini. Dekorator ini memungkinkan sebuah metode untuk diperlakukan seperti atribut, sehingga dapat diakses tanpa tanda kurung `()`.

### Cara Menggunakan `@property`
1.  Definisikan sebuah metode dengan nama yang sama dengan atribut yang ingin Anda buat sebagai properti.
2.  Tambahkan dekorator `@property` di atas definisi metode tersebut.
3.  Metode ini akan berfungsi sebagai **getter** untuk properti tersebut.

```python
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property # Dekorator property
    def info(self):
        # Logika dinamis di dalam getter
        return f"Nama: {self.name}\n\tHealth: {self.__health}"

# ...
sniper = Hero("sniper", 100, 10)
print(sniper.info) # Akses seperti atribut, bukan metode

# Keuntungan: Jika name berubah, info akan otomatis diperbarui
sniper.name = "dadang"
print(sniper.info) # Output: Nama: dadang\n\tHealth: 100
```
Dengan `@property`, `info` sekarang adalah properti yang nilainya dihitung secara dinamis setiap kali diakses, dan tidak dapat diubah secara langsung oleh klien.

Kita juga dapat menggunakan `@property` untuk atribut privat seperti `__armor`:
```python
class Hero:
    # ... (init dan atribut lainnya)

    @property
    def armor(self):
        # Ini adalah getter untuk __armor
        return self.__armor

# ...
sniper = Hero("sniper", 100, 10)
print(sniper.armor) # Mengakses __armor melalui properti
```
Jika hanya getter yang didefinisikan, mencoba mengubah nilai properti (`sniper.armor = 50`) akan menghasilkan kesalahan `AttributeError`, karena tidak ada mekanisme untuk mengatur nilainya.

## Dekorator `@<property_name>.setter`

Untuk memungkinkan modifikasi nilai properti, kita perlu mendefinisikan **setter**. Setter didefinisikan dengan membuat metode lain dengan nama yang sama dengan properti, tetapi didekorasi dengan `@<property_name>.setter`.

### Cara Menggunakan `@<property_name>.setter`
1.  Definisikan metode baru dengan nama yang sama dengan properti (misalnya, `armor`).
2.  Dekorasi metode ini dengan `@<property_name>.setter` (misalnya, `@armor.setter`).
3.  Metode ini harus menerima satu argumen tambahan (selain `self`) yang akan menjadi nilai baru yang ingin diatur.

```python
class Hero:
    # ... (init dan atribut lainnya)

    @property
    def armor(self):
        return self.__armor

    @armor.setter # Dekorator setter
    def armor(self, new_armor): # new_armor adalah nilai yang akan diatur
        self.__armor = new_armor

# ...
sniper = Hero("sniper", 100, 10)
print(f"Armor awal: {sniper.armor}") # Output: Armor awal: 10
sniper.armor = 50 # Menggunakan setter seperti menetapkan nilai ke atribut
print(f"Armor setelah diubah: {sniper.armor}") # Output: Armor setelah diubah: 50
```
Keuntungan utama dari pendekatan ini adalah **kesederhanaan di sisi klien**. Pengguna kelas dapat mengubah nilai `armor` seolah-olah itu adalah atribut publik biasa (`sniper.armor = 50`), tanpa perlu memanggil metode `set_armor()` secara eksplisit. Namun, di balik layar, logika setter yang kita definisikan akan dieksekusi, memungkinkan validasi atau pemrosesan tambahan jika diperlukan.

## Dekorator `@<property_name>.deleter`

Selain getter dan setter, Python juga memungkinkan kita untuk mendefinisikan **deleter** untuk sebuah properti. Deleter akan dipanggil ketika properti dihapus menggunakan pernyataan `del`.

### Cara Menggunakan `@<property_name>.deleter`
1.  Definisikan metode baru dengan nama yang sama dengan properti.
2.  Dekorasi metode ini dengan `@<property_name>.deleter` (misalnya, `@armor.deleter`).
3.  Metode ini tidak menerima argumen tambahan selain `self`.

```python
class Hero:
    # ... (init, getter, dan setter untuk armor)

    @armor.deleter # Dekorator deleter
    def armor(self):
        print("Armor dihapus!")
        self.__armor = None # Mengatur atribut internal menjadi None atau menghapusnya

# ...
sniper = Hero("sniper", 100, 10)
print(f"Armor sebelum dihapus: {sniper.armor}")
del sniper.armor # Memanggil deleter
print(f"Armor setelah dihapus: {sniper.armor}") # Output: Armor setelah dihapus: None
```
Penggunaan deleter dapat berguna untuk membersihkan sumber daya atau mengatur ulang status objek ketika properti tertentu tidak lagi diperlukan.

## Perbandingan: Pythonic vs. Tradisional

Pendekatan Pythonic menggunakan dekorator `property` untuk getter, setter, dan deleter menawarkan beberapa keuntungan dibandingkan dengan metode getter/setter tradisional:
*   **Sintaksis yang Lebih Bersih**: Kode klien terlihat lebih seperti mengakses atribut daripada memanggil metode, membuat kode lebih mudah dibaca dan dipahami.
*   **Fleksibilitas**: Kita dapat memulai dengan atribut publik sederhana, dan kemudian dengan mudah mengubahnya menjadi properti dengan getter/setter/deleter tanpa mengubah kode klien yang sudah ada.
*   **Enkapsulasi yang Efektif**: Meskipun terlihat seperti atribut publik, properti tetap memberikan kontrol penuh atas bagaimana data diakses dan dimodifikasi, memungkinkan validasi dan logika bisnis lainnya di balik layar.

Secara keseluruhan, dekorator `property` adalah alat yang ampuh di Python untuk mencapai enkapsulasi yang elegan dan efisien.
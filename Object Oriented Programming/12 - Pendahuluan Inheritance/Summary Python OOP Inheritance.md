# Belajar Python OOP: Pendahuluan Inheritance

## Pendahuluan Inheritance

**Inheritance** (Pewarisan) adalah salah satu pilar utama dalam pemrograman berorientasi objek (OOP) yang memungkinkan sebuah kelas (disebut **kelas anak** atau *subclass*) untuk mewarisi atribut dan metode dari kelas lain (disebut **kelas induk** atau *superclass*). Konsep ini mempromosikan penggunaan kembali kode (*code reusability*) dan menciptakan hubungan "adalah sebuah" (*is-a relationship*) antara kelas-kelas.

### Konsep Kunci dalam Inheritance

1.  **Kelas Induk (Parent Class / Superclass)**
    *   Kelas yang atribut dan metodenya diwariskan kepada kelas lain.
    *   Mendefinisikan perilaku dan karakteristik umum.

2.  **Kelas Anak (Child Class / Subclass)**
    *   Kelas yang mewarisi atribut dan metode dari kelas induk.
    *   Dapat menambahkan atribut dan metode baru, atau mengubah (meng-*override*) metode yang diwarisi dari kelas induk.
    *   Mewarisi semua anggota publik dan terlindungi dari kelas induk.

3.  **Method Overriding (Mengganti Metode)**
    *   Kemampuan kelas anak untuk menyediakan implementasi spesifik untuk metode yang sudah didefinisikan di kelas induknya.
    *   Ketika metode yang sama dipanggil pada objek kelas anak, implementasi kelas anak yang akan dieksekusi.

4.  **Fungsi `super()`**
    *   Digunakan dalam kelas anak untuk memanggil metode dari kelas induk.
    *   Sering digunakan dalam konstruktor (`__init__`) kelas anak untuk memastikan bahwa konstruktor kelas induk juga dipanggil, menginisialisasi atribut yang diwarisi.
    *   Memungkinkan kelas anak untuk memperluas fungsionalitas kelas induk tanpa sepenuhnya menggantinya.

### Manfaat Inheritance

*   **Penggunaan Kembali Kode (*Code Reusability*)**: Mengurangi duplikasi kode karena fungsionalitas umum dapat didefinisikan sekali di kelas induk dan digunakan oleh banyak kelas anak.
*   **Ekstensibilitas (*Extensibility*)**: Memudahkan penambahan fitur baru atau modifikasi perilaku tanpa mengubah kode kelas induk.
*   **Organisasi Kode (*Code Organization*)**: Membantu dalam menyusun kode secara hierarkis, mencerminkan hubungan dunia nyata antara objek.
*   **Pemeliharaan (*Maintainability*)**: Perubahan pada fungsionalitas umum hanya perlu dilakukan di satu tempat (kelas induk), yang menyederhanakan pemeliharaan.

### Contoh Sederhana Inheritance di Python

```python
# Kelas Induk (Superclass)
class Hewan:
    def __init__(self, nama):
        self.nama = nama
        print(f"{self.nama} adalah hewan.")

    def bersuara(self):
        print("Hewan ini bersuara.")

# Kelas Anak (Subclass) yang mewarisi dari Hewan
class Anjing(Hewan):
    def __init__(self, nama, ras):
        # Memanggil konstruktor kelas induk menggunakan super()
        super().__init__(nama)
        self.ras = ras
        print(f"{self.nama} adalah anjing ras {self.ras}.")

    # Mengganti (override) metode bersuara dari kelas induk
    def bersuara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# Kelas Anak lain
class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna
        print(f"{self.nama} adalah kucing berwarna {self.warna}.")

    def bersuara(self):
        print(f"{self.nama} mengeong: Meong meong!")

# Membuat objek
hewan_umum = Hewan("Binatang")
hewan_umum.bersuara()
# Output:
# Binatang adalah hewan.
# Hewan ini bersuara.

anjing_saya = Anjing("Buddy", "Golden Retriever")
anjing_saya.bersuara()
# Output:
# Buddy adalah hewan.
# Buddy adalah anjing ras Golden Retriever.
# Buddy menggonggong: Guk guk!

kucing_saya = Kucing("Milo", "Oranye")
kucing_saya.bersuara()
# Output:
# Milo adalah hewan.
# Milo adalah kucing berwarna Oranye.
# Milo mengeong: Meong meong!
```
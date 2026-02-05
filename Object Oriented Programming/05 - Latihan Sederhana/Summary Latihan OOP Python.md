# Belajar Python OOP: Latihan Sederhana

## Gambaran Umum

Catatan ini merangkum konsep dasar Object-Oriented Programming (OOP) di Python melalui sebuah latihan sederhana. Fokusnya adalah memahami bagaimana mendefinisikan kelas, membuat objek, serta mengelola atribut dan metode untuk merepresentasikan entitas dunia nyata dalam kode. Latihan ini akan menggunakan contoh kelas `Mahasiswa` untuk mengilustrasikan prinsip-prinsip OOP dasar.

## Konsep Dasar OOP dalam Python

### 1. Kelas (Class)

**Kelas** adalah cetak biru (blueprint) atau templat untuk membuat objek. Kelas mendefinisikan struktur data (atribut) dan perilaku (metode) yang akan dimiliki oleh objek-objek yang dibuat darinya. Dalam Python, kelas didefinisikan menggunakan kata kunci `class`.

### 2. Objek (Object)

**Objek** adalah instansi konkret dari sebuah kelas. Setiap objek memiliki atributnya sendiri dan dapat memanggil metode yang didefinisikan dalam kelasnya. Objek dibuat dengan memanggil kelas seperti fungsi.

### 3. Atribut (Attributes)

**Atribut** adalah variabel yang menyimpan data atau karakteristik dari sebuah objek. Atribut mendefinisikan "apa" yang dimiliki oleh objek. Ada dua jenis atribut utama:
*   **Atribut Instansi**: Unik untuk setiap objek (instansi) dari kelas. Didefinisikan di dalam metode `__init__` menggunakan `self`.
*   **Atribut Kelas**: Dibagi oleh semua objek dari kelas. Didefinisikan langsung di dalam kelas tetapi di luar metode apa pun.

### 4. Metode (Methods)

**Metode** adalah fungsi yang terkait dengan sebuah objek. Metode mendefinisikan "apa" yang dapat dilakukan oleh objek. Metode selalu memiliki parameter pertama `self`, yang merujuk pada instansi objek itu sendiri.

### 5. Konstruktor (`__init__`)

Metode khusus `__init__` (dibaca "dunder init") adalah **konstruktor** dalam Python. Metode ini secara otomatis dipanggil saat sebuah objek baru dibuat (diinstansiasi) dari sebuah kelas. Tujuannya adalah untuk menginisialisasi atribut-atribut objek.

### 6. Parameter `self`

Parameter `self` adalah konvensi dalam Python yang merujuk pada instansi objek itu sendiri. Ketika sebuah metode dipanggil pada objek, Python secara otomatis meneruskan objek tersebut sebagai argumen pertama ke metode tersebut, yang diterima oleh parameter `self`. Ini memungkinkan metode untuk mengakses dan memodifikasi atribut objek.

## Latihan OOP Sederhana: Kelas `Mahasiswa`

Untuk memahami konsep-konsep di atas, kita akan membuat kelas `Mahasiswa` yang merepresentasikan seorang mahasiswa.

### Studi Kasus

Kita ingin membuat program yang dapat menyimpan dan menampilkan informasi dasar tentang beberapa mahasiswa, seperti nama, Nomor Induk Mahasiswa (NIM), dan jurusan.

### Definisi Kelas `Mahasiswa`

Kelas `Mahasiswa` akan memiliki:
*   **Atribut Instansi**: `nama`, `nim`, `jurusan`.
*   **Metode**:
    *   `__init__(self, nama, nim, jurusan)`: Untuk menginisialisasi objek `Mahasiswa` dengan nama, NIM, dan jurusan yang diberikan.
    *   `tampilkan_info(self)`: Untuk menampilkan semua informasi detail tentang mahasiswa tersebut.

### Implementasi Kode

```python
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        print(f"Objek Mahasiswa '{self.nama}' berhasil dibuat.") #

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print("-" * 20) #
```

### Membuat Objek (Instansiasi)

Setelah kelas `Mahasiswa` didefinisikan, kita dapat membuat beberapa objek mahasiswa dari kelas tersebut. Setiap objek akan menjadi instansi unik dari `Mahasiswa`.

```python
# Membuat objek mahasiswa pertama
mahasiswa1 = Mahasiswa("Budi Santoso", "12345", "Teknik Informatika")

# Membuat objek mahasiswa kedua
mahasiswa2 = Mahasiswa("Siti Aminah", "67890", "Sistem Informasi")
```

### Mengakses Atribut dan Memanggil Metode

Kita dapat mengakses atribut objek menggunakan notasi titik (`.`) dan memanggil metode objek dengan cara yang sama.

```python
# Mengakses atribut objek
print(f"Nama mahasiswa1: {mahasiswa1.nama}") # Output: Nama mahasiswa1: Budi Santoso
print(f"Jurusan mahasiswa2: {mahasiswa2.jurusan}") # Output: Jurusan mahasiswa2: Sistem Informasi

# Memanggil metode objek
print("\nInformasi Mahasiswa 1:")
mahasiswa1.tampilkan_info() #

print("Informasi Mahasiswa 2:")
mahasiswa2.tampilkan_info() #
```

### Modifikasi Atribut

Atribut objek dapat dimodifikasi setelah objek dibuat, kecuali jika atribut tersebut didefinisikan sebagai *private* (dengan konvensi `__` di awal nama atribut).

```python
# Memodifikasi atribut mahasiswa1
mahasiswa1.jurusan = "Manajemen Bisnis" #
print("\nInformasi Mahasiswa 1 setelah diubah:")
mahasiswa1.tampilkan_info()
```
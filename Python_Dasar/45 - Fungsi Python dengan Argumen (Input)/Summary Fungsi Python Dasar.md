# Fungsi Python dengan Argumen (Input)

## Pendahuluan
Fungsi dalam Python dapat dibuat lebih dinamis dan fleksibel dengan menerima **argumen** (sering juga disebut **parameter** atau **input**). Argumen memungkinkan fungsi untuk memproses data yang berbeda setiap kali dipanggil, alih-alih selalu melakukan operasi yang sama secara statis.

## Konsep Dasar Argumen
Argumen adalah nilai yang diteruskan ke fungsi saat fungsi tersebut dipanggil. Nilai ini kemudian dapat digunakan di dalam "badan fungsi" (function body) sebagai variabel lokal.

### Struktur Fungsi dengan Argumen
Struktur dasar untuk mendefinisikan fungsi dengan argumen adalah sebagai berikut:
```python
def nama_fungsi(argumen_1, argumen_2, ...):
    # Badan fungsi
    # Argumen dapat digunakan di sini
```
-   `def`: Kata kunci untuk mendefinisikan fungsi.
-   `nama_fungsi`: Nama unik untuk fungsi tersebut.
-   `()`: Tanda kurung ini digunakan untuk menempatkan argumen.
-   `argumen_1, argumen_2, ...`: Variabel yang akan menerima nilai saat fungsi dipanggil. Variabel ini "hidup" hanya di dalam fungsi tersebut.

**Tips Penamaan Argumen**: Disarankan untuk menggunakan nama argumen yang deskriptif (misalnya `nama` daripada `n`) agar kode lebih mudah dibaca dan dipahami.

## Contoh Penggunaan Argumen

### 1. Argumen String Tunggal
Contoh fungsi `hello_world` yang menerima satu argumen berupa string (`nama`) dan mencetaknya:

```python
def hello_world(nama):
    '''Fungsi hello world menerima input dengan variabel nama'''
    print(f"Selamat datang dunia wahai {nama}") # src-1:03:49, src-2:p.2

hello_world("Ucup") # src-1:04:30
hello_world("Asep") # src-2:p.2
```
Ketika `hello_world("Ucup")` dipanggil, string `"Ucup"` akan diteruskan ke variabel `nama` di dalam fungsi, dan fungsi akan mencetak "Selamat datang dunia wahai Ucup".

### 2. Argumen Numerik Ganda
Fungsi dapat menerima lebih dari satu argumen. Contoh fungsi `tambah` yang menerima dua argumen numerik (`angka1` dan `angka2`) untuk melakukan operasi penjumlahan:

```python
def tambah(angka1, angka2):
    '''Fungsi tambah'''
    hasil = angka1 + angka2 # src-1:06:00, src-2:p.3
    print(f"{angka1} + {angka2} = {hasil}") # src-1:06:15, src-2:p.3

tambah(1, 5) # src-1:06:30
tambah(10000, 1) # src-1:06:30
```
Argumen tidak terbatas pada string atau angka; mereka bisa berupa tipe data apa pun, termasuk boolean atau list.

### 3. Argumen Berupa List (Daftar)
Saat meneruskan list sebagai argumen, penting untuk memahami perilaku "pass by reference" di Python. Jika list dimodifikasi di dalam fungsi, perubahan tersebut akan memengaruhi list asli di luar fungsi. Untuk menghindari ini, gunakan metode `.copy()`.

Contoh fungsi `say_hi` yang menerima list peserta:
```python
def say_hi(list_peserta):
    '''Fungsi say hi'''
    # Gunakan .copy() agar list asli tidak berubah
    data_peserta = list_peserta.copy() # src-1:08:40, src-2:p.4
    
    for peserta in data_peserta: # src-1:09:00
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup", "Otong", "Dudung"] # src-1:07:50
say_hi(anggota_boyband) # src-1:08:20
```
Dalam contoh ini, `anggota_boyband` adalah list di luar fungsi. Ketika `say_hi(anggota_boyband)` dipanggil, `list_peserta` di dalam fungsi akan merujuk ke objek list yang sama. Dengan menggunakan `data_peserta = list_peserta.copy()`, kita membuat salinan list, sehingga modifikasi pada `data_peserta` tidak akan memengaruhi `anggota_boyband` yang asli.

## Kesimpulan dan Lanjutan
Menggunakan argumen membuat fungsi menjadi alat yang sangat kuat dan dapat digunakan kembali dalam pemrograman. Setelah memahami cara kerja fungsi dengan argumen, langkah selanjutnya adalah mempelajari **fungsi dengan nilai kembalian (return)**, yang memungkinkan fungsi untuk mengembalikan hasil komputasi.
# Pengenalan Fungsi dalam Python

Fungsi adalah blok kode yang terorganisir dan dapat digunakan kembali, dirancang untuk melakukan tugas tertentu. Penggunaan fungsi bertujuan untuk membuat program lebih ringkas, mudah dibaca, dan efisien.

## 1. Apa itu Fungsi?

Dalam pemrograman, fungsi sering disebut dengan beberapa istilah lain seperti **`function`**, **`method`**, atau **`subroutine`**. Konsep utamanya adalah mengelompokkan serangkaian instruksi ke dalam satu unit yang dapat dipanggil kapan saja.

## 2. Mengapa Menggunakan Fungsi?

Tujuan utama penggunaan fungsi adalah untuk menerapkan prinsip **`Don't Repeat Yourself` (DRY)**, yaitu menghindari pengulangan kode yang sama. Manfaat spesifik dari penggunaan fungsi meliputi:

*   **Meringkas Kode**: Mengubah bagian kode yang panjang dan berulang menjadi satu panggilan fungsi yang sederhana. Ini membuat program terlihat lebih bersih dan mudah dipahami.
*   **Reusabilitas (Dapat Digunakan Kembali)**: Setelah sebuah fungsi didefinisikan, ia dapat dipanggil berkali-kali di berbagai bagian program tanpa perlu menulis ulang kode di dalamnya.
*   **Kemudahan Pemeliharaan**: Jika ada perubahan yang perlu dilakukan pada logika kode yang berulang, perubahan hanya perlu dilakukan di satu tempat (di dalam definisi fungsi). Semua pemanggilan fungsi akan otomatis mengikuti perubahan tersebut.

## 3. Cara Membuat Fungsi di Python

Untuk membuat fungsi di Python, kita menggunakan kata kunci **`def`** (singkatan dari `definition`).

### Sintaks Dasar

Struktur dasar untuk mendefinisikan fungsi adalah sebagai berikut:
```python
def nama_fungsi():
    # Isi program di sini
    # Blok kode ini akan dieksekusi saat fungsi dipanggil
```

*   **`def`**: Kata kunci untuk memulai definisi fungsi.
*   **`nama_fungsi`**: Nama unik untuk fungsi Anda. Ikuti konvensi penamaan Python (huruf kecil, kata dipisahkan oleh *underscore*).
*   **`()`**: Tanda kurung setelah nama fungsi, yang nantinya akan digunakan untuk argumen atau parameter.
*   **`:`**: Titik dua yang menandai awal dari blok kode fungsi.
*   **Indentation**: Semua baris kode di dalam fungsi harus di-*indent* (menjorok ke dalam) dengan jumlah spasi yang sama (biasanya 4 spasi).

### Contoh Fungsi Sederhana

Berikut adalah contoh fungsi `hello_world` yang menampilkan beberapa pesan ke konsol:
```python
def hello_world():
    # Ini adalah docstring atau komentar untuk menjelaskan fungsi
    print("Hello world")
    print("Kepada Ucup Surucup")
    print("Dan juga kepada Otong Surotong")
```

## 4. Memanggil Fungsi

Setelah sebuah fungsi didefinisikan, Anda dapat memanggilnya dengan menulis nama fungsi diikuti dengan tanda kurung `()`.

```python
# Definisi fungsi (seperti di atas)
def hello_world():
    print("Hello world")
    print("Kepada Ucup Surucup")
    print("Dan juga kepada Otong Surotong")

# Memanggil fungsi
hello_world() # Memanggil fungsi pertama kali
hello_world() # Memanggil fungsi kedua kali
```

Setiap kali `hello_world()` dipanggil, semua baris kode di dalamnya akan dieksekusi. Jika isi fungsi diubah, semua pemanggilan fungsi akan mencerminkan perubahan tersebut secara otomatis.

## 5. Aturan Penting: Urutan Definisi dan Pemanggilan

Python adalah bahasa **`interpreted language`**. Ini berarti kode dieksekusi baris per baris dari atas ke bawah. Oleh karena itu, ada aturan krusial mengenai urutan definisi dan pemanggilan fungsi:

**Fungsi harus didefinisikan terlebih dahulu SEBELUM dipanggil**.

Jika Anda mencoba memanggil fungsi sebelum Python membaca dan memproses definisinya, akan terjadi kesalahan `NameError` karena fungsi tersebut belum dikenal.

### Contoh Urutan yang Salah (Akan Error)
```python
# Ini akan ERROR karena fungsi() dipanggil sebelum didefinisikan
# fungsi() # <--- NameError: name 'fungsi' is not defined

def fungsi():
    print("Ini adalah fungsi")
```

### Contoh Urutan yang Benar
```python
# Definisi fungsi harus di atas pemanggilan
def fungsi():
    print("Ini adalah fungsi")

# Ini BARU BENAR, fungsi dipanggil setelah didefinisikan
fungsi()
```

## 6. Langkah Selanjutnya

Setelah memahami fungsi dasar tanpa parameter, langkah selanjutnya adalah mempelajari fungsi yang dapat menerima **argumen** atau **parameter**. Ini memungkinkan fungsi untuk bekerja dengan data yang berbeda setiap kali dipanggil, menjadikannya lebih fleksibel dan kuat.
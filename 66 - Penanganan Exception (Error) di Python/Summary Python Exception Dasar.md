# Penanganan Exception (Error) di Python

Penanganan *exception* (atau *error*) adalah mekanisme penting dalam pemrograman untuk membuat aplikasi lebih tangguh dan tidak mudah *crash*. Ini memungkinkan program untuk merespons kesalahan tak terduga dengan cara yang terkontrol, daripada berhenti secara tiba-tiba.

## Memahami Jenis-jenis Error

Dalam Python, terdapat dua jenis utama kesalahan yang dapat terjadi:

### 1. Syntax Error
**Syntax Error** adalah kesalahan penulisan atau tata bahasa dalam kode. Program tidak akan dapat dijalankan sama sekali jika terdapat *syntax error*. Ini biasanya terdeteksi oleh *interpreter* Python sebelum eksekusi dimulai.
*   **Contoh**: Menulis `print "halo"` tanpa tanda kurung pada Python 3.

### 2. Runtime Error (Exception)
**Runtime Error**, sering disebut juga **Exception**, adalah kesalahan yang terjadi saat program sedang berjalan. Kode secara *syntax* sudah benar, tetapi kondisi tertentu saat eksekusi menyebabkan masalah. Jika tidak ditangani, *runtime error* akan menghentikan program secara mendadak.
*   **Contoh**:
    *   **`ZeroDivisionError`**: Terjadi ketika mencoba membagi angka dengan nol.
    *   **`FileNotFoundError`**: Terjadi ketika program mencoba membuka file yang tidak ada.
    *   **`ValueError`**: Terjadi ketika fungsi menerima argumen dengan tipe yang benar tetapi nilai yang tidak sesuai (misalnya, `int("abc")`).

Penanganan *exception* berfokus pada *runtime error* ini, memastikan program dapat melanjutkan eksekusi atau memberikan pesan kesalahan yang informatif kepada pengguna.

## Mekanisme `try` dan `except`

Mekanisme dasar untuk menangani *runtime error* adalah menggunakan blok `try` dan `except`.

*   **`try`**: Blok kode yang berpotensi menimbulkan *exception* ditempatkan di sini. Python akan mencoba menjalankan kode di dalam blok `try`.
*   **`except`**: Jika *exception* terjadi di dalam blok `try`, eksekusi akan langsung melompat ke blok `except`. Kode di dalam blok `except` akan dijalankan untuk menangani *exception* tersebut.

**Contoh Sederhana Pembagian dengan Nol:**
```python
input_user = int(input("Masukkan angka: "))
hasil = 0

try:
    hasil = 10 / input_user
    print(f"Hasil = {hasil}")
except:
    print("Input tidak boleh nol!") # Pesan kesalahan jika terjadi exception
    hasil = float('nan') # Mengatur hasil menjadi Not a Number
print(f"Hasil akhir: {hasil}")
```
Dalam contoh ini, jika `input_user` adalah 0, `ZeroDivisionError` akan terjadi, dan program akan mencetak "Input tidak boleh nol!" tanpa *crash*.

## Menangani Exception Spesifik

Kita dapat menangani berbagai jenis *exception* secara terpisah untuk memberikan penanganan yang lebih spesifik dan informatif.

```python
while True:
    try:
        angka = int(input("Masukkan angka pembagi: "))
        hasil = 10 / angka
        print(f"Hasil = {hasil}")
        break # Keluar dari loop jika berhasil
    except ValueError:
        print("Yang Anda masukkan BUKAN ANGKA!") # Menangani input non-numeric
    except ZeroDivisionError:
        print("Angka tidak boleh NOL!") # Menangani pembagian dengan nol
    except Exception as e:
        print(f"Error tidak dikenal: {e}") # Menangani exception lain yang tidak spesifik
```
*   Setiap blok `except` dapat menangani jenis *exception* tertentu. Jika `ValueError` terjadi, blok `except ValueError` akan dieksekusi. Jika `ZeroDivisionError` terjadi, blok `except ZeroDivisionError` akan dieksekusi.
*   Blok `except Exception as e` adalah penangkap *exception* umum. Ini akan menangkap *exception* apa pun yang tidak ditangani oleh blok `except` sebelumnya. Variabel `e` akan berisi objek *exception* yang memberikan detail tentang kesalahan.

## Struktur Lengkap `try-except-else-finally`

Python menyediakan struktur yang lebih lengkap untuk penanganan *exception* dengan menambahkan blok `else` dan `finally`.

*   **`try`**: Kode yang dicoba (berpotensi *error*).
*   **`except`**: Jalan jika terjadi *error*.
*   **`else`**: Blok ini akan dieksekusi **hanya jika** kode di dalam blok `try` berhasil dijalankan tanpa *exception*.
*   **`finally`**: Blok ini **akan selalu dieksekusi**, terlepas dari apakah *exception* terjadi atau tidak. Ini sangat berguna untuk operasi pembersihan (misalnya, menutup file atau koneksi database).

**Contoh dengan Penanganan File:**
```python
file = None # Inisialisasi file agar terdefinisi di luar blok try
try:
    # Coba membuka file dalam mode baca ('r')
    file = open("data_test.txt", 'r')
    print("File berhasil dibuka")
except FileNotFoundError:
    print("File tidak ditemukan! Membuat file baru...")
    # Jika file tidak ditemukan, buat file baru dalam mode tulis ('w')
    with open("data_test.txt", 'w', encoding='utf8') as new_file:
        new_file.write("Ini adalah file baru.\n")
    print("File baru berhasil dibuat.")
else:
    # Jika tidak ada exception (file ditemukan dan dibuka), baca isinya
    print("Membaca isi file:")
    print(file.read())
finally:
    # Pastikan file ditutup, baik ada error maupun tidak
    if file and not file.closed:
        file.close()
        print("File ditutup (Cleanup).")
print("Akhir dari program.")
```
Dalam contoh ini, jika `data_test.txt` tidak ada, blok `except FileNotFoundError` akan membuat file baru. Jika file ada, blok `else` akan membaca isinya. Blok `finally` akan selalu memastikan file ditutup dengan benar.

## Membuat dan Mengangkat Exception Kustom (`raise`)

Selain menangani *exception* bawaan Python, kita juga bisa membuat dan mengangkat *exception* kita sendiri menggunakan kata kunci `raise`. Ini berguna untuk memberlakukan aturan atau kondisi tertentu dalam kode kita.

**Contoh Fungsi dengan Validasi Input:**
```python
def tambah(a, b):
    # Memastikan kedua input adalah angka
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Mengangkat ValueError jika input bukan angka
        raise ValueError("Input harus angka!")
    return a + b

try:
    print(tambah(5, 6))
    print(tambah(5, "V")) # Ini akan memicu exception kustom
except ValueError as e:
    print(f"Terjadi kesalahan: {e}")
```
Dalam fungsi `tambah`, jika salah satu argumen bukan angka, `ValueError` kustom akan diangkat, dan pesan "Input harus angka!" akan ditampilkan.

## Aplikasi Praktis Exception Handling

*   **Membuat Program Robust**: Exception handling mencegah program berhenti secara tak terduga, menjadikannya lebih tahan banting terhadap input yang tidak valid atau kondisi sistem yang tidak terduga.
*   **Validasi Input**: Menggunakan `try-except` dalam loop `while True` memungkinkan program untuk terus meminta input hingga pengguna memberikan data yang valid.
*   **Penanganan File**: Memastikan file ditutup dengan benar (`finally`) dan menangani skenario seperti file tidak ditemukan (`FileNotFoundError`).
*   **Pengalaman Pengguna yang Lebih Baik**: Memberikan pesan kesalahan yang jelas dan membantu pengguna memahami apa yang salah, daripada hanya melihat program *crash*.
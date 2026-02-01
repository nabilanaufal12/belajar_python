# Catatan Belajar: Latihan Dictionary Python - Input Data Mahasiswa

## Pendahuluan

Catatan ini membahas latihan dasar penggunaan **dictionary** di Python untuk mengelola data mahasiswa, khususnya dalam mengambil input dari pengguna dan menyimpannya ke dalam struktur dictionary. Konsep utama yang akan dipelajari adalah pembuatan template dictionary dan inisialisasi dictionary baru menggunakan `dict.fromkeys()`.

## 1. Persiapan Awal dan Modul yang Dibutuhkan

Sebelum memulai, beberapa modul perlu diimpor untuk fungsionalitas tambahan:

*   **`datetime`**: Digunakan untuk menangani informasi tanggal dan waktu, khususnya untuk menyimpan tanggal lahir mahasiswa.
*   **`os`**: Digunakan untuk berinteraksi dengan sistem operasi, dalam hal ini untuk membersihkan layar konsol agar tampilan program lebih rapi.

```python
import datetime
import os
```

### Membersihkan Layar Konsol

Untuk memastikan tampilan program selalu bersih setiap kali dijalankan, fungsi `os.system()` dapat digunakan. Perintah yang digunakan bervariasi tergantung sistem operasi:
*   **Windows**: `cls`
*   **Linux/macOS**: `clear`

```python
os.system("cls") # Gunakan "clear" jika di Mac/Linux
```

## 2. Membuat Template Dictionary Mahasiswa

Langkah pertama adalah mendefinisikan sebuah template dictionary yang akan menjadi acuan struktur data mahasiswa. Template ini berisi kunci-kunci (keys) yang akan digunakan untuk setiap data mahasiswa, seperti `nama`, `nim`, `sks_lulus`, dan `lahir`.

*   **`mahasiswa_template`**: Dictionary ini berfungsi sebagai cetak biru. Nilai awal yang diberikan pada setiap kunci hanyalah *placeholder* atau nilai default.
    *   `'nama'`: String untuk nama mahasiswa.
    *   `'nim'`: String untuk Nomor Induk Mahasiswa.
    *   `'sks_lulus'`: Integer untuk jumlah SKS yang telah diluluskan.
    *   `'lahir'`: Objek `datetime.datetime` sebagai *placeholder* tanggal lahir.

```python
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11) # Placeholder tanggal lahir
}
```

Selain itu, disiapkan juga sebuah dictionary kosong `data_mahasiswa` yang nantinya bisa digunakan untuk menampung banyak data mahasiswa (meskipun dalam latihan ini hanya fokus pada satu data).

## 3. Inisialisasi Dictionary Mahasiswa Baru dengan `dict.fromkeys()`

Untuk membuat dictionary baru yang memiliki struktur kunci yang sama dengan `mahasiswa_template` tetapi dengan nilai awal kosong, digunakan metode **`dict.fromkeys()`**.

*   **`mahasiswa = dict.fromkeys(mahasiswa_template.keys())`**: Baris ini akan membuat dictionary baru bernama `mahasiswa`. Kunci-kunci dictionary ini diambil dari semua kunci yang ada di `mahasiswa_template`. Secara *default*, nilai untuk setiap kunci di dictionary baru ini akan diinisialisasi dengan `None`.

```python
mahasiswa = dict.fromkeys(mahasiswa_template.keys())
```

Setelah langkah ini, dictionary `mahasiswa` akan terlihat seperti ini:
`{'nama': None, 'nim': None, 'sks_lulus': None, 'lahir': None}`.

## 4. Antarmuka Pengguna dan Pengambilan Input

Program menampilkan pesan selamat datang dan header untuk memberikan tampilan yang lebih baik kepada pengguna.

```python
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-" * 20)
```

Selanjutnya, program akan meminta pengguna untuk memasukkan data mahasiswa satu per satu menggunakan fungsi `input()`:

*   **Nama Mahasiswa**: Input string biasa.
*   **NIM Mahasiswa**: Input string biasa.
*   **SKS Lulus**: Input integer, sehingga perlu dikonversi menggunakan `int()`.
*   **Tanggal Lahir**: Dipecah menjadi `tahun_lahir`, `bulan_lahir`, dan `tanggal_lahir`. Masing-masing adalah input integer.

```python
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))

tahun_lahir = int(input("Tahun Lahir (YYYY): "))
bulan_lahir = int(input("Bulan Lahir (1-12): "))
tanggal_lahir = int(input("Tanggal Lahir (1-31): "))
```

## 5. Pembentukan Objek `datetime` dan Pengisian Dictionary

Setelah semua komponen tanggal lahir didapatkan, objek `datetime.datetime` dibuat dan disimpan ke dalam kunci `'lahir'` di dictionary `mahasiswa`.

```python
mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
``` = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)"]

## 6. Menampilkan Hasil

Terakhir, dictionary `mahasiswa` yang sudah terisi dengan data dari pengguna dicetak untuk memverifikasi bahwa input telah berhasil disimpan.

```python
print("\nData berhasil diinput:")
print(mahasiswa)
```

## Kode Lengkap

Berikut adalah rangkuman kode lengkap untuk latihan ini:

```python
import datetime
import os

# Template Dictionary
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

# Dictionary kosong untuk menampung semua data (tidak digunakan di latihan ini, tapi disiapkan)
data_mahasiswa = {}

# Membersihkan layar konsol
os.system("cls") # Gunakan "clear" untuk Mac/Linux

# Header Program
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-" * 20)

# Membuat dictionary mahasiswa baru dari template dengan nilai awal None
mahasiswa = dict.fromkeys(mahasiswa_template.keys())

# Mengambil input dari pengguna
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))

tahun_lahir = int(input("Tahun Lahir (YYYY): "))
bulan_lahir = int(input("Bulan Lahir (1-12): "))
tanggal_lahir = int(input("Tanggal Lahir (1-31): "))

# Membuat objek datetime untuk tanggal lahir
mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

# Menampilkan hasil input
print("\nData berhasil diinput:")
print(mahasiswa)
```
# Latihan Dictionary Python: Looping Input Data Mahasiswa dengan Random Key

Catatan ini merangkum kelanjutan pengembangan program input data mahasiswa menggunakan struktur data **dictionary** di Python. Fokus utama adalah bagaimana membuat program dapat menerima input berulang kali dan mengatasi masalah penimpaan data dengan menggunakan kunci (key) yang di-generate secara acak.

## 1. Struktur Data Mahasiswa (Template)

Untuk memastikan konsistensi data, sebuah template dictionary digunakan sebagai cetak biru untuk setiap entri mahasiswa. Template ini mendefinisikan kunci-kunci standar yang harus ada untuk setiap mahasiswa.

*   **`mahasiswa_template`**:
    *   `'nama'`: Nama mahasiswa.
    *   `'nim'`: Nomor Induk Mahasiswa.
    *   `'sks_lulus'`: Jumlah SKS yang telah diluluskan.
    *   `'lahir'`: Tanggal lahir mahasiswa, disimpan sebagai objek `datetime`.

```python
import datetime
import os
import string
import random

# Template & Inisialisasi
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
data_mahasiswa = {}
```

## 2. Looping Input Data Mahasiswa

Agar program dapat menerima input data mahasiswa secara berulang, proses input dibungkus dalam sebuah loop tak terbatas (`while True`).

Setiap iterasi loop akan:
*   Mengosongkan layar konsol (`os.system("cls")` atau `"clear"`) untuk tampilan yang lebih bersih.
*   Menampilkan judul program.
*   Meminta input untuk setiap detail mahasiswa: nama, NIM, SKS lulus, serta tahun, bulan, dan tanggal lahir = input("].
*   Tanggal lahir kemudian digabungkan menjadi objek `datetime` = datetime.datetime("].

## 3. Menyimpan Data ke Dictionary Utama

Data mahasiswa yang baru diinput disimpan ke dalam dictionary utama `data_mahasiswa`. Metode `.update()` digunakan untuk menambahkan atau memperbarui entri dalam dictionary.

### Masalah Penimpaan Data (Overwrite)

Pada implementasi awal, jika kunci yang digunakan untuk menyimpan data mahasiswa bersifat statis (misalnya, `data_mahasiswa['MAH001']`), maka setiap data baru yang dimasukkan dengan kunci yang sama akan menimpa data sebelumnya. Ini berarti hanya data mahasiswa terakhir yang akan tersimpan.

## 4. Solusi: Generate Random Key

Untuk mengatasi masalah penimpaan data, setiap entri mahasiswa baru harus memiliki kunci yang unik. Solusinya adalah dengan membuat **kunci acak (random key)** untuk setiap mahasiswa.

### Implementasi Random Key

1.  **Import Modul**: Modul `string` dan `random` perlu diimpor untuk fungsionalitas ini.
2.  **Generasi Kunci**: Kunci acak dibuat dengan menggabungkan 6 karakter acak dari huruf kapital ASCII (`string.ascii_uppercase`).
    *   Sintaks yang digunakan adalah: `KEY = "".join(random.choice(string.ascii_uppercase) for i in range(6))`.
    *   `random.choice(string.ascii_uppercase)` memilih satu huruf kapital acak.
    *   `for i in range(6)` mengulang proses ini sebanyak 6 kali.
    *   `"".join(...)` menggabungkan karakter-karakter yang dipilih menjadi satu string kunci.
3.  **Pembaruan Dictionary**: Kunci acak ini kemudian digunakan saat memperbarui `data_mahasiswa`.

```python
    # Generate Random Key
    KEY = "".join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mahasiswa.update({KEY: mahasiswa})
```

Dengan cara ini, setiap data baru akan memiliki kunci unik (misalnya, 'XHJGYT', 'ABRTYU') dan tidak akan saling menimpa.

## 5. Menampilkan Data dalam Bentuk Tabel

Setelah data diinput dan disimpan, program akan menampilkan semua data mahasiswa yang ada dalam `data_mahasiswa` dalam format tabel yang rapi.

*   Tabel mencakup kolom: `KEY`, `Nama`, `NIM`, `SKS`, dan `Lahir`.
*   Penggunaan f-string (`f"{'KEY':<6}"`) membantu memformat output agar rata kiri dan memiliki lebar kolom yang konsisten.
*   Tanggal lahir diformat menggunakan `strftime("%x")` untuk tampilan yang standar['lahir'].strftime("%x")"].

## 6. Kontrol Loop: Lanjut atau Berhenti

Setelah menampilkan data, pengguna akan ditanya apakah ingin menambah data lagi atau tidak.

*   Input `is_done` akan meminta pengguna mengetik 'y' (ya) atau 'n' (tidak).
*   Jika pengguna memasukkan 'n', program akan keluar dari loop `while True` menggunakan pernyataan `break`.
*   Jika pengguna memasukkan 'y' (atau input lainnya), loop akan berlanjut untuk input data berikutnya.

## 7. Demo Program dan Penutup

Program ini memungkinkan input data mahasiswa secara interaktif, menghasilkan kunci unik untuk setiap entri, dan menampilkan semua data yang tersimpan. Setelah pengguna memilih untuk berhenti, program akan menampilkan pesan penutup.

Materi selanjutnya setelah pembahasan dictionary ini adalah **Fungsi (Function)** dalam Python, yang akan memungkinkan pembuatan aplikasi yang lebih terstruktur dan modular.
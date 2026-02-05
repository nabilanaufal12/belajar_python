# Belajar Python: Multi Keys & Nesting Dictionary untuk Struktur Data

## Pendahuluan

Dalam Python, **dictionary** adalah struktur data yang sangat fleksibel, memungkinkan penyimpanan data dalam pasangan *key-value*. Tutorial ini membahas bagaimana dictionary dapat menyimpan berbagai tipe data (*multi keys*) dan bagaimana dictionary dapat disarangkan (*nesting*) di dalam dictionary lain untuk membentuk struktur data yang lebih kompleks, mirip dengan database NoSQL atau format JSON. Kemampuan ini sangat penting untuk mengorganisir data secara terstruktur dan rapi, terutama dalam pengembangan aplikasi.

## 1. Dictionary dengan Berbagai Tipe Data (Multi Keys)

Sebuah dictionary Python dapat menyimpan *value* dengan berbagai tipe data di bawah *key* yang berbeda. Ini memungkinkan representasi data yang kaya untuk satu entitas, seperti data seorang mahasiswa.

### Tipe Data yang Dapat Disimpan

*   **String**: Untuk nama, NIM, atau kota. Contoh: `'nama': 'Ucup Surucup'`.
*   **Integer**: Untuk nilai numerik seperti SKS yang telah lulus. Contoh: `'sks_lulus': 130`.
*   **Boolean**: Untuk status benar/salah, seperti apakah mahasiswa mendapatkan beasiswa. Contoh: `'beasiswa': False`.
*   **Datetime**: Untuk menyimpan informasi tanggal dan waktu, seperti tanggal lahir. Ini memerlukan impor modul `datetime`.
    *   Objek `datetime` dibuat dengan `datetime.datetime(tahun, bulan, tanggal)`. Contoh: `datetime.datetime(2001, 4, 10)`.

### Contoh Struktur Data Mahasiswa Tunggal

Berikut adalah contoh dictionary yang merepresentasikan data satu mahasiswa dengan berbagai tipe data:
```python
import datetime

mahasiswa1 = {
    'nama': 'Ucup Surucup',
    'nim': '19022001',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2001, 4, 10),
    'kota': 'Surabaya'
}
```

## 2. Nesting Dictionary untuk Struktur Data Kompleks

**Nesting dictionary** adalah konsep di mana sebuah dictionary berisi dictionary lain sebagai salah satu *value*-nya. Ini memungkinkan kita untuk membangun struktur data yang hierarkis dan kompleks, seperti database mahasiswa yang berisi banyak entri mahasiswa individu.

### Konsep Nesting

Dalam contoh ini, kita membuat sebuah dictionary utama bernama `data_mahasiswa`. Setiap *key* dalam `data_mahasiswa` adalah kode unik (misalnya 'MAH001'), dan *value* yang terkait dengan *key* tersebut adalah dictionary data mahasiswa individu (`mahasiswa1`, `mahasiswa2`, dst.). Struktur ini sangat mirip dengan bagaimana data disimpan dalam database NoSQL atau format JSON.

### Contoh `data_mahasiswa`

```python
# Asumsikan mahasiswa1, mahasiswa2, mahasiswa3 sudah didefinisikan
# seperti pada bagian sebelumnya.

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}
```

## 3. Menampilkan Data dengan Format Rapi (Tabel)

Untuk menampilkan data dari *nested dictionary* secara terstruktur dan mudah dibaca, seperti dalam format tabel, kita dapat menggunakan kombinasi iterasi dan *f-string* dengan *width formatting*.

### Langkah-langkah Menampilkan Data

1.  **Iterasi Dictionary Utama**: Gunakan perulangan `for` untuk mengiterasi *key* utama dari `data_mahasiswa` (misalnya 'MAH001', 'MAH002').
    ```python
    for mahasiswa_key in data_mahasiswa:
        # ...
    ```
2.  **Mengakses Data Bersarang**: Untuk mengakses *value* dari dictionary bersarang, gunakan *chaining keys*. Contoh: `data_mahasiswa[mahasiswa_key]['nama']`['nama']"].
3.  **Formatting String (f-string)**:
    *   **Width Formatting**: Menggunakan `:<lebar>` untuk rata kiri, `:>lebar>` untuk rata kanan, dan `:^lebar>` untuk rata tengah. Contoh: `f"{'KEY':<6}"` akan mencetak string 'KEY' rata kiri dalam lebar 6 karakter.
    *   **Garis Pemisah**: Dapat dibuat dengan mengalikan karakter tertentu, misalnya `print("-" * 50)`.
4.  **Formatting Tanggal (`datetime`)**: Objek `datetime` dapat diformat menjadi string tanggal yang diinginkan menggunakan metode `.strftime()`. Format `%x` akan menghasilkan representasi tanggal lokal yang ringkas (misalnya `MM/DD/YY`).

### Contoh Kode untuk Menampilkan Data dalam Tabel

```python
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':^9} {'Lahir':<10}")
print("-" * 50)

for mahasiswa_key in data_mahasiswa:
    data_mhs = data_mahasiswa[mahasiswa_key] # Mengambil dictionary mahasiswa individu
    
    nama = data_mhs['nama']
    sks = data_mhs['sks_lulus']
    beasiswa = data_mhs['beasiswa']
    lahir = data_mhs['lahir'].strftime("%x") # Memformat objek datetime

    print(f"{mahasiswa_key:<6} {nama:<17} {sks:<3} {beasiswa:^9} {lahir:<10}")
```

## 4. Aplikasi dan Manfaat

Penggunaan *multi keys* dan *nesting dictionary* memberikan beberapa manfaat signifikan:

*   **Struktur Data yang Rapi**: Memungkinkan pengorganisasian data yang kompleks menjadi format yang logis dan mudah diakses.
*   **Fleksibilitas**: Dapat menampung berbagai tipe data dalam satu entitas, menjadikannya sangat adaptif untuk berbagai jenis informasi.
*   **Simulasi Database**: Struktur ini sangat mirip dengan bagaimana data disimpan dalam database NoSQL atau format JSON, menjadikannya dasar yang baik untuk bekerja dengan data dari API atau database.
*   **Dasar Pengembangan Aplikasi**: Konsep ini adalah fondasi untuk membangun program yang lebih interaktif, seperti program input data dinamis yang akan dibahas dalam tutorial selanjutnya.
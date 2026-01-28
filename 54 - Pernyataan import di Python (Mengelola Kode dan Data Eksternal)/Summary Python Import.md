# Pernyataan `import` di Python: Mengelola Kode dan Data Eksternal

Pernyataan `import` adalah fitur fundamental di Python yang memungkinkan program untuk mengakses dan menggunakan kode, data, atau fungsi yang didefinisikan dalam file eksternal atau pustaka (`library`). Ini sangat penting untuk modularitas, memungkinkan pengembang untuk memecah program besar menjadi bagian-bagian yang lebih kecil dan terorganisir, serta memanfaatkan kode yang sudah ada yang dibuat oleh orang lain.

## 1. Fungsi Dasar `import`: Menjalankan Kode Eksternal

Fungsi utama `import` adalah untuk mengambil program dari file `.py` eksternal dan menjalankannya. Ini sangat berguna ketika sebuah program menjadi terlalu panjang (misalnya, seribu baris kode) dan perlu dipecah menjadi beberapa file untuk menjaga keterbacaan dan pengelolaan.

**Contoh Skenario**:
Misalkan kita memiliki file `program_print.py` yang berisi kode untuk mencetak pesan:
```python
# program_print.py
print("Halo saya dari program_print")
```
Untuk menjalankan kode ini dari file utama `main.py`, kita cukup menggunakan pernyataan `import`:
```python
# main.py
import program_print
```
Ketika `main.py` dijalankan, output dari `program_print.py` akan langsung muncul, seolah-olah kode di `program_print.py` disalin dan ditempelkan ke `main.py`.

## 2. Mengimpor Data (Variabel) dengan Konsep Namespace

`import` juga dapat digunakan untuk mengakses data atau variabel yang didefinisikan dalam file eksternal.

**Masalah Potensial dan Solusi Namespace**:
Jika kita mendefinisikan variabel di file eksternal, misalnya `variabel.py` dan `kucuy.py`, dan mencoba mengaksesnya secara langsung di `main.py` setelah mengimpor, akan terjadi kesalahan `NameError` karena variabel tersebut tidak didefinisikan dalam cakupan `main.py` secara langsung.

**Contoh**:
File `variabel.py`:
```python
# variabel.py
data = "Faqihza ganteng abis"
```
File `kucuy.py`:
```python
# kucuy.py
data = "Mukhlis ganteng pol"
```
Untuk mengakses variabel `data` dari file-file ini, kita harus menggunakan **Namespace**. Namespace adalah nama file (tanpa ekstensi `.py`) yang bertindak sebagai wadah untuk semua entitas (variabel, fungsi, kelas) yang didefinisikan di dalamnya. Ini mencegah bentrokan nama jika ada variabel dengan nama yang sama di file yang berbeda.

Di `main.py`, akses variabel menggunakan format `nama_file.nama_variabel`:
```python
# main.py
import variabel
import kucuy

print(variabel.data) # Output: Faqihza ganteng abis
print(kucuy.data)    # Output: Mukhlis ganteng pol
```

## 3. Mengimpor Fungsi

`import` juga memungkinkan kita untuk mengimpor dan menggunakan fungsi yang didefinisikan dalam file eksternal. Ini adalah praktik umum untuk mengorganisir fungsi-fungsi terkait dalam satu file (modul) dan mengimpornya saat dibutuhkan.

**Contoh**:
Misalkan kita memiliki file `matematika.py` yang berisi fungsi `tambah`:
```python
# matematika.py
def tambah(a: float, b: float) -> float:
    return a + b
```
Di `main.py`, kita dapat mengimpor file `matematika` dan memanggil fungsi `tambah` menggunakan namespace `matematika`:
```python
# main.py
import matematika

hasil = matematika.tambah(4, 5)
print(f"Hasil tambah: {hasil}") # Output: Hasil tambah: 9
```
Hasilnya akan menjadi `9`.

## 4. Manfaat dan Langkah Selanjutnya

Penggunaan pernyataan `import` adalah dasar untuk membangun program Python yang terstruktur dan mudah dikelola. Dengan memecah kode menjadi file-file kecil (disebut **modul**), kita dapat:
*   Meningkatkan keterbacaan kode.
*   Memfasilitasi penggunaan kembali kode.
*   Membuat program lebih mudah di-debug dan dipelihara.

Ke depannya, konsep `import` akan diperluas untuk membuat dan mengelola **modul** dan **package** yang lebih kompleks, yang sangat penting untuk organisasi program yang lebih besar.
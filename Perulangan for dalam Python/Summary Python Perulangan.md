# Summary Python Perulangan

> Generated: January 19th, 2026 5:41 PM
> Sources: Belajar Python [Dasar] - 24 - For Loop (Perulangan.youtube, pasted-text-1.md

---

# Catatan Studi: Perulangan `for` dalam Python

Perulangan, atau *looping*, adalah salah satu konsep fundamental dalam pemrograman yang memungkinkan eksekusi blok kode secara berulang. Dalam Python, `for` loop adalah alat yang sangat kuat dan fleksibel untuk melakukan iterasi melalui berbagai jenis koleksi data.

## 1. Konsep Perulangan (Looping)

Perulangan adalah mekanisme di mana sebuah aksi atau serangkaian aksi diulang berkali-kali. Ini berbeda dengan **percabangan** (seperti `if/else`), yang hanya memilih satu jalur eksekusi dan kemudian melanjutkan program ke bawah. Sebaliknya, perulangan akan "kembali ke atas" untuk mengulang aksi selama kondisi tertentu terpenuhi atau selama ada elemen yang tersisa untuk diiterasi.

*   **Tujuan Utama**: Menghindari penulisan kode yang berulang-ulang untuk tugas yang sama. Misalnya, jika Anda perlu menambahkan angka 3 ke sebuah variabel sebanyak 100 kali, perulangan akan melakukannya secara otomatis tanpa perlu menulis 100 baris kode.
*   **Contoh Aksi Berulang**:
    *   Menambahkan nilai ke sebuah angka secara bertahap.
    *   Meminta *login* berulang kali jika *password* salah.
    *   Mencetak "Saya Keren" berkali-kali.

## 2. Sintaks Dasar `for` Loop di Python

Python dirancang untuk memiliki sintaks yang mudah dibaca dan "manusiawi" dibandingkan bahasa pemrograman lain seperti C++ atau Java, yang seringkali memiliki sintaks `for (int i=0; i<10; i++)` yang lebih kompleks.

Sintaks dasar `for` loop di Python adalah:
```python
for variabel_iterasi in koleksi_data:
    # Aksi yang akan diulang
    # Blok kode ini akan dieksekusi untuk setiap item dalam koleksi_data
```
*   **`variabel_iterasi`**: Sebuah variabel yang akan mengambil nilai dari setiap item dalam `koleksi_data` secara berurutan pada setiap putaran *loop*.
*   **`in`**: Kata kunci yang menunjukkan bahwa `variabel_iterasi` akan mengambil nilai "di dalam" `koleksi_data`.
*   **`koleksi_data`**: Objek yang dapat diiterasi (*iterable*), seperti `list`, `range`, atau `string`.

## 3. Penggunaan `for` Loop dengan Berbagai Tipe Data

`for` loop di Python sangat serbaguna dan dapat digunakan untuk mengiterasi berbagai jenis *sequence* atau koleksi data.

### 3.1. Iterasi dengan `List`

**List** adalah kumpulan data terurut yang dapat diubah. `for` loop dapat dengan mudah menelusuri setiap elemen dalam sebuah *list*.

```python
# Ini adalah list (kumpulan angka)
angka_list = [0, 2, 4, 8, 10] # src-1:10:46, src-2:t:"angka2_list = [0, 2, 4, 8, 10]"

print("--- FOR LOOP dengan LIST ---")
for i in angka_list:
    # 'i' akan mengambil nilai dari setiap item di list secara berurutan
    print(f"i sekarang -> {i}") # src-1:08:20

print("Akhir dari program 1 \n") # src-1:11:00
```
**Penjelasan**:
Pada setiap putaran *loop*, variabel `i` akan mengambil nilai dari elemen *list* `angka_list` secara berurutan (pertama 0, lalu 2, lalu 4, dst.) hingga semua elemen telah diproses.

### 3.2. Iterasi dengan `range()`

Fungsi `range()` digunakan untuk menghasilkan urutan angka. Ini sangat berguna ketika Anda ingin mengulang sebuah aksi sebanyak N kali tanpa perlu membuat *list* angka secara manual.

`range()` memiliki beberapa bentuk:
*   **`range(stop)`**: Menghasilkan urutan angka dari 0 hingga `stop-1`. Jumlah angka yang dihasilkan adalah `stop`.
    *   Contoh: `range(5)` akan menghasilkan 0, 1, 2, 3, 4.
*   **`range(start, stop)`**: Menghasilkan urutan angka dari `start` hingga `stop-1`.
    *   Contoh: `range(1, 5)` akan menghasilkan 1, 2, 3, 4. Angka `stop` (5) tidak termasuk.
*   **`range(start, stop, step)`**: Menghasilkan urutan angka dari `start` hingga `stop-1` dengan peningkatan `step` tertentu.

```python
print("--- FOR LOOP dengan RANGE ---")
# Range 5 (0 sampai 4)
for i in range(5): # src-1:12:30
    print(f"i sekarang -> {i}")

print("\n")

# Range 1 sampai 10 (1 sampai 9)
for i in range(1, 10): # src-1:14:00
    print(f"i sekarang -> {i}")
    # Kita bisa taruh aksi apa aja di sini
    # print("Saya Keren") # src-1:14:53

print("Akhir dari program 2 \n") # src-1:13:00
```
**Penjelasan**:
`range(5)` akan membuat `i` bernilai 0, 1, 2, 3, dan 4. `range(1, 10)` akan membuat `i` bernilai 1, 2, ..., hingga 9. Anda dapat menempatkan aksi apa pun di dalam *loop* ini, seperti mencetak teks atau melakukan perhitungan.

### 3.3. Iterasi dengan `String`

**String** adalah kumpulan karakter. `for` loop dapat digunakan untuk mengiterasi setiap karakter dalam sebuah *string*.

```python
print("--- FOR LOOP dengan STRING ---")
data_str = "saya ganteng abis" # src-1:16:06

for huruf in data_str: # src-1:16:15
    print(huruf)

print("Akhir dari program 3 \n")
```
**Penjelasan**:
Pada setiap putaran *loop*, variabel `huruf` akan mengambil satu per satu karakter dari *string* `data_str` (pertama 's', lalu 'a', lalu 'y', dst.) dan mencetaknya ke bawah.

## 4. Perbedaan dengan `while` Loop (Sekilas)

Meskipun `for` loop sangat efektif untuk mengiterasi *sequence* data, ada jenis perulangan lain yang disebut **`while` loop**. `while` loop digunakan ketika Anda ingin mengulang sebuah aksi berdasarkan kondisi tertentu yang bernilai `True` atau `False`, bukan berdasarkan jumlah item dalam koleksi. Pembahasan lebih lanjut tentang `while` loop akan dilakukan di tutorial berikutnya.
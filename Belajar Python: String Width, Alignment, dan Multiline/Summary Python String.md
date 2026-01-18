# Summary Python String

> Generated: January 18th, 2026 11:12 PM
> Sources: Belajar Python [Dasar] - 19 - String width and Ali.youtube, pasted-text-1.md

---

# Belajar Python: String Width, Alignment, dan Multiline

Tutorial ini membahas teknik-teknik penting dalam Python untuk memformat string, khususnya dalam mengatur lebar (width), perataan (alignment), dan menampilkan string dalam beberapa baris (multiline). Kemampuan ini sangat berguna untuk membuat output program lebih rapi dan mudah dibaca, seperti pada laporan atau struk.

## 1. Pengantar F-String dan Data Dasar

Dalam Python, **f-string** (formatted string literals) adalah cara yang efisien dan mudah dibaca untuk menyematkan ekspresi Python di dalam string literal. Ini adalah dasar untuk melakukan formatting string yang akan dibahas.

Sebagai contoh, kita akan menggunakan data berikut:
```python
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44
```

Secara standar, tanpa formatting khusus, output string akan ditampilkan dalam satu baris panjang:
```python
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"=" + "Data String" + 5*"=")
print(data_string)
# Output: =====Data String=====
#         nama = Ucup Surucup, umur = 17, tinggi = 150.1, sepatu = 44
```

## 2. String Multiline

Ada dua cara utama untuk membuat string multiline di Python:

### 2.1. Menggunakan Karakter Newline (`\n`)

Karakter **newline** (`\n`) digunakan untuk memaksa baris baru dalam string. Setiap kali `\n` ditemui, teks setelahnya akan dimulai dari baris baru.

```python
data_string_newline = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"=" + "Data String (Newline)" + 5*"=")
print(data_string_newline)
# Output:
# =====Data String (Newline)=====
# nama = Ucup Surucup,
# umur = 17,
# tinggi = 150.1,
# sepatu = 44
```
Perhatikan bahwa spasi atau indentasi sebelum `\n` akan tetap dipertahankan pada baris berikutnya jika tidak diatur. Metode ini efektif namun bisa menjadi "ribet" karena harus menulis `\n` berulang kali.

### 2.2. Menggunakan Triple Quotes (`"""..."""` atau `'''...'''`)

Cara yang lebih rapi dan direkomendasikan untuk string multiline adalah dengan menggunakan **triple quotes** (tiga tanda kutip ganda atau tiga tanda kutip tunggal).

Dengan triple quotes, Anda dapat menulis string secara langsung dalam beberapa baris di dalam kode, dan Python akan mempertahankan semua baris baru serta indentasi yang Anda masukkan.

```python
data_string_triple_quotes = f"""
nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"=" + "Data String (Triple Quotes)" + 5*"=")
print(data_string_triple_quotes)
# Output:
# =====Data String (Triple Quotes)=====
#
# nama   = Ucup Surucup
# umur   = 17
# tinggi = 150.1
# sepatu = 44
```
Metode ini "jauh lebih bersih dan mudah dibaca" karena representasi string dalam kode mirip dengan output yang diinginkan.

## 3. Mengatur Lebar (Width) dan Perataan (Alignment) String

Untuk membuat tampilan data lebih rapi, terutama ketika nilai-nilai memiliki panjang yang berbeda, kita dapat mengatur lebar total placeholder dan perataan teks di dalamnya.

Sintaksnya adalah `{nilai:alignment_symbol lebar}` di dalam f-string.

### 3.1. Konsep Dasar

*   **`:`**: Pemisah antara nilai dan spesifikasi format.
*   **`alignment_symbol`**: Simbol untuk menentukan perataan.
*   **`lebar`**: Angka yang menentukan lebar total minimum dari placeholder. Jika nilai lebih pendek dari lebar, spasi akan ditambahkan.

### 3.2. Perataan Kanan (`:>`)

Simbol `>` digunakan untuk **perataan kanan**. Ini akan menambahkan spasi di sisi kiri nilai untuk mencapai lebar yang ditentukan.

Contoh dengan `data_nama = "Ucup"` dan `data_tinggi = 105.17`:
```python
data_nama_short = "Ucup"
data_tinggi_decimal = 105.17

data_string_rata_kanan = f"""
nama   = {data_nama_short:>10}
umur   = {data_umur:>10}
tinggi = {data_tinggi_decimal:>10}
sepatu = {data_nomor_sepatu:>10}
"""
print("\n"+5*"=" + "Data String (Rata Kanan)" + 5*"=")
print(data_string_rata_kanan)
# Output:
# =====Data String (Rata Kanan)=====
#
# nama   =       Ucup
# umur   =         17
# tinggi =     105.17
# sepatu =         44
```
Dalam contoh di atas, semua nilai akan diratakan ke kanan dalam lebar 10 karakter, membuat kolom terlihat lurus dan rapi.

### 3.3. Perataan Kiri (`:<`)

Simbol `<` digunakan untuk **perataan kiri**. Ini adalah perilaku default untuk string, tetapi dapat digunakan secara eksplisit. Spasi akan ditambahkan di sisi kanan nilai.

### 3.4. Perataan Tengah (`:^`)

Simbol `^` digunakan untuk **perataan tengah**. Spasi akan ditambahkan di kedua sisi nilai untuk memusatkannya dalam lebar yang ditentukan.

### 3.5. Catatan Penting

*   Jika panjang nilai string melebihi lebar yang ditentukan, string tidak akan terpotong. Ia akan tetap ditampilkan secara penuh, meskipun itu berarti melebihi lebar yang telah diatur.
*   Teknik formatting ini sangat fleksibel dan ada banyak opsi lain yang tersedia dalam Python untuk formatting string yang lebih kompleks.

Dengan menguasai teknik multiline dan alignment, Anda dapat menyajikan data di konsol dengan cara yang jauh lebih profesional dan mudah dibaca.
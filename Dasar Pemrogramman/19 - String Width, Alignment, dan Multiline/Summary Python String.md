# Catatan Belajar Python: String Width, Alignment, dan Multiline

Tutorial ini membahas cara mengatur lebar (width) dan perataan (alignment) string, serta membuat string multiline di Python menggunakan f-string. Kemampuan ini sangat berguna untuk menghasilkan output yang rapi dan mudah dibaca di konsol.

## 1. Pengantar: Output String Standar

Pada awalnya, kita memiliki beberapa data dasar seperti nama, umur, tinggi, dan nomor sepatu.

```python
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44
```

Ketika data ini digabungkan menjadi satu string menggunakan f-string standar, hasilnya akan ditampilkan dalam satu baris panjang:

```python
# Cara standard (tanpa multiline/alignment)
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"=" + "Data String" + 5*"=")
print(data_string)
# Output: nama = Ucup Surucup, umur = 17, tinggi = 150.1, sepatu = 44 (Satu baris panjang)
```
Output standar ini mungkin tidak ideal untuk tampilan yang lebih terstruktur.

## 2. String Multiline

Ada dua cara utama untuk membuat string ditampilkan dalam beberapa baris (multiline) di Python:

### 2.1. Menggunakan Karakter Newline (`\n`)

Karakter **newline** (`\n`) digunakan untuk menambahkan baris baru pada string. Setiap kali `\n` ditempatkan dalam string, teks setelahnya akan dimulai pada baris baru.

```python
data_string_newline = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"=" + "Data String (Newline)" + 5*"=")
print(data_string_newline)
```
Meskipun efektif, cara ini bisa menjadi "ribet" karena memerlukan penulisan `\n` secara berulang.

### 2.2. Menggunakan Triple Quotes (`"""..."""` atau `'''...'''`)

Metode yang lebih rapi dan direkomendasikan untuk string multiline adalah menggunakan **triple quotes** (tiga tanda kutip ganda atau tiga tanda kutip tunggal). Dengan triple quotes, Anda dapat menulis string dalam beberapa baris langsung di dalam kode, dan Python akan mempertahankan semua jeda baris dan spasi yang Anda masukkan.

```python
data_string_triple_quotes = f"""
nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"=" + "Data String (Triple Quotes)" + 5*"=")
print(data_string_triple_quotes)
```
Cara ini membuat kode lebih bersih dan mudah dibaca, karena format output visualnya langsung terlihat di dalam kode.

## 3. Mengatur Lebar dan Alignment String

Seringkali, panjang data yang berbeda-beda dapat menyebabkan tampilan output menjadi tidak rapi, terutama jika Anda ingin meluruskan kolom atau teks. Python menyediakan cara untuk mengatur lebar minimum dan perataan (alignment) string di dalam f-string.

### 3.1. Konsep Dasar

Sintaks umum untuk mengatur lebar dan alignment dalam f-string adalah `{value:alignment_char width}`.
*   `value`: Variabel atau ekspresi yang akan diformat.
*   `alignment_char`: Karakter yang menentukan jenis perataan.
*   `width`: Lebar minimum total string yang diinginkan.

### 3.2. Jenis Alignment

Ada beberapa jenis karakter alignment yang dapat digunakan:

*   **Rata Kanan (`:>`)**: Menggeser data ke kanan dalam lebar yang ditentukan. Jika string lebih pendek dari lebar, spasi akan ditambahkan di sebelah kiri.
*   **Rata Kiri (`:<`)**: Menggeser data ke kiri dalam lebar yang ditentukan. Ini adalah perataan default untuk string.
*   **Rata Tengah (`:^`)**: Memusatkan data dalam lebar yang ditentukan, menambahkan spasi di kedua sisi.

### 3.3. Contoh Penerapan

Mari kita gunakan data yang lebih singkat untuk demonstrasi alignment:

```python
data_nama_singkat = "Ucup"
data_tinggi_baru = 105.17
```

Untuk membuat output lebih rapi, kita bisa mengatur agar nama dan tinggi rata kanan dengan lebar tertentu, misalnya 5 karakter.

```python
data_string_aligned = f"""
nama   = {data_nama_singkat:>5}
tinggi = {data_tinggi_baru:>5}
"""
print("\n"+5*"=" + "Data String (Aligned)" + 5*"=")
print(data_string_aligned)
# Output:
# nama   =  Ucup (ada spasi di depan biar total lebar 5)
# tinggi = 105.17
```
Perhatikan bahwa jika string asli lebih panjang dari lebar yang ditentukan, string tersebut tidak akan terpotong, tetapi akan tetap ditampilkan sepenuhnya, meskipun mungkin melebihi lebar yang diinginkan.

**Contoh Kasus Rata Kanan untuk Tampilan Terstruktur:**
Untuk membuat tampilan seperti struk atau laporan yang rapi, kita bisa menerapkan rata kanan dengan lebar yang konsisten untuk semua item data.

```python
data_string_struk = f"""
nama   = {data_nama:>10}
umur   = {data_umur:>10}
tinggi = {data_tinggi:>10}
sepatu = {data_nomor_sepatu:>10}
"""
print("\n"+5*"=" + "Data String (Struk Rapi)" + 5*"=")
print(data_string_struk)
# Output (Rata Kanan):
# nama   =       Ucup Surucup
# umur   =                 17
# tinggi =              150.1
# sepatu =                 44
```
Dengan teknik ini, tampilan data di konsol menjadi jauh lebih rapi dan profesional.
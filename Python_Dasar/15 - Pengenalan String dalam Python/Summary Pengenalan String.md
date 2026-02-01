# Pengenalan String dalam Python

## Gambaran Umum
String adalah salah satu tipe data fundamental dalam Python yang merepresentasikan urutan karakter. Catatan ini akan membahas definisi string, berbagai cara untuk membuatnya, penggunaan karakter *escape*, *raw string*, dan *multiline string* dalam Python.

## Apa Itu String?
**String** adalah kumpulan karakter, seperti huruf, angka, atau simbol, yang membentuk sebuah teks. Dalam Python, string adalah objek dari kelas `str`.

## Cara Membuat String
Untuk membuat string, teks harus diapit oleh tanda kutip. Python menyediakan beberapa cara untuk melakukan ini:

### 1. Menggunakan Tanda Kutip Tunggal (`'...'`)
String dapat dibuat dengan mengapit teks di antara tanda kutip tunggal.
```python
data = 'ini adalah string menggunakan single quote'
print(data)
```

### 2. Menggunakan Tanda Kutip Ganda (`"..."`)
Alternatifnya, string juga bisa dibuat dengan mengapit teks di antara tanda kutip ganda.
```python
data = "ini adalah string menggunakan double quote"
print(data)
```

Kedua metode ini menghasilkan string yang sama. Pilihan antara kutip tunggal atau ganda seringkali tergantung pada preferensi atau kebutuhan untuk menyertakan tanda kutip di dalam string itu sendiri.

### 3. Menggabungkan Tanda Kutip
Kita dapat menggabungkan penggunaan kutip tunggal dan ganda untuk menangani situasi di mana string itu sendiri mengandung tanda kutip.
*   Jika string mengandung kutip tunggal, gunakan kutip ganda untuk mengapit string:
    ```python
    print("ini adalah hari Jum'at")
    ```
*   Jika string mengandung kutip ganda, gunakan kutip tunggal untuk mengapit string:
    ```python
    print('"Halo, apa kabar?"')
    ```
*   Jika string mengandung kedua jenis kutip, atau jika ingin secara eksplisit menyertakan tanda kutip yang sama dengan pembungkusnya, kita perlu menggunakan *escape character*.

## Karakter Escape (Backslash `\`)
**Karakter *escape***, yang ditandai dengan *backslash* (`\`), digunakan untuk menyertakan karakter khusus atau karakter yang tidak dapat dicetak langsung ke dalam string. Ini memungkinkan Python untuk menginterpretasikan karakter setelah *backslash* sebagai bagian dari string, bukan sebagai perintah atau penutup string.

Beberapa karakter *escape* yang umum:

*   **Kutip Tunggal (`\'`)**: Untuk menyertakan kutip tunggal dalam string yang juga diapit kutip tunggal.
    ```python
    print('mari shalat Jum\'at')
    ```
*   **Backslash (`\\`)**: Untuk mencetak karakter *backslash* itu sendiri. Jika tidak di-*escape*, *backslash* dapat diinterpretasikan sebagai awal dari karakter *escape* lain.
    ```python
    print("C:\\user\\ucup")
    ```
*   **Tab (`\t`)**: Untuk menyisipkan karakter tabulasi (jarak horizontal).
    ```python
    print("ucup\t\t\totong, semakin jauh")
    ```
*   **Backspace (`\b`)**: Untuk menghapus satu karakter sebelumnya.
    ```python
    print("ucup \botong") # Output: ucupotong (spasi terhapus)
    ```
*   **Newline (`\n`)**: Untuk membuat baris baru (seperti menekan tombol Enter).
    ```python
    print("baris pertama.\nbaris kedua.")
    # Output:
    # baris pertama.
    # baris kedua.
    ```

### Konvensi Baris Baru
Ada beberapa konvensi untuk mendeteksi akhir baris atau baris baru di berbagai sistem operasi:
*   **LF (Line Feed)**: `\n`. Umum digunakan di sistem Unix, Linux, dan macOS.
*   **CR (Carriage Return)**: `\r`. Digunakan pada sistem lama seperti Commodore, Acorn, atau Lisp.
*   **CRLF (Carriage Return Line Feed)**: `\r\n`. Kombinasi ini digunakan di sistem operasi Windows.

Perbedaan konvensi ini dapat menyebabkan masalah kompatibilitas saat memproses file teks antar sistem operasi yang berbeda.

## Raw String (Literal String)
**Raw string** adalah string di mana karakter *backslash* (`\`) diperlakukan sebagai karakter literal, bukan sebagai awal dari karakter *escape*. Ini sangat berguna saat bekerja dengan *path* file (terutama di Windows) atau ekspresi reguler, di mana banyak *backslash* digunakan.

Untuk membuat *raw string*, tambahkan huruf `r` (huruf kecil) sebelum tanda kutip pembuka string:
```python
# Hati-hati: \n akan diinterpretasikan sebagai newline
print('C:\new folder')

# Menggunakan Raw String, \n diperlakukan sebagai karakter literal
print(r'C:\new folder') # Output: C:\new folder
```
Dalam *raw string*, semua karakter di dalamnya dianggap string biasa, dan *backslash* tidak dianggap sebagai perintah khusus.

## Multiline String
**Multiline string** memungkinkan kita untuk membuat string yang membentang di beberapa baris kode. Ini sangat berguna untuk teks panjang seperti paragraf, dokumentasi, atau *template*.

Untuk membuat *multiline string*, gunakan tiga tanda kutip tunggal (`'''...'''`) atau tiga tanda kutip ganda (`"""..."""`):
```python
print("""
Nama : Ucup
Kelas : 3 SD
""")
# Output akan mempertahankan format baris baru dan spasi
# Nama : Ucup
# Kelas : 3 SD
```

### Menggabungkan Raw String dan Multiline String
Kita juga dapat menggabungkan konsep *raw string* dengan *multiline string* dengan menambahkan `r` sebelum tiga tanda kutip. Ini berguna untuk teks panjang yang mungkin mengandung *backslash* dan juga memerlukan format multibaris, seperti *path* file yang kompleks atau *template* dengan banyak *backslash*.
```python
path_kompleks = r"""
Ini adalah path: C:\Users\Admin\Documents\new_project\file.txt
Dan ini baris kedua dengan \n literal.
"""
print(path_kompleks)
```

## Kesimpulan
Pengenalan string mencakup pemahaman tentang cara dasar membuat string menggunakan kutip tunggal atau ganda, mengelola karakter khusus dengan *escape character* (`\n`, `\t`, `\b`, `\\`, `\'`), menggunakan *raw string* (`r''`) untuk menghindari interpretasi *escape character*, dan membuat teks multibaris dengan *triple quotes* (`"""..."""` atau `'''...'''`). Pemahaman ini adalah dasar penting untuk manipulasi string yang lebih kompleks.

Tutorial selanjutnya akan membahas operasi dan manipulasi string yang lebih mendalam, seperti mengakses karakter, menggabungkan string, dan menghitung panjang string.
# Python: IF dan ELSE Statement untuk Control Flow

Program komputer biasanya berjalan secara sekuensial, mengeksekusi instruksi dari atas ke bawah dalam satu alur linear. Namun, untuk membuat program lebih dinamis dan "pintar", kita memerlukan kemampuan untuk mengatur alur eksekusi berdasarkan kondisi tertentu. Kemampuan ini disebut **Control Flow**. Salah satu alat paling fundamental untuk mengendalikan alur program adalah statement **IF** dan **ELSE**, yang memungkinkan program membuat **percabangan**.

## Konsep Dasar Percabangan

Percabangan memungkinkan program untuk memilih jalur eksekusi yang berbeda berdasarkan evaluasi suatu kondisi. Sebagai contoh, program dapat menanyakan nama pengguna dan memberikan respons yang berbeda jika nama tersebut adalah "Ucup" atau bukan.

Secara diagram, percabangan `if` memiliki struktur sebagai berikut:
1.  **Kondisi**: Sebuah ekspresi yang dievaluasi menjadi `True` atau `False`.
2.  **Aksi True**: Serangkaian instruksi yang dijalankan jika kondisi bernilai `True`.
3.  **Aksi False**: Serangkaian instruksi yang dijalankan jika kondisi bernilai `False` (ini akan ditangani oleh `else`).

Setelah salah satu aksi dijalankan, program akan melanjutkan ke instruksi berikutnya di luar blok percabangan.

## IF Statement

Statement `if` digunakan untuk mengeksekusi blok kode tertentu hanya jika suatu kondisi terpenuhi (bernilai `True`).

### Kondisi Boolean
Kondisi dalam statement `if` harus selalu menghasilkan nilai **Boolean**, yaitu `True` atau `False`. Contoh kondisi: `nama == "Ucup"`, `umur > 18`, `is_active == True`.

### Sintaks Dasar IF
Sintaks dasar `if` di Python adalah sebagai berikut:

```python
if kondisi:
    # Aksi yang akan dijalankan jika kondisi True
```

Perhatikan penggunaan titik dua (`:`) setelah kondisi, yang menandakan awal dari blok kode `if`.

#### Format Inline (Satu Baris)
Untuk aksi yang sangat sederhana dan hanya terdiri dari satu baris, `if` dapat ditulis secara inline:

```python
nama = input("Siapa nama anda? ")
if nama == "Ucup": print("Kamu Ganteng abis!") # Aksi satu baris
print(f"Terima kasih {nama}")
```
Jika `nama` yang diinput adalah "Ucup", maka "Kamu Ganteng abis!" akan dicetak. Jika bukan, baris `print("Kamu Ganteng abis!")` akan dilewati, dan program langsung mencetak "Terima kasih [nama]".

#### Format dengan Indentasi (Blok Kode)
Untuk program yang lebih kompleks dengan banyak aksi, Python menggunakan **indentasi** (spasi atau tab menjorok ke dalam) untuk menandai blok kode yang menjadi bagian dari statement `if`. Ini berbeda dengan bahasa pemrograman lain yang mungkin menggunakan kurung kurawal `{}`.

```python
nama = input("Siapa nama anda? ")

if nama == "Ucup":
    # Blok ini hanya jalan jika nama == "Ucup"
    print("Kamu Ganteng abis!")
    print("Kamu juga keren banget!") # Baris ini juga bagian dari blok IF
    # Semua baris yang menjorok ke dalam dianggap satu paket
print(f"Terima kasih {nama}") # Ini di luar IF, selalu jalan
```
**Penting**: Semua baris yang memiliki indentasi yang sama di bawah `if` dianggap sebagai satu blok kode. Begitu indentasi kembali ke kiri (sejajar dengan `if`), itu menandakan akhir dari blok `if`. Kesalahan indentasi dapat menyebabkan `IndentationError` atau logika program yang salah.

## ELSE Statement

Statement `else` menyediakan jalur alternatif eksekusi jika kondisi `if` bernilai `False`. `else` tidak memiliki kondisi karena ia menangani semua kasus yang tidak dipenuhi oleh `if` sebelumnya.

### Sintaks ELSE
Sintaks `else` adalah sebagai berikut:

```python
if kondisi:
    # Aksi jika kondisi True
else:
    # Aksi jika kondisi False
```

Sama seperti `if`, `else` juga diakhiri dengan titik dua (`:`) dan blok kodenya ditentukan oleh indentasi.

### Contoh Program IF-ELSE
Dengan `if-else`, program memiliki dua cabang jalur eksekusi yang jelas:

```python
nama = input("Siapa nama anda? ")

if nama == "Otong":
    print("Hai Otong, si keren!") # Aksi jika nama adalah "Otong"
else:
    print("Ah, kamu bukan Otong, kamu gak keren! :(") # Aksi jika nama bukan "Otong"

print("Akhir dari program") # Selalu dijalankan setelah if-else
```
Jika pengguna menginput "Otong", program akan mencetak "Hai Otong, si keren!". Jika menginput nama lain seperti "Mario", program akan mencetak "Ah, kamu bukan Otong, kamu gak keren! :(".

## Catatan Penting

*   **Indentasi**: Selalu perhatikan indentasi di Python. Ini bukan hanya masalah gaya, tetapi merupakan bagian dari sintaksis bahasa. Gunakan spasi atau tab secara konsisten.
*   **Titik Dua (`:`):** Jangan lupa menambahkan titik dua di akhir baris `if` dan `else`.

## Lanjutan: ELIF (Else If)

Bagaimana jika ada lebih dari dua cabang kondisi? Misalnya, jika namanya "Ucup" lakukan A, jika "Otong" lakukan B, dan jika "Mario" lakukan C? Untuk skenario ini, Python menyediakan statement **ELIF** (singkatan dari "else if"), yang akan dibahas lebih lanjut di tutorial berikutnya.
# Summary Python Continue Pass

> Generated: January 19th, 2026 7:28 PM
> Sources: Belajar Python [Dasar] - 26 - Continue dan Pass.youtube, pasted-text-1.md

---

# Python Control Flow: `pass` dan `continue`

Tutorial ini membahas dua pernyataan kontrol alur (`control flow`) penting dalam Python: `pass` dan `continue`. Keduanya digunakan untuk memanipulasi jalannya perulangan (`loop`) atau struktur kode lainnya, namun dengan fungsi yang berbeda. Selain itu, akan disinggung sedikit tentang `break` yang akan dibahas lebih lanjut di video berikutnya.

## 1. Pernyataan `pass`

Pernyataan `pass` berfungsi sebagai **dummy** atau **placeholder**. Ini berarti `pass` tidak melakukan tindakan apa pun dan tidak akan dieksekusi.

### Tujuan Penggunaan `pass`
`pass` digunakan ketika sintaks Python memerlukan sebuah pernyataan, tetapi Anda belum ingin menuliskan kode implementasi apa pun. Ini berguna untuk mencegah kesalahan (`error`) saat membuat struktur program yang belum lengkap.

Contoh kasus penggunaan `pass`:
*   **Fungsi atau Metode yang Belum Diimplementasikan**: Saat mendefinisikan fungsi (`def`) atau metode dalam kelas (`class`) tetapi belum ada logika yang ingin dituliskan.
    ```python
    def fungsi_belum_diimplementasi():
        pass

    class Hero:
        pass # Tidak ada implementasi untuk kelas Hero
    ```
*   **Blok Kondisional atau Perulangan Kosong**: Ketika Anda memiliki blok `if`, `else`, `while`, atau `for` yang harus ada, tetapi Anda ingin melewatinya tanpa melakukan apa-apa.

### Contoh `pass` dalam Perulangan `while`
Pertimbangkan perulangan berikut yang mencetak angka dari 1 hingga 5. Jika `angka` adalah 3, pernyataan `pass` akan dieksekusi.
```python
print("--- CONTOH PASS ---")
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass # Tidak melakukan apa-apa, cuma lewat doang
    print(angka)
```
**Output:**
```
--- CONTOH PASS ---
1
2
3
4
5
```
Seperti yang terlihat dari output, `pass` tidak memengaruhi alur program sama sekali. Angka 3 tetap dicetak seperti biasa, karena `pass` hanya "melewatkan" tanpa tindakan.

## 2. Pernyataan `continue`

Pernyataan `continue` berfungsi untuk **melewatkan (skip)** sisa aksi di dalam perulangan pada iterasi saat itu, dan langsung **loncat ke awal perulangan** untuk iterasi selanjutnya.

### Mekanisme `continue`
Ketika `continue` ditemui dalam sebuah perulangan, semua kode yang berada di bawah `continue` dalam blok perulangan untuk iterasi saat itu akan diabaikan. Eksekusi kemudian akan langsung melompat ke kondisi perulangan berikutnya (misalnya, ke awal `while` atau `for`) untuk memulai iterasi selanjutnya.

### Contoh `continue` dalam Perulangan `while`
Mari kita lihat contoh di mana kita ingin mencetak angka dari 1 hingga 5, tetapi dengan perlakuan khusus untuk angka 3.
```python
print("\n--- CONTOH CONTINUE ---")
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # Aksi 1

    if angka == 3:
        print("Nice!")
        continue # Loncat ke awal loop (while), skip aksi di bawahnya

    print("Whassup!") # Aksi 2
```
**Analisis Output:**
*   **Angka 1**:
    *   `angka` menjadi 1.
    *   Cetak "angka sekarang -> 1" (Aksi 1).
    *   Kondisi `if angka == 3` (yaitu `1 == 3`) adalah `False`.
    *   Cetak "Whassup!" (Aksi 2).
*   **Angka 2**:
    *   `angka` menjadi 2.
    *   Cetak "angka sekarang -> 2" (Aksi 1).
    *   Kondisi `if angka == 3` (yaitu `2 == 3`) adalah `False`.
    *   Cetak "Whassup!" (Aksi 2).
*   **Angka 3**:
    *   `angka` menjadi 3.
    *   Cetak "angka sekarang -> 3" (Aksi 1).
    *   Kondisi `if angka == 3` (yaitu `3 == 3`) adalah `True`.
    *   Cetak "Nice!".
    *   Bertemu `continue`. Ini menyebabkan program **langsung meloncat ke awal perulangan `while`** untuk iterasi berikutnya. Pernyataan `print("Whassup!")` (Aksi 2) **TIDAK DIJALANKAN** untuk iterasi ini.
*   **Angka 4**:
    *   `angka` menjadi 4.
    *   Cetak "angka sekarang -> 4" (Aksi 1).
    *   Kondisi `if angka == 3` (yaitu `4 == 3`) adalah `False`.
    *   Cetak "Whassup!" (Aksi 2).
*   **Angka 5**:
    *   `angka` menjadi 5.
    *   Cetak "angka sekarang -> 5" (Aksi 1).
    *   Kondisi `if angka == 3` (yaitu `5 == 3`) adalah `False`.
    *   Cetak "Whassup!" (Aksi 2).

**Output:**
```
--- CONTOH CONTINUE ---
angka sekarang -> 1
Whassup!
angka sekarang -> 2
Whassup!
angka sekarang -> 3
Nice!
angka sekarang -> 4
Whassup!
angka sekarang -> 5
Whassup!
```
Perhatikan bahwa "Whassup!" tidak dicetak saat `angka` adalah 3, karena `continue` melompati sisa aksi dalam iterasi tersebut.

### Penempatan `continue`
Jika pernyataan `continue` dipindahkan ke bawah, maka lebih banyak aksi dalam perulangan akan dilewati.

## 3. Perbandingan Singkat dan Teaser `break`

*   **`pass`**: Hanya sebagai **placeholder** yang tidak melakukan apa-apa. Program akan terus berjalan secara normal seolah-olah tidak ada `pass` di sana.
*   **`continue`**: **Melewatkan sisa kode** dalam iterasi saat ini dan langsung melanjutkan ke iterasi berikutnya dari perulangan.

Selain `pass` dan `continue`, ada juga pernyataan `break`. `break` digunakan untuk **menghentikan perulangan secara total**, keluar dari perulangan sepenuhnya, bukan hanya melompati satu iterasi. `break` akan dibahas lebih lanjut di video selanjutnya.
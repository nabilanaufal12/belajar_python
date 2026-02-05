# Mengenal Variabel di Python

Dalam pemrograman Python, variabel adalah konsep fundamental yang memungkinkan kita untuk menyimpan dan mengelola data. Tutorial ini membahas definisi, cara penggunaan, aturan penamaan, dan sifat-sifat variabel dalam Python.

## Interactive Shell sebagai Lingkungan Eksperimen

Sebelum masuk ke variabel, kita dapat bereksperimen dengan Python menggunakan **interactive shell**. Ini adalah lingkungan di mana kita bisa langsung mengetikkan perintah Python dan melihat hasilnya. Untuk masuk ke shell ini, ketik `python` (di Windows) atau `python3` (di Mac/Linux) di terminal.

Di interactive shell, kita bisa langsung melakukan operasi seperti `10 + 5` yang akan menghasilkan `15`. Kita juga bisa meng-assign nilai ke variabel, misalnya `a = 10`, lalu menggunakannya dalam operasi seperti `a + 5` yang juga akan menghasilkan `15`.

## Apa itu Variabel?

**Variabel** adalah tempat atau wadah untuk menyimpan data.

### Analogi dengan Matematika

Konsep variabel dalam Python sangat mirip dengan variabel dalam matematika yang mungkin sudah dipelajari di SMP.

Misalnya:
*   Jika $x = 2$
*   Dan $y = x + 4$
*   Maka nilai $y$ akan menjadi $2 + 4 = 6$.

Dalam contoh di atas:
*   $x$ disebut sebagai **variabel**.
*   Angka $2$ atau $4$ disebut sebagai **value** (nilai).

### Assignment (Penugasan Nilai)

Proses pemberian nilai ke sebuah variabel disebut **assignment**. Contohnya, `x = 2` berarti kita menugaskan nilai $2$ ke variabel $x$.

### Python: Assignment Tanpa Deklarasi Tipe Data

Salah satu perbedaan utama Python dengan bahasa pemrograman lain seperti C++ atau Java adalah Python tidak memerlukan **deklarasi** tipe data saat membuat variabel.

*   Di C++ atau Java, kita mungkin menulis `int a;` untuk mendeklarasikan variabel `a` sebagai integer, lalu `a = 10;`.
*   Di Python, kita bisa langsung melakukan assignment: `a = 10`.

## Membuat dan Menggunakan Variabel

Untuk membuat variabel, gunakan sintaks `nama_variabel = nilai`.

Contoh:
*   `a = 10` (variabel `a` menyimpan nilai `10`)
*   `x = 5` (variabel `x` menyimpan nilai `5`)
*   `panjang = 1000` (variabel `panjang` menyimpan nilai `1000`)

Untuk melihat atau menggunakan nilai yang disimpan dalam variabel, kita bisa memanggilnya. Misalnya, menggunakan fungsi `print()`:
*   `print(a)` akan menampilkan `10`.
*   Kita juga bisa mencetak variabel bersama dengan teks lain: `print('Nilai a =', a)` akan menampilkan `Nilai a = 10`.

## Aturan Penamaan Variabel

Ada beberapa aturan penting dalam menamai variabel di Python:

*   **Tidak boleh mengandung spasi**: Jika ingin menggunakan nama dengan beberapa kata, gunakan underscore (`_`) sebagai pengganti spasi.
    *   **Tidak valid**: `nilai y = 15`
    *   **Valid**: `nilai_y = 15`
*   **Tidak boleh diawali dengan angka**: Variabel tidak boleh dimulai dengan digit.
    *   **Tidak valid**: `10juta = 10000000`
*   **Boleh mengandung angka setelah karakter pertama**: Angka boleh ada di tengah atau akhir nama variabel.
    *   **Valid**: `juta10 = 10000000`
*   **Boleh menggunakan *camelCase***: Gaya penulisan `camelCase` (misalnya `nilaiZ`) juga valid.
    *   **Valid**: `nilaiZ = 17.5`

## Sifat Variabel: Nilai Dapat Diubah (Reassignment)

Nilai yang disimpan dalam variabel tidak bersifat permanen dan dapat diubah kapan saja. Ketika nilai baru di-assign ke variabel yang sudah ada, nilai lama akan ditimpa.

Contoh:
1.  `a = 10` (nilai `a` adalah `10`)
2.  `a = 7` (nilai `a` sekarang berubah menjadi `7`, menimpa nilai `10` sebelumnya)
3.  Jika `print(a)` setelah perubahan, hasilnya akan `7`.

## Assignment Tidak Langsung (Indirect Assignment)

Variabel juga dapat di-assign nilainya dari variabel lain. Ini disebut assignment tidak langsung.

Contoh:
1.  `a = 10`
2.  `a = 7` (nilai `a` sekarang `7`)
3.  `b = a` (variabel `b` akan mengambil nilai *terakhir* dari `a`, yaitu `7`)
4.  Jika `print(b)`, hasilnya akan `7`.

Ini menunjukkan bahwa variabel `b` tidak terhubung secara dinamis ke `a`; ia hanya mengambil *nilai* `a` pada saat assignment dilakukan.

## Langkah Selanjutnya: Tipe Data

Setelah memahami variabel, langkah selanjutnya adalah mempelajari **tipe data**. Variabel dapat menyimpan berbagai jenis data, seperti angka bulat (integer), angka desimal (float), teks (string), dan banyak lagi.
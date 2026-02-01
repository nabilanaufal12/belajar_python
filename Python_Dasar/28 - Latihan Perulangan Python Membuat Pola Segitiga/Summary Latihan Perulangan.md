# Latihan Perulangan Python: Membuat Pola Segitiga

Pembelajaran ini berfokus pada penerapan konsep perulangan (`for` dan `while`) dalam Python untuk membuat berbagai pola segitiga. Ini adalah latihan dasar yang membantu memahami kontrol alur program, termasuk penggunaan `break` dan `continue`.

## 1. Segitiga Siku-siku Dasar (Menggunakan `for` Loop)

Untuk membuat segitiga siku-siku sederhana, kita dapat menggunakan perulangan `for`. Logikanya adalah mencetak karakter bintang (`*`) yang jumlahnya bertambah di setiap baris.

*   **Variabel `sisi`**: Menentukan tinggi atau jumlah baris segitiga.
*   **Variabel `count`**: Bertambah satu di setiap iterasi, merepresentasikan jumlah bintang yang akan dicetak pada baris tersebut.
*   **Pencetakan Bintang**: String bintang (`"*"`) dikalikan dengan nilai `count` untuk menghasilkan baris bintang yang sesuai.

```python
sisi = 10 # Contoh: jumlah baris segitiga

print("Awal dari For Loop") #
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

print("Akhir dari For Loop") #
```

**Contoh Output (untuk `sisi = 4`):**
```
*
**
***
****
```

## 2. Segitiga Siku-siku Dasar (Menggunakan `while` Loop)

Perulangan `while` juga dapat digunakan untuk membuat pola yang sama. Perbedaan utamanya adalah kita perlu secara eksplisit mengelola kondisi berhenti agar tidak terjadi *infinite loop*.

*   **`while True`**: Membuat perulangan berjalan terus-menerus.
*   **Kondisi `break`**: Perulangan akan berhenti jika nilai `count` melebihi `sisi` yang ditentukan.
*   **Variabel `count`**: Sama seperti `for` loop, `count` bertambah di setiap iterasi untuk menentukan jumlah bintang.

```python
sisi = 10 # Contoh: jumlah baris segitiga

print("Awal dari While Loop") #
count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break #

print("Akhir dari While Loop") #
```

## 3. Segitiga dengan Baris Ganjil Saja (Menggunakan `while` Loop dengan `continue`)

Untuk membuat pola yang hanya mencetak baris dengan jumlah bintang ganjil, kita dapat memanfaatkan operator modulus (`%`) dan pernyataan `continue`.

*   **Operator Modulus (`%`)**: Digunakan untuk memeriksa apakah `count` adalah bilangan ganjil atau genap. `count % 2` akan menghasilkan `1` (True) jika `count` ganjil, dan `0` (False) jika `count` genap.
*   **Pernyataan `continue`**: Jika `count` adalah bilangan genap, `continue` akan dilewati dan perulangan akan langsung melompat ke iterasi berikutnya tanpa mencetak bintang. Ini memastikan hanya baris ganjil yang dicetak.

```python
sisi = 10 # Contoh: jumlah baris segitiga

print("Awal dari While Loop (Ganjil)") #
count = 1
while True:
    if (count % 2): # True jika ganjil
        print("*" * count) #
        count += 1
    else: # Jika genap
        count += 1
        continue #

    if count > sisi:
        break

print("Akhir dari While Loop")
```

**Contoh Output (untuk `sisi = 10`):**
```
*
***
*****
*******
*********
```

## 4. Segitiga Sama Kaki (Piramida)

Membuat segitiga sama kaki (piramida) melibatkan penambahan spasi di awal setiap baris untuk memposisikan bintang di tengah.

*   **Variabel `spasi`**: Dihitung berdasarkan `sisi` (misalnya, `sisi // 2` untuk pembagian integer) dan akan berkurang di setiap baris yang dicetak.
*   **Pencetakan**: Spasi dicetak terlebih dahulu, diikuti oleh karakter pola (misalnya `+`) yang jumlahnya sesuai dengan `count`.
*   **Logika Ganjil**: Sama seperti sebelumnya, hanya baris ganjil yang dicetak untuk membentuk piramida yang simetris.

```python
sisi = 9 # Contoh: jumlah baris segitiga (biasanya ganjil untuk piramida)

print("Awal dari Segitiga Sama Kaki") #
count = 1
spasi = int(sisi / 2) #

while True:
    if (count % 2): # Hanya cetak jika ganjil
        print(" " * spasi, "+" * count) #
        spasi -= 1 # Kurangi spasi untuk baris berikutnya
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("Akhir dari Segitiga Sama Kaki")
```

**Contoh Output (untuk `sisi = 9`):**
```
    +
   +++
  +++++
 +++++++
+++++++++
```

## Kesimpulan & Tugas Lanjutan

Latihan ini menunjukkan bagaimana perulangan `for` dan `while`, dikombinasikan dengan `break`, `continue`, dan operator modulus, dapat digunakan untuk membuat pola visual yang kompleks. Kunci utamanya adalah memahami bagaimana variabel `count` (untuk jumlah bintang) dan `spasi` (untuk posisi) berubah di setiap iterasi.

**Tugas (PR)**: Coba buat pola **Ketupat**. Pola ini merupakan pengembangan dari segitiga sama kaki, di mana setelah mencapai puncak, pola akan berbalik (spasi bertambah, bintang berkurang) untuk membentuk bagian bawah ketupat.

**Materi Selanjutnya**: Pembelajaran akan dilanjutkan dengan tipe data koleksi di Python, seperti **List, Tuple, Set, dan Dictionary**, yang merupakan bagian penting dari pemrograman Python.
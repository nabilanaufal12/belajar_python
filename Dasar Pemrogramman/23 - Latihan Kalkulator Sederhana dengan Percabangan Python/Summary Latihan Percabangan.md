# Kalkulator Sederhana dengan Percabangan Python

Catatan ini merangkum proses pembuatan kalkulator sederhana menggunakan bahasa pemrograman Python, dengan fokus pada penerapan struktur percabangan (`if-elif-else`) untuk menangani berbagai operasi matematika. Tujuannya adalah untuk memahami bagaimana program dapat mengambil keputusan berdasarkan input pengguna.

## Pendahuluan

Tutorial ini membahas latihan percabangan dalam Python dengan membuat **kalkulator sederhana**. Kalkulator ini dirancang untuk melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian antara dua angka. Logika utamanya melibatkan pengambilan input dari pengguna dan kemudian menggunakan percabangan untuk menentukan operasi yang akan dilakukan berdasarkan operator yang dimasukkan.

## Logika Dasar Kalkulator

Untuk membuat kalkulator sederhana, kita membutuhkan beberapa komponen utama:
*   **Angka 1**: Bilangan pertama yang akan dioperasikan.
*   **Operator**: Simbol operasi matematika (+, -, *, /).
*   **Angka 2**: Bilangan kedua yang akan dioperasikan.
*   **Hasil**: Output dari operasi yang dilakukan.

Alur program secara umum adalah sebagai berikut:
1.  Ambil data input dari pengguna, yaitu `angka 1`, `operator`, dan `angka 2`.
2.  Lakukan percabangan (`if-elif-else`) untuk mengecek operator yang dimasukkan.
3.  Berdasarkan operator, lakukan perhitungan yang sesuai.
4.  Tampilkan hasil perhitungan kepada pengguna.

## Implementasi Python: Mengambil Input User

Langkah pertama dalam implementasi adalah menyiapkan tampilan dan mengambil input dari pengguna.

### Tampilan Awal
Program dimulai dengan menampilkan judul "Kalkulator Sederhana" untuk user interface yang lebih baik.

```python
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")
```

### Mengambil Angka dan Operator
Input dari pengguna diambil menggunakan fungsi `input()`. Penting untuk mengubah tipe data input angka dari *string* (default dari `input()`) menjadi **float** agar dapat melakukan perhitungan desimal.

```python
angka_1 = float(input("Masukkan angka 1 = ")) # Mengubah input ke float
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("Masukkan angka 2 = ")) # Mengubah input ke float
```

## Implementasi Python: Logika Percabangan (IF-ELIF-ELSE)

Setelah mendapatkan semua input, program menggunakan struktur percabangan `if-elif-else` untuk menentukan operasi yang benar.

*   **Penjumlahan**: Jika operator adalah `+`, lakukan penjumlahan.
    ```python
    if operator == "+":
        hasil = angka_1 + angka_2
        print(f"Hasilnya adalah {hasil}") # Menggunakan f-string untuk output
    ```
*   **Pengurangan**: Jika operator adalah `-`, lakukan pengurangan.
    ```python
    elif operator == "-":
        hasil = angka_1 - angka_2
        print(f"Hasilnya adalah {hasil}")
    ```
*   **Perkalian**: Jika operator adalah `x` atau `*`, lakukan perkalian. Perhatikan penggunaan `or` untuk mengakomodasi dua simbol perkalian yang mungkin dimasukkan pengguna.
    ```python
    elif operator == "x" or operator == "*":
        hasil = angka_1 * angka_2
        print(f"Hasilnya adalah {hasil}")
    ```
*   **Pembagian**: Jika operator adalah `/`, lakukan pembagian.
    ```python
    elif operator == "/":
        hasil = angka_1 / angka_2
        print(f"Hasilnya adalah {hasil}")
    ```

## Penanganan Input Tidak Valid

Untuk operator yang tidak dikenal atau tidak didukung, blok `else` akan dieksekusi untuk memberikan pesan kesalahan kepada pengguna.

```python
else:
    print("Masukan yang bener dong!, aku pusing!")
```

Setelah semua operasi selesai, program akan menampilkan pesan penutup.

## Keterbatasan Kalkulator Sederhana

Kalkulator yang dibuat ini sangat sederhana dan memiliki keterbatasan:
*   Hanya dapat melakukan satu operasi dalam satu waktu (misalnya, `angka1 operator angka2`).
*   Tidak dapat menangani ekspresi matematika yang lebih kompleks seperti `5 * 10 + 6` atau urutan operasi (misalnya, perkalian sebelum penjumlahan). Untuk kasus seperti ini, diperlukan logika yang lebih rumit, seperti *parsing* ekspresi dan penanganan prioritas operator.

## Kode Lengkap

Berikut adalah kode Python lengkap untuk kalkulator sederhana ini:

```python
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("Masukkan angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Masukan yang bener dong!, aku pusing!")

print("Akhir dari program, terima gajih!")
```

Setelah materi percabangan ini, topik selanjutnya yang akan dibahas adalah **Looping (Perulangan)**.
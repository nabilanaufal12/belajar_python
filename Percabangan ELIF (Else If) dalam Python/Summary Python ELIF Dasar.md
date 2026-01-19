# Summary Python ELIF Dasar

> Generated: January 19th, 2026 12:31 PM
> Sources: Belajar Python [Dasar] - 22 - ELIF Statement.youtube, pasted-text-1.md

---

# Percabangan `ELIF` (Else If) dalam Python

## Gambaran Umum

Pernyataan `ELIF` (singkatan dari "Else If") dalam Python adalah konstruksi percabangan yang memungkinkan program untuk mengevaluasi beberapa kondisi secara berurutan. Ini merupakan pengembangan dari pernyataan `if-else` dasar, yang hanya menangani dua kemungkinan jalur eksekusi (kondisi benar atau salah). Dengan `ELIF`, kita dapat membuat program yang merespons berbagai skenario dengan lebih spesifik, mirip dengan "tangga" kondisi yang diperiksa satu per satu.

## Konsep Dasar dan Alur Eksekusi

Ketika menggunakan `if-elif-else`, Python akan mengevaluasi kondisi secara berurutan dari atas ke bawah:

1.  **Kondisi `if` pertama** akan diperiksa.
    *   Jika kondisi ini `True`, blok kode di bawah `if` akan dieksekusi, dan seluruh struktur `if-elif-else` akan dilewati (program akan melanjutkan ke kode setelah blok percabangan).
2.  **Jika kondisi `if` pertama `False`**, Python akan melanjutkan untuk memeriksa **kondisi `elif` pertama**.
    *   Jika kondisi `elif` ini `True`, blok kode di bawah `elif` tersebut akan dieksekusi, dan sisa struktur percabangan akan dilewati.
3.  Proses ini berlanjut untuk **setiap pernyataan `elif` berikutnya**. Python akan memeriksa kondisi `elif` satu per satu hanya jika semua kondisi `if` dan `elif` sebelumnya adalah `False`.
4.  **Jika semua kondisi `if` dan `elif` adalah `False`**, dan ada pernyataan `else` di akhir, maka blok kode di bawah `else` akan dieksekusi. Pernyataan `else` berfungsi sebagai penangkap kondisi *default* atau "sisanya" ketika tidak ada kondisi lain yang terpenuhi.

Penting untuk diingat bahwa **urutan kondisi sangat penting**. Begitu satu kondisi ditemukan `True`, Python akan mengeksekusi blok kode yang sesuai dan tidak akan memeriksa kondisi `elif` atau `else` lainnya di bawahnya.

## Sintaks `ELIF` dalam Python

Sintaks umum untuk struktur `if-elif-else` adalah sebagai berikut:

```python
if kondisi_1:
    # Aksi yang dilakukan jika kondisi_1 True
elif kondisi_2:
    # Aksi yang dilakukan jika kondisi_2 True (dan kondisi_1 False)
elif kondisi_3:
    # Aksi yang dilakukan jika kondisi_3 True (dan kondisi_1, kondisi_2 False)
# ... bisa ada lebih banyak elif ...
else:
    # Aksi default jika semua kondisi di atas False
```

## Contoh Implementasi: Program Sapaan Nama

Berikut adalah contoh program sederhana yang menggunakan `if-elif-else` untuk menyapa pengguna berdasarkan nama yang mereka masukkan:

```python
nama = input("Nama kamu siapa? ") # Meminta input nama dari pengguna

if nama == "ucup": # Kondisi 1: Jika nama adalah "ucup"
    print("Hai ganteng beuds!") # Aksi 1
elif nama == "otong": # Kondisi 2: Jika nama adalah "otong" (dan bukan "ucup")
    print("Hai si kece bangeeet!") # Aksi 2
elif nama == "mario": # Kondisi 3: Jika nama adalah "mario" (dan bukan "ucup" atau "otong")
    print("Hai humoriis!") # Aksi 3
else: # Kondisi default: Jika nama bukan "ucup", "otong", atau "mario"
    print("Au ah gak kenal!") # Aksi default

print("ini adalah akhir dari program") # Pernyataan ini selalu dieksekusi setelah blok if-elif-else
```

**Contoh Alur Eksekusi:**

*   Jika input `ucup`: Program akan mencetak "Hai ganteng beuds!" dan kemudian "ini adalah akhir dari program". Kondisi `elif` dan `else` tidak akan diperiksa.
*   Jika input `otong`: Kondisi `if nama == "ucup"` akan `False`. Program kemudian memeriksa `elif nama == "otong"`, yang akan `True`. Program mencetak "Hai si kece bangeeet!" dan kemudian "ini adalah akhir dari program".
*   Jika input `bambang`: Semua kondisi `if` dan `elif` akan `False`. Program akan mengeksekusi blok `else` dan mencetak "Au ah gak kenal!", diikuti oleh "ini adalah akhir dari program".

## Poin Penting dan Tips

*   **Banyaknya `elif`**: Anda dapat menggunakan sebanyak mungkin pernyataan `elif` sesuai kebutuhan untuk menangani berbagai kondisi spesifik.
*   **`else` bersifat opsional**: Pernyataan `else` tidak wajib ada dalam struktur `if-elif`. Namun, sangat disarankan untuk menggunakannya sebagai penanganan *default* untuk kasus-kasus yang tidak terduga atau tidak spesifik.
*   **Urutan adalah kunci**: Python mengevaluasi kondisi dari atas ke bawah. Pastikan kondisi yang lebih spesifik diletakkan di atas kondisi yang lebih umum jika ada potensi tumpang tindih.
*   **Perbedaan dengan `if-else`**: `if-else` hanya memiliki dua jalur (benar atau salah), sedangkan `if-elif-else` memungkinkan banyak jalur percabangan berdasarkan beberapa kondisi yang berbeda.

Pernyataan `if-elif-else` sangat berguna untuk membangun aplikasi yang lebih kompleks, seperti kalkulator sederhana yang dapat mendeteksi berbagai operator matematika (`+`, `-`, `*`, `/`) dan melakukan operasi yang sesuai.
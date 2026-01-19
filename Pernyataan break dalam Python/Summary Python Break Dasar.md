# Summary Python Break Dasar

> Generated: January 19th, 2026 8:13 PM
> Sources: Belajar Python [Dasar] - 27 - Break.youtube, pasted-text-1.md

---

# Pernyataan `break` dalam Python

Pernyataan `break` adalah salah satu kontrol aliran dalam perulangan (loop) di Python yang berfungsi untuk menghentikan eksekusi loop secara total dan segera keluar dari blok perulangan tersebut. Ini berbeda dengan pernyataan `continue`, yang hanya akan melewati sisa kode pada iterasi saat ini dan melanjutkan ke iterasi berikutnya dari loop.

## Konsep dan Fungsi `break`

Ketika `break` dieksekusi di dalam sebuah loop (baik `for` maupun `while`), program akan langsung keluar dari loop tersebut dan melanjutkan eksekusi ke baris kode setelah loop.

**Perbedaan `break` dan `continue`:**
*   **`continue`**: Melewati sisa aksi di bawahnya dalam iterasi saat ini, lalu kembali ke awal loop untuk iterasi berikutnya.
*   **`break`**: Menghentikan loop sepenuhnya. Program langsung keluar dari loop dan melanjutkan ke kode setelah loop berakhir.

**Fungsi utama `break`:**
1.  **Pencarian Data**: Menghentikan pencarian segera setelah data yang dicari ditemukan, menghindari pemrosesan iterasi yang tidak perlu.
2.  **Mengontrol Loop Tak Terbatas**: Menghentikan loop yang dirancang untuk berjalan terus-menerus (misalnya `while True`) berdasarkan kondisi tertentu.

## Contoh Dasar Penggunaan `break`

Pertimbangkan sebuah loop `while` yang menghitung angka dari 1 hingga 5. Kita ingin menghentikan loop ini jika angka mencapai 3.

```python
print("--- CONTOH 1 ---")
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("Nice!")
        break # Loop langsung berhenti total di sini

    print("Whassup!")

print("Finish!\n")
```

**Penjelasan dan Output:**
1.  **`angka = 1`**: `print("angka sekarang -> 1")`, kondisi `angka == 3` salah, `print("Whassup!")`.
2.  **`angka = 2`**: `print("angka sekarang -> 2")`, kondisi `angka == 3` salah, `print("Whassup!")`.
3.  **`angka = 3`**: `print("angka sekarang -> 3")`, kondisi `angka == 3` benar.
    *   `print("Nice!")` dieksekusi.
    *   Pernyataan `break` dieksekusi. Loop `while` segera berhenti.
    *   Baris `print("Whassup!")` tidak dieksekusi untuk iterasi ini.
    *   Iterasi untuk `angka = 4` dan `angka = 5` tidak pernah terjadi.
4.  Program melanjutkan eksekusi setelah loop, yaitu `print("Finish!")`.

**Output yang dihasilkan:**
```
--- CONTOH 1 ---
angka sekarang -> 1
Whassup!
angka sekarang -> 2
Whassup!
angka sekarang -> 3
Nice!
Finish!
```

## Contoh Implementasi dengan Input Pengguna

`break` sangat berguna untuk mengontrol loop tak terbatas (`while True`) berdasarkan input atau kondisi yang ditentukan pengguna.

```python
print("--- CONTOH 2 ---")
data_int = int(input("Hitung sampai = "))

angka = 0
while True: # Loop selamanya (Infinite Loop)
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("Nice!")
        break # Berhenti jika angka sudah mencapai target user

    print("Whassup!")

print("Finish!")
```

**Penjelasan:**
Dalam contoh ini, loop `while True` akan berjalan tanpa henti jika tidak ada `break`. Namun, dengan adanya kondisi `if angka == data_int: break`, loop akan berhenti secara terkontrol saat variabel `angka` mencapai nilai yang dimasukkan oleh pengguna (`data_int`). Ini memungkinkan program untuk melakukan tugas berulang sampai kondisi tertentu terpenuhi, yang seringkali ditentukan secara dinamis.

Misalnya, jika pengguna memasukkan `5` untuk "Hitung sampai = ":
```
--- CONTOH 2 ---
Hitung sampai = 5
count = 1
Whassup!
count = 2
Whassup!
count = 3
Whassup!
count = 4
Whassup!
count = 5
Nice!
Finish!
```

Pernyataan `break` adalah alat yang ampuh untuk mengelola aliran eksekusi dalam perulangan, memungkinkan pengembang untuk membuat loop yang lebih efisien dan responsif terhadap kondisi dinamis.
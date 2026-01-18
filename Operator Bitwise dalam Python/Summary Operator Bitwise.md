# Summary Operator Bitwise

> Generated: January 17th, 2026 2:28 PM
> Sources: Belajar Python [Dasar] - 13 - Operator Bitwise.youtube, pasted-text-1.md

---

# Operator Bitwise dalam Python

Operator bitwise adalah operasi tambahan dalam Python yang bekerja pada tingkat **bit** (binary digit) dari angka integer. Ini berarti operasi dilakukan pada masing-masing 0 dan 1 yang membentuk representasi biner dari sebuah angka. Meskipun mungkin tidak sering digunakan oleh pemula, pemahaman tentang operator ini penting untuk pengetahuan dasar pemrograman.

## Konsep Dasar Representasi Biner

Sebelum memahami operator bitwise, penting untuk mengetahui bagaimana angka integer direpresentasikan dalam format biner. Setiap angka integer dapat diubah menjadi serangkaian bit (0 dan 1).

*   **Representasi Biner**: Angka biner dibaca dari kanan ke kiri, di mana setiap posisi mewakili pangkat dari 2, dimulai dari $2^0$ (indeks 0).
    *   $2^0 = 1$
    *   $2^1 = 2$
    *   $2^2 = 4$
    *   $2^3 = 8$
    *   dan seterusnya.

*   **Contoh Konversi**:
    *   Angka **1** dalam 8-bit biner adalah `00000001` ($2^0$).
    *   Angka **2** dalam 8-bit biner adalah `00000010` ($2^1$).
    *   Angka **9** dalam 8-bit biner adalah `00001001` ($2^3 + 2^0 = 8 + 1$).

Untuk menampilkan representasi biner dari sebuah angka di Python, kita dapat menggunakan fungsi `format()` dengan spesifier `'08b'` untuk memastikan output 8-bit.

```python
a = 9
b = 5

print(f"Nilai a: {a}, biner: {format(a, '08b')}")
print(f"Nilai b: {b}, biner: {format(b, '08b')}")
# Output:
# Nilai a: 9, biner: 00001001
# Nilai b: 5, biner: 00000101
```

## Jenis-jenis Operator Bitwise

Python menyediakan beberapa operator bitwise: OR, AND, XOR, NOT, Shift Right, dan Shift Left.

### 1. Bitwise OR (`|`)

*   **Simbol**: `|` (palang tegak).
*   **Aturan**: Jika salah satu atau kedua bit adalah `1`, hasilnya adalah `1`. Jika kedua bit adalah `0`, hasilnya adalah `0`.

*   **Contoh**: `9 | 5`
    ```
    00001001 (9)
    00000101 (5)
    ---------- (|)
    00001101 (13)
    ```
    $00001101_2 = 2^3 + 2^2 + 2^0 = 8 + 4 + 1 = 13$.

*   **Kode Python**:
    ```python
    c_or = a | b
    print(f"Hasil a | b: {c_or}, biner: {format(c_or, '08b')}")
    # Output: Hasil a | b: 13, biner: 00001101
    ```

### 2. Bitwise AND (`&`)

*   **Simbol**: `&` (ampersand).
*   **Aturan**: Hasilnya adalah `1` hanya jika kedua bit adalah `1`. Jika tidak, hasilnya adalah `0`.

*   **Contoh**: `9 & 5`
    ```
    00001001 (9)
    00000101 (5)
    ---------- (&)
    00000001 (1)
    ```
    $00000001_2 = 2^0 = 1$.

*   **Kode Python**:
    ```python
    c_and = a & b
    print(f"Hasil a & b: {c_and}, biner: {format(c_and, '08b')}")
    # Output: Hasil a & b: 1, biner: 00000001
    ```

### 3. Bitwise XOR (`^`)

*   **Simbol**: `^` (topi/caret).
*   **Aturan**: Hasilnya adalah `1` jika bit-nya berbeda (satu `0` dan satu `1`). Hasilnya adalah `0` jika bit-nya sama (keduanya `0` atau keduanya `1`).

*   **Contoh**: `9 ^ 5`
    ```
    00001001 (9)
    00000101 (5)
    ---------- (^)
    00001100 (12)
    ```
    $00001100_2 = 2^3 + 2^2 = 8 + 4 = 12$.

*   **Kode Python**:
    ```python
    c_xor = a ^ b
    print(f"Hasil a ^ b: {c_xor}, biner: {format(c_xor, '08b')}")
    # Output: Hasil a ^ b: 12, biner: 00001100
    ```

### 4. Bitwise NOT (`~`)

*   **Simbol**: `~` (tilde).
*   **Aturan**: Operator ini membalikkan setiap bit (0 menjadi 1, 1 menjadi 0). Namun, di Python, karena angka integer adalah **signed** (memiliki tanda positif/negatif), hasilnya tidak hanya pembalikan bit sederhana.
*   **Rumus**: Python menggunakan rumus `~a = -a - 1` untuk operator NOT. Ini sering disebut sebagai perilaku "mirroring" di mana angka positif dicerminkan ke angka negatif.

*   **Contoh**: `~9`
    *   Menggunakan rumus: `~9 = -9 - 1 = -10`.

*   **Kode Python**:
    ```python
    c_not = ~a
    print(f"Hasil ~a: {c_not}")
    # Output: Hasil ~a: -10
    ```

*   **Catatan**: Jika ingin benar-benar membalikkan semua bit (seperti *flipping* bit tanpa efek tanda), triknya adalah menggunakan operator XOR dengan semua bit `1`.

### 5. Shift Right (`>>`)

*   **Simbol**: `>>`.
*   **Aturan**: Menggeser bit ke kanan sejumlah posisi yang ditentukan. Bit yang digeser keluar dari ujung kanan akan hilang, dan bit `0` akan ditambahkan di ujung kiri. Efeknya mirip dengan pembagian integer dengan pangkat 2.

*   **Contoh**: `9 >> 2` (geser 9 ke kanan 2 kali)
    ```
    00001001 (9)
    Geser kanan 1 kali: 00000100 (4)
    Geser kanan 2 kali: 00000010 (2)
    ```
    $00000010_2 = 2^1 = 2$.

*   **Kode Python**:
    ```python
    c_sr = a >> 2
    print(f"Hasil a >> 2: {c_sr}, biner: {format(c_sr, '08b')}")
    # Output: Hasil a >> 2: 2, biner: 00000010
    ```

### 6. Shift Left (`<<`)

*   **Simbol**: `<<`.
*   **Aturan**: Menggeser bit ke kiri sejumlah posisi yang ditentukan. Bit yang digeser keluar dari ujung kiri akan hilang, dan bit `0` akan ditambahkan di ujung kanan. Efeknya mirip dengan perkalian dengan pangkat 2.

*   **Contoh**: `9 << 2` (geser 9 ke kiri 2 kali)
    ```
    00001001 (9)
    Geser kiri 1 kali: 00010010 (18)
    Geser kiri 2 kali: 00100100 (36)
    ```
    $00100100_2 = 2^5 + 2^2 = 32 + 4 = 36$.

*   **Kode Python**:
    ```python
    c_sl = a << 2
    print(f"Hasil a << 2: {c_sl}, biner: {format(c_sl, '08b')}")
    # Output: Hasil a << 2: 36, biner: 00100100
    ```

## Kesimpulan

Operator bitwise memungkinkan manipulasi data pada tingkat bit, yang bisa berguna dalam skenario tertentu seperti pengoptimalan kinerja, pengolahan data biner, atau implementasi algoritma kriptografi. Penting untuk diingat bahwa angka di Python adalah *signed*, yang memengaruhi perilaku operator NOT (`~`).
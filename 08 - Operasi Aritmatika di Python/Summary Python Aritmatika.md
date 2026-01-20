# Catatan Studi: Operasi Aritmatika di Python

## Pendahuluan
Dalam pemrograman, operasi aritmatika merupakan dasar yang esensial, mencakup perhitungan seperti penjumlahan, pengurangan, perkalian, dan pembagian. Python menyediakan berbagai operator untuk melakukan perhitungan ini, mulai dari yang dasar hingga yang lebih spesifik seperti eksponen, modulus, dan *floor division*.

## Operasi Aritmatika Dasar

Python mendukung operasi aritmatika standar yang sering digunakan dalam matematika:

*   **Penjumlahan (`+`)**
    Operator `+` digunakan untuk menjumlahkan dua nilai.
    Contoh: `a = 10`, `b = 3`, maka `a + b` akan menghasilkan `13`.
    ```python
    a = 10
    b = 3
    hasil = a + b
    print(f"{a} + {b} = {hasil}") # Output: 10 + 3 = 13
    ```

*   **Pengurangan (`-`)**
    Operator `-` digunakan untuk mengurangi satu nilai dari nilai lainnya.
    Contoh: `a = 10`, `b = 3`, maka `a - b` akan menghasilkan `7`.
    ```python
    a = 10
    b = 3
    hasil = a - b
    print(f"{a} - {b} = {hasil}") # Output: 10 - 3 = 7
    ```

*   **Perkalian (`*`)**
    Operator `*` digunakan untuk perkalian. Penting untuk menggunakan tanda bintang (`*`) dan bukan huruf `x` untuk operasi ini.
    Contoh: `a = 10`, `b = 3`, maka `a * b` akan menghasilkan `30`.
    ```python
    a = 10
    b = 3
    hasil = a * b
    print(f"{a} * {b} = {hasil}") # Output: 10 * 3 = 30
    ```

*   **Pembagian (`/`)**
    Operator `/` digunakan untuk pembagian. Di Python, hasil dari operasi pembagian akan selalu bertipe data **float** (bilangan desimal), bahkan jika hasilnya adalah bilangan bulat.
    Contoh: `a = 10`, `b = 3`, maka `a / b` akan menghasilkan `3.333...`.
    ```python
    a = 10
    b = 3
    hasil = a / b
    print(f"{a} / {b} = {hasil}") # Output: 10 / 3 = 3.3333333333333335
    ```

## Operasi Aritmatika Khusus

Selain operasi dasar, Python juga memiliki operator aritmatika khusus:

*   **Eksponen / Pangkat (`**`)**
    Operator `**` digunakan untuk menghitung pangkat (eksponen).
    Contoh: `a = 10`, `b = 3`, maka `a ** b` (10 pangkat 3) akan menghasilkan `1000`.
    ```python
    a = 10
    b = 3
    hasil = a ** b
    print(f"{a} ** {b} = {hasil}") # Output: 10 ** 3 = 1000
    ```

*   **Modulus (`%`)**
    Operator `%` mengembalikan **sisa pembagian** dari dua bilangan.
    Contoh: `10 % 3` akan menghasilkan `1` (karena 10 dibagi 3 adalah 3 sisa 1). Jika `12 % 3`, hasilnya adalah `0` karena tidak ada sisa pembagian.
    ```python
    a = 10
    b = 3
    hasil = a % b
    print(f"{a} % {b} = {hasil}") # Output: 10 % 3 = 1

    a = 12
    b = 3
    hasil = a % b
    print(f"{a} % {b} = {hasil}") # Output: 12 % 3 = 0
    ```

*   **Floor Division (`//`)**
    Operator `//` melakukan pembagian dan kemudian **membulatkan hasilnya ke bawah** ke bilangan bulat terdekat. Ini menghasilkan bagian bilangan bulat dari hasil pembagian.
    Contoh: `10 // 3` akan menghasilkan `3` (karena 10 dibagi 3 adalah 3.33..., dibulatkan ke bawah menjadi 3).
    ```python
    a = 10
    b = 3
    hasil = a // b
    print(f"{a} // {b} = {hasil}") # Output: 10 // 3 = 3
    ```

## Prioritas Operasi (Operator Precedence)

Ketika sebuah ekspresi mengandung lebih dari satu operator, Python mengikuti aturan prioritas operasi untuk menentukan urutan eksekusi. Urutan ini mirip dengan aturan matematika pada umumnya.

Berikut adalah urutan prioritas operator aritmatika dari yang tertinggi ke terendah:

1.  **Kurung `()`**: Operasi di dalam tanda kurung selalu dieksekusi terlebih dahulu, mengesampingkan prioritas operator lain.
2.  **Eksponen `**`**: Operator pangkat memiliki prioritas tertinggi setelah tanda kurung.
3.  **Perkalian `*`, Pembagian `/`, Modulus `%`, Floor Division `//`**: Operator-operator ini memiliki prioritas yang sama. Jika ada beberapa operator ini dalam satu ekspresi, mereka dieksekusi dari kiri ke kanan.
4.  **Penjumlahan `+`, Pengurangan `-`**: Operator-operator ini memiliki prioritas terendah. Jika ada beberapa operator ini dalam satu ekspresi, mereka dieksekusi dari kiri ke kanan.

**Contoh Kasus Prioritas Operasi:**
Misalkan kita memiliki ekspresi kompleks dengan nilai `x = 3`, `y = 2`, dan `z = 4`:
`hasil = x ** y * z + x / y - y % z // x`

Langkah-langkah evaluasi berdasarkan prioritas:
1.  **Eksponen**: `x ** y` menjadi `3 ** 2 = 9`.
    Ekspresi menjadi: `9 * z + x / y - y % z // x`
2.  **Perkalian/Pembagian/Modulus/Floor Division (dari kiri ke kanan)**:
    *   `9 * z` menjadi `9 * 4 = 36`.
        Ekspresi menjadi: `36 + x / y - y % z // x`
    *   `x / y` menjadi `3 / 2 = 1.5`.
        Ekspresi menjadi: `36 + 1.5 - y % z // x`
    *   `y % z` menjadi `2 % 4 = 2` (sisa pembagian 2 dibagi 4 adalah 2).
        Ekspresi menjadi: `36 + 1.5 - 2 // x`
    *   `2 // x` menjadi `2 // 3 = 0` (floor division 2 dibagi 3 adalah 0).
        Ekspresi menjadi: `36 + 1.5 - 0`
3.  **Penjumlahan/Pengurangan (dari kiri ke kanan)**:
    *   `36 + 1.5` menjadi `37.5`.
        Ekspresi menjadi: `37.5 - 0`
    *   `37.5 - 0` menjadi `37.5`.
        Hasil akhir adalah `37.5`.

**Penggunaan Tanda Kurung untuk Mengubah Prioritas:**
Tanda kurung dapat digunakan untuk memaksa operasi tertentu dieksekusi terlebih dahulu, meskipun prioritas operatornya lebih rendah.
Contoh:
*   Tanpa kurung: `x + y * z` dengan `x=3, y=2, z=4` akan dihitung sebagai `3 + (2 * 4) = 3 + 8 = 11`.
*   Dengan kurung: `(x + y) * z` dengan `x=3, y=2, z=4` akan dihitung sebagai `(3 + 2) * 4 = 5 * 4 = 20`.
    ```python
    x = 3
    y = 2
    z = 4

    # Tanpa kurung
    hasil_tanpa_kurung = x + y * z
    print(f"Hasil tanpa kurung: {hasil_tanpa_kurung}") # Output: 11

    # Dengan kurung
    hasil_dengan_kurung = (x + y) * z
    print(f"Hasil dengan kurung: {hasil_dengan_kurung}") # Output: 20
    ```
Tanda kurung "mengambil langkah paling pertama" dalam urutan eksekusi.
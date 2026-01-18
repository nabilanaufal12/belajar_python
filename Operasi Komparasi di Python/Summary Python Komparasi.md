# Summary Python Komparasi

> Generated: January 15th, 2026 8:53 PM
> Sources: Belajar Python [Dasar] - 10 - Operasi Komparasi.youtube, pasted-text-1.md

---

# Operasi Komparasi di Python

## Pendahuluan

Operasi komparasi dalam Python digunakan untuk membandingkan dua nilai atau objek. Hasil dari setiap operasi komparasi selalu berupa nilai **Boolean**, yaitu `True` atau `False`.

Python menyediakan berbagai operator komparasi yang dapat dibagi menjadi dua kategori utama: operator komparasi berbasis nilai dan operator identitas objek.

## Operator Komparasi Berbasis Nilai (Value-based Comparison Operators)

Operator ini membandingkan nilai dari dua operan.

### 1. Lebih Besar Dari (`>`)

Operator `>` menguji apakah nilai di sisi kiri lebih besar dari nilai di sisi kanan. Hasilnya `True` jika kondisi terpenuhi, `False` jika tidak.

*   **Contoh**:
    *   `a = 4`, `b = 2`
    *   `a > 3` $\rightarrow$ `True` (karena 4 lebih besar dari 3)
    *   `b > 3` $\rightarrow$ `False` (karena 2 tidak lebih besar dari 3)
    *   `b > 2` $\rightarrow$ `False` (karena 2 *sama dengan* 2, bukan *lebih besar* dari 2. Untuk menjadi `True`, nilainya harus lebih besar, misalnya `2.0001`)

### 2. Kurang Dari (`<`)

Operator `<` menguji apakah nilai di sisi kiri kurang dari nilai di sisi kanan. Hasilnya `True` jika kondisi terpenuhi, `False` jika tidak.

*   **Contoh**:
    *   `a = 4`, `b = 2`
    *   `a < 3` $\rightarrow$ `False` (karena 4 tidak kurang dari 3)
    *   `b < 3` $\rightarrow$ `True` (karena 2 kurang dari 3)
    *   `b < 2` $\rightarrow$ `False` (karena 2 *sama dengan* 2, bukan *kurang dari* 2)

### 3. Lebih Besar Sama Dengan (`>=`)

Operator `>=` menguji apakah nilai di sisi kiri lebih besar dari atau sama dengan nilai di sisi kanan. Batas nilai (angka yang dibandingkan) termasuk dalam kondisi `True`.

*   **Contoh**:
    *   `a = 4`, `b = 2`
    *   `a >= 3` $\rightarrow$ `True` (karena 4 lebih besar dari 3)
    *   `b >= 3` $\rightarrow$ `False` (karena 2 tidak lebih besar atau sama dengan 3)
    *   `b >= 2` $\rightarrow$ `True` (karena 2 sama dengan 2)

### 4. Kurang Dari Sama Dengan (`<=`)

Operator `<=` menguji apakah nilai di sisi kiri kurang dari atau sama dengan nilai di sisi kanan. Batas nilai (angka yang dibandingkan) termasuk dalam kondisi `True`.

*   **Contoh**:
    *   `a = 4`, `b = 2`
    *   `a <= 3` $\rightarrow$ `False` (karena 4 tidak kurang dari atau sama dengan 3)
    *   `b <= 3` $\rightarrow$ `True` (karena 2 kurang dari 3)
    *   `b <= 2` $\rightarrow$ `True` (karena 2 sama dengan 2)

### 5. Sama Dengan (`==`)

Operator `==` digunakan untuk membandingkan apakah dua nilai sama. Ini membandingkan **nilai** (value) dari operan.

*   **Penting**: Operator `==` berbeda dengan operator `=` (assignment). Operator `=` digunakan untuk memberikan nilai ke sebuah variabel, sedangkan `==` digunakan untuk komparasi.
*   **Contoh**:
    *   `a = 4`, `b = 2`
    *   `a == 4` $\rightarrow$ `True` (karena nilai `a` adalah 4)
    *   `b == 4` $\rightarrow$ `False` (karena nilai `b` adalah 2, bukan 4)

### 6. Tidak Sama Dengan (`!=`)

Operator `!=` menguji apakah dua nilai tidak sama. Ini adalah kebalikan dari operator `==`.

*   **Contoh**:
    *   `a = 4`, `b = 2`
    *   `a != 4` $\rightarrow$ `False` (karena nilai `a` adalah 4, jadi mereka sama)
    *   `b != 4` $\rightarrow$ `True` (karena nilai `b` adalah 2, yang tidak sama dengan 4)

## Operator Identitas Objek (Object Identity Operators)

Operator `is` dan `is not` membandingkan **identitas objek** atau **alamat memori** dari dua variabel, bukan hanya nilainya.

### 1. `is`

Operator `is` menguji apakah dua variabel merujuk pada objek yang sama di memori.

*   **Konsep Identitas Objek**: Setiap objek di Python memiliki identitas unik, yang dapat diakses menggunakan fungsi `id()`. Alamat memori ini sering direpresentasikan dalam format heksadesimal menggunakan `hex(id())`.
*   **Optimisasi Python**: Untuk nilai-nilai sederhana seperti bilangan bulat kecil (misalnya -5 hingga 256), Python melakukan optimisasi dengan menyimpan nilai-nilai ini di lokasi memori yang sama. Ini berarti jika dua variabel memiliki nilai bilangan bulat kecil yang sama, mereka mungkin akan merujuk pada objek yang sama di memori.
*   **Contoh**:
    ```python
    x = 5
    y = 5
    print('nilai x =', x, ', id =', hex(id(x)))
    print('nilai y =', y, ', id =', hex(id(y)))
    print(x is y) # True (karena id/address-nya sama)
    ```
    Output menunjukkan `id` untuk `x` dan `y` adalah sama, sehingga `x is y` menghasilkan `True`.
*   **Perbedaan Nilai**: Jika nilai berbeda, alamat memori juga akan berbeda.
    ```python
    x = 5
    y = 6
    # id mereka akan berbeda
    print(x is y) # False
    ```
    Output menunjukkan `id` untuk `x` dan `y` berbeda, sehingga `x is y` menghasilkan `False`.
*   **`is` vs `==`**:
    *   Gunakan `==` untuk membandingkan **nilai** (value) dari dua objek.
    *   Gunakan `is` untuk membandingkan **identitas objek** (apakah mereka adalah objek yang sama di memori).
*   **Peringatan Penggunaan `is` dengan Literal**: Sejak Python 3.5, menggunakan `is` untuk membandingkan variabel dengan literal (misalnya `x is 5`) akan menghasilkan *Syntax Warning*. Disarankan untuk selalu menggunakan `==` saat membandingkan dengan literal.

### 2. `is not`

Operator `is not` adalah kebalikan dari `is`. Ini menguji apakah dua variabel tidak merujuk pada objek yang sama di memori.

*   **Contoh**:
    *   `x = 5`, `y = 6`
    *   `x is not y` $\rightarrow$ `True` (karena `x` dan `y` merujuk pada objek yang berbeda)
    *   `x = 5`, `y = 5`
    *   `x is not y` $\rightarrow$ `False` (karena `x` dan `y` merujuk pada objek yang sama)

Operator `is` dan `is not` sangat berguna ketika bekerja dengan objek yang lebih kompleks atau ketika perlu memastikan apakah dua variabel benar-benar menunjuk ke instance objek yang sama, bukan hanya memiliki nilai yang sama.
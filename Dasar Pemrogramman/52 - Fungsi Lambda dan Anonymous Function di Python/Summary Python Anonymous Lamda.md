# Fungsi Lambda dan Anonymous Function di Python

## Pendahuluan
Catatan ini membahas tentang **Fungsi Lambda** (juga dikenal sebagai **Anonymous Function**) di Python, sebuah konsep yang memungkinkan pembuatan fungsi sederhana dalam satu baris kode. Pembahasan meliputi definisi, sintaks dasar, serta berbagai kegunaannya dalam pemrograman Python, termasuk *sorting*, *filtering*, dan teknik *currying*.

## Apa itu Fungsi Lambda?
**Fungsi Lambda** adalah cara untuk membuat fungsi yang ringkas dan sederhana dalam satu baris, tanpa perlu menggunakan kata kunci `def` dan memberikan nama pada fungsi tersebut.

*   **Perbandingan dengan Fungsi `def` Biasa**:
    Secara tradisional, sebuah fungsi untuk menghitung kuadrat angka didefinisikan sebagai berikut:
    ```python
    def kuadrat(angka):
        return angka**2
    ```
    Dengan Lambda, fungsi yang sama dapat ditulis lebih ringkas:
    ```python
    kuadrat = lambda angka: angka**2
    print(kuadrat(3)) # Output: 9
    ```

*   **Sintaks Umum**:
    Bentuk umum dari fungsi Lambda adalah `lambda argument: expression`.
    *   `argument`: Satu atau lebih parameter yang diterima fungsi.
    *   `expression`: Ekspresi yang akan dievaluasi dan hasilnya akan dikembalikan oleh fungsi.

*   **Contoh dengan Banyak Argumen**:
    Fungsi Lambda dapat menerima lebih dari satu argumen.
    ```python
    pangkat = lambda num, pow: num**pow
    print(pangkat(4, 2)) # Output: 16 (4 pangkat 2)
    ```

## Kegunaan Fungsi Lambda

Fungsi Lambda sangat berguna ketika dibutuhkan fungsi kecil sebagai parameter untuk fungsi lain, sehingga kode menjadi lebih ringkas dan mudah dibaca.

### 1. Sorting List
Lambda sering digunakan untuk mengurutkan list berdasarkan kriteria tertentu yang ditentukan secara *on-the-fly*.
Contoh, mengurutkan list string berdasarkan panjang stringnya:
```python
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama: len(nama))
print(data_list)
# Output: ['Ucup', 'Otong', 'Dudung'] (Urut berdasarkan panjang string)
```
Tanpa Lambda, kita perlu mendefinisikan fungsi `def` terpisah untuk `key` parameter, yang akan membuat kode lebih panjang.

### 2. Filtering List
Lambda juga sering dikombinasikan dengan fungsi `filter()` untuk menyaring elemen-elemen dalam sebuah list berdasarkan kondisi tertentu.
Contoh, memfilter angka yang kurang dari 5 dari sebuah list:
```python
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka_kecil = list(filter(lambda x: x < 5, data_angka))
print(angka_kecil) # Output: [1, 2, 3, 4]
```

Contoh lain untuk memfilter angka genap, ganjil, atau kelipatan tertentu:
```python
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Ambil angka genap
data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(f"Angka Genap: {data_genap}") # Output: [2, 4, 6, 8, 10, 12]

# Ambil angka ganjil
data_ganjil = list(filter(lambda x: (x % 2 != 0), data_angka))
print(f"Angka Ganjil: {data_ganjil}") # Output: [1, 3, 5, 7, 9, 11]

# Ambil kelipatan 3
data_3 = list(filter(lambda x: (x % 3 == 0), data_angka))
print(f"Kelipatan 3: {data_3}") # Output: [3, 6, 9, 12]
```

### 3. Anonymous Function (Currying)
Salah satu teknik lanjutan dengan Lambda adalah **Currying**, sebuah konsep yang berasal dari Haskell Curry. Currying memungkinkan kita membuat fungsi yang mengembalikan fungsi lain sebagai hasilnya. Ini sangat berguna dalam paradigma *Functional Programming*.

Contoh implementasi Currying untuk membuat fungsi pangkat:
```python
def pangkat(n):
    return lambda angka: angka**n

pangkat2 = pangkat(2) # Membuat fungsi yang akan memangkatkan angka dengan 2
print(pangkat2(5)) # Output: 25 (5 pangkat 2)

pangkat3 = pangkat(3) # Membuat fungsi yang akan memangkatkan angka dengan 3
print(pangkat3(3)) # Output: 27 (3 pangkat 3)
```
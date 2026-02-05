# Fungsi dengan Return Value di Python

## Pendahuluan

Dalam pemrograman Python, fungsi adalah blok kode yang dirancang untuk melakukan tugas tertentu. Untuk membuat fungsi yang lebih fleksibel dan dapat menghasilkan nilai yang bisa digunakan kembali dalam program, kita menggunakan konsep **fungsi dengan *return value*** atau **fungsi dengan kembalian**. Konsep ini memungkinkan fungsi untuk mengembalikan hasil komputasinya sebagai *output*, mirip dengan bagaimana fungsi matematika bekerja.

## Konsep Dasar Fungsi dengan Return

Secara fundamental, fungsi dengan *return value* dapat dianalogikan dengan persamaan matematika `y = f(x)`.
*   `f` adalah **nama fungsi**.
*   `x` adalah **input** atau **argumen** yang diberikan ke fungsi.
*   `y` adalah **output** atau **hasil** yang dikembalikan oleh fungsi.

Dalam Python, untuk menghasilkan *output* `y` dari sebuah fungsi, kita harus menggunakan kata kunci (**keyword**) `return`.
*   **Tanpa `return`**: Fungsi hanya akan menjalankan perintah di dalamnya tetapi tidak akan menghasilkan nilai yang dapat disimpan atau digunakan kembali. Hasilnya akan menjadi `None`.
*   **Dengan `return`**: Fungsi akan mengembalikan nilai spesifik yang dapat ditangkap oleh variabel lain atau digunakan dalam ekspresi. Ini membuat fungsi menjadi lebih lengkap karena memiliki nama, input, dan output.

## Implementasi Fungsi dengan Return

### 1. Fungsi dengan Single Return (Mengembalikan Satu Nilai)

Contoh paling sederhana adalah fungsi yang mengkuadratkan sebuah angka.

**Struktur Umum:**
```python
def nama_fungsi(argumen):
    # Logika fungsi
    output = argumen * argumen # Contoh
    return output
```

**Contoh: Fungsi Kuadrat**
Fungsi ini menerima satu angka sebagai input dan mengembalikan kuadrat dari angka tersebut.

```python
def kuadrat(input_angka):
    '''Fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat
```

**Penggunaan:**
Hasil dari fungsi `kuadrat` dapat disimpan dalam variabel atau langsung digunakan dalam operasi lain.
*   **Menyimpan hasil ke variabel:**
    ```python
    y = kuadrat(3)
    print(f"y = kuadrat(3) = {y}") # Output: y = kuadrat(3) = 9
    ```
*   **Menggunakan dalam ekspresi matematika:**
    ```python
    z = 10 + kuadrat(7)
    print(f"z = 10 + kuadrat(7) = {z}") # Output: z = 10 + kuadrat(7) = 59
    ```
    Ini menunjukkan bahwa nilai yang dikembalikan oleh fungsi (`kuadrat(7)` menghasilkan 49) dapat langsung berpartisipasi dalam perhitungan lain.

### 2. Fungsi dengan Multi Input dan Single Return

Fungsi juga dapat menerima lebih dari satu input (argumen) dan tetap mengembalikan satu nilai sebagai hasilnya.

**Contoh: Fungsi Penjumlahan**
Fungsi ini menerima dua angka dan mengembalikan hasil penjumlahannya.

```python
def fungsi_tambah(angka_1, angka_2):
    '''Fungsi return dengan multi input'''
    return angka_1 + angka_2
```

**Penggunaan:**
```python
a = fungsi_tambah(10, 8)
print(f"10 + 8 = {a}") # Output: 10 + 8 = 18
```

### 3. Fungsi dengan Multi Return (Mengembalikan Banyak Nilai Sekaligus)

Salah satu fitur menarik di Python adalah kemampuan untuk mengembalikan **banyak nilai sekaligus** dari satu fungsi. Nilai-nilai ini dikembalikan sebagai sebuah *tuple*, meskipun kita tidak perlu menuliskannya secara eksplisit sebagai *tuple*.

**Contoh: Fungsi Operasi Matematika Lengkap**
Fungsi ini menerima dua angka dan mengembalikan hasil kali, bagi, tambah, dan kurang dari kedua angka tersebut.

```python
def operasi_matematika(angka_1, angka_2):
    '''Fungsi dengan return value banyak'''
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    
    return tambah, kurang, kali, bagi # Urutan return bisa disesuaikan
```

**Cara Mengambil Return Value (Unpacking)**
Untuk mengambil nilai-nilai yang dikembalikan oleh fungsi multi-return, kita menggunakan teknik yang disebut **unpacking**. Kita menugaskan hasil fungsi ke beberapa variabel sekaligus, sesuai dengan urutan nilai yang dikembalikan.

```python
k, l, m, n = operasi_matematika(9, 5)

print(f"Hasil tambah = {k}") # k akan berisi hasil tambah (9+5=14)
print(f"Hasil kurang = {l}") # l akan berisi hasil kurang (9-5=4)
print(f"Hasil kali = {m}")   # m akan berisi hasil kali (9*5=45)
print(f"Hasil bagi = {n}")   # n akan berisi hasil bagi (9/5=1.8)
```

Output dari kode di atas akan menunjukkan hasil dari keempat operasi tersebut secara terpisah:
```
Hasil tambah = 14
Hasil kurang = 4
Hasil kali = 45
Hasil bagi = 1.8
```

## Kesimpulan

Penggunaan `return value` membuat fungsi Python menjadi sangat kuat dan fleksibel. Fungsi dapat melakukan perhitungan kompleks dan mengembalikan hasilnya, yang kemudian dapat digunakan kembali di bagian lain dari program, baik sebagai bagian dari ekspresi, disimpan dalam variabel, atau bahkan di-unpack menjadi beberapa variabel. Ini membantu dalam membuat kode yang lebih modular, mudah dibaca, dan efisien.

## Materi Selanjutnya

Setelah memahami fungsi dengan *return value*, materi selanjutnya yang akan dibahas adalah **Default Argument** pada fungsi, yang memberikan fleksibilitas lebih dalam mendefinisikan argumen fungsi.
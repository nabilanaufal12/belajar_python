# Summary Python Format String

> Generated: January 18th, 2026 9:44 PM
> Sources: Belajar Python [Dasar] - 18 - Format String.youtube, pasted-text-1.md

---

# Catatan Belajar: Format String (f-string) pada Python

F-string, atau *formatted string literals*, adalah fitur pada Python yang menyediakan cara yang ringkas dan mudah untuk menyematkan ekspresi Python di dalam string literal. Ini merupakan metode pemformatan string yang lebih modern dan efisien dibandingkan cara lama seperti konkatenasi (`+`) atau metode `.format()`.

## Pengenalan f-string

F-string didefinisikan dengan menambahkan huruf `f` (atau `F`) di depan tanda kutip string (`''` atau `""`). Variabel atau ekspresi yang ingin disisipkan ke dalam string ditempatkan di dalam kurung kurawal `{}`.

**Contoh Dasar:**
```python
nama = "Marlin"
format_str = f"Hello {nama}"
print(format_str) # Output: Hello Marlin
```

## Tipe Data yang Didukung

F-string dapat menampilkan berbagai tipe data secara langsung tanpa memerlukan konversi manual (casting) ke string.

*   **String**:
    ```python
    nama = "Marlin"
    print(f"Hello {nama}") # Output: Hello Marlin
    ```
*   **Angka (Float)**:
    ```python
    angka = 2005.5
    print(f"angka = {angka}") # Output: angka = 2005.5
    ```
*   **Boolean**:
    ```python
    boolean = True
    print(f"boolean = {boolean}") # Output: boolean = True
    ```

## Format Angka

F-string menyediakan berbagai spesifikasi format untuk mengontrol tampilan angka.

### Bilangan Bulat (Integer)

Untuk menampilkan angka sebagai bilangan bulat tanpa bagian desimal, gunakan spesifier `:d`.
**Penting**: Variabel yang diformat harus bertipe integer. Jika float, akan menghasilkan error.

```python
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str) # Output: bilangan bulat = 15
```

### Pemisah Ribuan

Untuk angka besar, f-string dapat secara otomatis menambahkan koma (atau pemisah ribuan lainnya sesuai lokal) menggunakan spesifier `:,`.

```python
angka_ribuan = 2000
format_str_ribuan = f"ribuan = {angka_ribuan:,}"
print(format_str_ribuan) # Output: ribuan = 2,000

angka_jutaan = 2000000
format_str_jutaan = f"jutaan = {angka_jutaan:,}"
print(format_str_jutaan) # Output: jutaan = 2,000,000
```

### Bilangan Desimal (Float)

Untuk mengontrol jumlah digit di belakang koma, gunakan spesifier `:.Jf`, di mana `J` adalah jumlah digit yang diinginkan.

```python
angka = 2005.54321
format_str_2digit = f"desimal (2 digit) = {angka:.2f}"
print(format_str_2digit) # Output: desimal (2 digit) = 2005.54

format_str_3digit = f"desimal (3 digit) = {angka:.3f}"
print(format_str_3digit) # Output: desimal (3 digit) = 2005.543
```

### Leading Zero (Nol di Depan)

Anda bisa mengatur total lebar karakter string dan mengisi kekosongan di depan dengan nol menggunakan spesifier `:0Jf`. `J` adalah total lebar karakter yang diinginkan.

```python
angka = 2005.54321
# Total lebar 10 karakter, 3 digit desimal, sisanya diisi nol di depan.
format_str = f"desimal = {angka:010.3f}"
print(format_str) # Output: 002005.543
```

### Tanda Plus/Minus

Secara *default*, hanya tanda minus (`-`) yang ditampilkan untuk angka negatif. Untuk menampilkan tanda plus (`+`) pada angka positif, gunakan spesifier `:+`.

```python
angka_minus = -10
angka_plus = 10.1234

format_minus = f"minus = {angka_minus:+d}"
print(format_minus) # Output: minus = -10

format_plus = f"plus = {angka_plus:+.2f}"
print(format_plus) # Output: plus = +10.12
```

### Persentase

Untuk mengonversi angka menjadi format persentase (mengalikan dengan 100 dan menambahkan simbol `%`), gunakan spesifier `:%`. Anda juga bisa mengontrol jumlah digit desimal.

```python
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen) # Output: persen = 4.50%
```

## Operasi Aritmatika dalam f-string

F-string memungkinkan Anda melakukan operasi aritmatika langsung di dalam *placeholder* `{}`. Hasil operasi akan langsung diformat ke dalam string.

```python
harga = 10000
jumlah = 5
format_str = f"harga total = Rp{harga*jumlah:,}"
print(format_str) # Output: harga total = Rp50,000
```

## Format Basis Angka Lain

F-string juga dapat menampilkan angka dalam basis yang berbeda seperti biner, oktal, atau heksadesimal. Ini dapat dilakukan dengan menggunakan fungsi bawaan Python (`bin()`, `oct()`, `hex()`) atau spesifier format khusus (`:b`, `:o`, `:x`).

```python
angka = 255

format_binary = f"binary = {bin(angka)}"
print(format_binary) # Output: binary = 0b11111111

format_octal = f"octal = {oct(angka)}"
print(format_octal) # Output: octal = 0o377

format_hex = f"hex = {hex(angka)}"
print(format_hex) # Output: hex = 0xff
```

## Apa Selanjutnya?

Setelah memahami berbagai opsi pemformatan ini, langkah selanjutnya adalah mempelajari bagaimana mengatur lebar dan perataan teks (*string width and alignment*) agar tampilan output di konsol menjadi lebih rapi dan terstruktur.
# Mengambil Input Data dari User di Python

## Pendahuluan: Fungsi `input()`

Dalam pemrograman Python, fungsi `input()` digunakan untuk mengambil data atau masukan dari pengguna (user) melalui konsol atau terminal. Fungsi ini memungkinkan program untuk berinteraksi secara dinamis dengan pengguna, meminta informasi yang diperlukan untuk melanjutkan eksekusi program.

### Cara Penggunaan Dasar

Sintaks dasar untuk menggunakan fungsi `input()` adalah sebagai berikut:
```python
data = input("Pesan prompt untuk user: ")
```
*   `"Pesan prompt untuk user:"` adalah teks yang akan ditampilkan kepada pengguna, memberitahu mereka apa yang harus dimasukkan. Ini bersifat opsional tetapi sangat disarankan untuk kejelasan.
*   Setelah pengguna memasukkan data dan menekan Enter, data tersebut akan disimpan ke dalam variabel (dalam contoh ini, `data`).

Contoh:
```python
data = input("Masukkan data: ")
print("data =", data)
```
Jika pengguna memasukkan "Otong", maka outputnya akan `data = Otong`.

## Tipe Data Default: String (`str`)

Penting untuk dipahami bahwa fungsi `input()` **selalu mengembalikan nilai dalam bentuk tipe data string (`str`)**, terlepas dari apa yang dimasukkan oleh pengguna.

*   Jika pengguna memasukkan angka `10`, `input()` akan menganggapnya sebagai string `"10"`.
*   Jika pengguna memasukkan angka desimal `10.18`, `input()` akan menganggapnya sebagai string `"10.18"`.
*   Bahkan jika pengguna memasukkan angka yang sangat besar seperti `10 juta`, itu tetap akan dianggap sebagai string.

Untuk memverifikasi tipe data, kita bisa menggunakan fungsi `type()`:
```python
data = input("Masukkan data: ")
print("data =", data, ", type =", type(data))
```
Apapun inputnya, `type(data)` akan selalu menunjukkan `<class 'str'>`.

## Mengambil Input Angka (Casting ke `int` atau `float`)

Karena `input()` selalu mengembalikan string, jika kita ingin melakukan operasi matematika atau perbandingan numerik, kita perlu mengubah (casting) tipe data string tersebut ke tipe data numerik yang sesuai, yaitu `int` (integer/bilangan bulat) atau `float` (bilangan desimal).

### Untuk Integer (`int`)

Untuk mengubah input menjadi bilangan bulat, kita membungkus fungsi `input()` dengan fungsi `int()`:
```python
angka = int(input("Masukkan angka: "))
print("data =", angka, ", type =", type(angka))
```
Jika pengguna memasukkan `10`, variabel `angka` akan berisi `10` dengan tipe data `<class 'int'>`.

### Untuk Float (`float`)

Sama halnya dengan integer, untuk bilangan desimal, kita membungkus `input()` dengan fungsi `float()`:
```python
angka = float(input("Masukkan angka: "))
print("data =", angka, ", type =", type(angka))
```
Jika pengguna memasukkan `10.5`, variabel `angka` akan berisi `10.5` dengan tipe data `<class 'float'>`. Ini memungkinkan perhitungan dengan angka desimal.

## Mengambil Input Boolean (`bool`) - Metode Khusus

Mengambil input boolean (`True`/`False`) sedikit lebih rumit karena perilaku casting string ke boolean.

### Permasalahan Langsung Casting ke `bool`

Jika kita mencoba langsung casting `input()` ke `bool` seperti ini:
```python
nilai_boolean = bool(input("Masukkan nilai boolean: "))
```
Ini akan menghasilkan masalah:
*   Jika pengguna mengetik `True` atau `False` (sebagai string), hasilnya akan **selalu `True`**.
*   Bahkan jika pengguna mengetik string kosong (hanya menekan Enter), hasilnya akan `False`.
Ini karena dalam Python, string non-kosong apapun akan dievaluasi menjadi `True` saat di-cast ke boolean.

### Solusi: Casting Bertahap (`int` lalu `bool`)

Cara yang paling umum dan mudah untuk mengambil input boolean adalah dengan meminta pengguna memasukkan `0` untuk `False` dan `1` untuk `True`, kemudian melakukan casting dua kali: pertama ke `int`, lalu ke `bool`.

```python
biner = bool(int(input("Masukkan nilai boolean (0/1): ")))
print("data =", biner, ", type =", type(biner))
```
Dengan metode ini:
*   Jika pengguna mengetik `1`:
    *   `"1"` (string) di-cast ke `1` (integer).
    *   `1` (integer) di-cast ke `True` (boolean).
*   Jika pengguna mengetik `0`:
    *   `"0"` (string) di-cast ke `0` (integer).
    *   `0` (integer) di-cast ke `False` (boolean).

Ini adalah cara paling sederhana sebelum mempelajari struktur kontrol seperti `if-else` yang dapat menangani input boolean dengan lebih fleksibel.

## Ringkasan Tipe Data dan Input

Secara keseluruhan, ada empat tipe data utama yang dibahas dalam konteks pengambilan input dari user:
1.  **String (`str`)**: Tipe data default dari fungsi `input()`.
2.  **Integer (`int`)**: Untuk bilangan bulat, memerlukan casting `int(input())`.
3.  **Float (`float`)**: Untuk bilangan desimal, memerlukan casting `float(input())`.
4.  **Boolean (`bool`)**: Untuk nilai `True`/`False`, memerlukan casting bertahap `bool(int(input()))` dengan input `0` atau `1`.

Memahami cara kerja `input()` dan pentingnya casting adalah dasar penting untuk membuat program Python yang interaktif dan fungsional.
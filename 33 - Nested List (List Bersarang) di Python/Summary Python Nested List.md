# Catatan Belajar: Nested List (List Bersarang) di Python

## Overview

**Nested List** atau **List Bersarang** adalah sebuah konsep dalam Python di mana sebuah list dapat berisi elemen-elemen yang juga berupa list. Ini memungkinkan penyimpanan data yang lebih kompleks dan terstruktur, seperti data dua dimensi (matriks) atau kumpulan objek dengan beberapa atribut. Namun, penting untuk memahami bagaimana operasi seperti penyalinan (copy) bekerja pada nested list, karena metode `copy()` standar hanya melakukan *shallow copy* yang dapat menyebabkan perilaku tidak terduga terkait referensi objek.

## Definisi dan Konsep Dasar Nested List

**Nested List** adalah list yang elemen-elemennya adalah list lain. Konsep ini memungkinkan kita untuk merepresentasikan data dalam bentuk dua dimensi, mirip dengan matriks.

Contoh sederhana pembuatan nested list:
```python
data_0 = [1, 2]
data_1 = [3, 4]

list_2D = [data_0, data_1]
print(f"list 2D = {list_2D}")
# Output: [[1, 2], [3, 4]]
```"]

Nested list juga dapat berisi campuran antara list dan elemen-elemen biasa (misalnya angka), seperti `[data_0, data_1, 6, 7]`"].

## Contoh Penggunaan: Data Kompleks (Peserta)

Nested list sangat berguna untuk menyimpan data yang lebih kompleks dan terstruktur, di mana setiap elemen utama mewakili sebuah entitas, dan elemen-elemen di dalamnya mewakili atribut-atribut entitas tersebut.

Misalnya, untuk menyimpan data peserta yang memiliki nama, umur, dan jenis kelamin:
```python
# Data Peserta [Nama, Umur, Gender]
peserta_0 = ["Ucup", 25, "Laki-laki"]
peserta_1 = ["Otong", 10, "Laki-laki"]
peserta_2 = ["Dedeh", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")
# Output: [['Ucup', 25, 'Laki-laki'], ['Otong', 10, 'Laki-laki'], ['Dedeh', 50, 'Wanita']]
```"]

Penggunaan nested list seperti ini membuat data lebih terorganisir dan mudah dilacak, dibandingkan jika kita harus membuat list terpisah untuk nama, umur, dan jenis kelamin.

## Mengakses Data dalam Nested List

Untuk mengakses dan menampilkan data dari nested list, kita dapat menggunakan perulangan (looping). Ini memungkinkan kita untuk mengiterasi setiap sub-list dan mengakses elemen-elemen di dalamnya berdasarkan indeks.

Contoh mengakses data peserta:
```python
for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")
```

Output dari kode di atas akan menampilkan setiap peserta dengan atributnya secara rapi:
```
Nama    : Ucup
Umur    : 25
Gender  : Laki-laki

Nama    : Otong
Umur    : 10
Gender  : Laki-laki

Nama    : Dedeh
Umur    : 50
Gender  : Wanita
```

## Masalah Referensi (Shallow Copy) pada Nested List

Salah satu permasalahan yang perlu diperhatikan saat bekerja dengan nested list adalah ketika melakukan penyalinan (copy) menggunakan metode `.copy()`. Metode ini hanya melakukan **shallow copy** (salinan dangkal), yang berarti:
*   Kontainer list terluar akan disalin.
*   Namun, list-list yang ada di dalamnya (nested lists) tidak disalin secara independen. Sebaliknya, mereka masih berupa **referensi** ke objek list yang sama dengan list aslinya.

Akibatnya, jika kita mengubah elemen di dalam sub-list pada list asli, perubahan tersebut juga akan terlihat pada list hasil salinan, karena keduanya merujuk ke objek sub-list yang sama.

Demonstrasi masalah shallow copy:
```python
list_copy = list_peserta.copy()

print(f"peserta = {list_peserta}")
print(f"copy    = {list_copy}")

print("\nUbah nama peserta pertama jadi Michael")
peserta_0[0] = "Michael" # Mengubah elemen di list asli

print(f"peserta = {list_peserta}")
print(f"copy    = {list_copy}") # list_copy juga ikut berubah!
```

Output setelah perubahan:
```
peserta = [['Ucup', 25, 'Laki-laki'], ['Otong', 10, 'Laki-laki'], ['Dedeh', 50, 'Wanita']]
copy    = [['Ucup', 25, 'Laki-laki'], ['Otong', 10, 'Laki-laki'], ['Dedeh', 50, 'Wanita']]

Ubah nama peserta pertama jadi Michael
peserta = [['Michael', 25, 'Laki-laki'], ['Otong', 10, 'Laki-laki'], ['Dedeh', 50, 'Wanita']]
copy    = [['Michael', 25, 'Laki-laki'], ['Otong', 10, 'Laki-laki'], ['Dedeh', 50, 'Wanita']]
```
Terlihat bahwa `list_copy` ikut berubah meskipun yang dimodifikasi adalah `peserta_0` (bagian dari `list_peserta` asli).

## Solusi: Deep Copy

Untuk mengatasi masalah referensi pada nested list dan memastikan bahwa semua elemen, termasuk sub-list, disalin secara independen, diperlukan **Deep Copy** (salinan mendalam). Metode deep copy akan menduplikasi seluruh struktur data, termasuk objek-objek yang bersarang di dalamnya. Pembahasan lebih lanjut mengenai deep copy akan dibahas pada tutorial berikutnya.
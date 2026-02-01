# Latihan Komparasi dan Logika di Python

Pembelajaran ini berfokus pada penggunaan operator komparasi dan logika (`OR`, `AND`) dalam Python untuk mengecek apakah suatu angka berada dalam rentang tertentu. Tujuannya adalah untuk membangun program yang dapat menentukan apakah input pengguna memenuhi kriteria rentang yang ditentukan, baik itu rentang gabungan (union) maupun irisan (intersection).

## 1. Kasus Gabungan (Union) dengan Operator `OR`

Kasus pertama melibatkan penentuan apakah sebuah angka berada dalam salah satu dari dua rentang yang terpisah. Logika yang digunakan adalah "kurang dari 3 **ATAU** lebih besar dari 10".

### Deskripsi Masalah
Kita ingin mengecek apakah sebuah `inputUser` memenuhi kondisi:
*   `inputUser < 3`
*   `inputUser > 10`

Jika salah satu kondisi tersebut benar, maka hasilnya adalah `True`.
Representasi visual rentang ini adalah: `+++++ 3 ----- 10 +++++`. Area `+++++` menunjukkan nilai `True`, sedangkan `-----` menunjukkan nilai `False`.

### Langkah-langkah Implementasi
Untuk kasus gabungan seperti ini, digunakan operator logika **`OR`**.

1.  **Mendapatkan Input**: Minta pengguna memasukkan angka.
2.  **Memeriksa `angka < 3`**: Buat variabel `isKurangDari` yang bernilai `True` jika angka kurang dari 3, dan `False` jika tidak.
3.  **Memeriksa `angka > 10`**: Buat variabel `isLebihDari` yang bernilai `True` jika angka lebih dari 10, dan `False` jika tidak.
4.  **Menggabungkan Hasil dengan `OR`**: Gabungkan kedua hasil pemeriksaan menggunakan operator `OR`. Jika `isKurangDari` **atau** `isLebihDari` bernilai `True`, maka `isCorrect` akan menjadi `True`.

### Contoh Kode Python
```python
# KASUS 1: Gabungan (OR)
# Angka < 3 ATAU Angka > 10
inputUser = float(input("Masukkan angka yang bernilai < 3 atau > 10: ")) #

# 1. Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3) #
print("Kurang dari 3 =", isKurangDari) #

# 2. Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10) #
print("Lebih dari 10 =", isLebihDari) #

# 3. Penggabungan dengan OR
isCorrect = isKurangDari or isLebihDari #
print("Angka yang anda masukkan: ", isCorrect) #
```

### Contoh Hasil
*   **Input 1**: `isKurangDari` = `True`, `isLebihDari` = `False`. Hasil `isCorrect` = `True`.
*   **Input 5**: `isKurangDari` = `False`, `isLebihDari` = `False`. Hasil `isCorrect` = `False`.
*   **Input 11**: `isKurangDari` = `False`, `isLebihDari` = `True`. Hasil `isCorrect` = `True`.

## 2. Kasus Irisan (Intersection) dengan Operator `AND`

Kasus kedua melibatkan penentuan apakah sebuah angka berada dalam rentang tunggal di antara dua batas. Logika yang digunakan adalah "lebih besar dari 3 **DAN** kurang dari 10".

### Deskripsi Masalah
Kita ingin mengecek apakah sebuah `inputUser` memenuhi kedua kondisi secara bersamaan:
*   `inputUser > 3`
*   `inputUser < 10`

Kedua kondisi ini harus `True` agar hasilnya `True`.
Representasi visual rentang ini adalah: `----- 3 +++++ 10 -----`. Hanya area tengah (`+++++`) yang bernilai `True`.

### Langkah-langkah Implementasi
Karena kedua syarat harus terpenuhi, digunakan operator logika **`AND`**.

1.  **Mendapatkan Input**: Minta pengguna memasukkan angka.
2.  **Memeriksa `angka > 3`**: Buat variabel `isLebihDari` yang bernilai `True` jika angka lebih dari 3.
3.  **Memeriksa `angka < 10`**: Buat variabel `isKurangDari` yang bernilai `True` jika angka kurang dari 10.
4.  **Menggabungkan Hasil dengan `AND`**: Gabungkan kedua hasil pemeriksaan menggunakan operator `AND`. Hanya jika `isLebihDari` **dan** `isKurangDari` keduanya `True`, maka `isCorrect` akan menjadi `True`.

### Contoh Kode Python
```python
# KASUS 2: Irisan (AND)
# Angka > 3 DAN Angka < 10
print("\n",10*"=","\n") #
inputUser = float(input("Masukkan angka yang bernilai > 3 dan < 10: ")) #

# 1. Memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3) #
print("Lebih dari 3 =", isLebihDari) #

# 2. Memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10) #
print("Kurang dari 10 =", isKurangDari) #

# 3. Penggabungan dengan AND
isCorrect = isLebihDari and isKurangDari #
print("Angka yang anda masukkan: ", isCorrect) #
```

### Contoh Hasil
*   **Input 1**: `isLebihDari` = `False`, `isKurangDari` = `True`. Hasil `isCorrect` = `False`.
*   **Input 5**: `isLebihDari` = `True`, `isKurangDari` = `True`. Hasil `isCorrect` = `True`.
*   **Input 11**: `isLebihDari` = `True`, `isKurangDari` = `False`. Hasil `isCorrect` = `False`.

## Latihan Tambahan (PR)

Untuk melatih pemahaman logika komparasi dan operator `AND`/`OR`, berikut adalah dua soal latihan yang lebih kompleks.

1.  **Soal 1**: Buat logika untuk rentang `----- 0 +++++ 5 ----- 8 +++++ 11 -----`.
    Angka harus: (`> 0` **DAN** `< 5`) **ATAU** (`> 8` **DAN** `< 11`).

2.  **Soal 2**: Buat logika untuk rentang `+++++ 0 ----- 5 +++++ 8 ----- 11 +++++`.
    Angka harus: (`< 0`) **ATAU** (`> 5` **DAN** `< 8`) **ATAU** (`> 11`).

Materi selanjutnya yang akan dibahas adalah **Operator Bitwise**.
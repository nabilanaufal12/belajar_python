# Summary Casting Tipe Data

> Generated: January 14th, 2026 2:52 PM
> Sources: Belajar Python [Dasar] - 06 - Casting Tipe Data.youtube, pasted-text-1.md

---

# Casting Tipe Data di Python

Casting tipe data adalah proses mengubah tipe data dari satu jenis ke jenis lainnya. Ini merupakan operasi fundamental dalam pemrograman Python yang memungkinkan fleksibilitas dalam manipulasi data.

## Konsep Dasar Casting

Casting dilakukan menggunakan fungsi bawaan Python yang sesuai dengan tipe data tujuan, seperti `int()`, `float()`, `str()`, dan `bool()`.

## Casting dari Integer

Ketika sebuah nilai **integer** di-cast ke tipe data lain, perilakunya adalah sebagai berikut:

*   **Ke Float**: Integer akan diubah menjadi representasi float dengan `.0` di belakangnya.
    *   Contoh: `float(9)` akan menghasilkan `9.0`.
*   **Ke String**: Integer akan diubah menjadi representasi string (teks).
    *   Contoh: `str(9)` akan menghasilkan `"9"`.
*   **Ke Boolean**:
    *   Nilai integer `0` akan di-cast menjadi `False`.
    *   Semua nilai integer **selain `0`** (positif atau negatif) akan di-cast menjadi `True`.
        *   Contoh: `bool(9)` menghasilkan `True`.
        *   Contoh: `bool(-1)` menghasilkan `True`.

## Casting dari Float

Ketika sebuah nilai **float** di-cast ke tipe data lain, perilakunya adalah sebagai berikut:

*   **Ke Integer**: Float akan diubah menjadi integer dengan cara **dibulatkan ke bawah** (floor). Bagian desimal akan dihilangkan, tidak peduli seberapa besar nilai desimalnya.
    *   Contoh: `int(9.5)` akan menghasilkan `9`.
    *   Contoh: `int(9.9)` juga akan menghasilkan `9`.
*   **Ke String**: Float akan diubah menjadi representasi string (teks).
    *   Contoh: `str(9.5)` akan menghasilkan `"9.5"`.
*   **Ke Boolean**:
    *   Nilai float `0.0` akan di-cast menjadi `False`.
    *   Semua nilai float **selain `0.0`** (positif atau negatif) akan di-cast menjadi `True`.
        *   Contoh: `bool(9.5)` menghasilkan `True`.

## Casting dari Boolean

Ketika sebuah nilai **boolean** di-cast ke tipe data lain, perilakunya adalah sebagai berikut:

*   **Ke Integer**:
    *   `True` akan diubah menjadi `1`.
    *   `False` akan diubah menjadi `0`.
*   **Ke Float**:
    *   `True` akan diubah menjadi `1.0`.
    *   `False` akan diubah menjadi `0.0`.
*   **Ke String**: Boolean akan diubah menjadi representasi string dari nilai boolean itu sendiri.
    *   Contoh: `str(True)` akan menghasilkan `"True"`.
    *   Contoh: `str(False)` akan menghasilkan `"False"`.

## Casting dari String

Casting dari **string** memiliki beberapa aturan penting dan potensi kesalahan:

*   **Ke Integer**: String harus berupa representasi angka bulat yang valid.
    *   Contoh: `int("10")` akan menghasilkan `10`.
    *   Jika string bukan angka (misalnya `"Ucup"`), akan terjadi `ValueError` (ERROR).
*   **Ke Float**: String harus berupa representasi angka (bulat atau desimal) yang valid.
    *   Contoh: `float("10")` akan menghasilkan `10.0`.
    *   Contoh: `float("9.5")` akan menghasilkan `9.5`.
    *   Sama seperti integer, jika string bukan angka, akan terjadi `ValueError`.
*   **Ke Boolean**:
    *   String **kosong** (`""`) akan di-cast menjadi `False`.
    *   Semua string **yang tidak kosong**, termasuk string yang berisi angka (`"0"`, `"-1"`) atau teks (`"False"`, `"Ucup"`), akan di-cast menjadi `True`.
        *   Contoh: `bool("10")` menghasilkan `True`.
        *   Contoh: `bool("False")` (string `"False"`) menghasilkan `True`, karena string tersebut tidak kosong.

## Kesimpulan

Setiap tipe data memiliki perilaku casting yang unik. Memahami aturan-aturan ini sangat penting untuk menghindari kesalahan dan memastikan manipulasi data yang benar dalam program Python.
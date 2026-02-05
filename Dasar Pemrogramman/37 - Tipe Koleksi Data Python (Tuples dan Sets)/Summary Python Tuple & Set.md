# Tipe Koleksi Data Python: Tuples dan Sets

## Pengantar Tipe Koleksi Data

Dalam Python, terdapat beberapa tipe data koleksi yang digunakan untuk menyimpan kumpulan nilai. Sebelumnya, kita telah mengenal **List**, yang merupakan salah satu tipe koleksi yang sangat fleksibel. List didefinisikan menggunakan kurung siku `[]` dan bersifat *mutable*, artinya elemen-elemen di dalamnya bisa diubah, ditambahkan, atau dihapus setelah List dibuat.

Pada catatan ini, kita akan membahas dua tipe koleksi lainnya: **Tuples** dan **Sets**, yang memiliki karakteristik unik dan kegunaan spesifik dalam pemrograman Python.

## Tuples

**Tuples** adalah tipe koleksi data yang mirip dengan List, namun memiliki perbedaan mendasar pada sifat *mutability*-nya. Tuples didefinisikan menggunakan kurung biasa `()`.

### Karakteristik Tuples

*   **Memiliki Indeks**: Sama seperti List, elemen-elemen dalam Tuple dapat diakses menggunakan indeks (posisi) mereka. Misalnya, `data_tuples[1]` akan mengembalikan elemen pada indeks ke-1.
*   **Immutable (Tidak Bisa Diubah)**: Ini adalah sifat utama yang membedakan Tuple dari List. Setelah Tuple dibuat, elemen-elemen di dalamnya **tidak dapat diubah**, ditambahkan, atau dihapus.
    *   Mencoba mengubah elemen seperti `data_tuples[1] = "ucup"` akan menghasilkan `TypeError` = "ucup", akan Error"].
    *   Tuple juga tidak memiliki metode seperti `.append()` untuk menambahkan elemen baru.

### Kegunaan Tuples

Karena sifatnya yang *immutable*, Tuples sangat cocok digunakan untuk data yang harus bersifat **konstan** atau **tidak boleh berubah** selama program berjalan. Contoh penggunaannya meliputi:
*   Menyimpan konfigurasi sistem yang tidak boleh diubah.
*   Mengembalikan beberapa nilai dari sebuah fungsi yang ingin dipastikan tidak dimodifikasi oleh pemanggil.
*   Representasi data yang bersifat tetap, seperti koordinat geografis atau tanggal lahir.

### Contoh Tuples

```python
data_tuples = (7, 8, 9, 10) # Contoh Tuple
print(f"data tuples = {data_tuples}") # Output: data tuples = (7, 8, 9, 10)
print(f"data tuples[1] = {data_tuples[1]}") # Output: data tuples[1] = 8 = {data_tuples[1]}"]

# data_tuples[1] = "ucup" # Akan ERROR: TypeError: 'tuple' object does not support item assignment
# data_tuples.append(1)   # Akan ERROR: AttributeError: 'tuple' object has no attribute 'append'
```

## Sets

**Sets** adalah tipe koleksi data yang merepresentasikan konsep himpunan dalam matematika. Sets didefinisikan menggunakan kurung kurawal `{}`.

### Karakteristik Sets

*   **Tidak Memiliki Indeks**: Berbeda dengan List dan Tuple, elemen-elemen dalam Set **tidak memiliki urutan** dan **tidak dapat diakses menggunakan indeks**. Mencoba mengakses `data_sets[0]` akan menghasilkan `TypeError`.
*   **Unik (Tidak Ada Duplikat)**: Setiap elemen dalam Set harus unik. Jika ada elemen duplikat yang dimasukkan, Set secara otomatis akan menghapus duplikat tersebut dan hanya menyimpan satu instansinya.
*   **Tidak Berurut (Unordered)**: Urutan elemen dalam Set tidak dijamin dan dapat berubah setiap kali Set dicetak atau diakses.

### Kegunaan Sets

Sets sangat berguna untuk operasi yang melibatkan himpunan matematika dan kebutuhan akan data unik:
*   Melakukan operasi himpunan seperti gabungan (union), irisan (intersection), selisih (difference), atau komplemen.
*   Menyimpan koleksi data unik di mana urutan tidak penting.
*   Menghilangkan duplikat dari List atau koleksi lainnya dengan cepat.

### Contoh Sets

```python
data_sets = {10, 4, 3, 2, 4, 7, 6, 5} # Contoh Set
print(f"data sets = {data_sets}") # Output: data sets = {2, 3, 4, 5, 6, 7, 10} (urutan bisa berbeda, duplikat '4' hilang)

# print(data_sets[0]) # Akan ERROR: TypeError: 'set' object is not subscriptable
```

## Perbandingan List, Tuples, dan Sets

Berikut adalah ringkasan perbandingan antara List, Tuples, dan Sets:

| Fitur             | List (`[]`)                               | Tuples (`()`)                               | Sets (`{}`)                                    |
| :---------------- | :---------------------------------------- | :------------------------------------------ | :--------------------------------------------- |
| **Sintaks**       | Kurung siku `[]`                          | Kurung biasa `()`                           | Kurung kurawal `{}`                            |
| **Mutable**       | **Ya** (bisa diubah)                      | **Tidak** (tidak bisa diubah)               | **Ya** (bisa menambah/menghapus elemen)        |
| **Memiliki Indeks** | **Ya** (elemen berurutan)                 | **Ya** (elemen berurutan)                   | **Tidak** (elemen tidak berurutan)             |
| **Duplikat**      | Diizinkan                                 | Diizinkan                                   | **Tidak** diizinkan (elemen harus unik)        |
| **Kegunaan Umum** | Koleksi data umum, daftar item yang berubah | Data konstan, konfigurasi, return value fungsi | Himpunan matematika, data unik, menghilangkan duplikat |

Pemilihan tipe koleksi yang tepat sangat penting untuk efisiensi dan kejelasan kode. Setelah memahami List, Tuples, dan Sets, langkah selanjutnya adalah mempelajari **Dictionary**, yang memiliki perilaku lebih unik lagi.
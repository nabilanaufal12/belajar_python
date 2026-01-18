# Summary Python Dasar Operasi

> Generated: January 18th, 2026 1:07 PM
> Sources: Belajar Python [Dasar] - 16 - Operasi dan manipula.youtube, pasted-text-1.md

---

# Operasi dan Manipulasi String di Python

Materi ini membahas berbagai operasi dan manipulasi dasar yang dapat dilakukan pada tipe data string di Python, termasuk penggabungan, penghitungan panjang, pengecekan keanggotaan, pengulangan, pengindeksan, pemotongan, serta penggunaan nilai ASCII dan method bawaan string.

## 1. Menyambung String (Concatenation)

**Concatenation** adalah proses menggabungkan dua atau lebih string menjadi satu string baru.

*   **Operator**: Penggabungan string dilakukan menggunakan operator `+`.
*   **Penambahan Spasi**: Jika ingin menambahkan spasi atau karakter lain di antara string yang digabungkan, spasi tersebut harus disertakan sebagai string terpisah (`" "`).

**Contoh:**
```python
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

# Menggabungkan string dengan spasi dan tanda kutip
nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)
# Output: Ucup D'Fame
```

## 2. Menghitung Panjang String (Length)

Untuk mengetahui jumlah karakter dalam sebuah string, digunakan fungsi `len()`.

*   **Fungsi**: `len()` adalah fungsi bawaan Python yang mengembalikan jumlah karakter dalam string.
*   **Penghitungan**: Fungsi ini menghitung semua karakter, termasuk spasi dan karakter khusus lainnya.

**Contoh:**
```python
nama_lengkap = "Ucup D'Fame" # Menggunakan contoh dari bagian sebelumnya
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))
# Output: panjang dari Ucup D'Fame = 11
```

## 3. Operator Membership (`in` & `not in`)

Operator membership digunakan untuk mengecek apakah sebuah karakter atau substring tertentu ada atau tidak ada di dalam sebuah string.

*   **`in`**: Mengembalikan nilai `True` jika karakter atau substring ditemukan dalam string, dan `False` jika tidak ditemukan.
*   **`not in`**: Mengembalikan nilai `True` jika karakter atau substring *tidak* ditemukan dalam string, dan `False` jika ditemukan (kebalikan dari `in`).
*   **Peka Huruf Besar/Kecil**: Operator ini bersifat *case-sensitive*, artinya huruf besar dan kecil dianggap berbeda.

**Contoh:**
```python
nama_lengkap = "Ucup D'Fame"

# Mengecek keberadaan karakter 'd' (huruf kecil)
status_d_kecil = "d" in nama_lengkap
print("d" + " ada di " + nama_lengkap + " = " + str(status_d_kecil)) # Output: False

# Mengecek keberadaan karakter 'D' (huruf besar)
status_D_besar = "D" in nama_lengkap
print("D" + " ada di " + nama_lengkap + " = " + str(status_D_besar)) # Output: True

# Mengecek ketidakberadaan karakter 'd' (huruf kecil)
status_d_kecil_not_in = "d" not in nama_lengkap
print("d" + " tidak ada di " + nama_lengkap + " = " + str(status_d_kecil_not_in)) # Output: True
```

## 4. Mengulang String

String dapat diulang berkali-kali menggunakan operator perkalian.

*   **Operator**: Operator perkalian (`*`) digunakan untuk mengulang string.
*   **Fungsi**: String akan diulang sebanyak angka yang diberikan setelah operator `*`.

**Contoh:**
```python
print("wk"*10)      # Output: wkwkwkwkwkwkwkwkwkwk
print(15*"mantap ") # Output: mantap mantap mantap mantap mantap mantap mantap mantap mantap mantap mantap mantap mantap mantap mantap
```

## 5. Indexing dan Slicing

String di Python adalah urutan karakter, di mana setiap karakter memiliki posisi atau **indeks** yang unik.

### 5.1. Indexing

**Indexing** adalah cara untuk mengakses satu karakter spesifik dalam string berdasarkan posisinya.

*   **Indeks Awal**: Indeks dimulai dari `0` untuk karakter pertama.
*   **Indeks Negatif**:
    *   Indeks `[-1]` merujuk pada karakter terakhir.
    *   Indeks `[-2]` merujuk pada karakter kedua terakhir, dan seterusnya.

**Contoh:**
```python
nama_lengkap = "Ucup D'Fame"
print("index ke-0 : " + nama_lengkap[0])   # Output: U
print("index ke-6 : " + nama_lengkap[6])   # Output: '
print("index ke-(-1) : " + nama_lengkap[-1]) # Output: e
print("index ke-(-2) : " + nama_lengkap[-2]) # Output: m
```)"]

### 5.2. Slicing

**Slicing** adalah cara untuk mengambil potongan (substring) dari string, yaitu serangkaian karakter dari indeks awal hingga indeks akhir.

*   **Sintaks**: `[start:stop:step]``"].
    *   `start`: Indeks awal (inklusif) dari potongan. Jika dihilangkan, dimulai dari `0`.
    *   `stop`: Indeks akhir (eksklusif) dari potongan, karakter pada indeks `stop` *tidak* disertakan.
    *   `step`: Langkah atau jeda antar karakter (opsional, default `1`).

**Contoh `stop` eksklusif**: Jika ingin mengambil karakter dari indeks 0 hingga 3, kita perlu menulis `[0:4]` karena indeks `4` tidak akan diikutkan.

**Contoh:**
```python
nama_lengkap = "Ucup D'Fame"
print("index ke-[0:3] : " + nama_lengkap[0:3])     # Output: Ucu (mengambil indeks 0, 1, 2)
print("index ke-[3:7] : " + nama_lengkap[3:7])     # Output: p D' (mengambil indeks 3, 4, 5, 6)
print("index ke-[0:11:2] : " + nama_lengkap[0:11:2]) # Output: Uu 'ae (mengambil indeks 0, 2, 4, 6, 8, 10)
``` : " + nama_lengkap[0:3])"]

## 6. Item Paling Kecil dan Paling Besar (ASCII Code)

Setiap karakter memiliki nilai numerik yang unik, yang dikenal sebagai **ASCII Code** atau **Unicode**. Python menyediakan fungsi untuk bekerja dengan nilai-nilai ini.

*   **`min()`**: Mengembalikan karakter dengan nilai ASCII terkecil dalam string. Seringkali, karakter spasi (`" "`) memiliki nilai ASCII terkecil.
*   **`max()`**: Mengembalikan karakter dengan nilai ASCII terbesar dalam string.
*   **`ord()`**: Mengambil nilai ASCII (integer) dari sebuah karakter.
*   **`chr()`**: Mengambil karakter dari nilai ASCII (integer).

**Contoh:**
```python
nama_lengkap = "Ucup D'Fame"
print("paling kecil : " + min(nama_lengkap)) # Output: " " (spasi)
print("paling besar : " + max(nama_lengkap)) # Output: u

ascii_spasi = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_spasi)) # Output: 32

karakter_117 = chr(117)
print("char untuk ASCII 117 adalah " + karakter_117) # Output: u
```

## 7. Operator dalam Bentuk Method

String di Python adalah objek, dan sebagai objek, ia memiliki fungsi bawaan yang disebut **method**. Method ini digunakan untuk melakukan berbagai operasi spesifik pada string.

*   **Konsep**: Method diakses menggunakan notasi titik (`.`) setelah nama variabel string (misalnya, `string_variable.method_name()`).
*   **Perbedaan**: Method berbeda dengan operator (`+`, `*`) atau fungsi built-in (`len()`, `min()`, `max()`, `ord()`, `chr()`) karena method "menempel" pada objek string itu sendiri.
*   **Contoh `count()`**: Method `count()` digunakan untuk menghitung berapa kali sebuah karakter atau substring muncul dalam string.

**Contoh:**
```python
data = "otong surotong pararotong"
jumlah_o = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah_o))
# Output: jumlah o pada otong surotong pararotong = 6
```

Akan ada banyak method string lainnya yang akan dibahas lebih lanjut dalam materi berikutnya.
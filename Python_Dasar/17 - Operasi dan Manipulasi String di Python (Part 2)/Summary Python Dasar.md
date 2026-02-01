# Operasi dan Manipulasi String pada Python (Bagian 2)

Catatan ini membahas berbagai metode bawaan (built-in methods) untuk memanipulasi dan memeriksa string di Python, yang merupakan kelanjutan dari materi dasar string. Metode-metode ini sangat berguna untuk pemrosesan teks dan validasi data.

## 1. Mengubah Case (Huruf Besar/Kecil)

Python menyediakan metode untuk mengubah format huruf pada string secara keseluruhan:

*   **`.upper()`**: Mengubah semua karakter dalam string menjadi huruf kapital (huruf besar).
    ```python
    salam = "bro!"
    print(salam.upper()) # Output: BRO!
    ```
*   **`.lower()`**: Mengubah semua karakter dalam string menjadi huruf kecil.
    ```python
    alay = "aKu KeCe AbieZZZ"
    print(alay.lower()) # Output: aku kece abiezzz
    ```

## 2. Pengecekan String (`isX` Methods)

Metode-metode ini digunakan untuk memeriksa karakteristik string dan selalu mengembalikan nilai **Boolean** (`True` atau `False`), sehingga sangat berguna untuk validasi :

*   **`.islower()`**: Memeriksa apakah semua karakter dalam string adalah huruf kecil.
    ```python
    salam = "sist"
    apakah_lower = salam.islower() # True
    ```
*   **`.isupper()`**: Memeriksa apakah semua karakter dalam string adalah huruf besar.
    ```python
    salam = "sist"
    apakah_upper = salam.isupper() # False
    ```
*   **`.isalpha()`**: Memeriksa apakah semua karakter dalam string adalah huruf (tanpa angka, spasi, atau simbol lainnya).
*   **`.isalnum()`**: Memeriksa apakah semua karakter dalam string adalah huruf atau angka (alphanumeric). Metode ini sering digunakan untuk validasi seperti pada password.
*   **`.isdecimal()`**: Memeriksa apakah semua karakter dalam string adalah angka desimal.
*   **`.isspace()`**: Memeriksa apakah string hanya terdiri dari karakter spasi, tab, atau newline.
*   **`.istitle()`**: Memeriksa apakah setiap kata dalam string diawali dengan huruf besar, seperti format judul.
    *   Perlu diperhatikan bahwa tanda baca seperti apostrof atau kutipan dapat menyebabkan metode ini mengembalikan `False` jika tidak sesuai dengan aturan penulisan judul.
    ```python
    judul = "It Is Okay Not To Be Orkay"
    cek_judul = judul.istitle() # True

    judul_salah = "It's Okay" # Ada apostrof
    cek_judul_salah = judul_salah.istitle() # False
    ```

## 3. Pengecekan Awal dan Akhir String

Metode ini digunakan untuk memeriksa apakah sebuah string dimulai atau diakhiri dengan substring tertentu:

*   **`.startswith("kata")`**: Memeriksa apakah string dimulai dengan substring yang ditentukan.
*   **`.endswith("kata")`**: Memeriksa apakah string diakhiri dengan substring yang ditentukan.
*   Kedua metode ini bersifat *case-sensitive* (membedakan huruf besar dan kecil).
    ```python
    kalimat = "Sajangnim Oppa"
    cek_start = kalimat.startswith("Sajangnim") # True
    cek_end = kalimat.endswith("Oppa") # True

    cek_start_salah = kalimat.startswith("sajangnim") # False (karena 's' kecil)
    ```

## 4. Penggabungan dan Pemisahan String (`join` & `split`)

Metode ini sangat berguna untuk bekerja dengan kumpulan data string, terutama saat berinteraksi dengan tipe data `list`:

*   **`.join(list_of_strings)`**: Menggabungkan elemen-elemen dari sebuah list string menjadi satu string tunggal, menggunakan string yang memanggil metode `.join()` sebagai pemisah (separator).
    ```python
    pisah = ['aku', 'sayang', 'kamu']
    gabungan_koma = ','.join(pisah) # Output: aku,sayang,kamu
    gabungan_spasi = ' '.join(pisah) # Output: aku sayang kamu
    ```
*   **`.split('delimiter')`**: Memisahkan string menjadi sebuah list string berdasarkan delimiter (pemisah) yang ditentukan. Metode ini akan mengembalikan sebuah list.
    ```python
    gabungan = "aku-sayang-kamu"
    list_kata = gabungan.split('-') # Output: ['aku', 'sayang', 'kamu']
    ```

## 5. Alokasi Karakter (Rata Kanan/Kiri/Tengah)

Metode ini digunakan untuk mengatur perataan teks dalam lebar tertentu, seringkali untuk merapikan tampilan di konsol:

*   **`.rjust(width, fillchar)`**: Meratakan string ke kanan dalam lebar (`width`) yang ditentukan. Karakter sisa di sebelah kiri akan diisi dengan `fillchar` (karakter pengisi) opsional; jika tidak ditentukan, akan diisi dengan spasi.
*   **`.ljust(width, fillchar)`**: Meratakan string ke kiri dalam lebar (`width`) yang ditentukan. Karakter sisa di sebelah kanan akan diisi dengan `fillchar` opsional.
*   **`.center(width, fillchar)`**: Menengahkan string dalam lebar (`width`) yang ditentukan. Karakter sisa di kedua sisi akan diisi dengan `fillchar` opsional.
    *   `width` adalah total panjang string yang dihasilkan.
    *   `fillchar` dapat berupa karakter apa pun.
    ```python
    kanan = "kanan".rjust(10)
    print("'" + kanan + "'") # Output: '     kanan'

    kiri = "kiri".ljust(10, '*')
    print("'" + kiri + "'") # Output: 'kiri******'

    tengah = "tengah".center(20, "-")
    print("'" + tengah + "'") # Output: '-------tengah-------'
    ```

## 6. Menghapus Karakter (`strip`)

Metode `.strip()` digunakan untuk menghapus karakter tertentu dari awal dan akhir string. Jika tidak ada karakter yang ditentukan, metode ini akan menghapus spasi kosong (whitespace) secara default:

```python
teks_dengan_strip = "---tengah---"
print(teks_dengan_strip.strip("-")) # Output: tengah

teks_dengan_spasi = "   kata   "
print(teks_dengan_spasi.strip()) # Output: kata
```

## Selanjutnya: Format String

Setelah mempelajari berbagai metode manipulasi string ini, materi selanjutnya akan membahas **Format String**. Ini adalah cara yang lebih canggih dan fleksibel untuk menggabungkan string dengan tipe data lain (seperti angka atau float) dibandingkan dengan konkatenasi (`+`) biasa yang memerlukan *casting* manual ke string.
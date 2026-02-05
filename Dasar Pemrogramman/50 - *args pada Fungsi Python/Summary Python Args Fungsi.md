# Catatan Belajar: `*args` pada Fungsi Python

## Pendahuluan
Dalam pengembangan fungsi Python, seringkali kita dihadapkan pada kebutuhan untuk membuat fungsi yang dapat menerima jumlah argumen yang fleksibel atau dinamis. Secara default, fungsi Python memiliki jumlah argumen yang telah ditentukan. Namun, dengan menggunakan `*args`, kita dapat mengatasi batasan ini, memungkinkan fungsi untuk menerima argumen sebanyak apa pun yang diberikan.

## Masalah dengan Argumen Tetap (Fixed Arguments)
Ketika sebuah fungsi didefinisikan dengan jumlah parameter yang tetap, seperti `def fungsi(nama, tinggi, berat):`, fungsi tersebut hanya dapat dipanggil dengan jumlah argumen yang persis sama. Jika kita mencoba memanggilnya dengan jumlah argumen yang berbeda, Python akan menghasilkan error. Pendekatan ini menjadi tidak praktis atau bahkan mustahil ketika kita perlu memasukkan input yang jumlahnya bisa bervariasi (misalnya, 1, 10, atau 100 input) tanpa harus membungkusnya dalam sebuah `List` secara manual.

```python
def fungsi_biasa(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_biasa("Ucup", 170, 40) # Berjalan normal
# fungsi_biasa("Ucup", 170) # Akan error karena argumen kurang
# fungsi_biasa("Ucup", 170, 40, "Jakarta") # Akan error karena argumen berlebih
```

## Solusi: Menggunakan `*args`
Untuk mengatasi keterbatasan argumen tetap, Python menyediakan sintaks `*args`. Dengan menambahkan tanda bintang (`*`) di depan nama parameter saat mendefinisikan fungsi, kita dapat memungkinkan fungsi tersebut untuk menerima jumlah argumen posisi (positional arguments) yang tidak terbatas.

### Cara Kerja `*args`
*   **Sintaks**: Cukup tambahkan `*` di depan nama parameter dalam definisi fungsi, misalnya `def fungsi(*args):`.
*   **Tipe Data**: Semua argumen yang diteruskan ke fungsi melalui `*args` akan dikumpulkan dan disimpan dalam sebuah **Tuple**. Tuple ini kemudian dapat diakses dan diiterasi di dalam fungsi.
*   **Nama Parameter**: Nama parameter setelah `*` tidak harus `args`; bisa apa saja, misalnya `*data` atau `*items`. Yang terpenting adalah adanya tanda bintang (`*`).

```python
def fungsi_args(*args):
    # args akan menjadi Tuple
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_args("Dudung", 120, 120)
# fungsi_args("Bambang", 150, 50, "Indonesia") # Ini juga bisa, tapi kita harus menangani argumen ke-4 di dalam fungsi
```

## Studi Kasus: Fungsi Penjumlahan Dinamis
Salah satu contoh penggunaan `*args` yang paling umum adalah membuat fungsi yang dapat menjumlahkan sejumlah angka yang tidak diketahui sebelumnya. Tanpa `*args`, kita harus membuat fungsi terpisah untuk menjumlahkan 2 angka, 3 angka, dan seterusnya, atau mengharuskan pengguna memasukkan angka dalam bentuk `List`. Dengan `*args`, fungsi menjadi sangat fleksibel.

```python
def tambah(*data):
    # data adalah tuple, bisa di-iterasi
    output = 0
    for angka in data:
        output += angka
    return output

print(tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)) # Output: 45
print(tambah(10, 5, 15)) # Output: 30
print(tambah(1, 2)) # Output: 3
print(tambah()) # Output: 0 (jika tidak ada argumen, tuple kosong)
```

Fungsi `tambah` di atas dapat menerima sejumlah angka berapa pun dan mengembalikan total penjumlahannya. Ini menunjukkan bagaimana `*args` membuat fungsi menjadi lebih adaptif dan kuat.

## Kesimpulan
`*args` adalah fitur yang sangat berguna di Python untuk membuat fungsi yang lebih fleksibel. Poin-poin penting mengenai `*args` adalah:
1.  Memungkinkan fungsi untuk menerima **banyak argumen secara dinamis**.
2.  Argumen-argumen tersebut dikumpulkan dan disimpan dalam sebuah **Tuple**.
3.  Nama parameter setelah tanda bintang (`*`) **tidak harus `args`**.

Di video selanjutnya, akan dibahas `**kwargs` (Keyword Arguments) untuk input yang lebih kompleks lagi.
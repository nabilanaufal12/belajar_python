# Memahami `**kwargs` pada Fungsi Python

## Pendahuluan
`**kwargs` (keyword arguments) adalah fitur pada Python yang memungkinkan sebuah fungsi menerima sejumlah argumen kata kunci yang tidak ditentukan sebelumnya. Fitur ini sangat berguna untuk membuat fungsi yang fleksibel dan dinamis, terutama saat berinteraksi dengan library atau framework yang membutuhkan konfigurasi beragam.

## Memahami `**kwargs`
### Definisi dan Perbedaan dengan `*args`
`**kwargs` adalah sintaks khusus dalam definisi fungsi Python yang memungkinkan fungsi menerima argumen dalam bentuk **kata kunci** (keyword arguments) yang tidak terdefinisi secara eksplisit. Argumen-argumen ini kemudian dikumpulkan menjadi sebuah **dictionary** di dalam fungsi.

Perbedaannya dengan `*args` adalah sebagai berikut:
*   `*args` (satu bintang) menerima argumen posisi (positional arguments) dan mengumpulkannya menjadi sebuah **Tuple**.
*   `**kwargs` (dua bintang) menerima argumen kata kunci (keyword arguments) dan mengumpulkannya menjadi sebuah **Dictionary**.

### Cara Kerja `**kwargs`
Ketika sebuah fungsi didefinisikan dengan parameter `**kwargs`, setiap argumen yang diteruskan ke fungsi dalam format `key=value` akan dikumpulkan ke dalam sebuah dictionary. Nama parameter `kwargs` hanyalah konvensi; Anda bisa menggunakan nama lain seperti `**data_tambahan`, tetapi `**kwargs` adalah yang paling umum.

**Contoh Sederhana:**
```python
def fungsi(**kwargs):
    print(kwargs)

fungsi(nama="Ucup", tinggi=183, berat=79)
# Output: {'nama': 'Ucup', 'tinggi': 183, 'berat': 79}
```
Dalam contoh di atas, `nama="Ucup"`, `tinggi=183`, dan `berat=79` diteruskan sebagai argumen kata kunci, dan `kwargs` di dalam fungsi menjadi dictionary `{'nama': 'Ucup', 'tinggi': 183, 'berat': 79}`.

### Mengakses Nilai dalam `**kwargs`
Karena `kwargs` adalah sebuah dictionary, Anda dapat mengakses nilai-nilainya menggunakan kunci (key) atau metode `.get()` yang umum digunakan pada dictionary.

```python
def fungsi_detail(**kwargs):
    '''Fungsi dengan keyword arguments'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_detail(nama="Ucup", tinggi=183, berat=79)
# Output: Ucup punya tinggi 183 dan berat 79
```
Menggunakan `.get()` lebih aman karena tidak akan menimbulkan `KeyError` jika kunci tidak ada, melainkan mengembalikan `None` atau nilai default yang ditentukan.

## Menggabungkan `*args` dan `**kwargs`
Sangat memungkinkan untuk menggunakan `*args` dan `**kwargs` secara bersamaan dalam satu definisi fungsi. Ini memberikan fleksibilitas maksimal untuk fungsi yang dapat menerima argumen posisi maupun argumen kata kunci.

### Aturan Penulisan
Ketika menggabungkan keduanya, ada aturan penting yang harus diikuti: `*args` (untuk argumen posisi) harus selalu ditulis **sebelum** `**kwargs` (untuk argumen kata kunci) dalam definisi fungsi.

```python
def fungsi_gabungan(*args, **kwargs):
    # *args harus sebelum **kwargs
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
```

### Contoh Penggunaan
```python
def math(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

math(1, 2, 3, 4, option="tambah")
# Output:
# args: (1, 2, 3, 4)
# kwargs: {'option': 'tambah'}
```
Dalam contoh ini, `1, 2, 3, 4` dikumpulkan ke dalam `args` sebagai tuple `(1, 2, 3, 4)`, sementara `option="tambah"` dikumpulkan ke dalam `kwargs` sebagai dictionary `{'option': 'tambah'}`. Pola ini sangat berguna untuk membuat fungsi dengan opsi yang dinamis.

## Studi Kasus: Kalkulator Dinamis
`**kwargs` sangat efektif untuk membuat fungsi yang perilakunya dapat dikonfigurasi melalui argumen kata kunci. Salah satu contoh nyata adalah membuat fungsi kalkulator yang operasinya ditentukan oleh `kwargs`.

### Implementasi
```python
def math(*args, **kwargs):
    '''Fungsi matematika dinamis'''
    output = 0
    
    if kwargs["option"] == "tambah":
        print("Operasi Penjumlahan")
        for angka in args:
            output += angka
            
    elif kwargs["option"] == "kali":
        print("Operasi Perkalian")
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")

    return output

hasil_tambah = math(1, 2, 3, 4, 5, option="tambah")
print(f"Hasil jumlah: {hasil_tambah}") # Output: Hasil jumlah: 15

hasil_kali = math(1, 2, 3, 4, option="kali")
print(f"Hasil kali: {hasil_kali}")     # Output: Hasil kali: 24
```
Dalam fungsi `math` ini, argumen posisi `*args` digunakan untuk angka-angka yang akan dioperasikan, sedangkan `kwargs["option"]` digunakan untuk menentukan jenis operasi (`"tambah"` atau `"kali"`).

### Penerapan dalam Praktik
Pola penggunaan `*args` dan `**kwargs` seperti ini sangat sering ditemukan dalam library dan framework Python yang populer, seperti Django atau Matplotlib. Mereka menggunakannya untuk menyediakan fleksibilitas konfigurasi yang tinggi, memungkinkan pengguna untuk meneruskan berbagai parameter dan opsi tanpa harus mengubah definisi fungsi inti.
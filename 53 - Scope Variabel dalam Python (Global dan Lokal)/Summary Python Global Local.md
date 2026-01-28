# Scope Variabel dalam Python: Global dan Lokal

Dalam pemrograman Python, **scope** (cakupan) variabel menentukan di mana variabel dapat diakses dan digunakan dalam kode. Memahami scope sangat penting untuk menghindari kesalahan dan menulis kode yang bersih serta dapat diprediksi. Python memiliki dua jenis scope utama: **Global Scope** dan **Local Scope**.

## 1. Global Scope

**Variabel Global** adalah variabel yang didefinisikan di luar fungsi, loop, atau blok `if`. Variabel ini dapat diakses dari mana saja dalam program, baik di dalam fungsi, loop, maupun pernyataan `if`.

### 1.1. Akses Variabel Global

*   **Dari dalam Fungsi**: Variabel global dapat dengan mudah diakses dan digunakan di dalam fungsi tanpa deklarasi khusus.
    ```python
    nama_global = "Otong" # Variabel Global

    def fungsi_tampilkan():
        print(f"Fungsi menampilkan {nama_global}") # Mengakses nama_global

    fungsi_tampilkan()
    # Output: Fungsi menampilkan Otong
    ```
    Variabel `nama_global` yang didefinisikan di luar fungsi `fungsi_tampilkan()` dapat langsung digunakan di dalamnya.

*   **Dari dalam Loop (`for`, `while`)**: Variabel global juga dapat diakses dan digunakan di dalam blok perulangan.
    ```python
    nama_global = "Otong"
    for i in range(3):
        print(f"Loop ke-{i} menampilkan {nama_global}") # Mengakses nama_global
    # Output:
    # Loop ke-0 menampilkan Otong
    # Loop ke-1 menampilkan Otong
    # Loop ke-2 menampilkan Otong
    ```

*   **Dari dalam Pernyataan Kondisional (`if`, `elif`, `else`)**: Sama seperti loop, variabel global dapat diakses di dalam blok kondisional.
    ```python
    nama_global = "Otong"
    if True:
        print(f"Ini adalah if menampilkan {nama_global}") # Mengakses nama_global
    # Output: Ini adalah if menampilkan Otong
    ```
    Secara umum, variabel global "hidup dimanapun program kita berada".

### 1.2. Mengubah Variabel Global dari dalam Fungsi (Keyword `global`)

Secara *default*, jika Anda mencoba mengubah nilai variabel global dari dalam fungsi dengan melakukan *assignment* (`variabel = nilai_baru`), Python akan menganggap Anda membuat **variabel lokal baru** dengan nama yang sama di dalam fungsi tersebut, bukan mengubah variabel global aslinya.

Untuk benar-benar mengubah nilai variabel global dari dalam fungsi, Anda harus menggunakan kata kunci **`global`** sebelum nama variabel di dalam fungsi.

```python
angka = 0
nama = "Ucup"

def ubah_data(nilai_baru, nama_baru):
    global angka # Memberi akses untuk mengubah variabel global 'angka'
    global nama  # Memberi akses untuk mengubah variabel global 'nama'
    
    angka = nilai_baru # Mengubah variabel global 'angka'
    nama = nama_baru   # Mengubah variabel global 'nama'

print(f"Sebelum: Angka = {angka}, Nama = {nama}") # Output: Sebelum: Angka = 0, Nama = Ucup
ubah_data(10, "Otong")
print(f"Sesudah: Angka = {angka}, Nama = {nama}") # Output: Sesudah: Angka = 10, Nama = Otong
```
Tanpa `global`, `angka` dan `nama` di luar fungsi tidak akan berubah.

## 2. Local Scope

**Variabel Lokal** adalah variabel yang didefinisikan di dalam sebuah fungsi. Variabel ini **HANYA** hidup dan dapat diakses di dalam fungsi tempat ia didefinisikan. Variabel lokal tidak dapat diakses dari luar fungsi.

```python
def fungsi_lokal():
    nama_lokal = "Ucup" # Variabel Lokal
    print(f"Di dalam fungsi: {nama_lokal}")

fungsi_lokal()
# Output: Di dalam fungsi: Ucup

# print(nama_lokal) # <--- Ini akan ERROR: NameError: name 'nama_lokal' is not defined
```
Pesan `NameError` muncul karena `nama_lokal` hanya ada di dalam `fungsi_lokal()` dan tidak dikenal di luar fungsi tersebut.

## 3. Perbedaan Scope pada Fungsi vs. Loop/If

Ini adalah aspek penting dan seringkali membingungkan dalam Python:

*   **Fungsi (`def`) menciptakan Local Scope**: Seperti yang dijelaskan di atas, variabel yang didefinisikan di dalam fungsi adalah lokal untuk fungsi tersebut dan tidak dapat diakses dari luar. Ini adalah satu-satunya konstruksi di Python yang menciptakan scope lokal yang terisolasi.

*   **Loop (`for`, `while`) dan Pernyataan Kondisional (`if`, `elif`, `else`) TIDAK menciptakan Local Scope**: Variabel yang didefinisikan atau diubah di dalam blok `for` atau `if` **masih dianggap sebagai variabel global** (atau variabel dari scope terluar yang mengelilinginya) dan dapat diakses serta diubah dari luar blok tersebut.

    ```python
    angka_loop = 0
    for i in range(5):
        angka_loop += i
        angka_dummy = 0 # Didefinisikan di dalam loop
        if i == 2:
            angka_if = 10 # Didefinisikan di dalam if
    
    print(f"Angka Loop: {angka_loop}")   # Output: Angka Loop: 10 (0+1+2+3+4)
    print(f"Angka Dummy: {angka_dummy}") # Output: Angka Dummy: 0 (bisa diakses dari luar loop)
    print(f"Angka If: {angka_if}")       # Output: Angka If: 10 (bisa diakses dari luar if)
    ```
    Contoh di atas menunjukkan bahwa `angka_dummy` dan `angka_if`, meskipun didefinisikan di dalam blok `for` dan `if`, tetap dapat diakses dari luar blok tersebut. Ini berbeda dengan perilaku variabel di dalam fungsi.

## Ringkasan

| Fitur                 | Variabel Global                                  | Variabel Lokal                                   |
| :-------------------- | :----------------------------------------------- | :----------------------------------------------- |
| **Definisi**          | Di luar fungsi/blok                              | Di dalam fungsi                                  |
| **Aksesibilitas**     | Dapat diakses dari mana saja (fungsi, loop, if)  | Hanya dapat diakses di dalam fungsi yang sama    |
| **Modifikasi**        | Dari luar fungsi: Langsung. Dari dalam fungsi: Gunakan `global` | Hanya dapat diubah di dalam fungsi yang sama     |
| **Scope yang Dibuat** | Tidak ada scope baru yang dibuat                 | Fungsi menciptakan scope lokal yang terisolasi   |
| **Loop/If**           | Variabel di dalam loop/if tetap global           | Loop/if tidak menciptakan scope lokal terisolasi |
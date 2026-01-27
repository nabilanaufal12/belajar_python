# Default Argument pada Fungsi Python

## Pendahuluan
Default argument adalah fitur dalam Python yang memungkinkan kita untuk memberikan **nilai awal** (default) pada parameter fungsi. Ini berarti jika saat pemanggilan fungsi suatu argumen tidak diberikan, nilai default yang telah ditentukan akan digunakan secara otomatis. Fitur ini sangat berguna untuk membuat fungsi lebih fleksibel dan mengurangi kemungkinan error akibat argumen yang hilang.

## 1. Apa itu Default Argument?
Ketika sebuah fungsi didefinisikan, argumen-argumennya dapat diberikan nilai default. Jika argumen tersebut tidak disediakan saat fungsi dipanggil, Python akan menggunakan nilai default yang telah ditetapkan. Jika argumen tidak memiliki nilai default dan tidak diberikan saat pemanggilan, maka akan terjadi error.

### Sintaks Dasar
Untuk mendefinisikan default argument, gunakan tanda sama dengan (`=`) setelah nama parameter di dalam definisi fungsi, diikuti dengan nilai defaultnya.

```python
def nama_fungsi(argumen_biasa, argumen_default="nilai_default"):
    # ... kode fungsi ...
```

### Contoh Sederhana: `say_hello`
Pertimbangkan fungsi `say_hello` yang menyapa seseorang. Tanpa default argument, jika nama tidak diberikan, fungsi akan error.

```python
def say_hello(nama):
    print(f"Halo {nama}")

# say_hello() # Ini akan menyebabkan error: missing 1 required positional argument: 'nama'
```

Dengan default argument, kita bisa menetapkan nilai default seperti "Ganteng" atau "Kamu" untuk `nama`.

```python
def say_hello(nama="Ganteng"): # Default argument 'nama'
    print(f"Halo {nama}")

say_hello("Ucup") # Output: Halo Ucup
say_hello()       # Output: Halo Ganteng (menggunakan nilai default)
```

## 2. Fungsi dengan Multiple Arguments
Fungsi dapat memiliki kombinasi argumen biasa (tanpa default) dan argumen dengan nilai default.

### Aturan Penempatan Default Argument
**Penting**: Argumen dengan nilai default harus selalu diletakkan **setelah** argumen-argumen biasa (yang tidak memiliki nilai default) dalam definisi fungsi. Jika aturan ini tidak diikuti, Python akan menghasilkan error sintaks.

### Contoh: `sapa_dia`
Misalnya, fungsi `sapa_dia` membutuhkan `nama` dan `pesan`. Kita bisa memberikan nilai default untuk `pesan`.

```python
# Penempatan yang benar: default argument di akhir
def sapa_dia(nama, pesan="Apa kabar?"): # 'pesan' adalah default argument
    print(f"Hai {nama}, {pesan}")

sapa_dia("Dudung", "Hai Ganteng") # Output: Hai Dudung, Hai Ganteng
sapa_dia("Otong")                 # Output: Hai Otong, Apa kabar? (menggunakan default 'pesan')
```

Jika `pesan` diletakkan sebelum `nama` dengan nilai default, akan terjadi error:
```python
# def sapa_dia(pesan="Apa kabar?", nama): # Ini akan menyebabkan SyntaxError
#     print(f"Hai {nama}, {pesan}")
```

## 3. Keyword Arguments (Argumen Kata Kunci)
Selain memanggil fungsi berdasarkan posisi argumen, kita juga bisa memanggilnya dengan menyebutkan nama argumen secara eksplisit. Ini disebut **keyword arguments**.

### Manfaat Keyword Arguments
1.  **Fleksibilitas Urutan**: Memungkinkan kita untuk mengubah urutan argumen saat memanggil fungsi, asalkan nama argumennya disebutkan.
2.  **Keterbacaan**: Meningkatkan keterbacaan kode, terutama untuk fungsi dengan banyak argumen.

### Contoh: `hitung_pangkat`
Fungsi `hitung_pangkat` menghitung `angka` dipangkatkan `pangkat`. `pangkat` diberikan nilai default 2.

```python
def hitung_pangkat(angka, pangkat=2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2, 4)) # Output: 16 (2 pangkat 4)
print(hitung_pangkat(pangkat=3, angka=5)) # Output: 125 (5 pangkat 3). Urutan argumen ditukar menggunakan keyword arguments.
```

## 4. Fungsi dengan Banyak Argumen
Default argument dan keyword arguments sangat berguna ketika sebuah fungsi memiliki banyak parameter, dan kita hanya ingin mengubah beberapa di antaranya tanpa harus mengingat urutan semua argumen.

### Contoh: Fungsi dengan Empat Input
Misalnya, sebuah fungsi `fungsi` memiliki empat input, semuanya dengan nilai default.

```python
def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi()) # Output: 10 (1+2+3+4). Semua menggunakan nilai default.
print(fungsi(input3=10)) # Output: 17 (1+2+10+4). Hanya 'input3' yang diubah menggunakan keyword argument.
```

Teknik ini banyak digunakan dalam library Python yang besar, seperti Matplotlib, untuk mengatur konfigurasi atau opsi plot. Ini memungkinkan pengguna untuk hanya menentukan parameter yang ingin mereka ubah, sementara sisanya menggunakan nilai default yang masuk akal.
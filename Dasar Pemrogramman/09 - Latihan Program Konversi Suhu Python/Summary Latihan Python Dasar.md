# Latihan Program Konversi Suhu Python

Catatan ini merangkum materi tentang pembuatan program sederhana untuk mengkonversi satuan suhu dari Celcius ke Reamur, Fahrenheit, dan Kelvin menggunakan bahasa pemrograman Python. Materi ini juga mencakup penjelasan rumus, implementasi kode, dan tugas latihan.

## Pendahuluan
Program konversi suhu ini merupakan latihan dasar dalam pemrograman Python untuk mengaplikasikan rumus matematika sederhana. Tujuannya adalah untuk mengubah suhu dari skala **Celcius** ke tiga skala lainnya: **Reamur**, **Fahrenheit**, dan **Kelvin**.

## Rumus Konversi Suhu
Berikut adalah rumus konversi dari Celcius (C) ke skala suhu lainnya:

*   **Celcius ke Reamur**:
    $R = \frac{4}{5} \times C$
*   **Celcius ke Fahrenheit**:
    $F = \left(\frac{9}{5} \times C\right) + 32$
*   **Celcius ke Kelvin**:
    $K = C + 273$

## Implementasi Program Python

Program ini diawali dengan menampilkan judul, menerima input suhu dalam Celcius, melakukan perhitungan konversi, dan menampilkan hasilnya.

### 1. Struktur Program
Program dimulai dengan mencetak judul dan kemudian meminta input suhu dari pengguna. Setelah itu, program akan menghitung konversi ke Reamur, Fahrenheit, dan Kelvin, lalu menampilkan semua hasil konversi tersebut.

```python
print("\nPROGRAM KONVERSI TEMPERATUR\n") # Judul program

# Input suhu dalam Celcius
celcius = float(input('Masukkan suhu dalam Celcius : '))
print("Suhu adalah", celcius, "Celcius")

# Konversi ke Reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")

# Konversi ke Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Konversi ke Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")
```

### 2. Input Pengguna
Untuk menerima input suhu dari pengguna, digunakan fungsi `input()`. Karena suhu bisa berupa bilangan desimal (misalnya, 50.5 derajat), input harus diubah ke tipe data `float` menggunakan `float()`.

```python
celcius = float(input('Masukkan suhu dalam Celcius : '))
print("Suhu adalah", celcius, "Celcius")
```

### 3. Konversi ke Reamur
Rumus konversi Celcius ke Reamur adalah $R = \frac{4}{5} \times C$. Penting untuk menggunakan tanda kurung `()` pada pecahan `(4/5)` untuk memastikan operasi pembagian dilakukan terlebih dahulu sebelum perkalian, sesuai dengan urutan operasi matematika.

```python
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")
```

### 4. Konversi ke Fahrenheit
Rumus konversi Celcius ke Fahrenheit adalah $F = \left(\frac{9}{5} \times C\right) + 32$. Sama seperti Reamur, penggunaan tanda kurung `()` pada `(9/5)` sangat disarankan untuk menjaga preseden operasi dan menghindari kesalahan perhitungan.

```python
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")
```

### 5. Konversi ke Kelvin
Konversi Celcius ke Kelvin adalah yang paling sederhana, yaitu $K = C + 273$.

```python
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")
```

### Contoh Eksekusi Program
Berikut adalah contoh hasil eksekusi program dengan beberapa input suhu:

*   **Input**: `0` Celcius
    *   Reamur: `0.0`
    *   Fahrenheit: `32.0`
    *   Kelvin: `273.0`
*   **Input**: `10` Celcius
    *   Reamur: `8.0`
    *   Fahrenheit: `50.0`
    *   Kelvin: `283.0`

## Tugas / Latihan
Sebagai latihan, disarankan untuk membuat dua program konversi suhu tambahan:

1.  **Konversi Fahrenheit ke Kelvin**: Konversi ini tidak bisa langsung; biasanya memerlukan konversi ke Celcius atau Reamur terlebih dahulu sebagai perantara.
2.  **Konversi Kelvin ke Fahrenheit**.

Setiap program diharapkan cukup singkat, sekitar lima baris kode.
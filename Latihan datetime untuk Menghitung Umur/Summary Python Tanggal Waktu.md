# Summary Python Tanggal Waktu

> Generated: January 19th, 2026 10:03 AM
> Sources: Belajar Python [Dasar] - 20 - Latihan Date and Tim.youtube, pasted-text-1.md

---

# Catatan Belajar Python: Latihan `datetime` untuk Menghitung Umur

Tutorial ini membahas penggunaan library `datetime` di Python untuk membuat aplikasi sederhana penghitung umur. Kita akan belajar cara mendapatkan tanggal saat ini, membuat objek tanggal spesifik, mengambil input dari pengguna, dan melakukan perhitungan selisih tanggal untuk menentukan umur dalam tahun dan bulan.

## Pengenalan Library `datetime`

`datetime` adalah library bawaan Python yang menyediakan kelas untuk memanipulasi tanggal dan waktu. Ini sangat berguna untuk berbagai aplikasi yang memerlukan penanganan data waktu.

Untuk menggunakan library ini, kita perlu mengimpornya. Umumnya, `datetime` diimpor dengan alias `dt` untuk mempersingkat penulisan kode.

```python
import datetime as dt
```

## Mendapatkan Tanggal Saat Ini

Untuk mengetahui tanggal hari ini, kita dapat menggunakan metode `date.today()` dari modul `datetime`. Metode ini akan mengembalikan objek `date` yang merepresentasikan tanggal saat kode dijalankan.

```python
hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
# Contoh Output: Hari ini tanggal: 2023-10-27
```

## Membuat Objek Tanggal Spesifik

Selain tanggal hari ini, kita juga bisa membuat objek tanggal secara manual, misalnya untuk merepresentasikan tanggal lahir. Ini dilakukan dengan memanggil `dt.date()` dan memberikan argumen tahun, bulan, dan tanggal secara berurutan.

```python
tanggal_spesifik = dt.date(2005, 10, 10)
print(tanggal_spesifik)
# Output: 2005-10-10
```

## Mengambil Input Tanggal Lahir dari Pengguna

Agar aplikasi lebih interaktif, kita dapat meminta pengguna untuk memasukkan tanggal, bulan, dan tahun lahir mereka. Input dari fungsi `input()` selalu berupa string, sehingga perlu dikonversi ke tipe data integer (`int()`) agar dapat digunakan oleh `dt.date()`.

```python
print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan   = int(input("Bulan \t\t: "))
tahun   = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
```

## Menampilkan Hari Lahir

Setelah mendapatkan objek `tanggal_lahir`, kita bisa mengetahui hari apa seseorang lahir. Ini dapat dilakukan dengan menggunakan *format string* `%A` di dalam f-string. `%A` akan mengonversi tanggal menjadi nama hari lengkap (misalnya, "Monday", "Friday").

```python
print(f"Harinya adalah : {tanggal_lahir:%A}")
# Contoh Output: Harinya adalah : Monday
```

## Menghitung Umur

Inti dari aplikasi ini adalah menghitung selisih antara tanggal hari ini dengan tanggal lahir.

### Selisih Waktu (`timedelta`)

Ketika dua objek `date` dikurangi, hasilnya adalah objek `timedelta`. Objek ini merepresentasikan durasi atau selisih waktu antara dua tanggal.

```python
hari_ini = dt.date.today() # Pastikan hari_ini sudah didefinisikan
umur_hari = hari_ini - tanggal_lahir
print(f"Umur anda adalah: {umur_hari}")
# Contoh Output: Umur anda adalah: 6591 days, 0:00:00
```

### Mengambil Jumlah Hari

Untuk mendapatkan total jumlah hari dari objek `timedelta`, kita dapat mengakses atribut `.days`.

```python
total_hari_umur = umur_hari.days
print(f"Total hari umur: {total_hari_umur} hari")
```

### Konversi ke Tahun dan Sisa Bulan

Karena `umur_hari` memberikan selisih dalam hari, kita perlu mengonversinya ke tahun dan bulan agar lebih mudah dipahami.

1.  **Menghitung Tahun**: Kita dapat membagi total hari dengan 365 (rata-rata jumlah hari dalam setahun) menggunakan pembagian integer (`//`).
2.  **Menghitung Sisa Bulan**: Sisa hari setelah dihitung tahunnya (`% 365`) kemudian dibagi dengan 30 (rata-rata jumlah hari dalam sebulan) menggunakan pembagian integer (`//`).

```python
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
```

## Kode Lengkap

Berikut adalah contoh kode lengkap untuk aplikasi penghitung umur sederhana:

```python
import datetime as dt

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan   = int(input("Bulan \t\t: "))
tahun   = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
```
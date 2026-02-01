# Pengenalan Library datetime
import datetime as dt

# Mendapatkan Tanggal Saat Ini
hari_ini = dt.date.today()
print("Hari ini tanggal:", hari_ini)

# Membuat Objek Tanggal Spesifik
tanggal_lahir = dt.date(2006, 1, 12)
print("Tanggal lahir:", tanggal_lahir)

# Mengambil Input Tanggal Lahir dari Pengguna
print("Masukkan tanggal, bulan, dan tahun lahir Anda:")
tanggal = int(input("Tanggal: "))
bulan = int(input("Bulan: "))
tahun = int(input("Tahun: "))
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print("Tanggal lahir Anda:", tanggal_lahir)

# Menampilkan Hari Lahir
print(f"Anda lahir pada hari: {tanggal_lahir:%A}")
hari_lahir = tanggal_lahir.strftime("%A")
print("Anda lahir pada hari:", hari_lahir)

# Menghitung Umur
## Selisih Waktu (timedelta)
umur_hari = hari_ini - tanggal_lahir
print(f"Umur Anda dalam hari adalah: {umur_hari.days} hari")

## Mengambil Jumlah Hari
jumlah_hari = umur_hari.days
print("Umur Anda adalah:", jumlah_hari, "hari")

## Konversi ke Tahun dan Sisa Bulan
umur_tahun = jumlah_hari // 365
sisa_hari = jumlah_hari % 365
umur_bulan = sisa_hari // 30
sisa_hari_akhir = sisa_hari % 30
print(f"Umur Anda adalah: {umur_tahun} tahun, {umur_bulan} bulan, dan {sisa_hari_akhir} hari")

## Menghitung Umur dalam Tahun
umur = hari_ini.year - tanggal_lahir.year
print("Umur Anda adalah:", umur, "tahun")
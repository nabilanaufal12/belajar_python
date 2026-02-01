# Modul datetime
import datetime

data_waktu = datetime.datetime.now()
print(f"Waktu sekarang: {data_waktu}")
print(f"Tahun: {data_waktu.year}")
print(f"Bulan {data_waktu.month} ")
print(f"Hari: {data_waktu.day} ({data_waktu.strftime('%A')})")


# Modul collections (Counter)
from collections import Counter

data = ["a", "b", "c", "a", "d", "a", "a", "b", "d"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"Jumlah A: {data_count['a']}")
print(f"Jumlah B: {data_count['b']}")
print(f"Jumlah C: {data_count['c']}")
print(f"Jumlah D: {data_count['d']}")


# Modul io (Penanganan File)
import io

file = io.open("text.txt", "r")

print(file.read())
# Pernyataan continue

## Mekanisme continue
# Pernyataan continue digunakan untuk melewati iterasi saat ini dalam sebuah loop dan melanjutkan ke iterasi berikutnya.

## Contoh penggunaan continue dalam Perulangan while
print("""\nContoh penggunaan continue dalam while loop
jika nilai ganjil, lewati iterasi dan lanjut ke nilai berikutnya""")
nilai = 0
while nilai < 5:
    if nilai % 2 == 1:
        nilai += 1  # Pastikan untuk menambah nilai sebelum continue
        continue  # Melewati iterasi saat ini jika nilai ganjil
    print(f"Nilai: {nilai}")
    nilai += 1
print("Selesai")
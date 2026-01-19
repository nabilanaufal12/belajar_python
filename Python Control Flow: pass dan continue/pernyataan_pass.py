# Pernyataan pass

# Tujuan Penggunaan pass
## Fungsi atau Metode yang Belum Diimplementasikan
def fungsi_belum_implementasi():
    pass  # Placeholder untuk fungsi yang belum diimplementasikan
## Kelas yang Belum Diimplementasikan
class KelasBelumImplementasi:
    pass  # Placeholder untuk kelas yang belum diimplementasikan
## Struktur Kontrol yang Kosong
for i in range(5):
    pass  # Placeholder untuk loop yang belum diisi

# Contoh pass dalam Perulangan while
print("""\nContoh penggunaan pass dalam while loop
ika nilai genap, tidak melakukan apa-apa""")
nilai = 0
while nilai < 5:
    if nilai % 2 == 0:
        pass  # Placeholder untuk kondisi genap
    else:
        print(f"Nilai: {nilai}")
    nilai += 1
print("Selesai")
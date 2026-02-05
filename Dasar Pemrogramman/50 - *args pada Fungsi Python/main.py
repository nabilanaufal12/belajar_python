# Catatan Belajar: `*args` pada Fungsi Python

# Masalah dengan Argumen Tetap (Fixed Arguments)
def fungsi_biasa(nama, tinggi, berat):
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi_biasa("Mizu", 160, 47)
# fungsi_biasa("Miwa", 159) akan error karena kurang argumen
# fungsi_biasa("Mika", 149, 44, 67) error karena kelebian argumen

# Solusi: Menggunakan *args
def fungsi_args(*args):
    # args akan menjadi tuple
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi_args("Mizuha", 170, 90)
fungsi_args("Mie", 166, 100, "Japan")

# Studi Kasus: Fungsi Penjumlahan Dinamis
def tambah(*data):
    hasil = 0
    for angka in data:
        hasil += angka
    return hasil

print(tambah(1, 2, 3, 4, 5))
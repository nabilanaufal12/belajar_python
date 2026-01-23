# Program Database Buku Sederhana dengan Python List

print("=== Program Database Buku Sederhana ===")

# Inisialisasi list untuk menyimpan data buku
buku_list = []

while True:
    print("\n" + "="*10 + " Masukkan Data Buku Baru " + "="*10)
    judul = input("Masukkan Judul Buku\t: ")
    penulis = input("Masukkan Nama Penulis\t: ")
    tahun_terbit = input("Masukkan Tahun Terbit\t: ")

    buku_baru = [judul, penulis, tahun_terbit]
    buku_list.append(buku_baru)

    print("\nData buku berhasil ditambahkan!")
    print("No.\t| Judul Buku\t| Penulis\t| Tahun Terbit")
    for i, buku in enumerate(buku_list):
        print(f"{i+1}\t| {buku[0]}\t| {buku[1]}\t| {buku[2]}")

    print("-"*40)

    lanjut = input("Apakah Anda ingin menambahkan data buku lagi? (y/n): ")
    if lanjut.lower() != 'y':
        break

print("\nTerima kasih telah menggunakan program database buku sederhana!")
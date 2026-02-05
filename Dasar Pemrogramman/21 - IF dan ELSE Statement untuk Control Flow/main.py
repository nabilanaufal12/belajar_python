# Konsep Dasar Percabangan
"""
Secara diagram, percabangan if memiliki struktur sebagai berikut :
1. Kondisi: Sebuah ekspresi yang dievaluasi menjadi True atau False.
2. Aksi True: Serangkaian instruksi yang dijalankan jika kondisi bernilai True.
3. Aksi False: Serangkaian instruksi yang dijalankan jika kondisi bernilai False (ini akan ditangani oleh else).
"""

# IF Statement
## Kondisi Boolean
# nama = "Andi"
# umur > 20
# is_student = False

## Sintaks Dasar IF
# if kondisi:
#     aksi_true

### Format Inline (Satu Baris)
input_nama = input("Siapa nama anda? ")
if input_nama == "Andi": print("Halo Andi, selamat datang kembali!")
print(f"Terimakasih {input_nama} sudah mengunjungi program ini.")

### Format dengan Indentasi (Blok Kode)
if input_nama == "Andi":
    print("\nHalo Andi, selamat datang kembali!")
    print("Apa kabar hari ini?")
print(f"Terimakasih {input_nama} sudah mengunjungi program ini.")

# IF...ELSE Statement
## Sintaks Dasar IF...ELSE
# if kondisi:
#     aksi_true
# else:
#     aksi_false

## Contoh Program IF-ELSE
if input_nama == "Andi":
    print("\nHalo Andi, selamat datang kembali!")
    print("Apa kabar hari ini?")
else:
    print(f"\nHalo {input_nama}, senang bertemu denganmu!")
    print("Semoga harimu menyenangkan!")
print(f"Terimakasih {input_nama} sudah mengunjungi program ini.")
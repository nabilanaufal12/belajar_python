# Penanganan Exception (Error) di Python
# Memahami Jenis-jenis Error

## 1. Syntax Error
# print "halo" <-- akan error

## 2. Runtime Error (Exception)
'''
1. ZeroDivisionError: Terjadi ketika mencoba membagi angka dengan nol.
2. FileNotFoundError: Terjadi ketika program mencoba membuka file yang tidak ada.
3. ValueError: Terjadi ketika fungsi menerima argumen dengan tipe yang benar tetapi nilai yang tidak sesuai (misalnya, int("abc")).
'''


# Mekanisme try dan except
print("=== Mekanisme try dan except ===")
input_user = int(input("Masukkan angka: "))
hasil = 0

try:
    hasil = 10/input_user
    print(f"Hasil: {hasil}")
except:
    print("Input tidak boleh nol!") # Pesan kesalahan jika terjadi exception
    hasil = float('nan') # Mengatur hasil menjadi Not a Number

print(f"Hasil akhir: {hasil}")


# Menangani Exception Spesifik
print("\n=== Menangani Exception Spesifik ===")
while True:
    try:
        angka = int(input("Masukkan angka pembagi: "))
        hasil = 10/angka
        print(f"Hasil: {hasil}")
        break # Keluar dari loop jika berhasil
    except ValueError:
        print("Yang Anda masukkan BUKAN ANGKA!") # Menangani input non-numeric
    except ZeroDivisionError:
        print("Angka tidak boleh NOL!") # Menangani pembagian dengan nol
    except Exception as e:
        print(f"Error tidak dikenal: {e}") # Menangani exception lain yang tidak spesifik


# Struktur Lengkap try-except-else-finally
print("\n=== Struktur Lengkap try-except-else-finally ===")
file = None # Inisialisasi file agar terdefinisi di luar blok try
try:
    # Coba membuka file dalam mode baca ('r')
    file = open("data_test.txt", 'r')
    print("File berhasil dibuka")
except FileNotFoundError:
    print("File tidak ditemukan! Membuat file baru...")
    # Jika file tidak ditemukan, buat file baru dalam mode tulis ('w')
    with open("data_test.txt", 'w', encoding="utf-8") as new_file:
        new_file.write("Ini adalah file baru.\n")
    print("File baru telah berhasil dibuat.")
else:
    # Jika tidak ada exception (file ditemukan dan dibuka), baca isinya
    print("Membaca isi file:")
    print(file.read())
finally:
    # Pastikan file ditutup, baik ada error maupun tidak
    if file and not file.closed:
        file.close()
        print("File ditutup (Cleanup).")

print("Akhir dari program.")


# Membuat dan Mengangkat Exception Kustom (raise)
print("\n=== Membuat dan Mengangkat Exception Kustom (raise) ===")
def tambah(a, b):
    # Memastikan kedua input adalah angka
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Mengangkat ValueError jika input bukan angka
        raise ValueError("Input harus angka!")
    return a + b

try:
    print(tambah(2, 3))
    print(tambah(2, "a")) # Ini akan memicu exception kustom
except ValueError as e:
    print(f"Terjadi kesalahan: {e}")
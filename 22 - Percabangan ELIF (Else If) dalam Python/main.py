# Konsep Dasar dan Alur Eksekusi
"""
1. Kondisi IF dievaluasi terlebih dahulu. Jika kondisi IF bernilai True, 
   blok kode di dalam IF akan dieksekusi, dan program akan melompat keluar dari struktur percabangan.
2. Jika kondisi IF bernilai False, maka program akan melanjutkan ke kondisi ELIF berikutnya (jika ada).
3. Jika kondisi ELIF bernilai True, blok kode di dalam ELIF tersebut akan dieksekusi, dan program akan melompat keluar dari struktur percabangan.
4. Jika semua kondisi IF dan ELIF bernilai False, maka blok kode di dalam ELSE (jika ada) akan dieksekusi.
"""

# Sintaks ELIF dalam Python
"""
if kondisi1:
    # blok kode jika kondisi1 True
elif kondisi2:
    # blok kode jika kondisi2 True
elif kondisi3:
    # blok kode jika kondisi3 True
else:
    # blok kode jika semua kondisi di atas False
"""

# Contoh Implementasi: Program Sapaan Nama
nama = input("Masukkan nama Anda: ")

if nama == "Alice":
    print("Halo Alice! Selamat datang kembali.")
elif nama == "Bob":
    print("Hai Bob! Senang bertemu denganmu lagi.")
elif nama == "Charlie":
    print("Selamat datang Charlie! Apa kabar?")
else:
    print(f"Halo {nama}! Senang bertemu dengan Anda.")

print("Program selesai.")
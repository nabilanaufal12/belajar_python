# Scope Variabel dalam Python: Global dan Lokal

# 1. Global Scope
## 1.1. Akses Variabel Global
var_global = "Mizu"

# Dari dalam Fungs
def f_tampilkan():
    print(f"Halo, {var_global}")

f_tampilkan()

# Dari dalam Loop (for, while)
for i in range(3):
    print(f"Loop ke-{i}: {var_global}")

# Dari dalam Pernyataan Kondisional (if, elif, else)
if True:
    print(f"Ini aku {var_global}")

## 1.2. Mengubah Variabel Global dari dalam Fungsi (Keyword global)
angka = 0
nama = "Miwa"

def ubah_data(angka_baru, nama_baru):
    global angka
    global nama

    angka = angka_baru
    nama = nama_baru

print(f"Sebelum menggunakan keyword globa: {angka}, {nama}")
ubah_data(10, "Mizu")
print(f"Sesudah menggunakan keyword globa: {angka}, {nama}")


# 2. Local Scope
def f_local():
    nama_local = "Mika"
    print(f"{nama_local} dalam fungsi local")

f_local()
# f_local(nama_local) ERROR


# 3. Perbedaan Scope pada Fungsi vs. Loop/If
angka_loop = 0

for i in range(5):
    angka_loop += 1
    angka_dummy = 0 # Didefinisikan di dalam loop
    if i == 2:
        angka_if = 10 # Didefinisikan di dalam if

print(f"Angka loop: {angka_loop}")
print(f"Angka dummy: {angka_dummy}")
print(f"Angka if: {angka_if}")
# Nested List (List Bersarang) di Python

# Definisi dan Konsep Dasar Nested List
data_1 = [1, 2, 3]
data_2 = ['a', 'b', 'c']

nested_list = [data_1, data_2]
print("Nested List:", nested_list)
print()

# Contoh Penggunaan: Data Kompleks (Peserta)
siswa_1 = ['Andi', 20, ['Matematika', 'Fisika']]
siswa_2 = ['Budi', 22, ['Biologi', 'Kimia']]
siswa_3 = ['Citra', 21, ['Sejarah', 'Geografi']]

daftar_siswa = [siswa_1, siswa_2, siswa_3]
print("Daftar Siswa:", daftar_siswa)
print()

# Mengakses Data dalam Nested List
print("Nama Siswa Pertama:", daftar_siswa[0][0])
print("Usia Siswa Kedua:", daftar_siswa[1][1])
print("Mata Pelajaran Siswa Ketiga:", daftar_siswa[2][2])
print()

for siswa in daftar_siswa:
    nama = siswa[0]
    usia = siswa[1]
    mata_pelajaran = ', '.join(siswa[2])
    print(f"Nama: {nama}, Usia: {usia}, Mata Pelajaran: {mata_pelajaran}")
print()

# Masalah Referensi (Shallow Copy) pada Nested List
list_copy = daftar_siswa.copy()

print(5*"=" + "Sebelum Modifikasi" + 5*"=")
print("Daftar Siswa Asli:", daftar_siswa)
print("List Copy:", list_copy)
print()

print(5*"=" + "Setelah Modifikasi" + 5*"=")
list_copy[0][0] = 'Andi Modified'
print("Daftar Siswa Asli:", daftar_siswa)
print("List Copy:", list_copy)
print()
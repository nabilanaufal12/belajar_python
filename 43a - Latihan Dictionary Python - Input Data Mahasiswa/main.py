# Catatan Belajar: Latihan Dictionary Python - Input Data Mahasiswa

# 1. Persiapan Awal dan Modul yang Dibutuhkan
import datetime
import os

os.system('cls' if os.name == 'nt' else 'clear') # Membersihkan Layar Konsol

# 2. Membuat Template Dictionary Mahasiswa
template_mahasiswa = {
    "nama": "",
    "nim": "",
    "jurusan": "",
    "tanggal_masuk": datetime.datetime.now().strftime("%Y-%m-%d"),
    "ipk": 0.0
}

# 3. Inisialisasi Dictionary Mahasiswa Baru dengan dict.fromkeys()
data_mahasiswa = dict.fromkeys(template_mahasiswa.keys())

# 4. Antarmuka Pengguna dan Pengambilan Input
print("=== Input Data Mahasiswa ===")
data_mahasiswa["nama"] = input("Masukkan Nama Mahasiswa\t\t\t: ")
data_mahasiswa["nim"] = input("Masukkan NIM Mahasiswa\t\t\t: ")
data_mahasiswa["jurusan"] = input("Masukkan Jurusan Mahasiswa\t\t: ")
data_mahasiswa["tanggal_masuk"] = input("Masukkan Tanggal Masuk (YYYY-MM-DD)\t: ")
data_mahasiswa["ipk"] = float(input("Masukkan IPK Mahasiswa\t\t\t: "))

# 5. Menampilkan Data Mahasiswa yang Telah Diinput
print("\n=== Data Mahasiswa yang Dimasukkan ===")
for key, value in data_mahasiswa.items():
    print(f"{key.capitalize()}: {value}")
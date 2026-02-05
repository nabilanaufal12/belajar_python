# Latihan Dictionary Python: Looping Input Data Mahasiswa dengan Random Key

# 1. Struktur Data Mahasiswa (Template)
import datetime
import os
import string
import random


template_mahasiswa = {
    "nama": "",
    "nim": "",
    "jurusan": "",
    "tanggal_masuk": datetime.datetime.now().strftime("%Y-%m-%d"),
    "ipk": 0.0
}

# 2. Looping Input Data Mahasiswa
while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Membersihkan Layar Konsol

    data_mahasiswa = dict.fromkeys(template_mahasiswa.keys())

    print("=== Input Data Mahasiswa ===")
    data_mahasiswa["nama"] = input("Masukkan Nama Mahasiswa\t\t\t: ")
    data_mahasiswa["nim"] = input("Masukkan NIM Mahasiswa\t\t\t: ")
    data_mahasiswa["jurusan"] = input("Masukkan Jurusan Mahasiswa\t\t: ")
    data_mahasiswa["tanggal_masuk"] = input("Masukkan Tanggal Masuk (YYYY-MM-DD)\t: ")
    data_mahasiswa["ipk"] = float(input("Masukkan IPK Mahasiswa\t\t\t: "))

    print("\n=== Data Mahasiswa yang Dimasukkan ===")
    for key, value in data_mahasiswa.items():
        print(f"{key.capitalize()}: {value}")

    # 3. Solusi: Generate Random Key
    key_random = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    template_mahasiswa[key_random] = data_mahasiswa

    # 4. Menampilkan Data dalam Bentuk Tabel
    print("\n=== Data Mahasiswa Tersimpan ===")
    print(f"{'Key':<10} {'Nama':<20} {'NIM':<15} {'Jurusan':<20} {'Tanggal Masuk':<15} {'IPK':<5}")
    print("-" * 85)
    for key, mhs in template_mahasiswa.items():
        if isinstance(mhs, dict):
            print(f"{key:<10} {mhs['nama']:<20} {mhs['nim']:<15} {mhs['jurusan']:<20} {mhs['tanggal_masuk']:<15} {mhs['ipk']:<5}")

    # 5. Kontrol Loop: Lanjut atau Berhenti
    lanjut = input("\nApakah Anda ingin memasukkan data lagi? (y/n): ").lower()
    if lanjut != 'y':
        break

print("\nTerima kasih telah menggunakan program ini!")
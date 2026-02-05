# Belajar Python: Multi Keys & Nesting Dictionary untuk Struktur Data

# 1. Dictionary dengan Berbagai Tipe Data (Multi Keys)
import datetime

data_mahasiswa1 = {
    "nama": "Andi",
    "umur": 21,
    "is_active": True,
    "tanggal_lahir": datetime.date(2002, 5, 17),
    "nilai": [85, 90, 78],
}

data_mahasiswa2 = {
    "nama": "Budi",
    "umur": 22,
    "is_active": False,
    "tanggal_lahir": datetime.date(2001, 8, 25),
    "nilai": [88, 76, 92],
}

data_mahasiswa3 = {
    "nama": "Citra",
    "umur": 20,
    "is_active": True,
    "tanggal_lahir": datetime.date(2003, 3, 10),
    "nilai": [91, 89, 95],
}

# 2. Nesting Dictionary untuk Struktur Data Kompleks
data_mahasiswa = {
    "MHS001": data_mahasiswa1,
    "MHS002": data_mahasiswa2,
    "MHS003": data_mahasiswa3,
}

# 3. Menampilkan Data dengan Format Rapi (Tabel)
print(f"{'ID':<10} {'Nama':<10} {'Umur':<5} {'Aktif':<7} {'Tanggal Lahir':<15} {'Nilai':<20}")
print("-" * 70)
for mhs_id, mhs_data in data_mahasiswa.items():
    nama = mhs_data["nama"]
    umur = mhs_data["umur"]
    is_active = "Ya" if mhs_data["is_active"] else "Tidak"
    tanggal_lahir = mhs_data["tanggal_lahir"].strftime("%d-%m-%Y")
    nilai = ", ".join(map(str, mhs_data["nilai"]))
    
    print(f"{mhs_id:<10} {nama:<10} {umur:<5} {is_active:<7} {tanggal_lahir:<15} {nilai:<20}")
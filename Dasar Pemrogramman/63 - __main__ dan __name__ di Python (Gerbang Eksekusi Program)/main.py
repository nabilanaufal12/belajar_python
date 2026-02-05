# __main__ dan __name__ di Python: Gerbang Eksekusi Program

# Konsep Variabel Spesial __name__
## Ketika File Dijalankan Langsung
print(f"Nilai __name__ saat dijalankan langsung: '{__name__}'")

## Ketika File Diimpor sebagai Modul
import fungsi


# Penggunaan if __name__ == "__main__":
if __name__ == "__main__":
    print(f"Nilai __name__ pada main.py = '{__name__}'")
    angka1 = 5
    angka2 = 10
    hasil = fungsi.tambah(angka1, angka2) # Memanggil fungsi dari modul fungsi
    print(f"Hasil tambah di main program = {hasil}")


# __main__.py dalam Package Python

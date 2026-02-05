# Menulis ke File Eksternal di Python

# Mode Write (w)
with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("Ini adalah baris pertama.\n")
# Jika dijalankan lagi dengan teks berbeda, isi file akan terganti total.
with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("Ini adalah baris baru, data lama hilang.\n")

# Mode Append (a)
# Reset file (menggunakan 'w' untuk memastikan file bersih sebelum append)
with open("data_2.txt", 'w', encoding="utf-8") as file:
    file.write("Baris awal.\n")

# Menambahkan data
with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("Baris tambahan pertama.\n")

# Menambahkan data lagi
with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("Baris tambahan kedua.\n")

# Mode Read+Write (r+)
# Siapkan file dummy dengan mode 'w' terlebih dahulu
with open("data_3.txt", 'w', encoding="utf-8") as file:
    file.write("baris ke-1\nbaris ke-2\nbaris ke-3\n")

with open("data_3.txt", 'r+', encoding="utf-8") as file:
    # Menulis di awal file (menimpa karakter yang ada)
    file.write("Mizu")
    # File sekarang akan terlihat seperti: "Mizus ke-1\nbaris ke-2\nbaris ke-3\n"

    # Membaca sisa file dari posisi kursor saat ini
    data = file.read()
    print(data) # Output: " ke-1\nbaris ke-2\nbaris ke-3\n" (karena "Otong" menimpa "baris")
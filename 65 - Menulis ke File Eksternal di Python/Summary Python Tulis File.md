# Menulis ke File Eksternal di Python

Dalam pemrograman Python, kita dapat berinteraksi dengan file eksternal untuk menyimpan atau mengambil data. Proses menulis ke file eksternal melibatkan pemilihan mode yang tepat, yang menentukan bagaimana Python akan memperlakukan file tersebut, terutama jika file sudah ada atau belum. Selalu disarankan untuk menggunakan `encoding="utf-8"` untuk memastikan karakter ditangani dengan benar.

## 1. Mode Write (`w`)

Mode `w` (write) digunakan untuk menulis data ke file. Ini adalah mode yang paling dasar untuk membuat atau menimpa file.

*   **Perilaku File Baru**: Jika file yang ditentukan belum ada, Python akan secara otomatis **membuat file baru** dengan nama tersebut.
*   **Perilaku File Lama**: Jika file sudah ada, mode `w` akan **menimpa (overwrite)** seluruh isi file yang sudah ada dengan data baru. Ini berarti semua data lama di dalam file akan **hilang** dan digantikan sepenuhnya.
*   **Contoh Penggunaan**:
    ```python
    with open("data_1.txt", 'w', encoding="utf-8") as file:
        file.write("Ini adalah baris pertama.\n")
    # Jika dijalankan lagi dengan teks berbeda, isi file akan terganti total.
    with open("data_1.txt", 'w', encoding="utf-8") as file:
        file.write("Ini adalah baris baru, data lama hilang.\n")
    ```
    Dalam contoh di atas, setelah eksekusi kedua, "data_1.txt" hanya akan berisi "Ini adalah baris baru, data lama hilang.".

## 2. Mode Append (`a`)

Mode `a` (append) digunakan untuk menambahkan data ke akhir file tanpa menghapus konten yang sudah ada.

*   **Perilaku File Baru**: Sama seperti mode `w`, jika file belum ada, Python akan membuat file baru.
*   **Perilaku File Lama**: Jika file sudah ada, mode `a` akan menambahkan data baru di **akhir file**. Data lama tidak akan terhapus.
*   **Baris Baru**: Untuk memastikan setiap penambahan data berada di baris baru, sertakan karakter `\n` (newline) di akhir string yang ditulis.
*   **Contoh Penggunaan**:
    ```python
    # Reset file (menggunakan 'w' untuk memastikan file bersih sebelum append)
    with open("data_2.txt", 'w', encoding="utf-8") as file:
        file.write("Baris awal.\n")

    # Menambahkan data
    with open("data_2.txt", 'a', encoding="utf-8") as file:
        file.write("Baris tambahan pertama.\n")

    # Menambahkan data lagi
    with open("data_2.txt", 'a', encoding="utf-8") as file:
        file.write("Baris tambahan kedua.\n")
    ```
    Setelah eksekusi, "data_2.txt" akan berisi:
    ```
    Baris awal.
    Baris tambahan pertama.
    Baris tambahan kedua.
    ```
    Setiap kali mode `a` dijalankan, teks akan terus bertambah di bawahnya.

## 3. Mode Read+Write (`r+`)

Mode `r+` memungkinkan operasi membaca (`read`) dan menulis (`write`) pada file yang sama.

*   **Perilaku File Baru**: Mode `r+` umumnya memerlukan file yang sudah ada. Jika file tidak ada, operasi `open` mungkin akan gagal atau berperilaku tidak terduga tergantung sistem operasi dan versi Python. Disarankan untuk memastikan file sudah ada sebelum menggunakan `r+`.
*   **Perilaku Penulisan**: Penulisan dalam mode `r+` akan **menimpa (overwrite)** karakter yang ada di file, dimulai dari posisi kursor saat ini, dan sesuai dengan panjang data yang ditulis. Ini berbeda dengan mode `w` yang menghapus seluruh isi file.
    *   Jika kursor berada di awal file, dan kita menulis string "Otong" (5 karakter) ke file yang awalnya berisi "baris ke-1", maka "baris" akan tertimpa oleh "Otong", menghasilkan "Otong ke-1".
    *   Panjang data yang ditulis menentukan berapa banyak karakter yang akan tertimpa.
*   **Perilaku Pembacaan**: Setelah menulis, kursor akan berada di akhir data yang baru saja ditulis. Jika kita langsung membaca (`file.read()`) setelah menulis, ia akan membaca sisa file dari posisi kursor tersebut.
*   **Contoh Penggunaan**:
    ```python
    # Siapkan file dummy dengan mode 'w' terlebih dahulu
    with open("data_3.txt", 'w', encoding="utf-8") as file:
        file.write("baris ke-1\nbaris ke-2\nbaris ke-3\n")

    with open("data_3.txt", 'r+', encoding="utf-8") as file:
        # Menulis di awal file (menimpa karakter yang ada)
        file.write("Otong")
        # File sekarang akan terlihat seperti: "Otong ke-1\nbaris ke-2\nbaris ke-3\n"

        # Membaca sisa file dari posisi kursor saat ini
        data = file.read()
        print(data) # Output: " ke-1\nbaris ke-2\nbaris ke-3\n" (karena "Otong" menimpa "baris")
    ```
    Mode `r+` berguna untuk memodifikasi bagian tertentu dari file tanpa harus menulis ulang seluruh file, meskipun memerlukan penanganan kursor yang hati-hati.
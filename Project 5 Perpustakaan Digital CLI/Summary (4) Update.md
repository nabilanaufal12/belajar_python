# Implementasi Fitur Update Data Buku pada Aplikasi CRUD Python

Fitur update memungkinkan pengguna untuk mengubah data buku yang sudah ada dalam database. Proses ini melibatkan pembacaan data spesifik, modifikasi, dan penulisan kembali ke file. Implementasi ini memanfaatkan struktur data dengan panjang baris tetap untuk efisiensi.

## 1. Persiapan dan Alur Umum Fitur Update

Fitur update diimplementasikan melalui fungsi `update_console()` yang ditempatkan di `view.py`. Alur kerja utamanya adalah sebagai berikut:

1.  **Tampilkan Data**: Pertama, semua data buku yang ada akan ditampilkan kepada pengguna menggunakan `read_console()` agar pengguna dapat melihat daftar buku dan memilih mana yang ingin diubah.
2.  **Pilih Nomor Buku**: Pengguna diminta untuk memasukkan nomor buku (indeks) dari data yang ingin di-update.
3.  **Validasi Input**: Input nomor buku akan divalidasi dalam sebuah *loop* (`while True`) untuk memastikan nomor yang dimasukkan valid dan sesuai dengan data yang ada. Jika tidak valid, pesan kesalahan akan ditampilkan, dan pengguna diminta untuk memasukkan kembali.

## 2. Membaca Data Spesifik untuk Update

Untuk mendapatkan data buku yang spesifik berdasarkan nomor yang dipilih pengguna, fungsi `read()` di `operasi.py` dimodifikasi.

*   **Parameter `index`**: Fungsi `read()` kini dapat menerima argumen kata kunci (`keyword argument`) `index`. Jika `index` diberikan, fungsi akan mengembalikan hanya satu baris data spesifik, bukan semua data.
*   **Pengambilan Data**: Data dibaca menggunakan `file.readlines()`, yang menghasilkan daftar (`list`) baris-baris data. Data spesifik diambil dari daftar ini menggunakan `content[index_buku]`, di mana `index_buku` adalah `nomor_buku - 1` karena indeks daftar dimulai dari 0.
*   **Validasi Indeks**: Penting untuk memvalidasi `index_buku` agar tidak kurang dari 0 atau melebihi jumlah buku yang ada (`jumlah_buku`). Jika indeks tidak valid, fungsi akan mengembalikan `False`.

```python
# CRUD/operasi.py
def read(**kwargs):
    try:
        with open(database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku >= jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False
```

## 3. Interaksi Pengguna: Memilih dan Mengubah Data

Setelah data buku yang akan di-update berhasil diambil, langkah selanjutnya adalah berinteraksi dengan pengguna untuk melakukan perubahan:

1.  **Parsing Data**: Data buku yang didapat dari `read()` berupa string tunggal. String ini kemudian dipecah (`split(',')`) menjadi komponen-komponennya (PK, `date_add`, judul, penulis, tahun). Perlu diperhatikan bahwa karakter *newline* (`\n`) di akhir baris `tahun` harus dihilangkan.
2.  **Tampilkan Data Saat Ini**: Data buku yang sudah di-parse akan ditampilkan kepada pengguna, bersama dengan opsi untuk memilih bagian mana yang ingin diubah (1. Judul, 2. Penulis, 3. Tahun).
3.  **Pilih Field untuk Diubah**: Pengguna memasukkan pilihan (1, 2, atau 3). Program menggunakan `match case` untuk menangani pilihan ini dan meminta input data baru sesuai dengan field yang dipilih.
    *   **Validasi Tahun**: Input untuk tahun divalidasi untuk memastikan bahwa itu adalah angka dan memiliki 4 digit (format `yyyy`).
4.  **Konfirmasi Perubahan**: Setelah pengguna selesai memasukkan perubahan, data yang telah dimodifikasi akan ditampilkan kembali, dan pengguna diminta untuk mengonfirmasi apakah data sudah sesuai (`y/n`). Jika `y`, proses update dilanjutkan; jika `n`, pengguna dapat mengulang proses pemilihan field.

## 4. Mekanisme Teknis Update Data (`seek` dan `r+`)

Bagian paling teknis dari fitur update adalah bagaimana perubahan disimpan kembali ke file database. Metode yang digunakan memanfaatkan sifat file dengan panjang baris tetap dan fungsi `seek()`:

1.  **Mode `r+`**: File database dibuka dalam mode `r+` (read and write). Mode ini memungkinkan pembacaan dan penulisan ke file yang sama tanpa menghapus isinya.
2.  **Panjang Baris Tetap**: Asumsi krusial dalam implementasi ini adalah bahwa **setiap baris data dalam file memiliki panjang yang sama** (fixed length). Ini dicapai dengan menambahkan *padding* spasi pada setiap field saat data ditulis, memastikan setiap baris memiliki jumlah karakter yang konsisten.
3.  **Memindahkan Kursor (`file.seek()`)**: Karena panjang setiap baris data diketahui, posisi awal baris data yang ingin diubah dapat dihitung. Fungsi `file.seek()` digunakan untuk memindahkan kursor penulisan ke posisi byte yang tepat di awal baris tersebut.
    *   **Rumus Posisi**: Posisi byte dihitung dengan rumus: `panjang_data_per_baris * (no_buku - 1)`.
4.  **Menimpa Data (`file.write()`)**: Setelah kursor dipindahkan, data baru yang sudah diformat ulang (dengan panjang yang sama) akan ditimpa (`file.write()`) ke posisi tersebut, menggantikan data lama.
5.  **Efisiensi**: Keuntungan dari metode ini adalah tidak perlu membaca seluruh file ke memori, memodifikasinya, dan kemudian menulis ulang seluruh file. Hanya baris yang relevan yang diakses dan diubah, menjadikannya lebih efisien untuk file besar.

```python
# CRUD/operasi.py
def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = database.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + database.TEMPLATE["penulis"] * " "
    data["judul"] = judul + database.TEMPLATE["judul"] * " "
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    data_len = len(data_str) # Panjang data per baris (fixed length)
    
    try:
        with open(database.DB_NAME,'r+', encoding="utf-8") as file:
            # Pindah kursor ke awal baris data yang mau diedit
            file.seek(data_len * (no_buku - 1))
            # Timpa data lama dengan data baru
            file.write(data_str)
    except:
        print("Error dalam update data")
```

## 5. Integrasi ke Aplikasi Utama

Agar fitur update dapat diakses oleh pengguna, beberapa penyesuaian dilakukan pada file `main.py` dan `__init__.py`:

*   **`main.py`**: Pilihan "3" pada menu utama (`match user_option`) kini memanggil fungsi `CRUD.update_console()`.
*   **`CRUD/__init__.py`**: Fungsi `update_console` ditambahkan ke daftar fungsi yang diekspos dari paket `CRUD`, sehingga dapat diimpor dan digunakan oleh `main.py`.
# Instalasi Python dan VS Code di Windows untuk Pemula

Catatan ini merangkum langkah-langkah instalasi Python dan Visual Studio Code (VS Code) di sistem operasi Windows, serta konfigurasi dasar VS Code untuk pengembangan Python.

## 1. Instalasi Python

### Mengunduh Python
*   Akses situs resmi Python melalui peramban web Anda: `python.org`.
*   Pilih menu **Downloads** untuk melihat versi Python yang tersedia.
*   Unduh versi terbaru yang stabil. Saat video ini dibuat, versi terbarunya adalah **3.11.2**.
*   **Catatan penting untuk pengguna Windows 7**: Jika Anda menggunakan Windows 7, disarankan untuk mengunduh versi **3.8** karena versi 3.9 ke atas mungkin tidak kompatibel.

### Proses Instalasi
*   Setelah mengunduh *installer*, jalankan *file* tersebut.
*   **Sangat Penting**: Sebelum mengklik "Install Now", pastikan untuk mencentang opsi **"Add Python to PATH"** yang terletak di bagian bawah jendela *installer*. Opsi ini memungkinkan Python dipanggil langsung dari terminal atau *command prompt* tanpa perlu konfigurasi manual yang rumit.
*   Jika Anda lupa mencentang "Add Python to PATH", disarankan untuk menginstal ulang Python dan mengaktifkan opsi tersebut.
*   Lanjutkan instalasi dengan mengklik "Install Now".

### Mengatasi Batasan Panjang Path (Disable Path Length Limit)
*   Setelah proses instalasi selesai, mungkin akan muncul opsi **"Disable path length limit"**.
*   Disarankan untuk mengklik opsi ini. Ini berguna agar Windows dapat memproses jalur *file* yang sangat panjang (lebih dari 255 karakter), yang sering ditemui dalam proyek *coding* yang kompleks.

### Verifikasi Instalasi Python
*   Buka **Terminal**, **Command Prompt (CMD)**, atau **PowerShell**.
*   Ketik perintah berikut untuk memeriksa apakah Python sudah terinstal dengan benar: `python --version`.
*   Jika instalasi berhasil, versi Python yang terinstal akan ditampilkan (misalnya, `Python 3.11.2`).
*   Jika muncul *error*, kemungkinan opsi "Add Python to PATH" tidak dicentang saat instalasi.

## 2. Instalasi Visual Studio Code (VS Code)

### Mengunduh VS Code
*   Cari "Visual Studio Code" di mesin pencari atau kunjungi situs resminya.
*   Unduh *installer* untuk Windows, pastikan untuk memilih versi yang sesuai dengan arsitektur sistem Anda (32-bit atau 64-bit).

### Proses Instalasi
*   Jalankan *installer* VS Code yang telah diunduh.
*   Terima perjanjian lisensi dan klik "Next".
*   Pada langkah "Select Additional Tasks", pastikan untuk mencentang opsi-opsi berikut untuk kemudahan akses dan integrasi dengan Windows Explorer:
    *   **"Add 'Open with Code' action to Windows Explorer file context menu"**.
    *   **"Add 'Open with Code' action to Windows Explorer directory context menu"**.
    *   Opsi ini akan memudahkan Anda membuka *folder* proyek langsung di VS Code hanya dengan klik kanan pada *folder* tersebut.
*   Lanjutkan proses instalasi hingga selesai.

## 3. Konfigurasi VS Code untuk Pengembangan Python

### Membuat Ruang Kerja (Workspace)
*   Buka VS Code dan buat *folder* kerja baru di lokasi yang mudah diakses (misalnya, `C:\Users\NamaUser\Latihan`).
*   Pilih "File" > "Open Folder" dan navigasikan ke *folder* yang baru dibuat.
*   Konfirmasi "Trust the authors" untuk *workspace* yang baru dibuka.

### Pengaturan Kustom VS Code (`settings.json`)
*   Di dalam *folder* kerja Anda, buat *folder* baru bernama `.vscode`.
*   Di dalam *folder* `.vscode`, buat *file* bernama `settings.json`.
*   *File* ini digunakan untuk menyimpan pengaturan khusus untuk *workspace* Anda, memungkinkan Anda memiliki pengaturan yang berbeda untuk setiap proyek.
*   Beberapa pengaturan yang dapat disesuaikan di `settings.json` meliputi:
    *   `"window.zoomLevel": 1` (untuk memperbesar tampilan antarmuka pengguna VS Code).
    *   `"editor.fontSize": 18` (untuk memperbesar ukuran *font* kode agar lebih mudah dibaca).
    *   `"workbench.colorTheme": "Noctis Minimus"` (untuk mengganti tema warna editor).
    *   `"workbench.iconTheme": "vscode-icons"` (untuk mengganti tema ikon *file* dan *folder*).
*   **Menginstal Tema dan Ikon**: Tema dan ikon dapat diinstal melalui menu **Extensions** di VS Code. Contoh tema yang digunakan dalam video adalah **Noctis Minimus** dan tema ikon **VSCode Icons**.

### Instalasi Ekstensi Python di VS Code
*   Buat *file* baru bernama `main.py` di *folder* kerja Anda.
*   VS Code biasanya akan secara otomatis merekomendasikan instalasi **Ekstensi Python** dari Microsoft.
*   Jika rekomendasi tidak muncul, buka menu **Extensions** (ikon kotak-kotak di sisi kiri bilah aktivitas), cari "Python", dan instal ekstensi resmi dari Microsoft.
*   Ekstensi ini sangat penting untuk mengaktifkan fitur-fitur seperti *IntelliSense* (pelengkapan otomatis kode), *linting* (pemeriksaan kesalahan kode secara *real-time*), dan *debugging*.

## 4. Menjalankan Program Python Pertama (Hello World)

*   Setelah semua instalasi dan konfigurasi selesai, buka *file* `main.py` yang telah Anda buat.
*   Ketik kode Python sederhana berikut ini:
    ```python
    print("Hello World")
    ```
*   Simpan *file* (`Ctrl+S`).
*   Jalankan program dengan mengklik tombol **Run** (ikon segitiga hijau) yang terletak di pojok kanan atas editor VS Code.
*   Jika di terminal bawah VS Code muncul teks "Hello World", berarti instalasi dan *setup* lingkungan pengembangan Anda telah berhasil sepenuhnya.

## 5. Ringkasan Poin Penting

*   **Add Python to PATH**: Opsi ini wajib dicentang saat instalasi Python di Windows untuk memungkinkan akses Python dari *command line* atau terminal.
*   **Disable Path Length Limit**: Disarankan untuk diklik setelah instalasi Python selesai guna mendukung penanganan jalur *file* yang panjang dalam proyek *coding*.
*   **Verifikasi Instalasi**: Gunakan perintah `python --version` di CMD/Terminal untuk memastikan Python terinstal dengan benar dan dapat diakses.
*   **Ekstensi Python di VS Code**: Penting untuk diinstal di VS Code agar fitur-fitur bantuan *coding* Python (seperti *IntelliSense*, *linting*, *debugging*) dapat berfungsi optimal dan meningkatkan produktivitas.
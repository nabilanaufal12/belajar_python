# Panduan Instalasi Python dan Visual Studio Code di macOS

Panduan ini merangkum langkah-langkah instalasi Python dan Visual Studio Code (VS Code) di sistem operasi macOS, dengan fokus pada praktik terbaik untuk menghindari konflik dengan Python bawaan sistem.

## Pendahuluan: Mengapa Instalasi Python di macOS Berbeda?

macOS, terutama versi Catalina ke atas, sudah dilengkapi dengan instalasi Python bawaan (versi 2.7 atau 3.x lama) yang digunakan oleh sistem operasi itu sendiri. Sangat **tidak disarankan** untuk menggunakan atau mengotak-atik Python bawaan ini untuk pengembangan pribadi, karena menginstal *package* tambahan dapat mengganggu stabilitas sistem Mac. Oleh karena itu, diperlukan instalasi Python terpisah yang aman dan terisolasi.

Untuk mengatasi masalah ini, kita akan menggunakan **pyenv**, sebuah alat yang memungkinkan pengelolaan berbagai versi Python secara aman tanpa mengganggu sistem.

## Langkah-langkah Instalasi

### 1. Instalasi Homebrew

**Homebrew** adalah *package manager* yang mempermudah instalasi perangkat lunak di macOS.

*   **Cara Instalasi**:
    1.  Buka situs web resmi Homebrew (brew.sh).
    2.  Salin skrip instalasi yang tersedia di halaman utama.
    3.  Buka aplikasi Terminal di macOS Anda.
    4.  Tempel skrip yang sudah disalin ke Terminal, lalu tekan `Enter`. Tunggu hingga proses instalasi selesai.
*   **Verifikasi Instalasi**: Setelah selesai, ketik `brew --version` di Terminal untuk memastikan Homebrew terinstal dengan benar.

### 2. Instalasi pyenv

**pyenv** adalah alat penting untuk mengelola berbagai versi Python di satu mesin, memungkinkan Anda beralih antar versi dengan mudah.

*   **Cara Instalasi**:
    1.  Di Terminal, ketik perintah berikut:
        ```bash
        brew install pyenv
        ```
    2.  Tekan `Enter` dan tunggu proses instalasi selesai.
*   **Verifikasi Instalasi**: Ketik `pyenv --version` untuk memeriksa versi pyenv yang terinstal.
*   **Melihat Versi Python Bawaan**: Anda dapat melihat versi Python bawaan sistem dengan `python --version` atau `python3 --version`.

### 3. Menginstal Python Terbaru dengan pyenv

Setelah pyenv terinstal, Anda bisa menggunakannya untuk menginstal versi Python yang diinginkan.

*   **Melihat Daftar Versi (Opsional)**: Untuk melihat daftar semua versi Python yang tersedia untuk diinstal melalui pyenv, gunakan perintah:
    ```bash
    pyenv install --list
    ```
*   **Menginstal Versi Spesifik**: Untuk menginstal versi Python tertentu (misalnya, 3.8.2 seperti yang dicontohkan), gunakan perintah:
    ```bash
    pyenv install 3.8.2
    ```
    Proses ini akan mengunduh dan menginstal Python versi tersebut.
*   **Melihat Versi Python yang Terinstal via pyenv**: Setelah instalasi, Anda bisa melihat semua versi Python yang dikelola oleh pyenv dengan:
    ```bash
    pyenv versions
    ```

### 4. Konfigurasi Shell untuk pyenv (PENTING)

Meskipun Python sudah diinstal melalui pyenv, Terminal macOS mungkin masih menggunakan Python bawaan sistem. Langkah ini memastikan Terminal menggunakan versi Python yang dikelola oleh pyenv.

*   **Mengatur Versi Global**: Tetapkan versi Python yang baru diinstal sebagai versi global yang akan digunakan oleh Terminal:
    ```bash
    pyenv global 3.8.2
    ```
*   **Mengedit File Konfigurasi Shell**:
    1.  Identifikasi *shell* yang Anda gunakan:
        *   Jika menggunakan **ZSH** (default untuk macOS baru), Anda perlu mengedit file `.zshrc`.
        *   Jika menggunakan **Bash** (macOS lama), Anda perlu mengedit file `.bash_profile`.
    2.  Buka file konfigurasi menggunakan editor `nano`:
        *   Untuk ZSH: `nano ~/.zshrc`
        *   Untuk Bash: `nano ~/.bash_profile`
    3.  Tambahkan baris berikut di bagian paling bawah file:
        ```bash
        eval "$(pyenv init -)"
        ```
    4.  Simpan perubahan dengan menekan `Ctrl+X`, lalu `Y` (untuk Yes), dan `Enter`.
*   **Restart Terminal**: Tutup dan buka kembali aplikasi Terminal Anda agar perubahan konfigurasi diterapkan.
*   **Verifikasi**: Setelah Terminal di-restart, ketik `python3 --version`. Outputnya seharusnya menunjukkan versi Python yang Anda instal melalui pyenv (misalnya, 3.8.2), bukan versi bawaan sistem.

### 5. Instalasi Visual Studio Code

Visual Studio Code (VS Code) adalah editor kode populer yang akan digunakan untuk menulis program Python.

*   **Cara Instalasi**:
    1.  Unduh VS Code untuk macOS dari situs web resminya.
    2.  Ekstrak file `.zip` yang diunduh.
    3.  Pindahkan aplikasi `Visual Studio Code` ke folder **Applications** Anda.
    4.  Buka aplikasi VS Code.

### 6. Setup Proyek dan Ekstensi VS Code

*   **Membuka Folder Proyek**:
    1.  Di VS Code, pilih `File > Open Folder...` atau `Open...`.
    2.  Buat folder baru untuk proyek Python Anda (misalnya, `Tutorial Python`) dan buka folder tersebut.
*   **Membuat File Python**:
    1.  Di dalam folder proyek, buat file baru dengan nama `main.py`.
*   **Menginstal Ekstensi Python**:
    1.  VS Code biasanya akan merekomendasikan instalasi ekstensi Python secara otomatis saat Anda membuka file `.py`. Klik `Install`.
    2.  Jika tidak, Anda bisa mencarinya secara manual di panel Extensions (ikon kotak di sidebar kiri) dengan mencari "Python" oleh Microsoft.
    3.  Ekstensi Python menyediakan fitur-fitur penting seperti *linting* (pemeriksaan sintaks), *debugging*, IntelliSense (pelengkapan kode), dukungan Jupyter Notebook, dan *code formatting*.
    4.  Setelah instalasi, **Reload Window** VS Code jika diminta.

### 7. Konfigurasi Tampilan VS Code (Opsional)

Untuk meningkatkan pengalaman coding, Anda dapat menginstal ekstensi tema dan ikon, serta menyesuaikan pengaturan tampilan.

*   **Ekstensi Ikon**: Instal ekstensi `VSCode Icons` untuk tampilan ikon file yang lebih informatif.
*   **Ekstensi Tema**: Instal ekstensi tema `Noctis` (disarankan `Noctis Minimus`) untuk skema warna yang nyaman.
*   **Pengaturan Workspace**: Untuk menyimpan konfigurasi khusus proyek (seperti ukuran *font* atau *zoom level*), buat folder `.vscode` di dalam folder proyek Anda, lalu di dalamnya buat file `settings.json`.
    *   Contoh konfigurasi di `settings.json`:
        ```json
        {
            "window.zoomLevel": 1, // Memperbesar tampilan keseluruhan
            "editor.fontSize": 24, // Ukuran font editor
            "terminal.integrated.fontSize": 20, // Ukuran font terminal terintegrasi
            "workbench.colorTheme": "Noctis Minimus", // Tema warna
            "workbench.iconTheme": "vscode-icons" // Tema ikon
        }
        ```

### 8. Menguji Instalasi ("Hello World")

Untuk memastikan semua instalasi berhasil, buat program Python sederhana.

*   **Menulis Kode**: Di file `main.py`, tulis kode berikut:
    ```python
    print("Halo Dunia!")
    ```
*   **Menjalankan Kode**:
    1.  Simpan file (`Cmd+S`).
    2.  Klik tombol **Run Python File** (ikon segitiga hijau di pojok kanan atas editor).
    3.  Periksa output di panel Terminal di bagian bawah VS Code. Jika Anda melihat "Halo Dunia!", berarti instalasi Anda sukses.

Metode instalasi ini, meskipun sedikit lebih rumit di bagian konfigurasi Terminal dengan `pyenv`, merupakan **praktik terbaik** untuk menjaga sistem macOS Anda tetap bersih dan aman dari konflik versi Python.
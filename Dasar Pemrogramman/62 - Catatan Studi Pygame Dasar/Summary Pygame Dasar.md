# Catatan Studi Pygame Dasar

## Pengantar Pygame

**Pygame** adalah sebuah *library* atau *package* Python yang bersifat *cross-platform*, dirancang khusus untuk pengembangan game. Dengan Pygame, pengguna dapat membuat berbagai jenis game menggunakan bahasa pemrograman Python.

### Instalasi Pygame

Sebelum memulai, Pygame perlu diinstal menggunakan *package manager* `pip`:
```bash
pip install pygame
```

## Struktur Dasar Game Loop

Setiap game, terlepas dari kompleksitasnya, umumnya mengikuti struktur dasar yang terdiri dari empat langkah utama dalam sebuah *loop* yang terus berjalan:

1.  **Inisialisasi (Init)**: Proses pengaturan awal seperti memulai *engine* game, menyiapkan jendela tampilan, dan mendeklarasikan variabel-variabel penting.
2.  **Input Pengguna (User Input)**: Mengambil masukan dari pengguna melalui perangkat seperti keyboard, mouse, atau *joystick*. Ini juga bisa mencakup pengambilan data dari sumber lain seperti database.
3.  **Pembaruan Aset (Update Asset)**: Memperbarui logika game, posisi objek, status karakter, atau aset dinamis lainnya berdasarkan input pengguna atau aturan game. Ini bisa termasuk perubahan posisi, animasi, atau interaksi antar objek.
4.  **Render ke Layar (Render to Display)**: Menggambar ulang semua elemen game (objek, latar belakang, teks) ke layar. Langkah ini adalah yang paling berat dan menentukan *frame rate* (FPS) game.

**Perbandingan Loading Game (PC vs. Mobile)**:
Proses inisialisasi ini sangat memengaruhi waktu *loading* game. Game mobile cenderung lebih cepat *loading* karena menggunakan *flash storage* (SSD) dan aset yang lebih kecil. Sebaliknya, game PC dengan aset grafis yang besar membutuhkan waktu inisialisasi yang lebih lama, menyebabkan *loading* yang lebih panjang.

## Implementasi Pygame

Berikut adalah langkah-langkah untuk membuat game sederhana menggunakan Pygame, mengikuti struktur *game loop* di atas:

### 1. Inisialisasi Pygame dan Jendela Tampilan

Pertama, inisialisasi Pygame dan buat jendela tampilan (display surface) tempat semua elemen game akan digambar.

*   **Inisialisasi Engine**:
    `pygame.init()` digunakan untuk memulai semua modul Pygame yang diperlukan. Ini adalah langkah pertama yang harus dilakukan.
*   **Membuat Jendela Game**:
    `pygame.display.set_mode((lebar, panjang))` membuat jendela dengan ukuran yang ditentukan. Jendela ini akan menjadi "kanvas" tempat game berjalan.
    ```python
    import pygame

    pygame.init() # Inisialisasi Pygame

    window_lebar = 500
    window_panjang = 500
    window = pygame.display.set_mode((window_lebar, window_panjang))
    ```

### 2. Game Loop dan Penanganan Event

Game akan berjalan dalam sebuah *loop* tak terbatas (`while isRun`). Di dalam *loop* ini, semua event (kejadian) yang terjadi di jendela game harus ditangani.

*   **Variabel `isRun`**:
    Variabel boolean `isRun` digunakan untuk mengontrol apakah *game loop* harus terus berjalan atau berhenti. Awalnya diatur ke `True`.
*   **Penanganan Event `QUIT`**:
    Penting untuk menangkap event `pygame.QUIT` agar game dapat ditutup dengan benar saat pengguna mengklik tombol tutup jendela. Jika tidak ditangani, jendela game mungkin tidak bisa ditutup atau program akan *crash*.
    ```python
    isRun = True
    while isRun:
        for event in pygame.event.get(): # Ambil semua event
            if event.type == pygame.QUIT: # Jika event adalah QUIT
                isRun = False # Hentikan loop
    ```
*   **Mengakhiri Pygame**:
    Setelah *loop* berakhir, `pygame.quit()` dipanggil untuk menghentikan semua modul Pygame dan membersihkan sumber daya.

### 3. Menggambar Objek dan Latar Belakang

Di dalam *game loop*, objek-objek game digambar dan latar belakang diisi ulang.

*   **Mengisi Latar Belakang**:
    `window.fill((R, G, B))` digunakan untuk mengisi seluruh jendela dengan warna tertentu. Ini harus dilakukan di setiap *frame* untuk menghapus jejak objek dari *frame* sebelumnya.
    *   Warna hitam: `(0, 0, 0)`
    *   Warna putih: `(255, 255, 255)`
*   **Menggambar Persegi**:
    `pygame.draw.rect(surface, color, (x, y, lebar, panjang))` digunakan untuk menggambar persegi panjang.
    *   `surface`: Jendela tempat objek akan digambar (misalnya `window`).
    *   `color`: Warna objek dalam format RGB (misalnya `(255, 120, 0)` untuk oranye).
    *   `(x, y, lebar, panjang)`: Posisi dan ukuran objek. Koordinat `(0,0)` berada di pojok kiri atas jendela. Nilai X bertambah ke kanan, dan nilai Y bertambah ke bawah.
    ```python
    # Setup Object Game (Kotak)
    x = 250
    y = 250
    lebar_kotak = 20
    panjang_kotak = 20
    speed = 5

    # ... dalam game loop ...
    window.fill((255, 255, 255)) # Latar belakang putih
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar_kotak, panjang_kotak)) # Gambar kotak oranye
    ```

### 4. Input Keyboard dan Pergerakan Objek

Untuk membuat objek bergerak, kita perlu mendeteksi tombol keyboard yang ditekan dan memperbarui posisi objek.

*   **Mendeteksi Tombol Ditekan**:
    `pygame.key.get_pressed()` mengembalikan sebuah *dictionary* yang berisi status semua tombol keyboard. `keys[pygame.K_LEFT]` akan bernilai `True` jika tombol panah kiri ditekan.
*   **Memperbarui Posisi**:
    Jika tombol panah ditekan, koordinat `x` atau `y` objek diperbarui sesuai dengan `speed` yang ditentukan.
    *   Kiri: `x -= speed`
    *   Kanan: `x += speed`
    *   Atas: `y -= speed`
    *   Bawah: `y += speed`
*   **Batasan Layar**:
    Penting untuk menambahkan kondisi agar objek tidak keluar dari batas jendela.
    *   Kiri: `x > 0`
    *   Kanan: `x < window_lebar - lebar_kotak`
    *   Atas: `y > 0`
    *   Bawah: `y < window_panjang - panjang_kotak`
    ```python
    # ... dalam game loop, setelah event loop ...
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar_kotak:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < window_panjang - panjang_kotak:
        y += speed
    ```

### 5. Memperbarui Tampilan (Display Update)

Setelah semua objek digambar dan posisi diperbarui, tampilan harus diperbarui agar perubahan terlihat di layar.

*   **`pygame.display.update()`**:
    Fungsi ini sangat penting karena ia akan menampilkan semua yang telah digambar ke jendela. Tanpa ini, perubahan tidak akan terlihat.
*   **Kontrol Kecepatan (Delay)**:
    `pygame.time.delay(milidetik)` dapat digunakan untuk menambahkan jeda antar *frame*, mengontrol kecepatan game agar tidak terlalu cepat.
    ```python
    # ... dalam game loop, setelah menggambar objek ...
    pygame.display.update()
    pygame.time.delay(10) # Jeda 10 milidetik
    ```

## Kesimpulan

Dengan sekitar 60 baris kode, kita dapat membuat jendela game dengan objek yang dapat digerakkan menggunakan Pygame. Struktur `Input -> Update -> Render` adalah fundamental dalam pengembangan game apa pun. Konsep ini dapat dikembangkan lebih lanjut untuk membuat game yang lebih kompleks, seperti game Snake.
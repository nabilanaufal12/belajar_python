# Algoritma Pencarian: Simple Search dan Binary Search

Video ini membahas konsep dasar algoritma, khususnya masalah pencarian, serta memperkenalkan dua algoritma pencarian utama: **Simple Search** dan **Binary Search**. Materi ini juga menekankan pentingnya memahami *running time* algoritma, yang sering diukur menggunakan notasi Big O dan konsep logaritma.

## 1. Pengantar Algoritma

*   **Definisi Algoritma**: Algoritma adalah sekumpulan instruksi yang terdefinisi dengan baik untuk menyelesaikan suatu tugas atau masalah tertentu.
*   **Pentingnya Algoritma**: Algoritma yang dibahas dalam buku ini dipilih karena alasan seperti kecepatan, kemampuannya menyelesaikan masalah yang menarik, atau kombinasi keduanya.
*   **Implementasi**: Implementasi algoritma populer seringkali sudah tersedia dalam berbagai bahasa pemrograman (misalnya Python, Java, C++). Namun, penting untuk memahami *trade-off* atau perbandingan kelebihan dan kekurangan antar algoritma agar implementasinya tidak "percuma" atau *useless*.
*   **Running Time**: Memahami *running time* suatu algoritma, yang dikenal juga dengan istilah Big O Notation, adalah fondasi penting dalam studi algoritma.

## 2. Masalah Pencarian (Search Problem)

Masalah pencarian adalah tugas menemukan elemen tertentu dalam suatu koleksi data. Dua studi kasus digunakan untuk mengilustrasikan masalah ini:

*   **Mencari Kata dalam Kamus**: Jika mencari kata yang diawali dengan huruf 'K' dalam kamus, kita cenderung memulai pencarian dari bagian tengah kamus karena kamus terurut secara alfabetis.
*   **Menebak Angka**: Menebak angka antara 1 sampai 100 dengan jumlah tebakan sesedikit mungkin. Setiap tebakan akan diberikan *feedback* apakah terlalu kecil (*too low*), terlalu tinggi (*too high*), atau tepat.

## 3. Simple Search (Pencarian Sederhana)

*   **Mekanisme**: Simple Search bekerja dengan memeriksa setiap elemen secara sekuensial, mulai dari elemen pertama, hingga elemen yang dicari ditemukan.
    *   Contoh: Untuk menebak angka, kita akan mencoba 1, lalu 2, lalu 3, dan seterusnya.
*   **Karakteristik**:
    *   Setiap tebakan atau pengecekan hanya mengeliminasi satu kemungkinan angka.
    *   Algoritma ini disebut sebagai *stupid search* karena proses pencariannya sangat trivial atau "bodoh".
*   **Performa (Worst Case)**:
    *   Untuk mencari angka 99 dari rentang 1-100, Simple Search membutuhkan 99 tebakan.
    *   Untuk mencari kata dalam kamus berisi 240.000 kata, dalam skenario terburuk (kata yang dicari adalah yang terakhir), Simple Search membutuhkan 240.000 langkah.
    *   Secara umum, untuk *n* elemen, Simple Search membutuhkan *n* langkah dalam kondisi terburuk ($O(n)$).

## 4. Binary Search (Pencarian Biner)

*   **Definisi**: Binary Search adalah algoritma yang menerima *list* elemen yang **terurut** sebagai *input*. Jika elemen yang dicari ada, algoritma akan mengembalikan posisinya; jika tidak, ia akan mengembalikan nilai *null*.
*   **Mekanisme**:
    *   Algoritma ini selalu menebak angka di posisi tengah (*middle element*) dari rentang pencarian yang sedang aktif.
    *   Setiap tebakan berhasil mengeliminasi setengah dari sisa angka yang mungkin.
    *   Contoh: Jika menebak 50 (dari 1-100) dan hasilnya *too low*, maka 50 angka pertama (1-50) langsung tereliminasi.
*   **Performa (Worst Case)**:
    *   Untuk 100 angka, Binary Search membutuhkan maksimum 7 tebakan.
    *   Untuk kamus berisi 240.000 kata, Binary Search membutuhkan maksimum 18 langkah.
    *   Secara umum, untuk *n* elemen, Binary Search membutuhkan $\log_2 n$ langkah dalam kondisi terburuk ($O(\log n)$).
*   **Prasyarat Penting**: Binary Search **hanya berfungsi** ketika *list* atau data yang dicari sudah **terurut** (*sorted order*). Contohnya adalah daftar nama di buku telepon atau kata-kata dalam kamus.

## 5. Logaritma ($\log$)

*   **Definisi**: Logaritma adalah kebalikan dari pemangkatan (eksponensial).
*   **Contoh**:
    *   $10^2 = 100 \implies \log_{10} 100 = 2$
    *   $2^3 = 8 \implies \log_2 8 = 3$
    *   $2^4 = 16 \implies \log_2 16 = 4$
*   **Konvensi dalam Buku**: Ketika membahas *running time* dan Big O notation, ekspresi "log" selalu mengacu pada $\log_2$ (logaritma basis 2).
*   **Aplikasi pada Binary Search**:
    *   Untuk 8 elemen, Binary Search membutuhkan $\log_2 8 = 3$ pengecekan.
    *   Untuk 1024 elemen, Binary Search membutuhkan $\log_2 1024 = 10$ pengecekan. Ini jauh lebih efisien dibandingkan Simple Search yang membutuhkan 1024 pengecekan untuk kasus yang sama.

## 6. Implementasi Binary Search (Konseptual dalam Python)

Implementasi Binary Search melibatkan beberapa langkah kunci:

*   **Struktur Data**: Menggunakan *list* Python (yang berfungsi seperti *array* terurut) untuk menampung elemen.
*   **Indeks**: Elemen dalam *list* diindeks mulai dari 0 (indeks pertama adalah 0, kedua adalah 1, dan seterusnya).
*   **Fungsi `binary_search`**:
    *   Menerima dua parameter: `sorted_list` (list yang sudah terurut) dan `item` yang ingin dicari.
    *   Mengembalikan posisi `item` jika ditemukan, atau *null* jika tidak.
*   **Variabel Pelacak Rentang**:
    *   `low_index`: Indeks awal rentang pencarian (awalnya 0).
    *   `high_index`: Indeks akhir rentang pencarian (awalnya `len(list) - 1`).
*   **Proses Iteratif**:
    *   Dalam setiap iterasi, `mid_index` dihitung sebagai `(low_index + high_index) / 2`.
    *   `guess` adalah elemen pada `list[mid_index]`.
    *   **Perbandingan**:
        *   Jika `guess` terlalu kecil (*too low*) dari `item`, perbarui `low_index = mid_index + 1`.
        *   Jika `guess` terlalu besar (*too high*) dari `item`, perbarui `high_index = mid_index - 1`.
        *   Jika `guess` sama dengan `item`, kembalikan `mid_index` (item ditemukan).
    *   **Pembulatan**: Nilai `mid` akan otomatis dibulatkan ke bawah (*floor*) jika hasil penjumlahan `low` dan `high` bukan bilangan genap. (Perlu diperhatikan bahwa implementasi Python 3 memiliki karakteristik pembagian integer yang berbeda dari Python 2).
*   **Kondisi Berhenti**: Proses berlanjut selama `low_index <= high_index`. Jika `low_index` melebihi `high_index`, berarti `item` tidak ditemukan, dan fungsi akan mengembalikan *null*.
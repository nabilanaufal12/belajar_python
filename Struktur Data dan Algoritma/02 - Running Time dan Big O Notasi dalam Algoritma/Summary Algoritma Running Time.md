# Running Time dan Big O Notasi dalam Algoritma

## Pengantar Efisiensi Algoritma

Dalam pengembangan perangkat lunak, seringkali dihadapkan pada kebutuhan untuk memilih algoritma yang paling efisien. Efisiensi algoritma dioptimalkan dari segi waktu (running time) dan ruang (space). Memahami seberapa cepat suatu algoritma berjalan sangat penting, terutama ketika menggunakan algoritma yang dibuat oleh orang lain.

### Perbandingan Awal: Simple Search vs. Binary Search

Sebagai contoh, mari kita bandingkan dua algoritma pencarian:

*   **Simple Search (Pencarian Sederhana)**:
    *   Melakukan pengecekan satu per satu pada setiap elemen dalam daftar.
    *   Jika ada 100 elemen, dibutuhkan 100 pengecekan. Jika ada 4 miliar elemen, dibutuhkan 4 miliar pengecekan.
    *   Jumlah pengecekan maksimum sama dengan ukuran daftar (N).
    *   Disebut sebagai **linear time**.

*   **Binary Search (Pencarian Biner)**:
    *   Menggunakan pendekatan logaritmik, membagi daftar menjadi dua di setiap langkah.
    *   Jika ada 100 elemen, dibutuhkan paling banyak 7 pengecekan. Jika ada 4 miliar elemen, dibutuhkan paling banyak 32 pengecekan.
    *   Disebut sebagai **logarithmic time** atau **log time**.

| Algoritma      | Jumlah Item | Jumlah Tebakan (Pengecekan) | Tipe Waktu Berjalan |
| :------------- | :---------- | :-------------------------- | :------------------ |
| Simple Search  | 100         | 100                         | Linear Time         |
| Binary Search  | 100         | 7                           | Logarithmic Time    |
| Simple Search  | 4 Miliar    | 4 Miliar                    | Linear Time         |
| Binary Search  | 4 Miliar    | 32                          | Logarithmic Time    |

## Big O Notasi: Definisi dan Kegunaan

**Big O Notasi** ($O$) adalah notasi khusus yang digunakan untuk mendeskripsikan seberapa cepat suatu algoritma.

### Apa yang Diukur Big O Notasi?

*   Big O Notasi **tidak mengukur kecepatan algoritma dalam satuan detik**.
*   Sebaliknya, Big O Notasi mengukur **jumlah operasi** yang dilakukan algoritma.
*   Fokus utamanya adalah bagaimana **waktu berjalan (running time) algoritma meningkat seiring dengan peningkatan ukuran input** ($N$). Ini memungkinkan perbandingan algoritma secara relevan.
*   Bentuk umum penulisan Big O Notasi adalah $O(\text{jumlah operasi})$.

### Contoh Notasi Big O

*   **Simple Search**: Membutuhkan $N$ operasi untuk daftar berukuran $N$. Notasinya adalah $O(N)$ (linear time).
*   **Binary Search**: Membutuhkan $\log N$ operasi untuk daftar berukuran $N$. Notasinya adalah $O(\log N)$ (logarithmic time).

## Studi Kasus: Algoritma Bob untuk NASA

Seorang programmer bernama Bob diminta menulis algoritma untuk pendaratan roket NASA di bulan. Algoritma harus cepat dan akurat, dengan batas waktu 10 detik.

*   **Pilihan Algoritma**: Bob dihadapkan pada Simple Search (lebih mudah ditulis, minim *bug*) dan Binary Search (lebih cepat).
*   **Asumsi**: Setiap pengecekan membutuhkan 1 milidetik.

### Perhitungan Awal (100 Elemen)

*   **Simple Search**: 100 elemen $\rightarrow$ 100 pengecekan $\rightarrow$ 100 milidetik.
*   **Binary Search**: 100 elemen $\rightarrow$ 7 pengecekan $\rightarrow$ 7 milidetik.
    *   Pada skala ini, Binary Search sekitar 15 kali lebih cepat dari Simple Search.

### Perhitungan Realistis (1 Miliar Elemen)

Secara realistis, jumlah elemen yang perlu dicari bisa mencapai 1 miliar.

*   **Binary Search**: $\log_2(1 \text{ miliar}) \approx 30$ pengecekan $\rightarrow$ 30 milidetik.
*   **Kesalahan Bob**: Bob awalnya berasumsi bahwa jika Binary Search 15 kali lebih cepat, maka Simple Search untuk 1 miliar elemen akan memakan waktu $30 \text{ ms} \times 15 = 450 \text{ ms}$. Angka ini masih di bawah ambang batas 10 detik, sehingga Bob memutuskan menggunakan Simple Search.
*   **Kenyataan**: Bob membuat keputusan yang salah. Simple Search untuk 1 miliar elemen akan membutuhkan 1 miliar milidetik, yang setara dengan **11 hari**.

### Mengapa Bob Salah?

*   Waktu berjalan Binary Search dan Simple Search **tidak tumbuh pada laju yang sama** (*don't grow at the same rate*).
*   Perbedaan kecepatan menjadi sangat signifikan seiring dengan peningkatan jumlah elemen:
    *   **100 elemen**: Simple Search (100 ms), Binary Search (7 ms) $\rightarrow$ Binary Search $\approx$ 15x lebih cepat.
    *   **10.000 elemen**: Simple Search (10 detik), Binary Search (14 ms) $\rightarrow$ Binary Search jauh lebih cepat.
    *   **1 miliar elemen**: Simple Search (11 hari), Binary Search (32 ms) $\rightarrow$ Binary Search jauh lebih cepat.

Oleh karena itu, tidak cukup hanya mengetahui berapa lama suatu algoritma berjalan. Penting untuk memahami **bagaimana waktu berjalannya meningkat seiring dengan peningkatan ukuran input**. Di sinilah Big O Notasi menjadi sangat relevan.

## Big O Notasi: Skenario Terburuk (Worst-Case Scenario)

Big O Notasi selalu menggambarkan **skenario terburuk** (*worst-case scenario*) dari suatu algoritma.

*   **Contoh**: Mencari "Adit" di buku telepon menggunakan Simple Search.
    *   Jika "Adit" adalah entri pertama, algoritma hanya membutuhkan 1 operasi.
    *   Namun, Simple Search tetap dinotasikan sebagai $O(N)$ karena Big O berfokus pada skenario terburuk, di mana "Adit" mungkin berada di akhir daftar atau tidak ada sama sekali.
*   Ini memberikan jaminan bahwa Simple Search tidak akan pernah lebih lambat dari $O(N)$.

## Visualisasi Big O Notasi

Mari kita visualisasikan perbedaan waktu berjalan dengan contoh sederhana: menggambar 16 kotak. Asumsikan 10 operasi dapat dilakukan dalam 1 detik.

1.  **Algoritma 1 ($O(N)$ - Linear Time)**: Menggambar satu kotak per satu.
    *   Untuk 16 kotak: 16 operasi $\rightarrow 1.6$ detik.
    *   Untuk 1024 kotak: 1024 operasi $\rightarrow 102.4$ detik.

2.  **Algoritma 2 ($O(\log N)$ - Logarithmic Time)**: Melipat kertas untuk membuat kotak. Setiap lipatan menggandakan jumlah kotak.
    *   Untuk 16 kotak: $\log_2 16 = 4$ operasi $\rightarrow 0.4$ detik.
    *   Untuk 1024 kotak: $\log_2 1024 = 10$ operasi $\rightarrow 1$ detik.

Grafik berikut mengilustrasikan bagaimana jumlah operasi (sumbu Y) meningkat seiring dengan jumlah elemen (sumbu X) untuk berbagai notasi Big O:

| Notasi Big O | Waktu untuk 16 Elemen | Waktu untuk 1024 Elemen |
| :----------- | :-------------------- | :---------------------- |
| $O(\log N)$  | 0.4 detik             | 1 detik                 |
| $O(N)$       | 1.6 detik             | 102.4 detik             |
| $O(N \log N)$| 6.4 detik             | 1024 detik              |
| $O(N^2)$     | 25.6 detik            | 104857.6 detik          |
| $O(N!)$      | 66371 detik           | (Sangat besar)          |

Terlihat jelas bahwa perbedaan waktu berjalan menjadi sangat ekstrem seiring dengan bertambahnya jumlah elemen. Meskipun ada lebih banyak notasi Big O, kelima notasi ini adalah yang paling umum ditemui, dan grafik di atas adalah penyederhanaan untuk memudahkan pemahaman.

## Jenis-jenis Umum Big O Notasi

Berikut adalah daftar notasi Big O yang umum, diurutkan dari yang tercepat hingga terlambat:

1.  **$O(\log N)$ (Logarithmic Time)**:
    *   Tercepat.
    *   Contoh: Binary Search.
2.  **$O(N)$ (Linear Time)**:
    *   Contoh: Simple Search.
3.  **$O(N \log N)$**:
    *   Contoh: Quicksort.
4.  **$O(N^2)$ (Quadratic Time)**:
    *   Contoh: Selection Sort.
5.  **$O(N!)$ (Factorial Time)**:
    *   Terlambat.
    *   Contoh: Traveling Salesperson Problem.

## Ringkasan

*   Kecepatan algoritma tidak diukur dalam detik, melainkan berdasarkan **pertumbuhan jumlah operasinya** (*the growth of the number of operations*).
*   Big O Notasi menjelaskan seberapa cepat waktu berjalan algoritma meningkat seiring dengan bertambahnya ukuran input.
*   $O(\log N)$ lebih cepat daripada $O(N)$, dan perbedaan kecepatan ini akan semakin signifikan seiring dengan peningkatan jumlah item.
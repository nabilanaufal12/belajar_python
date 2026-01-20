# Summary Operasi List Python

> Generated: January 20th, 2026 2:13 PM
> Sources: Belajar Python [Dasar] - 31 - Operasi List.youtube, pasted-text-1.md

---

# Operasi Dasar List pada Python

List adalah salah satu struktur data fundamental di Python yang memungkinkan penyimpanan koleksi item. Python menyediakan berbagai operasi bawaan untuk memanipulasi list secara efisien. Catatan ini akan membahas beberapa operasi dasar yang sering digunakan, yaitu menghitung kemunculan elemen, mencari indeks, mengurutkan, dan membalik urutan list.

## 1. Menghitung Kemunculan Elemen (`.count()`)

Metode `.count()` digunakan untuk menghitung berapa kali suatu elemen spesifik muncul dalam sebuah list. Ini sangat berguna untuk analisis statistik sederhana pada data dalam list.

*   **Fungsi**: Mengembalikan jumlah kemunculan elemen yang dicari dalam list.
*   **Sintaks**: `list_anda.count(elemen_yang_dicari)`
*   **Contoh**:
    ```python
    data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]

    jumlah_data_4 = data_angka.count(4) # Menghitung angka 4
    jumlah_data_3 = data_angka.count(3) # Menghitung angka 3

    print(f"jumlah angka 4 = {jumlah_data_4}") # Output: jumlah angka 4 = 2
    print(f"jumlah angka 3 = {jumlah_data_3}") # Output: jumlah angka 3 = 3
    ```

## 2. Mencari Indeks Elemen (`.index()`)

Metode `.index()` digunakan untuk menemukan posisi (indeks) pertama dari suatu elemen dalam list. Indeks dimulai dari 0 untuk elemen pertama.

*   **Fungsi**: Mengembalikan indeks dari kemunculan pertama elemen yang dicari.
*   **Sintaks**: `list_anda.index(elemen_yang_dicari)`
*   **Contoh**:
    ```python
    data = ["Ucup", "Otong", "Dudung", "Ujang"]

    index_dudung = data.index("Dudung")
    index_ujang = data.index("Ujang")

    print(f"index si Dudung = {index_dudung}") # Output: index si Dudung = 2
    print(f"index si Ujang = {index_ujang}")   # Output: index si Ujang = 3
    ```
*   **Penting**: Jika elemen yang dicari tidak ada dalam list, metode ini akan menimbulkan `ValueError`.

## 3. Mengurutkan List (`.sort()`)

Metode `.sort()` digunakan untuk mengurutkan elemen-elemen dalam list secara *in-place*, yang berarti list asli akan diubah secara permanen.

*   **Fungsi**: Mengurutkan elemen list. Untuk angka, diurutkan dari terkecil ke terbesar. Untuk string, diurutkan secara alfabetis (A-Z).
*   **Sintaks**: `list_anda.sort()`
*   **Contoh**:
    ```python
    # Mengurutkan Angka
    data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
    print(f"data angka sebelum sort = \n{data_angka}")
    data_angka.sort()
    print(f"data angka sort = \n{data_angka}")
    # Output: data angka sort = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 7, 8, 9]

    # Mengurutkan String
    data = ["Ucup", "Otong", "Dudung", "Ujang"]
    print(f"data string sebelum sort = \n{data}")
    data.sort()
    print(f"data string sort = \n{data}")
    # Output: data string sort = ['Dudung', 'Otong', 'Ucup', 'Ujang']
    ```

## 4. Membalik Urutan List (`.reverse()`)

Metode `.reverse()` digunakan untuk membalik urutan elemen dalam list secara *in-place*, tanpa mengurutkannya berdasarkan nilai.

*   **Fungsi**: Membalik urutan elemen list dari belakang ke depan.
*   **Sintaks**: `list_anda.reverse()`
*   **Penggunaan Kombinasi**: Jika ingin mengurutkan list dari terbesar ke terkecil (atau Z-A untuk string), lakukan `.sort()` terlebih dahulu, kemudian diikuti dengan `.reverse()`.
*   **Contoh**:
    ```python
    # Membalik list angka (setelah disort, jadi dari besar ke kecil)
    data_angka = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 7, 8, 9] # Angka sudah diurutkan
    data_angka.reverse()
    print(f"data angka reverse = \n{data_angka}")
    # Output: data angka reverse = [9, 8, 7, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 0]

    # Membalik list string
    data = ['Dudung', 'Otong', 'Ucup', 'Ujang'] # String sudah diurutkan
    data.reverse()
    print(f"data string reverse = \n{data}")
    # Output: data string reverse = ['Ujang', 'Ucup', 'Otong', 'Dudung']
    ```

## 5. Catatan Penting: Duplikasi List (Copy List)

Operasi duplikasi list, atau "Copy List", adalah topik yang agak rumit dan memerlukan pemahaman khusus mengenai *shallow copy* dan *deep copy*. Hal ini akan dibahas lebih lanjut di materi berikutnya untuk menghindari perilaku yang tidak terduga saat bekerja dengan list.
# Operasi Dictionary di Python

Dokumen ini merangkum operasi-operasi dasar yang dapat dilakukan pada struktur data **dictionary** di Python, meliputi cara mendapatkan panjang, mengecek keberadaan kunci, mengakses nilai, memperbarui atau menambah data, serta menghapus data. Dictionary adalah koleksi pasangan **kunci-nilai** (key-value pair) yang tidak berurutan, di mana setiap kunci harus unik.

## 1. Mendapatkan Panjang Dictionary (`len()`)

Untuk mengetahui jumlah pasangan kunci-nilai (item) dalam sebuah dictionary, kita dapat menggunakan fungsi bawaan `len()` .

*   **Sintaks**: `len(nama_dictionary)`
*   **Contoh**:
    ```python
    data_dict = {
        "cp": "ucup surucup",
        "tg": "otong surotong",
        "dg": "dudung surudung"
    }
    panjang_dict = len(data_dict)
    print(f"Panjang dictionary adalah: {panjang_dict}") # Output: Panjang dictionary adalah: 3
    ```
    Dalam contoh di atas, `panjang_dict` akan bernilai 3, karena ada tiga pasangan kunci-nilai.

## 2. Mengecek Keberadaan Kunci (`in`)

Kita dapat memeriksa apakah sebuah kunci (key) tertentu ada di dalam dictionary menggunakan operator `in` . Operator ini akan mengembalikan nilai Boolean (`True` jika kunci ditemukan, `False` jika tidak).

*   **Sintaks**: `kunci_yang_dicari in nama_dictionary`
*   **Contoh**:
    ```python
    data_dict = {
        "cp": "ucup surucup",
        "tg": "otong surotong",
        "dg": "dudung surudung"
    }
    print(f"Apakah 'cp' ada di data_dict: {'cp' in data_dict}") # Output: True
    print(f"Apakah 'kis' ada di data_dict: {'kis' in data_dict}") # Output: False
    ```

## 3. Mengakses Nilai (Value) Dictionary

Ada dua cara utama untuk mengakses nilai dari sebuah dictionary berdasarkan kuncinya:

### a. Akses Langsung (`nama_dictionary['kunci']`)

Cara ini adalah metode standar untuk mengakses nilai. Namun, jika kunci yang dicari tidak ada, program akan menghasilkan `KeyError` dan berhenti berjalan .

*   **Sintaks**: `nama_dictionary['kunci']`
*   **Contoh**:
    ```python
    data_dict = {"cp": "ucup surucup"}
    print(data_dict['cp']) # Output: ucup surucup
    # print(data_dict['kis']) # Akan menyebabkan KeyError
    ```

### b. Menggunakan Metode `.get()`

Metode `.get()` adalah cara yang lebih aman untuk mengakses nilai karena tidak akan menghasilkan `KeyError` jika kunci tidak ditemukan.

*   Jika kunci ditemukan, `.get()` akan mengembalikan nilai yang terkait dengan kunci tersebut.
*   Jika kunci tidak ditemukan, `.get()` akan mengembalikan `None` secara default.
*   Kita juga bisa menyediakan nilai default yang akan dikembalikan jika kunci tidak ditemukan, alih-alih `None`.

*   **Sintaks**:
    *   `nama_dictionary.get('kunci')`
    *   `nama_dictionary.get('kunci', 'nilai_default')`
*   **Contoh**:
    ```python
    data_dict = {"cp": "ucup surucup"}
    print(data_dict.get('cp')) # Output: ucup surucup
    print(data_dict.get('kis')) # Output: None
    print(data_dict.get('kis', 'Key tidak ditemukan')) # Output: Key tidak ditemukan
    ```
Disarankan untuk menggunakan `.get()` untuk menghindari kesalahan program akibat kunci yang tidak ada.

## 4. Memperbarui dan Menambah Data

Ada beberapa cara untuk memperbarui nilai yang ada atau menambahkan pasangan kunci-nilai baru ke dictionary:

### a. Penugasan Langsung (`nama_dictionary['kunci'] = nilai`)

*   **Memperbarui Nilai**: Jika kunci sudah ada, nilai yang baru akan menimpa nilai yang lama.
*   **Menambah Data Baru**: Jika kunci belum ada, pasangan kunci-nilai baru akan ditambahkan ke dictionary.

*   **Contoh**:
    ```python
    data_dict = {"cp": "ucup surucup"}
    data_dict["cp"] = "ucup si ganteng" # Memperbarui nilai 'cp'
    print(data_dict) # Output: {'cp': 'ucup si ganteng'}

    data_dict["sf"] = "syef syef" # Menambah kunci 'sf'
    print(data_dict) # Output: {'cp': 'ucup si ganteng', 'sf': 'syef syef'}
    ```

### b. Menggunakan Metode `.update()`

Metode `.update()` adalah cara yang lebih fleksibel dan "elegan" untuk memperbarui atau menambah data, terutama ketika berhadapan dengan banyak pasangan kunci-nilai atau ketika kita tidak yakin apakah kunci sudah ada atau belum.

*   **Jika kunci sudah ada**: Nilai yang terkait dengan kunci tersebut akan diperbarui.
*   **Jika kunci tidak ada**: Pasangan kunci-nilai baru akan ditambahkan ke dictionary.

*   **Sintaks**: `nama_dictionary.update({kunci1: nilai1, kunci2: nilai2, ...})`
*   **Contoh**:
    ```python
    data_dict = {
        "cp": "ucup surucup",
        "tg": "otong surotong"
    }
    data_dict.update({"cp": "ucup surucup"}) # Mengembalikan nilai 'cp' ke awal
    print(data_dict) # Output: {'cp': 'ucup surucup', 'tg': 'otong surotong'}

    data_dict.update({"faqih": "faqihza si keren"}) # Menambah kunci 'faqih'
    print(data_dict) # Output: {'cp': 'ucup surucup', 'tg': 'otong surotong', 'faqih': 'faqihza si keren'}
    ```
Keunggulan `.update()` adalah kita tidak perlu memeriksa keberadaan kunci terlebih dahulu; metode ini akan secara otomatis memperbarui atau menambah sesuai kebutuhan.

## 5. Menghapus Data (`del`)

Untuk menghapus pasangan kunci-nilai dari dictionary, kita dapat menggunakan kata kunci `del` diikuti dengan dictionary dan kunci yang ingin dihapus .

*   **Sintaks**: `del nama_dictionary['kunci']`
*   **Peringatan**: Jika kunci yang ingin dihapus tidak ada, `del` akan menghasilkan `KeyError`.
*   **Contoh**:
    ```python
    data_dict = {
        "cp": "ucup surucup",
        "tg": "otong surotong",
        "dg": "dudung surudung"
    }
    del data_dict['tg'] # Menghapus item dengan kunci 'tg'
    print(data_dict) # Output: {'cp': 'ucup surucup', 'dg': 'dudung surudung'}
    ```

Setelah mempelajari operasi-operasi dasar ini, langkah selanjutnya adalah memahami cara melakukan *looping* atau iterasi pada dictionary, yang akan dibahas dalam tutorial berikutnya.
# Panduan Looping Dictionary di Python

Dictionary adalah struktur data di Python yang menyimpan pasangan **key-value**. Untuk mengakses atau memproses data di dalamnya, kita seringkali perlu melakukan *looping* atau iterasi. Python menyediakan beberapa cara untuk melakukan *looping* pada dictionary, masing-masing dengan kegunaan spesifiknya.

## Contoh Dictionary

Untuk demonstrasi, kita akan menggunakan dictionary `teman_teman` berikut:
```python
teman_teman = {
    "cup": "ucup surucup",
    "tong": "otong surotong",
    "dung": "dudung surudung",
    "sep": "asep si kasyep",
    "cuy": "ucuy surucuy"
}
```
Dictionary ini berisi nama panggilan (sebagai **key**) dan nama lengkap (sebagai **value**).

## Metode Looping Dictionary

Ada empat cara utama untuk melakukan *looping* pada dictionary:

### 1. Looping Standar (Hanya Key)

Ketika Anda melakukan *looping* langsung pada sebuah dictionary tanpa memanggil metode khusus, Python secara *default* akan mengiterasi melalui **key**-nya saja.

*   **Cara Penggunaan:**
    ```python
    print("--- Looping Standar ---")
    for teman in teman_teman:
        print(teman)
    ```
*   **Output:**
    ```
    cup
    tong
    dung
    sep
    cuy
    ```
*   **Penjelasan:** Output menunjukkan bahwa hanya *key* (`"cup"`, `"tong"`, dll.) yang diakses.

### 2. Mengambil Key dengan `.keys()`

Jika Anda ingin secara eksplisit mengiterasi hanya melalui **key** dari dictionary, Anda bisa menggunakan metode `.keys()`.

*   **Karakteristik:**
    *   Metode `.keys()` mengembalikan objek `dict_keys`, yang merupakan *iterable* (dapat diiterasi) yang berisi semua *key* dalam dictionary.
*   **Cara Penggunaan:**
    ```python
    print("\n--- Operator Keys ---")
    keys = teman_teman.keys()
    print(keys)

    for key in teman_teman.keys():
        print(f"{key} -> {teman_teman.get(key)}")
    ```
*   **Output:**
    ```
    dict_keys(['cup', 'tong', 'dung', 'sep', 'cuy'])
    cup -> ucup surucup
    tong -> otong surotong
    dung -> dudung surudung
    sep -> asep si kasyep
    cuy -> ucuy surucuy
    ```
*   **Penjelasan:** Setelah mendapatkan *key* melalui `.keys()`, Anda bisa menggunakan `dictionary.get(key)` atau `dictionary[key]` untuk mengambil *value* yang terkait.

### 3. Mengambil Value dengan `.values()`

Untuk mengiterasi hanya melalui **value** dari dictionary, Anda bisa menggunakan metode `.values()`.

*   **Karakteristik:**
    *   Metode `.values()` mengembalikan objek `dict_values`, yang merupakan *iterable* yang berisi semua *value* dalam dictionary.
*   **Cara Penggunaan:**
    ```python
    print("\n--- Operator Values ---")
    values = teman_teman.values()
    print(values)

    for value in teman_teman.values():
        print(value)
    ```
*   **Output:**
    ```
    dict_values(['ucup surucup', 'otong surotong', 'dudung surudung', 'asep si kasyep', 'ucuy surucuy'])
    ucup surucup
    otong surotong
    dudung surudung
    asep si kasyep
    ucuy surucuy
    ```
*   **Penjelasan:** Metode ini berguna ketika Anda hanya tertarik pada data *value* dan tidak memerlukan *key* yang terkait.

### 4. Mengambil Key dan Value dengan `.items()`

Jika Anda membutuhkan **key dan value secara bersamaan** dalam setiap iterasi, metode `.items()` adalah pilihan terbaik.

*   **Karakteristik:**
    *   Metode `.items()` mengembalikan objek `dict_items`, yang merupakan *iterable* dari **tuple**. Setiap *tuple* berisi pasangan `(key, value)`.
*   **Cara Penggunaan (Iterasi Tuple):**
    ```python
    print("\n--- Operator Items (Tuple) ---")
    items = teman_teman.items()
    print(items)

    for item in teman_teman.items():
        print(item)
    ```
*   **Output:**
    ```
    dict_items([('cup', 'ucup surucup'), ('tong', 'otong surotong'), ('dung', 'dudung surudung'), ('sep', 'asep si kasyep'), ('cuy', 'ucuy surucuy')])
    ('cup', 'ucup surucup')
    ('tong', 'otong surotong')
    ('dung', 'dudung surudung')
    ('sep', 'asep si kasyep')
    ('cuy', 'ucuy surucuy')
    ```
*   **Cara Paling Keren (Unpacking Tuple):**
    Python memungkinkan *unpacking* tuple secara langsung dalam loop `for`. Ini adalah cara yang paling sering digunakan dan direkomendasikan karena memisahkan *key* dan *value* ke dalam variabel terpisah secara otomatis.
    ```python
    print("\n--- Operator Items (Unpacking) ---")
    for key, value in teman_teman.items():
        print(f"key = {key}, value = {value}")
    ```
*   **Output:**
    ```
    key = cup, value = ucup surucup
    key = tong, value = otong surotong
    key = dung, value = dudung surudung
    key = sep, value = asep si kasyep
    key = cuy, value = ucuy surucuy
    ```
*   **Penjelasan:** Metode *unpacking* ini sangat efisien dan membuat kode lebih mudah dibaca saat Anda perlu bekerja dengan kedua bagian dari setiap entri dictionary.

## Ringkasan dan Perbandingan

| Metode Looping        | Apa yang Diiterasi? | Kapan Digunakan?                                                                |
| :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| **Looping Standar**   | Key                 | Ketika hanya membutuhkan *key* dan tidak keberatan dengan perilaku *default*. |
| **`.keys()`**         | Key                 | Ketika ingin secara eksplisit menyatakan bahwa Anda mengiterasi *key*.          |
| **`.values()`**       | Value               | Ketika hanya membutuhkan *value* dan tidak memerlukan *key* terkait.           |
| **`.items()`**        | (Key, Value) Tuple  | Ketika membutuhkan *key* dan *value* secara bersamaan. Paling sering digunakan dengan *unpacking*. |

Memahami berbagai metode *looping* ini memungkinkan Anda untuk memilih cara yang paling efisien dan mudah dibaca sesuai dengan kebutuhan spesifik Anda saat bekerja dengan dictionary di Python.

Di video selanjutnya, akan dibahas tentang cara menyalin (copy) dictionary, serta metode `pop()` dan `popitem()`.
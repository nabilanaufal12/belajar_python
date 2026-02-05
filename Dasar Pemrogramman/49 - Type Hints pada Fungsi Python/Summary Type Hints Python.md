# Type Hints pada Fungsi Python

## Gambaran Umum
Python dikenal dengan sifat *dynamic typing*-nya, yang memungkinkan fleksibilitas dalam penanganan tipe data variabel. Namun, kemudahan ini dapat menimbulkan masalah dalam proyek yang lebih besar, di mana ketidakjelasan tipe data yang diharapkan oleh suatu fungsi dapat menyebabkan *runtime error* dan mempersulit pemeliharaan kode. **Type Hints** diperkenalkan untuk mengatasi masalah ini dengan menyediakan cara untuk mengindikasikan tipe data yang diharapkan untuk argumen fungsi dan nilai kembaliannya, tanpa secara ketat memberlakukan pemeriksaan tipe pada saat *runtime*.

## Masalah Dynamic Typing Python
Python adalah bahasa *dynamic typing*, yang berarti tipe data variabel dapat berubah-ubah selama eksekusi program. Fleksibilitas ini, meskipun memudahkan pengembangan awal, dapat menjadi sumber masalah:
*   **Potensi *Runtime Error***: Sebuah fungsi mungkin dirancang untuk bekerja dengan tipe data tertentu (misalnya, angka), tetapi karena *dynamic typing*, ia dapat menerima tipe data lain (misalnya, string) tanpa *error* sintaksis awal. Kesalahan baru akan muncul saat operasi yang tidak valid dicoba pada tipe data yang salah tersebut.
    *   **Studi Kasus Fungsi Kuadrat**: Pertimbangkan fungsi sederhana untuk menghitung kuadrat.
        ```python
        def fungsi_kuadrat(parameter):
            hasil = parameter ** 2
            print(hasil)
        ```
        Jika dipanggil dengan integer, `fungsi_kuadrat(10)` akan menghasilkan `100` dengan aman. Namun, jika dipanggil dengan string, `fungsi_kuadrat("Ucup")` akan menyebabkan *error* karena string tidak dapat dipangkatkan.
*   **Kurangnya Kejelasan**: Dalam proyek besar atau ketika bekerja dalam tim, sulit untuk mengingat atau mengetahui tipe data yang diharapkan oleh suatu fungsi, terutama jika dokumentasinya kurang. Hal ini dapat menyebabkan penggunaan fungsi yang salah dan *error* yang sulit dilacak.

## Pengenalan Type Hints
**Type Hints** adalah fitur di Python yang memungkinkan pengembang untuk secara eksplisit mendeklarasikan tipe data yang diharapkan untuk argumen fungsi dan nilai kembaliannya.
*   **Tujuan**: Type Hints berfungsi sebagai petunjuk atau anotasi yang membantu pengembang dan alat pengembangan (seperti IDE) untuk memahami kode dengan lebih baik.
*   **Sifat Non-Enforcing**: Penting untuk diingat bahwa Type Hints di Python bersifat opsional dan tidak diberlakukan secara ketat oleh *interpreter* Python saat *runtime*. Ini berarti Python akan tetap menjalankan kode meskipun tipe data yang diberikan tidak sesuai dengan petunjuk, dan *error* akan muncul hanya jika operasi yang tidak valid dilakukan. Ini berbeda dengan bahasa *statically typed* seperti C++ atau Java, di mana kesalahan tipe akan terdeteksi pada tahap kompilasi.

## Implementasi Type Hints

### 1. Untuk Argumen Fungsi
Untuk memberikan petunjuk tipe pada argumen fungsi, tambahkan titik dua (`:`) diikuti dengan tipe data yang diharapkan setelah nama argumen.

**Contoh**:
```python
def sepuluh_pangkat(argument: int):
    output = 10 ** argument
    return output

hasil = sepuluh_pangkat(2)
print(f"Hasil: {hasil}") # Output: Hasil: 100
```
Dalam contoh ini, `argument: int` menunjukkan bahwa argumen `argument` diharapkan bertipe integer. Saat mengarahkan kursor ke fungsi di editor, akan muncul informasi tentang tipe argumen yang diharapkan.

### 2. Untuk Nilai Kembalian (Return Value)
Untuk memberikan petunjuk tipe pada nilai yang dikembalikan oleh fungsi, gunakan tanda panah (`->`) diikuti dengan tipe data yang diharapkan setelah kurung tutup fungsi.

**Contoh**:
```python
def fungsi_matematika(argument: int) -> int:
    output = 10 ** argument
    return output
```
Di sini, `-> int` menunjukkan bahwa fungsi ini diharapkan mengembalikan nilai bertipe integer.

*   **Fungsi Tanpa Nilai Kembalian**: Jika sebuah fungsi tidak secara eksplisit mengembalikan nilai (tidak ada pernyataan `return`), tipe kembaliannya adalah `None`.
    ```python
    def display(argument: str) -> None:
        print(argument)

    display("Ucup") # Output: Ucup
    ```
    Saat mengarahkan kursor ke fungsi `display`, editor akan menunjukkan bahwa outputnya adalah `None`.

## Manfaat Type Hints
Meskipun tidak diberlakukan secara ketat, Type Hints memberikan beberapa manfaat signifikan:
*   **Dokumentasi yang Lebih Baik**: Type Hints secara inheren mendokumentasikan ekspektasi fungsi, membuat kode lebih mudah dibaca dan dipahami oleh pengembang lain atau diri sendiri di masa depan.
*   **Dukungan Editor (Intellisense)**: Lingkungan Pengembangan Terpadu (IDE) dan editor kode seperti VS Code dapat memanfaatkan Type Hints untuk memberikan saran otomatis (autocomplete), pemeriksaan tipe dasar, dan mendeteksi potensi kesalahan lebih awal, bahkan sebelum kode dijalankan.
*   **Pemeliharaan Kode**: Memudahkan *debugging* dan pemeliharaan, terutama dalam basis kode yang besar dan kompleks, karena mengurangi ambiguitas tentang tipe data.

## Topik Lanjutan
Video selanjutnya akan membahas `*args` (arbitrary arguments) dan `**kwargs` (keyword arguments), yang merupakan fitur penting dalam Python dan sering digunakan dalam *framework* seperti Django.
# Python OOP: Override Method

## Pengertian Override Method

**Override method** adalah sebuah konsep dalam pemrograman berorientasi objek (OOP) di mana sebuah kelas anak (subclass) menyediakan implementasi spesifik untuk sebuah metode yang sudah didefinisikan di kelas induknya (superclass). Tujuan utama dari overriding adalah untuk memungkinkan kelas anak mengubah atau memperluas perilaku metode yang diwarisi dari kelas induknya, sehingga metode tersebut dapat melakukan tugas yang berbeda atau lebih spesifik sesuai kebutuhan kelas anak.

Dalam Python, ketika sebuah metode di kelas anak memiliki nama yang sama persis dengan metode di kelas induk, metode di kelas anak akan "menimpa" (override) metode di kelas induk. Ini berarti ketika metode tersebut dipanggil melalui objek kelas anak, implementasi dari kelas anaklah yang akan dieksekusi, bukan dari kelas induk.

## Cara Kerja Override Method

Agar sebuah metode dapat di-override, beberapa syarat harus terpenuhi:
*   **Pewarisan (Inheritance)**: Harus ada hubungan pewarisan antara kelas induk dan kelas anak. Kelas anak harus mewarisi dari kelas induk.
*   **Nama Metode yang Sama**: Metode di kelas anak harus memiliki nama yang sama persis dengan metode di kelas induk yang ingin di-override.
*   **Tanda Tangan Metode yang Kompatibel**: Meskipun Python tidak memiliki pemeriksaan tanda tangan metode yang ketat seperti bahasa lain (misalnya Java), secara konvensional, metode yang di-override diharapkan memiliki jumlah parameter yang sama atau setidaknya kompatibel.

Ketika sebuah objek dari kelas anak memanggil metode yang telah di-override, Python akan mencari implementasi metode tersebut pertama kali di kelas anak. Jika ditemukan, implementasi tersebut akan digunakan. Jika tidak ditemukan (atau jika metode tersebut tidak di-override), Python akan mencarinya di kelas induk, dan seterusnya ke atas dalam hierarki pewarisan.

**Contoh Konseptual:**
Misalkan ada kelas `Hewan` dengan metode `bersuara()`. Kelas `Anjing` yang mewarisi dari `Hewan` dapat meng-override metode `bersuara()` untuk mengeluarkan suara "Guk guk!", sementara kelas `Kucing` dapat meng-override-nya untuk mengeluarkan suara "Meong!".

```python
class Hewan:
    def bersuara(self):
        print("Hewan bersuara")

class Anjing(Hewan):
    def bersuara(self): # Meng-override metode bersuara() dari Hewan
        print("Guk guk!")

class Kucing(Hewan):
    def bersuara(self): # Meng-override metode bersuara() dari Hewan
        print("Meong!")

hewan_umum = Hewan()
anjing_peliharaan = Anjing()
kucing_peliharaan = Kucing()

hewan_umum.bersuara()       # Output: Hewan bersuara
anjing_peliharaan.bersuara() # Output: Guk guk!
kucing_peliharaan.bersuara() # Output: Meong!
```

## Kapan Menggunakan Override Method?

Override method sangat berguna dalam beberapa skenario:
*   **Polimorfisme**: Ini adalah salah satu pilar OOP yang memungkinkan objek dari kelas yang berbeda untuk diperlakukan sebagai objek dari kelas induk yang sama, namun tetap menunjukkan perilaku yang spesifik untuk kelasnya masing-masing.
*   **Kustomisasi Perilaku**: Kelas anak dapat menyediakan implementasi yang lebih spesifik atau berbeda dari metode yang diwarisi dari kelas induk, tanpa mengubah kode kelas induk.
*   **Ekstensi Fungsionalitas**: Kadang-kadang, metode di kelas anak mungkin perlu memanggil implementasi metode dari kelas induk sebelum atau sesudah menambahkan fungsionalitasnya sendiri. Ini dapat dilakukan dengan menggunakan fungsi `super()`.

```python
class Kendaraan:
    def bergerak(self):
        print("Kendaraan bergerak maju.")

class Mobil(Kendaraan):
    def bergerak(self): # Override
        super().bergerak() # Memanggil metode bergerak() dari kelas induk
        print("Mobil bergerak dengan empat roda.")

mobil_saya = Mobil()
mobil_saya.bergerak()
# Output:
# Kendaraan bergerak maju.
# Mobil bergerak dengan empat roda.
```

## Perbedaan dengan Overload Method

Penting untuk membedakan **override method** dengan **overload method**:
*   **Override Method**: Terjadi ketika sebuah kelas anak mendefinisikan ulang metode yang sudah ada di kelas induknya dengan nama dan (secara konseptual) tanda tangan yang sama. Tujuannya adalah mengubah perilaku metode yang diwarisi.
*   **Overload Method**: Terjadi ketika dalam satu kelas yang sama, terdapat beberapa metode dengan nama yang sama tetapi dengan jumlah atau tipe parameter yang berbeda. Python secara *default* tidak mendukung method overloading dalam arti yang sama seperti bahasa seperti Java atau C++. Jika Anda mendefinisikan dua metode dengan nama yang sama dalam satu kelas di Python, metode yang terakhir didefinisikan akan menimpa yang sebelumnya. Untuk mencapai fungsionalitas serupa di Python, biasanya digunakan parameter default atau `*args`/`**kwargs`.
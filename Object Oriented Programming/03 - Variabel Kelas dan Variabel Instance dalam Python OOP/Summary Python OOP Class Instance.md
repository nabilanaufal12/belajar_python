# Variabel Kelas dan Variabel Instance dalam Python OOP

Dalam pemrograman berorientasi objek (OOP) dengan Python, pemahaman tentang variabel adalah fundamental. Dua jenis variabel utama yang sering ditemui adalah **variabel instance** dan **variabel kelas (class variables)**. Keduanya memiliki cakupan dan perilaku yang berbeda, yang penting untuk dipahami agar dapat merancang kelas dan objek secara efektif.

## Pengenalan Variabel dalam OOP Python

Variabel dalam konteks OOP Python digunakan untuk menyimpan data yang terkait dengan objek atau kelas. Pemilihan jenis variabel yang tepat sangat krusial karena memengaruhi bagaimana data dibagikan dan diakses di antara objek-objek yang berbeda.

## Variabel Instance

Variabel instance adalah variabel yang unik untuk setiap objek (instance) dari sebuah kelas. Setiap objek memiliki salinan variabel instance-nya sendiri, dan perubahan pada variabel instance di satu objek tidak akan memengaruhi objek lain.

### Definisi dan Karakteristik
*   **Unik per objek**: Setiap objek memiliki set variabel instance-nya sendiri.
*   **Didefinisikan dalam metode `__init__`**: Umumnya dideklarasikan di dalam konstruktor `__init__` menggunakan kata kunci `self`.
*   **Akses melalui objek**: Diakses menggunakan sintaks `nama_objek.nama_variabel`.

### Cara Deklarasi dan Akses
Variabel instance biasanya dideklarasikan di dalam metode `__init__` menggunakan `self.nama_variabel`.
```python
class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama    # Variabel instance
        self.warna = warna  # Variabel instance

kucing1 = Kucing("Miko", "Putih")
kucing2 = Kucing("Luna", "Hitam")

print(kucing1.nama)  # Output: Miko
print(kucing2.nama)  # Output: Luna

kucing1.warna = "Coklat" # Mengubah variabel instance untuk kucing1 saja
print(kucing1.warna) # Output: Coklat
print(kucing2.warna) # Output: Hitam (tidak berubah)
```

### Perilaku
Perubahan pada variabel instance hanya berlaku untuk instance (objek) tempat perubahan tersebut dilakukan. Ini memastikan bahwa setiap objek dapat memiliki status datanya sendiri yang independen.

## Variabel Kelas (Class Variables)

Variabel kelas adalah variabel yang dimiliki oleh kelas itu sendiri, bukan oleh instance individual dari kelas tersebut. Semua instance dari kelas yang sama akan berbagi satu salinan variabel kelas yang sama.

### Definisi dan Karakteristik
*   **Dibagikan oleh semua objek**: Semua instance dari kelas yang sama berbagi salinan variabel kelas yang sama.
*   **Didefinisikan di luar metode**: Dideklarasikan langsung di dalam definisi kelas, tetapi di luar metode apa pun.
*   **Akses melalui kelas atau objek**: Dapat diakses menggunakan `NamaKelas.nama_variabel` atau `nama_objek.nama_variabel`.

### Cara Deklarasi dan Akses
Variabel kelas dideklarasikan langsung di dalam kelas.
```python
class Kucing:
    spesies = "Felis catus" # Variabel kelas

    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

kucing1 = Kucing("Miko", "Putih")
kucing2 = Kucing("Luna", "Hitam")

print(Kucing.spesies)    # Output: Felis catus (akses melalui kelas)
print(kucing1.spesies)   # Output: Felis catus (akses melalui objek)
print(kucing2.spesies)   # Output: Felis catus

Kucing.spesies = "Kucing Domestik" # Mengubah variabel kelas melalui kelas
print(kucing1.spesies) # Output: Kucing Domestik
print(kucing2.spesies) # Output: Kucing Domestik (berubah untuk semua objek)
```

### Perilaku
Jika variabel kelas diubah melalui kelas itu sendiri (`NamaKelas.variabel_kelas = nilai_baru`), perubahan tersebut akan terlihat oleh semua instance yang mengakses variabel kelas tersebut. Namun, jika variabel kelas diakses dan diubah melalui sebuah instance (`objek.variabel_kelas = nilai_baru`), Python akan membuat variabel instance baru dengan nama yang sama untuk objek tersebut, dan variabel kelas aslinya tidak akan terpengaruh untuk objek lain.

## Perbandingan Variabel Instance vs. Variabel Kelas

| Fitur              | Variabel Instance                                  | Variabel Kelas                                     |
| :----------------- | :------------------------------------------------- | :------------------------------------------------- |
| **Kepemilikan**    | Dimiliki oleh setiap objek (instance)              | Dimiliki oleh kelas itu sendiri                    |
| **Cakupan**        | Unik untuk setiap objek                            | Dibagikan oleh semua objek dari kelas yang sama    |
| **Deklarasi**      | Di dalam `__init__` menggunakan `self.`            | Langsung di dalam kelas, di luar metode            |
| **Akses**          | `objek.nama_variabel`                              | `Kelas.nama_variabel` atau `objek.nama_variabel`   |
| **Perubahan**      | Perubahan pada satu objek tidak memengaruhi objek lain | Perubahan melalui kelas memengaruhi semua objek; perubahan melalui objek membuat variabel instance baru |
| **Contoh Penggunaan** | Nama, warna, usia (data unik per objek)            | Konstanta, penghitung objek, atribut umum (data dibagikan) |

## Kapan Menggunakan Masing-Masing

*   **Gunakan Variabel Instance** ketika data perlu unik untuk setiap objek. Contohnya adalah nama, usia, alamat, atau status spesifik dari sebuah objek.
*   **Gunakan Variabel Kelas** ketika data perlu dibagikan oleh semua objek dari kelas yang sama, atau ketika data tersebut merupakan konstanta yang terkait dengan kelas secara keseluruhan. Contohnya adalah jumlah total objek yang dibuat, nama spesies, atau nilai default yang berlaku untuk semua instance.

Memahami perbedaan dan penggunaan yang tepat dari variabel instance dan variabel kelas adalah kunci untuk menulis kode Python OOP yang bersih, efisien, dan mudah dipelihara.
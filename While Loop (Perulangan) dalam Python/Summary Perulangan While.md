# Summary Perulangan While

> Generated: January 19th, 2026 7:02 PM
> Sources: Belajar Python [Dasar] - 25 - While Loop (Perulang.youtube, pasted-text-1.md

---

# While Loop (Perulangan) dalam Python

## Pengantar Perulangan

Perulangan (looping) adalah konsep fundamental dalam pemrograman yang memungkinkan eksekusi blok kode berulang kali. Dalam Python, terdapat dua jenis perulangan utama: **For Loop** dan **While Loop**.

### Perbedaan For Loop dan While Loop

| Fitur           | For Loop                                     | While Loop                                     |
| :-------------- | :------------------------------------------- | :--------------------------------------------- |
| **Dasar Iterasi** | Berdasarkan jumlah data atau rentang tertentu (misalnya, list, array, string) | Berdasarkan **kondisi boolean** |
| **Penghentian** | Otomatis berhenti setelah semua item data diiterasi | Berhenti ketika kondisi menjadi `False` |
| **Kapan Digunakan** | Ketika jumlah iterasi sudah diketahui atau ingin mengiterasi koleksi data. | Ketika jumlah iterasi tidak diketahui sebelumnya, dan perulangan harus terus berjalan selama suatu kondisi terpenuhi. |

## Konsep While Loop

**While Loop** akan terus mengeksekusi blok kode **selama** kondisi yang diberikan bernilai `True`. Begitu kondisi tersebut menjadi `False`, perulangan akan berhenti.

### Sintaks Dasar

Sintaks umum untuk `While Loop` adalah sebagai berikut:
```python
while kondisi:
    aksi
```
Di mana `kondisi` adalah ekspresi boolean yang akan dievaluasi pada setiap iterasi, dan `aksi` adalah blok kode yang akan dijalankan jika kondisi `True`.

## Bahaya: Infinite Loop

Salah satu hal yang perlu diwaspadai saat menggunakan `While Loop` adalah **infinite loop** (perulangan tak terbatas). Ini terjadi ketika kondisi `While Loop` selalu bernilai `True` dan tidak pernah berubah menjadi `False`. Akibatnya, program akan terus berjalan tanpa henti, yang dapat menyebabkan program *hang* atau *crash*.

### Contoh Infinite Loop

Pertimbangkan contoh berikut:
```python
angka = 10
while angka > 5:
    print("Saya Keren")
```
Dalam kasus ini, variabel `angka` selalu bernilai `10`, yang selalu lebih besar dari `5`. Karena kondisi `angka > 5` akan selalu `True`, perulangan ini tidak akan pernah berhenti.

## Mengontrol While Loop

Untuk menghindari *infinite loop* dan memastikan `While Loop` berhenti pada waktunya, kita harus memastikan bahwa ada mekanisme di dalam blok `aksi` yang akan mengubah kondisi menjadi `False` pada suatu titik. Biasanya, ini dilakukan dengan memperbarui nilai variabel yang digunakan dalam kondisi.

### Contoh While Loop Terkontrol

Berikut adalah contoh `While Loop` yang terkontrol, di mana perulangan akan berhenti setelah `angka` mencapai `5`:

```python
angka = 0
print(f"angka sekarang -> {angka}") #

while angka < 5: #
    angka += 1 # Ditambah 1 setiap putaran
    print(f"angka sekarang -> {angka}") #
    print("Otong ganteng maksimal!") #

print("Cukup") #
```

### Alur Eksekusi

Mari kita telusuri alur eksekusi kode di atas:

1.  **Inisialisasi**: `angka` dimulai dengan nilai `0`. Output: `angka sekarang -> 0`.
2.  **Iterasi 1**:
    *   Kondisi `0 < 5` adalah `True`.
    *   `angka` bertambah menjadi `1`.
    *   Output: `angka sekarang -> 1`, `Otong ganteng maksimal!`.
3.  **Iterasi 2**:
    *   Kondisi `1 < 5` adalah `True`.
    *   `angka` bertambah menjadi `2`.
    *   Output: `angka sekarang -> 2`, `Otong ganteng maksimal!`.
4.  **Iterasi 3**:
    *   Kondisi `2 < 5` adalah `True`.
    *   `angka` bertambah menjadi `3`.
    *   Output: `angka sekarang -> 3`, `Otong ganteng maksimal!`.
5.  **Iterasi 4**:
    *   Kondisi `3 < 5` adalah `True`.
    *   `angka` bertambah menjadi `4`.
    *   Output: `angka sekarang -> 4`, `Otong ganteng maksimal!`.
6.  **Iterasi 5**:
    *   Kondisi `4 < 5` adalah `True`.
    *   `angka` bertambah menjadi `5`.
    *   Output: `angka sekarang -> 5`, `Otong ganteng maksimal!`.
7.  **Penghentian**:
    *   Kondisi `5 < 5` adalah `False`.
    *   Perulangan berhenti, dan program melanjutkan eksekusi setelah `While Loop`.
    *   Output: `Cukup`.

## Kontrol Aliran Lanjutan

Setelah memahami dasar `While Loop`, kita dapat mempelajari cara mengontrol aliran perulangan lebih lanjut menggunakan pernyataan seperti **`continue`**, **`break`**, dan **`pass`**. Ini akan dibahas dalam materi selanjutnya.
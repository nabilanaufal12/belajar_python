# Belajar Python OOP: Latihan Inheritance

## Pendahuluan Inheritance dalam OOP Python

Inheritance (pewarisan) adalah konsep fundamental dalam Pemrograman Berorientasi Objek (OOP) yang memungkinkan sebuah kelas (kelas anak/subkelas) untuk mewarisi atribut dan metode dari kelas lain (kelas induk/superkelas). Ini mempromosikan penggunaan kembali kode (code reusability) dan menciptakan hierarki kelas yang logis. Latihan ini mendemonstrasikan implementasi inheritance untuk membuat sistem karakter dalam sebuah game.

## Kelas Induk: `Hero`

Kelas `Hero` berfungsi sebagai kelas dasar atau superkelas yang mendefinisikan karakteristik umum dari semua pahlawan.

### Atribut Kelas `Hero`
Setiap objek `Hero` akan memiliki atribut dasar berikut yang diinisialisasi melalui konstruktor `__init__`:
*   `name`: Nama pahlawan (string).
*   `health`: Poin kesehatan pahlawan (integer).
*   `attackPower`: Kekuatan serangan dasar pahlawan (integer).
*   `armorNumber`: Nilai armor pahlawan (integer).

### Metode Kelas `Hero`
Kelas `Hero` memiliki dua metode utama:
*   `serang(self, lawan)`: Metode ini digunakan untuk pahlawan menyerang lawan.
    *   Mengurangi `health` lawan berdasarkan `attackPower` pahlawan.
    *   Mencetak pesan yang menunjukkan serangan yang terjadi.
*   `diserang(self, lawan, attackPower_lawan)`: Metode ini dipanggil ketika pahlawan diserang.
    *   Menghitung kerusakan yang diterima dengan mengurangi `attackPower_lawan` dengan `armorNumber` pahlawan.
    *   Jika kerusakan kurang dari 0, maka dianggap 0.
    *   Mengurangi `health` pahlawan dengan kerusakan yang dihitung.
    *   Mencetak pesan yang menunjukkan pahlawan diserang dan sisa kesehatannya.

## Kelas Anak (Subkelas)

Dua kelas anak dibuat untuk merepresentasikan jenis pahlawan yang berbeda, mewarisi dari kelas `Hero`.

### 1. Kelas `Hero_Strength`

Kelas ini merepresentasikan pahlawan yang berfokus pada kekuatan fisik.
*   **Pewarisan**: `Hero_Strength` mewarisi dari `Hero`.
*   **Konstruktor `__init__`**:
    *   Menerima `name` dan `strength` sebagai parameter tambahan.
    *   Memanggil konstruktor kelas induk (`Hero.__init__`) menggunakan `super().__init__(name, 200, 10, 90)` untuk menginisialisasi atribut dasar `health`, `attackPower`, dan `armorNumber` dengan nilai spesifik untuk pahlawan kekuatan.
    *   Menambahkan atribut `strength` yang unik untuk kelas ini.
*   **Overriding Metode `serang`**:
    *   Metode `serang` di-override untuk menambahkan bonus serangan berdasarkan atribut `strength`.
    *   `attackPower` yang digunakan untuk menyerang adalah `self.attackPower + self.strength`.
    *   Memanggil metode `diserang` dari objek `lawan` dengan `attackPower` yang sudah dimodifikasi.

### 2. Kelas `Hero_Intelligent`

Kelas ini merepresentasikan pahlawan yang berfokus pada kecerdasan.
*   **Pewarisan**: `Hero_Intelligent` mewarisi dari `Hero`.
*   **Konstruktor `__init__`**:
    *   Menerima `name` dan `intelligence` sebagai parameter tambahan.
    *   Memanggil konstruktor kelas induk (`Hero.__init__`) menggunakan `super().__init__(name, 100, 20, 50)` untuk menginisialisasi atribut dasar `health`, `attackPower`, dan `armorNumber` dengan nilai spesifik untuk pahlawan cerdas.
    *   Menambahkan atribut `intelligence` yang unik untuk kelas ini.
*   **Overriding Metode `serang`**:
    *   Metode `serang` di-override untuk menambahkan bonus serangan berdasarkan atribut `intelligence`.
    *   `attackPower` yang digunakan untuk menyerang adalah `self.attackPower + self.intelligence`.
    *   Memanggil metode `diserang` dari objek `lawan` dengan `attackPower` yang sudah dimodifikasi.

## Implementasi dan Contoh Penggunaan

### Instansiasi Objek
Objek dari kelas anak dibuat untuk merepresentasikan pahlawan spesifik:
*   `hero_strength = Hero_Strength("Otong", 10)`
*   `hero_intelligent = Hero_Intelligent("Ucup", 15)`

### Interaksi Antar Objek
Demonstrasi interaksi antar pahlawan:
1.  `hero_strength` menyerang `hero_intelligent`.
2.  `hero_intelligent` menyerang `hero_strength`.

Output dari interaksi ini menunjukkan bagaimana metode `serang` yang di-override di setiap subkelas bekerja, serta bagaimana metode `diserang` dari kelas induk menangani pengurangan kesehatan. Ini menunjukkan bahwa meskipun kedua objek adalah "pahlawan", mereka memiliki perilaku serangan yang berbeda sesuai dengan jenis inheritance mereka.
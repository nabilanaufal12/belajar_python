# Pengenalan dan Sejarah

## Apa Itu Python dan Mengapa Harus Mempelajarinya?

Python adalah bahasa pemrograman yang sangat populer dan banyak digunakan karena beberapa alasan utama.

*   **Mudah Dimengerti**: Python dikenal dengan sintaksnya yang sederhana dan mirip bahasa manusia, membuatnya mudah dipelajari dan dipahami, bahkan bagi pemula tanpa latar belakang pemrograman.
*   **Gratis dan *Open Source***: Python dapat digunakan tanpa biaya lisensi. Ini berbeda dengan beberapa bahasa atau *software* lain yang mungkin memerlukan langganan atau pembelian.
*   **Dinamis dan *Multi-platform***: Python mendukung berbagai paradigma pemrograman (fungsional, *object-oriented*, prosedural) dan dapat berjalan di berbagai sistem operasi (Windows, macOS, Linux). Fleksibilitas ini memungkinkan Python digunakan untuk:
    *   **Web Development**
    *   **Mobile Apps**
    *   **Desktop Apps**
    *   **DevOps** (untuk manajemen server)
    *   **Data Science**
    *   **Robotics**
    *   **Machine Learning**
    *   **Data Analysis** (termasuk probabilitas dan statistik)
    *   **Artificial Intelligence (AI)**
*   **Populer (*Hype*)**: Python sedang sangat populer di kalangan programmer, ilmuwan data, matematikawan, dan profesional bisnis/keuangan karena kemampuannya yang serbaguna, sering disebut sebagai "*one language many kills*".

## Perbandingan Sintaks: "Hello World"

Kemudahan Python paling jelas terlihat saat membandingkan sintaks untuk tugas sederhana seperti menampilkan "Hello World" di layar:

*   **C++**: Membutuhkan banyak baris kode yang kompleks, termasuk `include <iostream>`, `int main()`, `std::cout`, dan `return 0`.
*   **Java**: Juga memerlukan sintaks yang panjang dan terstruktur, seperti `class Main`, `public static void main(String[] args)`, dan `System.out.println`.
*   **Python**: Hanya membutuhkan satu baris kode yang sangat intuitif: `print("Hello World")`.

Kesederhanaan ini membuat Python sangat menarik bagi orang-orang tanpa latar belakang ilmu komputer atau teknik informatika.

## Sejarah dan Pencipta Python

Python diciptakan oleh **Guido van Rossum**, seorang programmer jenius. Nama "Python" sendiri tidak berasal dari ular, melainkan dari acara sirkus komedi favorit Guido, **Monty Python's Flying Circus**.

Pengembangan Python dimulai pada tahun **1989** ketika Guido bekerja di Belanda. Ia diminta oleh Andrew S. Tanenbaum untuk membantu membuat bahasa pemrograman untuk sistem operasi terdistribusi bernama **Amoeba**. Guido memiliki pengalaman dengan bahasa **ABC** dan **Modula+**, yang merupakan bahasa *interpreted* dan dapat berpindah *platform* tanpa kompilasi ulang, menjadi dasar inspirasi untuk Python.

## Evolusi Versi Python

Python telah mengalami perjalanan panjang dalam pengembangannya selama lebih dari 30 tahun:

*   **Python 1.0**: Dirilis pada Januari 1994, merupakan rilis pertama yang dinamai dari Monty Python.
*   **Python 1.5**: Desember 1997, menambahkan *keywords arguments* dan *complex numbers*.
*   **Python 1.6**: September 2000, lisensi diubah menjadi GPL compatible license. Diperkenalkan *Python distribution utilities*, cikal bakal *package manager* yang sering disebut "cheese shop".
*   **Python 2.0**: Oktober 2000, menjadi rilis penting di bawah **Python Software Foundation** yang menjadikannya *open source* penuh. Fitur baru termasuk *list comprehension* dan *garbage collection*. Pada versi ini juga diperkenalkan **PEP (Python Enhancement Proposal)** untuk mengatur penambahan dan perbaikan bahasa secara teratur.
*   **Python 2.2**: Desember 2001, menambahkan integrasi dengan bahasa C (untuk tipe data seperti *float* dan *double*) serta *keyword class* khusus Python.
*   **Python 2.5**: September 2006, menambahkan *with statement*.
*   **Python 2.7**: Juli 2010, merupakan versi final dari seri 2.x. Versi ini terus didukung hingga tahun 2020 karena banyak digunakan di sistem operasi seperti Linux dan macOS.
*   **Python 3.0**: Desember 2008, merupakan perombakan besar-besaran dengan desain ulang dari awal untuk membuatnya lebih *expandable* dan *extensible*. Versi ini tidak *backward compatible* dengan seri 2.x. Disarankan untuk mulai belajar Python 3.
*   **Python 3.1**: Juni 2009, menambahkan *format string* dan *ordered dictionary*.
*   **Python 3.2**: Menambahkan *Stable ABI* untuk memastikan kompatibilitas modul pihak ketiga saat Python di-*upgrade*.
*   **Python 3.3**: Menambahkan *virtual environment* untuk *sandboxing* proyek, *implicit namespace*, *flexible string*, dan *Python launcher* untuk Windows.
*   **Python 3.4**: Maret 2014, **pip** (manajer paket Python) langsung terinstal bersama Python.
*   **Python 3.5**: Menambahkan *coroutines* (untuk *asynchronous programming*) dan *Matrix Operation*.
*   **Python 3.6**: 2016, memperkenalkan *format string literal* (f-string), *numeric literal*, *variable annotations*, dan *asynchronous generator*.
*   **Python 3.7**: Juni 2018, memperkenalkan *postponed evaluation of type annotations*, yang direncanakan akan dikembangkan lebih lanjut di Python 4.
*   **Python 3.8**: Oktober 2019 (versi stabil saat video dibuat), menambahkan *assignment expressions* (operator walrus `:=`), *positional-only parameter*, dan peningkatan pada *f-string*.
*   **Python 3.9**: Akan dirilis pada tahun 2020. Fitur yang diharapkan termasuk *deprecation warning* untuk modul 2.7, *dictionary merge*, dan *update operator*.

Masa depan Python setelah 3.9 masih belum pasti, apakah akan berlanjut ke Python 4 atau seri 3.10+.

## Persiapan Belajar Python

Untuk memulai belajar Python, ada beberapa hal yang dibutuhkan:

1.  **Python Interpreter**: Ini adalah mesin utama yang menjalankan kode Python.
2.  **Tools Coding**: Ada beberapa pilihan, tergantung preferensi:
    *   **IDE (Integrated Development Environment)**: Contohnya **PyCharm**, yang menyediakan lingkungan pengembangan lengkap.
    *   **Interactive Python Shell**: Memungkinkan eksekusi kode baris per baris, seperti **IPython** atau **Jupyter Notebook**.
    *   **Text Editor**: Pilihan yang direkomendasikan untuk mengelola *package* dan proyek. Dalam tutorial ini, akan digunakan **Visual Studio Code (VS Code)** karena ringan dan powerful.

Semua alat ini dapat diinstal di berbagai sistem operasi utama seperti Windows, macOS, dan Linux.
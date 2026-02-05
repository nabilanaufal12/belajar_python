# Belajar GUI dengan Tkinter di Python

# Membuat Jendela Utama (Window)
import tkinter as tk # Import Tkinter
from tkinter import ttk # Import ttk
from tkinter.messagebox import showinfo # Import showinfo

# Membuat Objek Window
window = tk.Tk()

# Konfigurasi Jendela
# Warna Latar Belakang (bg)
window.configure(bg="white")

# Ukuran (geometry)
window.geometry("300x200")

# Dapat Diubah Ukurannya (resizable)
window.resizable(False, False)

# Judul Jendela (title)
window.title("Test Tkinter")

# Membuat Var
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Membuat Fungsi
def tombol_click():
    """
    Docstring for tombol_click
    """
    # MessageBox untuk Interaksi
    # Menggunakan showinfo()
    pesan = f"Halo, {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="Sapa", message=pesan)

# Manajemen Tata Letak dengan Frame
# Membuat Objek Frame
input_frame = ttk.Frame(window)

# Penempatan Widget (pack)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Widget Dasar: Label dan Entry
# Label (Teks Statis) dan Entry (Kotak Input Teks)
nama_depan_label = ttk.Label(input_frame, text="Nama Depan: ")
nama_depan_label.pack(padx=10, fill="x")
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x")

nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang: ")
nama_belakang_label.pack(padx=10, fill="x")
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x")

# Widget Button dan Penanganan Event
# Membuat Objek Button
tombol_sapa = ttk.Button(input_frame, text="Hallo!", command=tombol_click)
tombol_sapa.pack(padx=10, fill="x")

# Menjalankan mainloop()
window.mainloop()
import tkinter

### Jendela Utama (`Tk` Class)
main_window = tkinter.Tk()

### Elemen GUI Lainnya (Label, Button)
label1 = tkinter.Label(main_window, text="label 1")
tombol1 = tkinter.Button(main_window, text="Ini adalah tombol 1")

### Penempatan Elemen (`pack()` Method)
label1.pack()
tombol1.pack()

### Menampilkan GUI (`mainloop()` Method)
main_window.mainloop()
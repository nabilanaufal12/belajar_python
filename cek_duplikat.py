import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def hash_file(path):
    """Hitung hash MD5 dari file."""
    hasher = hashlib.md5()
    try:
        with open(path, 'rb') as file:
            buf = file.read(65536)
            while buf:
                hasher.update(buf)
                buf = file.read(65536)
        return hasher.hexdigest()
    except:
        return None

def cari_duplikat(folder):
    hash_map = {}
    duplikat = []
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            file_hash = hash_file(path)
            if file_hash:
                if file_hash in hash_map:
                    duplikat.append((path, hash_map[file_hash]))
                else:
                    hash_map[file_hash] = path
    return duplikat

class DuplikatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pendeteksi Duplikat File")
        self.root.geometry("900x500")

        # Frame atas
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.folder_path = tk.StringVar()
        tk.Entry(frame, textvariable=self.folder_path, width=60).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Pilih Folder", command=self.pilih_folder).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Scan Duplikat", command=self.scan_duplikat).pack(side=tk.LEFT, padx=5)

        # Tabel hasil
        self.tree = ttk.Treeview(root, columns=("Duplikat", "Asli"), show="headings", selectmode="extended")
        self.tree.heading("Duplikat", text="File Duplikat")
        self.tree.heading("Asli", text="File Asli")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Tombol hapus
        tk.Button(root, text="Hapus yang Dipilih", command=self.hapus_dipilih, bg="red", fg="white").pack(pady=10)

    def pilih_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def scan_duplikat(self):
        folder = self.folder_path.get()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Folder tidak valid!")
            return

        hasil = cari_duplikat(folder)
        self.tree.delete(*self.tree.get_children())  # Kosongkan tabel

        if not hasil:
            messagebox.showinfo("Hasil", "Tidak ditemukan file duplikat.")
            return

        for dup, asli in hasil:
            self.tree.insert("", "end", values=(dup, asli))

    def hapus_dipilih(self):
        items = self.tree.selection()
        if not items:
            messagebox.showwarning("Peringatan", "Tidak ada file dipilih.")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah kamu yakin ingin menghapus file yang dipilih?")
        if not konfirmasi:
            return

        gagal = 0
        for item in items:
            path = self.tree.item(item, "values")[0]
            try:
                os.remove(path)
                self.tree.delete(item)
            except Exception as e:
                gagal += 1
                print(f"Gagal hapus {path}: {e}")

        messagebox.showinfo("Selesai", f"File berhasil dihapus. Gagal: {gagal}")

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = DuplikatApp(root)
    root.mainloop()

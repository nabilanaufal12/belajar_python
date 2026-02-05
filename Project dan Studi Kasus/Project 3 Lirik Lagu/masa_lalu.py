import tkinter as tk

class KaraokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyrics Player")
        self.root.geometry("600x400")
        self.root.configure(bg="#101010")

        self.label = tk.Label(
            root, 
            text="Siap...", 
            font=("Helvetica", 28, "bold"), 
            fg="#00ffcc",
            bg="#101010",
            wraplength=550
        )
        self.label.pack(expand=True)

        self.lyrics = [
            ("Jujur ku tak apa", 0.09),
            ("Kau bahagia dengannya", 0.07),
            ("Memang ku siapa?", 0.09),
            ("Dan dia pemenangnya", 0.07),
            ("Jujur ku tak apa", 0.09),
            ("Kau bahagia dengannya", 0.07),
            ("Memang ku siapa?", 0.09),
            ("Dan dia pemenangnya", 0.08),
        ]

        self.delays = [
            2300,
            4800,
            7300,
            9000,
            11000,
            13400,
            15400,
            17200
        ]

        self.root.after(1000, self.start_song)

    def type_text(self, text, speed, index=0):
        if index < len(text):
            current_text = text[:index+1]
            self.label.config(text=current_text)
            self.root.after(int(speed * 1000), self.type_text, text, speed, index + 1)

    def play_line(self, index):
        if index < len(self.lyrics):
            text, speed = self.lyrics[index]
            self.label.config(text="") 
            self.type_text(text, speed)

    def start_song(self):
        for i, delay in enumerate(self.delays):
            self.root.after(delay, self.play_line, i)

if __name__ == "__main__":
    root = tk.Tk()
    app = KaraokeApp(root)
    root.mainloop()
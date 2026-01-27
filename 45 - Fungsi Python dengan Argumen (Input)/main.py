# Fungsi Python dengan Argumen (Input)

# Contoh Penggunaan Argumen dalam Fungsi

## 1. Argumen String Tunggal

def greet(name):
    """Fungsi untuk menyapa seseorang dengan nama yang diberikan"""
    print(f"Hello, {name}!")

greet("Alice")

## 2. Argumen Numerik Ganda
def add_numbers(a, b):
    """Fungsi untuk menjumlahkan dua angka"""
    hasil = a + b
    print(f"Hasil penjumlahan {a} + {b} = {hasil}")

add_numbers(5, 10)

# 3. Argumen Berupa List (Daftar)
def print_fruits(fruits):
    """Fungsi untuk mencetak daftar buah"""
    for fruit in fruits:
        print(fruit)

fruit_list = ["Apel", "Pisang", "Jeruk"]
print_fruits(fruit_list)
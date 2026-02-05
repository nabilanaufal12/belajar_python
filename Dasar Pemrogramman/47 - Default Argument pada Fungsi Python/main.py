# Default Argument pada Fungsi Python

# 1. Apa itu Default Argument?
def say_hello(nama = "Udin"):
    print(f"Hello, {nama}")

say_hello()
say_hello("Raju")

# 2. Fungsi dengan Multiple Arguments
def sapa_teman(nama, pesan = "Selamat malam."):
    print(f"Halo {nama}, {pesan}")

sapa_teman("Mizu", "Apa kabar?")
sapa_teman("Miwa")

# 3. Keyword Arguments (Argumen Kata Kunci)
def hitung_pangkat(angka, pangkat=2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2, 4))
print(hitung_pangkat(pangkat=1, angka=6))

# 4. Fungsi dengan Banyak Argumen
def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=8))
# Multiline String dalam Python

# Menggunakan Tanda Kutip Tunggal Tiga ('''...''')
multiline_string_tunggal = '''Ini adalah contoh
multiline string menggunakan
tanda kutip tunggal tiga.'''
print(multiline_string_tunggal)
# Output:
# Ini adalah contoh
# multiline string menggunakan
# tanda kutip tunggal tiga.

# Menggunakan Tanda Kutip Ganda Tiga ("""...""")
multiline_string_ganda = """Ini adalah contoh
multiline string menggunakan
tanda kutip ganda tiga."""
print(multiline_string_ganda)
# Output:
# Ini adalah contoh
# multiline string menggunakan
# tanda kutip ganda tiga.

# Multiline string juga dapat menyimpan karakter khusus seperti baris baru dan tab
multiline_string_khusus = """Halo,\nIni adalah contoh multiline string dengan karakter khusus.
\t- Baris baru ditambahkan dengan \n
\t- Tab ditambahkan dengan \t"""
print(multiline_string_khusus)
# Output:
# Halo,
# Ini adalah contoh multiline string dengan karakter khusus.
#     - Baris baru ditambahkan dengan 
#     - Tab ditambahkan dengan

# Menggabungkan Raw String dengan Multiline String
raw_multiline_string = r"""Ini adalah contoh raw multiline string.
Karakter escape seperti \n dan \t tidak akan diinterpretasikan.
Jadi, ini akan ditampilkan apa adanya."""
print(raw_multiline_string)
# Output:
# Ini adalah contoh raw multiline string.
# Karakter escape seperti \n dan \t tidak akan diinterpretasikan.
# Jadi, ini akan ditampilkan apa adanya.
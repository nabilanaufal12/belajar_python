# String Multiline
# Dalam Python, kita dapat membuat string yang terdiri dari beberapa baris menggunakan tiga tanda kutip (''' atau """).
# Ada dua cara utama untuk membuat string multiline di Python:

# 1. Menggunakan tiga tanda kutip langsung:
multiline_string_1 = """Ini adalah contoh string
yang terdiri dari beberapa baris.
Kita dapat menulis teks di sini
dan semuanya akan tetap dalam satu string."""
print(5*"=" + " String Multiline dengan Tiga Tanda Kutip " + 5*"=")
print(multiline_string_1)

multiline_string_1b = '''Ini adalah contoh string
yang terdiri dari beberapa baris.
Kita dapat menulis teks di sini
dan semuanya akan tetap dalam satu string.'''
print("\n" + 5*"=" + " String Multiline dengan Tiga Tanda Kutip (Tunggal) " + 5*"=")
print(multiline_string_1b)

# 2. Menggunakan karakter newline (\n) di dalam string:
multiline_string_2 = "Ini adalah contoh string\nyang terdiri dari beberapa baris.\nKita dapat menulis teks di sini\ndan semuanya akan tetap dalam satu string."
print("\n" + 5*"=" + " String Multiline dengan Newline " + 5*"=")
print(multiline_string_2)
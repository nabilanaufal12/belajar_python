# Karakter Escape dalam Python (Backslash (\))

# Kutip Tunggal (\')
string_escape = 'Halo, \'Dunia\'!'
print(string_escape)  # Output: Halo, 'Dunia'!

# Kutip Ganda (\")
string_escape2 = "Halo, \"Dunia\"!"
print(string_escape2)  # Output: Halo, "Dunia"!

# Baris Baru (\n)
string_baris_baru = "Halo,\nDunia!"
print(string_baris_baru) # Output: Halo,
                         #         Dunia!

# Tab (\t)
string_tab = "Halo,\tDunia!"
print(string_tab)  # Output: Halo,    Dunia!

# Backslash (\\)
string_backslash = "Ini adalah backslash: \\"
print(string_backslash)  # Output: Ini adalah backslash: \

# Backspace (\b)
string_backspace = "Halo, Dunia!\b"
print(string_backspace)  # Output: Halo, Dunia!

# Carriage Return (\r)
string_carriage_return = "Halo, Dunia!\rPython"
print(string_carriage_return)  # Output: Python, Dunia!

# Line Feed (\n)
string_line_feed = "Halo,\nDunia!"
print(string_line_feed)  # Output: Halo,
                         #         Dunia!

# Carriage Return + Line Feed (\r\n)
string_crlf = "Halo,\r\nDunia!"
print(string_crlf)  # Output: Halo,
                    #         Dunia!

# Form Feed (\f)
string_form_feed = "Halo,\fDunia!"
print(string_form_feed)  # Output: Halo,
                         #         Dunia!

# Vertical Tab (\v)
string_vertical_tab = "Halo,\vDunia!"
print(string_vertical_tab)  # Output: Halo,
                            #         Dunia!

# Unicode (\uXXXX)
string_unicode = "Simbol hati: \u2764"
print(string_unicode)  # Output: Simbol hati: ❤

# Hexadecimal (\xXX)
string_hexadecimal = "Simbol centang: \xE2\x9C\x94"
print(string_hexadecimal)  # Output: Simbol centang: ✔

# Oktal (\ooo)
string_oktal = "Simbol bintang: \052"
print(string_oktal)  # Output: Simbol bintang: *

# Null Character (\0)
string_null_char = "Halo,\0Dunia!"
print(string_null_char)  # Output: Halo, Dunia!

# Bell/Alert (\a)
string_bell = "Halo,\aDunia!"
print(string_bell)  # Output: Halo, Dunia! (dengan bunyi bel)
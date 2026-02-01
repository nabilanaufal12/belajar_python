# String Width, Alignment, dan Multiline

# 1. Pengantar: Output String Standar
data_nama = "Andi"
data_umur = 25
data_tinggi = 175.5
data_status = True

print("Nama : ", data_nama)
print("Umur : ", data_umur)
print("Tinggi : ", data_tinggi)
print("Status : ", data_status)

data_string = f"Nama : {data_nama}, Umur : {data_umur}, Tinggi : {data_tinggi}, Status : {data_status}"
print("\n" + 5*"=" + "Data String (Standar)" + 5*"=")
print(data_string)

# 2. String Multiline

## 2.1. Menggunakan Karakter Newline (\n)
data_string_newline = f"Nama : {data_nama}, \nUmur : {data_umur}, \nTinggi : {data_tinggi}, \nStatus : {data_status}"
print("\n" + 5*"=" + "Data String (Newline)" + 5*"=")
print(data_string_newline)

## 2.2. Menggunakan Triple Quotes ("""...""" atau '''...''')
data_string_triple_quotes = f"""Nama : {data_nama},
Umur : {data_umur},
Tinggi : {data_tinggi},
Status : {data_status}"""
print("\n" + 5*"=" + "Data String (Triple Quotes)" + 5*"=")
print(data_string_triple_quotes)

data_string_triple_quotes_single = f'''Nama : {data_nama},
Umur : {data_umur},
Tinggi : {data_tinggi},
Status : {data_status}'''
print("\n" + 5*"=" + "Data String (Triple Quotes Single)" + 5*"=")
print(data_string_triple_quotes_single)

# 3. Mengatur Lebar dan Alignment String

## Konsep Dasar,Jenis Alignment dan Contoh Penerapan
data_nama = "Andi"
data_umur = 25
data_tinggi = 175.5
data_status = True

data_string_align = f"""|{data_nama:>10}|
|{data_umur:>10}|
|{data_tinggi:>10}|
|{data_status:>10}|"""
print("\n" + 5*"=" + "Data String (Right Alignment)" + 5*"=")
print(data_string_align)
data_string_align = f"""|{data_nama:<10}|
|{data_umur:<10}|
|{data_tinggi:<10}|
|{data_status:<10}|"""
print("\n" + 5*"=" + "Data String (Left Alignment)" + 5*"=")
print(data_string_align)
data_string_align = f"""|{data_nama:^10}|
|{data_umur:^10}|
|{data_tinggi:^10}|
|{data_status:^10}|"""
print("\n" + 5*"=" + "Data String (Center Alignment)" + 5*"=")
print(data_string_align)
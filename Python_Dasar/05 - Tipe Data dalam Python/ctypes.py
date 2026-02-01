from ctypes import c_int, c_float, c_double, c_char, c_bool, c_longlong, c_short, c_byte, c_ubyte, c_uint, c_ulong, c_ushort

data_c_int = c_int(10)
print("\nNilai data c_int:", data_c_int.value)
print("Tipe data c_int:", type(data_c_int))
print("ID data c_int:", id(data_c_int))

data_c_float = c_float(1.5)
print("\nNilai data c_float:", data_c_float.value)
print("Tipe data c_float:", type(data_c_float))
print("ID data c_float:", id(data_c_float))

data_c_double = c_double(2.5)
print("\nNilai data c_double:", data_c_double.value)
print("Tipe data c_double:", type(data_c_double))
print("ID data c_double:", id(data_c_double))

data_c_char = c_char(b'A')
print("\nNilai data c_char:", data_c_char.value)
print("Tipe data c_char:", type(data_c_char))
print("ID data c_char:", id(data_c_char))

data_c_bool = c_bool(True)
print("\nNilai data c_bool:", data_c_bool.value)
print("Tipe data c_bool:", type(data_c_bool))
print("ID data c_bool:", id(data_c_bool))

data_c_longlong = c_longlong(10000000000)
print("\nNilai data c_longlong:", data_c_longlong.value)
print("Tipe data c_longlong:", type(data_c_longlong))
print("ID data c_longlong:", id(data_c_longlong))

data_c_short = c_short(5)
print("\nNilai data c_short:", data_c_short.value)
print("Tipe data c_short:", type(data_c_short))
print("ID data c_short:", id(data_c_short))

data_c_byte = c_byte(120)
print("\nNilai data c_byte:", data_c_byte.value)
print("Tipe data c_byte:", type(data_c_byte))
print("ID data c_byte:", id(data_c_byte))

data_c_ubyte = c_ubyte(250)
print("\nNilai data c_ubyte:", data_c_ubyte.value)
print("Tipe data c_ubyte:", type(data_c_ubyte))
print("ID data c_ubyte:", id(data_c_ubyte))

data_c_uint = c_uint(3000000000)
print("\nNilai data c_uint:", data_c_uint.value)
print("Tipe data c_uint:", type(data_c_uint))
print("ID data c_uint:", id(data_c_uint))

data_c_ulong = c_ulong(4000000000)
print("\nNilai data c_ulong:", data_c_ulong.value)
print("Tipe data c_ulong:", type(data_c_ulong))
print("ID data c_ulong:", id(data_c_ulong))

data_c_ushort = c_ushort(60000)
print("\nNilai data c_ushort:", data_c_ushort.value)
print("Tipe data c_ushort:", type(data_c_ushort))
print("ID data c_ushort:", id(data_c_ushort))
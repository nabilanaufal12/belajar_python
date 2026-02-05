print("\n=== Program Konversi Suhu dari Kelvin ===\n")

kelvin = float(input("Masukkan suhu dalam Kelvin: "))
print("Suhu adalah", kelvin, "Kelvin")

# Celcius
celcius = kelvin - 273
print("Suhu dalam Celcius adalah", celcius, "Celcius")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")
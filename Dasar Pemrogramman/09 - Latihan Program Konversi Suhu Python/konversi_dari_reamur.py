print("\n=== Program Konversi Suhu dari Reamur ===\n")

reamur = float(input("Masukkan suhu dalam Reamur: "))
print("Suhu adalah", reamur, "Reamur")

# Celcius
celcius = (5/4) * reamur
print("Suhu dalam Celcius adalah", celcius, "Celcius")

# Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = ((5/4) * reamur) + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")
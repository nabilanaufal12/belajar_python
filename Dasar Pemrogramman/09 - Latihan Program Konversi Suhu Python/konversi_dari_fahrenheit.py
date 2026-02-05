print("\n=== Program Konversi Suhu dari Fahrenheit ===\n")

fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
print("Suhu adalah", fahrenheit, "Fahrenheit")

# Celcius
celcius = (5/9) * (fahrenheit - 32)
print("Suhu dalam Celcius adalah", celcius, "Celcius")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")
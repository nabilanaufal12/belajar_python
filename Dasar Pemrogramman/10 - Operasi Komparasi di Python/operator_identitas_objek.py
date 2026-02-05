a = 5
b = 5

print("Nilai a:", a, ", ID a:", hex(id(a)))
print("Nilai b:", b, ", ID b:", hex(id(b)))

# Identitas Sama dengan (is)
print("\nOperasi Komparasi: Identitas Sama dengan (is)")
hasil = a is b
print("a is b:", hasil)
hasil = b is a
print("b is a:", hasil)

# Identitas Tidak Sama dengan (is not)
print("\nOperasi Komparasi: Identitas Tidak Sama dengan (is not)")
hasil = a is not b
print("a is not b:", hasil)
hasil = b is not a
print("b is not a:", hasil)
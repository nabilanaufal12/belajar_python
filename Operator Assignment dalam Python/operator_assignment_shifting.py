# Operator Assignment Shifting dalam Python
print("Shiting Right (operator >>=)")
a = 0b0100 # Nilai awal dalam biner (4 dalam desimal)
print("Nilai a dalam biner:", format(a, '04b'))
a >>= 2  # Sama dengan a = a >> 2
print("Setelah a >>= 2, nilai a dalam biner:", format(a, '04b'))

print("\nShifting Left (operator <<=)")
a = 0b0100 # Nilai awal dalam biner (4 dalam desimal)
print("Nilai a dalam biner:", format(a, '04b'))
a <<= 1  # Sama dengan a = a << 1
print("Setelah a <<= 1, nilai a dalam biner:", format(a, '04b'))
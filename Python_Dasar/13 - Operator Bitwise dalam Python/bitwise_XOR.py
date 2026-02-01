a = 9
b = 5

print(f"Nilai a: {a}, biner: {format(a, '08b')}")
print(f"Nilai b: {b}, biner: {format(b, '08b')}")

# Operasi Bitwise XOR
print(f"\n{format(a, '08b')} ({a})")
print(f"{format(b, '08b')} ({b})")
print("-------- (^)")
hasil_xor = a ^ b
print(f"{format(hasil_xor, '08b')} ({hasil_xor})")

print(f"\nHasil dari {a} ^ {b} = {hasil_xor}")
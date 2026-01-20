a = 9
b = 5

print(f"Nilai a: {a}, biner: {format(a, '08b')}")
print(f"Nilai b: {b}, biner: {format(b, '08b')}")

# Operasi Bitwise NOT
print(f"\n{format(a, '08b')} ({a})")
print("-------- (~)")
hasil_not1 = ~a
print(f"{format(hasil_not1, '08b')} ({hasil_not1})")
print("-------- (^)")
d = 0b1111111111
e = 0b0000001001
hasil_not2 = d ^ a
print(f"{format(hasil_not2, '08b')} ({hasil_not2})")

print(f"\nHasil dari ~{a} = {hasil_not1} atau {d} ^ {a} = {hasil_not2}")
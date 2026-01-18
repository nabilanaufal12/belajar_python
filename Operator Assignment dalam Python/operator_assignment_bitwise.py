# Bitwise OR dengan Operator Assignment
print("\nBitwise OR (operator |=)")
a = True
print("Nilai a:", a)
a |= False  # Sama dengan a = a | False
print("Setelah a |= False, nilai a:", a)

a = False
print("Nilai a:", a)
a |= False  # Sama dengan a = a | False
print("Setelah a |= False, nilai a:", a)

# Bitwise AND dengan Operator Assignment
print("\nBitwise AND (operator &=)")
a = True
print("Nilai a:", a)
a &= False  # Sama dengan a = a & False
print("Setelah a &= False, nilai a:", a)
a = False
print("Nilai a:", a)
a &= False  # Sama dengan a = a & False
print("Setelah a &= False, nilai a:", a)

# Bitwise XOR dengan Operator Assignment
print("\nBitwise XOR (operator ^=)")
a = True
print("Nilai a:", a)
a ^= False  # Sama dengan a = a ^ False
print("Setelah a ^= False, nilai a:", a)
a = False
print("Nilai a:", a)
a ^= False  # Sama dengan a = a ^ False
print("Setelah a ^= False, nilai a:", a)
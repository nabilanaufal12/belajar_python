# Teknik Duplikasi List di Python: Pass by Reference vs. Copy

# Inisialisasi list awal
a = [1, 2, 3]

# 1. Assignment List (b = a) - Perilaku Pass by Reference
print("=== Pass by Reference ===")
print("Sebelum b = a:")
print("a:", a)  # Output: [1, 2, 3]
b = a  # b merujuk ke list yang sama dengan a
b.append(4)
print("Setelah b.append(4):")
print("a:", a)  # Output: [1, 2, 3, 4]
print("b:", b)  # Output: [1, 2, 3, 4]

# Cek apakah a dan b merujuk ke objek yang sama
print("a is b:", a is b)  # Output: True
print(f"Address a: {hex(id(a))}")
print(f"Address b: {hex(id(b))}")
print()

# 2. Duplikasi List dengan .copy() - Full Duplicate (Shallow Copy)
print("=== Full Duplicate (Shallow Copy) ===")
print("Sebelum c = a.copy():")
print("a:", a)  # Output: [1, 2, 3, 4]
c = a.copy()  # c adalah salinan baru dari a
c.append(5)
print("Setelah c.append(5):")
print("a:", a)  # Output: [1, 2, 3, 4]
print("c:", c)  # Output: [1, 2, 3, 4, 5]

# Cek apakah a dan c merujuk ke objek yang sama
print("a is c:", a is c)  # Output: False
print(f"Address a: {hex(id(a))}")
print(f"Address c: {hex(id(c))}")
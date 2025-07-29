#Cara menggunkan tipe data Tuple
foo = ("Belajar", "Python", "di", "Duniailkom")
bar = (100, 200, 300, 400)
baz = ("Python", 200, 6.99, True)

print(foo)
print(bar)
print(baz)
print("\n")

#Perbedaan tipe data List dan Tuple
foo = ["Belajar", "Python", "di", "Duniailkom"]
print(type(foo))
foo = ("Belajar", "Python", "di", "Duniailkom")
print(type(foo))
print("\n")

#Cara mengakses tipe data Tuple Python
foo = ("Python", 200, 6.99, True, 'Duniailkom', 99j)

print(foo[0])
print(foo[1])
print(foo[2])
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])

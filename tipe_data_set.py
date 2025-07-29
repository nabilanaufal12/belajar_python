#Cara pembuatan tipe data Set Python
foo = {"Belajar", "Python", "di", "Duniailkom"}
bar = {100, 200, 300, 400}
baz = {"Python", 200, 6.99, True}

print(foo)
print(bar)
print(baz)
print("\n")

#Perbedaan tipe data List, Tuple dan Set
foo = ["Belajar", "Python", "di", "Duniailkom"]
print(type(foo))

foo = ("Belajar", "Python", "di", "Duniailkom")
print(type(foo))

foo = {"Belajar", "Python", "di", "Duniailkom"}
print(type(foo))

print("\n")

#Sifat tipe data Set
foo = {"Belajar", "Python", "di", "Duniailkom", "di"}
bar = {100, 200, 300, 400, 200, 300}

print(foo)
print(bar)
print("\n")

#Operasi himpunan tipe data Set Python
foo = {1, 2, 3, 4, 5}
bar = {3, 4, 5, 6, 7}

print(foo | bar) #Union
print(foo & bar) #Intersection

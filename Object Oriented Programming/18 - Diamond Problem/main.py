class A:
    def info(self):
        print("Ini dari Kelas A")

class B(A):
    def info(self):
        print("Ini dari Kelas B")

class C(A):
    def info(self):
        print("Ini dari Kelas C")

class D(B, C):
    pass

# Membuat objec dari Kelas D
obj_d = D()
obj_d.info()

# Melihat MRO dari Kelas D
print(D.__mro__)
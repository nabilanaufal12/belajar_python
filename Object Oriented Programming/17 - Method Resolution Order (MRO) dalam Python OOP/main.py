## Contoh MRO
### 1. Pewarisan Tunggal (Single Inheritance)
class A:
    def info(self):
        print("Ini kelas A")

class B(A):
    def info(self):
        print("Ini kelas B")

# MRO untuk kelas B
print(B.mro())


### 2. Pewarisan Berganda Sederhana
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.mro())


### 3. Masalah Berlian (Diamond Problem)
class A:
    def show(self):
        print("Ini dari A")

class B(A):
    def show(self):
        print("Ini dari B")

class C(A):
    def show(self):
        print("Ini dari C")

class D(B, C):
    def show(self):
        print("Ini dari D")

print(D.mro())


## Fungsi `super()` dan MRO
### Contoh Penggunaan `super()` dengan MRO
class A:
    def method(self):
        print("Method dari A")

class B(A):
    def method(self):
        print("Method dari B")
        super().method() # Memanggil method berikutnya di MRO

class C(A):
    def method(self):
        print("Method dari C")
        super().method() # Memanggil method berikutnya di MRO

class D(B, C):
    def method(self):
        print("Method dari D")
        super().method() # Memanggil method berikutnya di MRO

d_obj = D()
d_obj.method()
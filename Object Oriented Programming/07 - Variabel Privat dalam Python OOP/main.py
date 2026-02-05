## Konvensi Penamaan Variabel
### 1. Variabel "Protected" (Satu Garis Bawah `_`)
class Mahasiswa:
    def __init__(self, nama, health):
        self._nama = nama # Variabel protected
        self.health = health

mhs1 = Mahasiswa("Mizu", 100)
print(mhs1._nama)

### 2. Variabel "Private" (Dua Garis Bawah `__`)
class Hero:
    def __init__(self, nama, health):
        self.__nama = nama # Veriabel yang akan di-mangled
        self.__health = health # Variabel __health milik Hero

hero1 = Hero("Miwa", 200)
# print(hero2.__nama) # Ini akan menghasilkan AttributeError

# Mengakses menggunakan nama yang di-mangled
print(hero1._Hero__nama)
print(hero1._Hero__health)


## Peran Name Mangling dalam Pewarisan
class Hero_Intelligent(Hero):
    def __init__(self, nama, health, intelligence):
        super().__init__(nama, health)
        self.__health = health # Variabel __health milik Hero_Intelligent
        self.intelligence = intelligence

hero2 = Hero("Mika", 100)
hero3 = Hero_Intelligent("Maki", 200, 50)

# Mengakses health dari objek Hero
print(hero2._Hero__health)

# Mengakses health dari objek Hero_Intelligent
# Perhatikan bahwa ini adalah __health milik Hero_Intelligent, bukan Hero
print(hero3._Hero_Intelligent__health)

# Variabel __health dari kelas induk (Hero) masih ada di objek hero2
# dan dapat diakses dengan nama mangled kelas induknya
print(hero3._Hero__health) # nilai yang diteruskan dari super().__init__
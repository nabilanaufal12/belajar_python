'''
## Pengantar Enkapsulasi Tradisional
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health # Atribut private
        self.__armor = armor # Atribut private
## Masalah dengan Atribut Dinamis dan Akses Langsung
        self.info = f"Nama: {self.name}\n\tHealth: {self.__health}"

    def get_health(self): # Metode getter
        return self.__health
    
hero = Hero("Miwa", 100, 10)
print(hero.info)
'''

## Dekorator `@property` untuk Getter
## Dekorator `@<property_name>.setter`
## Dekorator `@<property_name>.deleter`
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        # Logika dinamis di dalam getter
        return f"Nama: {self.name}\n\tHealth: {self.__health}"
    
    @property
    def armor(self):
        # Ini adalah getter untuk __armor
        return self.__armor
    
    @armor.setter # Dekorator setter
    def armor(self, new_armor): # new_armor adalah nilai yang akan
        self.__armor = new_armor

    @armor.deleter # Dekorator deleter
    def armor(self):
        print("Armor dihapus!")
        self.__armor = None # Mengatur atribut internal menjadi None atau menghapusnya
    
hero = Hero("Miwa", 100, 10)
print(hero.info) # Akses seperti atribut, bukan metode

# Keuntungan: Jika name berubah, info akan otomatis diperbarui
hero.name = "Mizu"
print(hero.info)

print(f"Armor awal: {hero.armor}") # Mengakses __armor melalui properti
hero.armor = 50 # Menggunakan setter seperti menetapkan nilai ke atribut
print(f"Armor setelah diubah: {hero.armor}")

print(f"Armor sebelum dihapus: {hero.armor}")
del hero.armor # Memanggil deleter
print(f"Armor setelah dihapus: {hero.armor}")
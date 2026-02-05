class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self._health = health
        self.__attack_power = attack_power

    # Getter untuk _health
    def getHealth(self):
        return self._health

    # Setter untuk _health dengan validasi
    def setHealth(self, new_health):
        if new_health < 0:
            print("Health tidak bisa kurang dari 0!")
        else:
            self._health = new_health

    # Getter untuk __attack_power
    def getAttackPower(self):
        return self.__attack_power

    # Setter untuk __attack_power dengan validasi
    def setAttackPower(self, new_power):
        if new_power < 0:
            print("Attack Power tidak bisa kurang dari 0!")
        else:
            self.__attack_power = new_power

# Membuat objek Hero
hero1 = Hero("Gatot Kaca", 100, 50)

# Mengakses atribut menggunakan getter
print(f"Nama: {hero1.name}")
print(f"Health: {hero1.getHealth()}")
print(f"Attack Power: {hero1.getAttackPower()}")

# Mengubah atribut menggunakan setter
hero1.setHealth(80)
hero1.setAttackPower(60)
print(f"Health baru: {hero1.getHealth()}")
print(f"Attack Power baru: {hero1.getAttackPower()}")

# Mencoba mengubah dengan nilai tidak valid
hero1.setHealth(-10)
hero1.setAttackPower(-5)
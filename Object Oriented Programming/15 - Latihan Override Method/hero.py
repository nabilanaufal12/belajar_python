class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(f"{self.name} diserang {lawan.name}")
        damage_received = attackPower_lawan - self.armorNumber
        if damage_received < 0:
            damage_received = 0
            print(f"Serangan tidak tembus armor: {damage_received}")
        else:
             print(f"Serangan terasa: {damage_received}")
        
        self.health -= damage_received
        print(f"Health {self.name} tersisa: {self.health}")

class Hero_Strength(Hero):
    def __init__(self, name, strength):
        super().__init__(name, 200, 10, 90)
        self.strength = strength

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        # Tambahan damage dari strength
        damage = self.attackPower + self.strength
        lawan.diserang(self, damage)

class Hero_Intelligent(Hero):
    def __init__(self, name, intelligence):
        super().__init__(name, 100, 20, 50)
        self.intelligence = intelligence

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        # Tambahan damage dari intelligence
        damage = self.attackPower + self.intelligence
        lawan.diserang(self, damage)
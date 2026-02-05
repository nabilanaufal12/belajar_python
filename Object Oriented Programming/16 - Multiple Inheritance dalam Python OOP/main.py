class A:
    def method_A(self):
        print("Ini adalah method A")

class B:
    def method_B(self):
        print("Ini adalah method B")

class C(A, B): # C mewarisi dari A dan B
    def method_C(self):
        pass

obj_c = C()
obj_c.method_A()
obj_c.method_B()


class Team:
    def set_team(self, team_name):
        self.team = team_name

    def show_team(self):
        print(f"\tTim: self {self.team}")

class TypeHero:
    def set_type(self, hero_type):
        self.type = hero_type

    def show_type(self):
        print(f"\tTipe Hero: {self.type}")

class Hero(Team, TypeHero): # Hero mewarisi dari Team dan TypeHero
    def __init__(self, name, health):
        self.name = name
        self.health = health
        print(f"Name Hero: {self.name}")

mizu = Hero("Mizu", 100)

# Menggunakan metode dari kelas Team
mizu.set_team("Hunter")
mizu.show_team()

# Menggunakan metode dari kelas TypeHero
mizu.set_type("Assasin")
mizu.show_type()
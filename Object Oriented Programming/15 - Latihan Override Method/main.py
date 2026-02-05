from hero import Hero_Strength, Hero_Intelligent

# Main Code
if __name__ == "__main__":
    hero_strength = Hero_Strength("Mizu", 10)
    hero_intelligent = Hero_Intelligent("Miwa", 15)

    # Periksa status awal
    print(f"Hero 1: {hero_strength.name}, Health: {hero_strength.health}")
    print(f"Hero 2: {hero_intelligent.name}, Health: {hero_intelligent.health}")
    print("-" * 20)

    # Interaksi
    hero_strength.serang(hero_intelligent)
    print("-" * 20)
    hero_intelligent.serang(hero_strength)

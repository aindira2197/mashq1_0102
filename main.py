class GameCharacter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} hujum qildi! Kuch: {self.attack_power}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} sog‘ligi {self.health} ga yetdi")


hero = GameCharacter("Knight", 100, 20)
hero.attack()
hero.heal(15)

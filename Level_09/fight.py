from typing import Optional

class Weapon:
    name: str
    damage: int

    def __init__(self: "Weapon", init_name: str, init_damage: int):
        self.name = init_name
        self.damage = init_damage
    
    def __repr__(self: "Weapon") -> str:
        return "Weapon(name=" + self.name + ", damage=" + str(self.damage) + ")"
    
class Supplement:
    name: str
    healing: int

    def __init__(self: "Supplement", name: str, healing: int):
        self.name = name
        self.healing = healing
    
    def __repr__(self: "Supplement") -> str:
        return "Supplement(name=" + self.name + ", healing=" + str(self.healing) + ")"

class Character:
    name: str
    health: int

    def __init__(self: "Character", name: str, health: int):
        self.name = name
        self.health = health
    
    def take(self: "Character", supplement: Supplement):
        self.health += supplement.healing

class Monster(Character):
    def __init__(self: "Monster", name: str, health: int = 5):
        super().__init__(name, health)

    def __repr__(self: "Monster") -> str:
        return "Monster(name=" + self.name + ", health=" + str(self.health) + ")"

class Player(Character):
    """A fearless wanderer, ready to attack."""
    weapon: Optional[Weapon] = None

    def __init__(self: "Player", name: str, health: int = 10):
        super().__init__(name, health)
    
    def __repr__(self: "Player") -> str:
        return "Player(name=" + self.name + ", health=" + str(self.health) + ", weapon=" + repr(self.weapon) + ")"

    def attack(self: "Player", other: "Player | Monster"):
        if self.weapon is None:
            other.health -= 1
        else:
            other.health -= self.weapon.damage

class Villager(Character):
    def __init__(self: "Villager", name: str):
        super().__init__(name, 9)

hero = Player("Hero")
orky = Monster("Orky")
sword = Weapon("Sword", 3)
hero.weapon = sword
hugo = Villager("Hugo Müller")
hero.attack(hugo)
heiltrank = Supplement("Donnergurgler", 10)


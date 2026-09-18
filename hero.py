import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self,name):
        self.name = name
        self.health = 125
        self.attack_power = 15

    def attack(self):
        #random value from 1 to the hero's attack power
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        #subtract damage but cant fall below 0
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        #if goblin has health remaining print True
        return self.health > 0

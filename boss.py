from enemy import Enemy
import random

class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attackPower=30)


# overrides parent attack with a much cooler attack
    def attack(self):
        attackStyle = random.randint(1,2)
        if attackStyle == 1:
            print("FIREBALL")
            return 5 * random.randint(1,4)
        else:
            print("STOMP")
            return self.attack_power * random.randint(1,2)

#hypbrid override. We do smth special but still use parents functions

    def take_damage(self,damage):
        damage = damage * .75
        super().take_damage(damage)

    def introduce(self):
        print(f"{self.name} JOINS THE FIGHT WITH {self.health} HEALTH!!!")
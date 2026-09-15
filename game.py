from goblin import Goblin
from hero import Hero
import random

ARENA_NAME = "The Iron Lung"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    

    goblin = Goblin("Gribble")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")




    goblin2 = Goblin("Dribble")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")

    Dominator = Hero("Dominator") 

    print(f"{Dominator.name} is summoned into the arena with {Dominator.health} health.")

    heroDamage = Dominator.attack()
    goblin.take_damage(heroDamage)
    def take_damage(self, damage):
        #subtract damage but cant fall below 0
        self.health = max(0, self.health - damage)
    if goblin.health > 0:
        goblinDamage = goblin.attack()
        if goblinDamage > 1:
            Dominator.take_damage(goblinDamage - 2)
        else:
            Dominator.take_damage(goblinDamage)
        print("Dominator's armor lessened Gribble's attack!!")

if __name__ == "__main__":
    main()

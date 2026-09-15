from goblin import Goblin
from hero import Hero
import random

ARENA_NAME = "The Iron Lung"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and goblin.is_alive():
        hero_damage = hero.attack()
        goblin.take_damage(hero_damage)
        if goblin.is_alive():
            goblin_damage = enemy.attack()
            hero.take_damage(goblin_damage)

        if hero.is_alive():
            print(f"{hero.name} wins!")
        else:
            print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")


    enemy = Goblin("Gribble")


    print(f"{enemy.name} enters the arena with {enemy.health} health.")
    print("But no hero has answered the call... yet.")

    enemy2 = Goblin("Dribble")
    print(f"{enemy2.name} enters the arena with {enemy2.health} health.")

    hero = Hero("Dominator") 

    print(f"{hero.name} is summoned into the arena with {hero.health} health.")

    heroDamage = hero.attack()
    enemy.take_damage(heroDamage)
    def take_damage(self, damage):
        #subtract damage but cant fall below 0
        self.health = max(0, self.health - damage)
    if enemy.health > 0:
        enemyDamage = enemy.attack()
        if enemyDamage > 1:
            hero.take_damage(enemyDamage - 2)
        else:
            hero.take_damage(enemyDamage)
        print("Dominator's armor lessened Gribble's attack!!")

if __name__ == "__main__":
    main()
    battle("Gribble", "Dominator")
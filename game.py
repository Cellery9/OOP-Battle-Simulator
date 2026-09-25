from goblin import Goblin
from hero import Hero
from boss import Boss
import random

ARENA_NAME = "The Iron Lung"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)


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

    enemy2 = Goblin("Scribble")

    print(f"{enemy2.name} enters the arena alongside {enemy.name} with {enemy2.health} health.")


    hero = Hero("Dominator") 

    print(f"{hero.name} is summoned into the arena with {hero.health} health.")
    battle(hero, enemy)

    bossGuy = Boss("Maximus")
    battle(hero, bossGuy)

if __name__ == "__main__":
    main()
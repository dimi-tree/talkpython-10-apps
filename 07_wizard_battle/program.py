import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def print_the_header():
    app_header = 'WIZARD GAME APP'
    print('-' * (20 + len(app_header)))
    print(' ' * 10 + app_header)
    print('-' * (20 + len(app_header)))
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50),
        Wizard('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has '
              f'appeared from a dark and foggy forrest...\n')

        cmd = input('Do you [a]ttack, [r]un away or [l]ook around? ').strip().lower()
        if cmd == 'a':
            # Assumption: only wizards can attack creatures. Creatures never initiate an attack.
            if hero.attack(active_creature):  # win
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for c in creatures:
                print(f'  * A {c.name} of level {c.level}')
        else:
            print('OK, exiting the game... bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


def main():
    print_the_header()
    game_loop()


if __name__ == '__main__':
    main()

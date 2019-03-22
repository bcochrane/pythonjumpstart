import random
from time import sleep
from actors import Creature, Wizard, SmallCreature, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------')
    print('   WIZARD GAME APP')
    print('---------------------')
    print()


def game_loop():
    creatures = [
        SmallCreature('Toad', 1),
        Creature('Tiger', 12),
        SmallCreature('Bat', 3),
        Dragon(name='Dragon', level=50, scaliness=75, breathes_fire=True),
        Wizard('Evil Wizard', 250),
    ]

    hero = Wizard('Gandalf', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared.')
        print()

        cmd = input(f'Does {hero.name} [A]ttack, [R]un away, or [L]ook around? ').upper()

        if cmd == 'A':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f'{hero.name} has bested the {active_creature.name}!')
                print()
            else:
                print(f'{hero.name} was defeated by the {active_creature.name}!')
                print(f'{hero.name} runs away to heal', end='')
                for _ in range(0, 5):
                    print('.', end='')
                    sleep(1)
                print(f' all rested up and ready for adventure!')
                print()

        elif cmd == 'R':
            print(f'{hero.name}, unsure of his powers, flees.')
            print()
        elif cmd == 'L':
            print(f'{hero.name} looks around and sees:')
            for c in creatures:
                print(f' * {c.name} of level {c.level}')
            print()
        else:
            print('Exiting...')
            break

        if not creatures:
            print('You have defeated all the creatures...bye!')
            break

if __name__ == '__main__':
    main()

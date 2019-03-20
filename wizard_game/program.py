from actors import Creature, Wizard


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------')
    print('   WIZARD GAME APP')
    print('---------------------')


def game_loop():
    creatures = [
        Creature('newt', 2),
        Creature('duck', 5),
        Creature('Norwegian Blue parrot', 12),
        Creature('penguin on the telly', 100),
        Creature('albatross', 25),
        Creature('rabbit with HUGE FANGS', 500),
    ]

    hero = Wizard('Tim', 250)

    while (True):
        cmd = input('Would you like to [a]ttack, [r]un away, or [l]ook around? ')

        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print('Exiting...')
            break


if __name__ == '__main__':
    main()

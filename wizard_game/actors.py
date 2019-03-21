import random
from time import sleep


class Wizard():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print(f'{self.name} attacks the {creature.name}.')

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print(f'You roll {my_roll}... ', end='')
        sleep(1)
        print(f'The {creature.name} rolls {creature_roll}... ', end='')
        sleep(1)

        if my_roll >= creature_roll:
            return True
        else:
            return False


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'Creature: {self.name} of level {self.level}'

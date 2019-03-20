class Wizard():
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'Creature: {self.name} of level {self.level}'
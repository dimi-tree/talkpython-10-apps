import random


class Creature:

    def __init__(self, name, level_):
        self.name = name
        self.level = level_

    def __str__(self):
        return f'Creature: {self.name} of level {self.level}'

    def __repr__(self):
        return f'Creature({repr(self.name)}, {self.level})'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        """
        In real-life application you want to separate UI piece from logic.
        """

        # UI
        print(f'The wizard {self.name} attacks {creature.name}')

        my_roll = self.get_defensive_roll()
        creatures_roll = creature.get_defensive_roll()

        # UI
        print(f'Your roll {my_roll}...')
        print(f'{creature.name} rolls {creatures_roll}...')

        if my_roll >= creatures_roll:
            # UI
            print(f'The wizard has handily triumphed over {creature.name}!')
            return True
        else:
            # UI
            print('The wizard has been DEFEATED!!!')
            return False


class SmallAnimal(Creature):

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return int(base_roll / 2)


class Dragon(Creature):

    def __init__(self, name, level_, scaliness, breaths_fire):
        super().__init__(name, level_)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10  # 10%
        return int(base_roll * fire_modifier * scale_modifier)

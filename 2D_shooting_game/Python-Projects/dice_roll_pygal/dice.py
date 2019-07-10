from random import randint


class Dice:
    """a class representing a single dice"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides  # default 6-sided dice

    def roll(self):
        return randint(1, self.num_sides)

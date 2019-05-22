from random import choice


class RandomWalk:
    """a class to generate coordinate pairs of random walk"""

    def __init__(self, num_points=5000):
        """initialize attributes of RandonWalk class"""
        self.num_points = num_points

        # define initial point
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all the points in the walk."""

        # keep tracking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # decide which direction to go and distance to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # if going nowhere, don't add to the walk sequence
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x and y values
            # your move should start from the previous position
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # add to the walk sequence
            self.x_values.append(next_x)
            self.y_values.append(next_y)

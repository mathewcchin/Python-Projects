from random_walk import RandomWalk
from matplotlib import pyplot as plt

# create an object
steps = RandomWalk()
steps.fill_walk()

# create a list representing point sequence
point_numbers = list(range(steps.num_points))

# plot random path
plt.scatter(steps.x_values, steps.y_values, s=1, c=point_numbers, cmap=plt.cm.Greens)
# plot origin
plt.scatter(0, 0, s=20)

plt.show()



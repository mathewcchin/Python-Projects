from random_walk import RandomWalk
from matplotlib import pyplot as plt

# create an object
steps = RandomWalk(150000)

# # plot random path
# plt.scatter(steps.x_values, steps.y_values, s=1)
# # plot origin
# plt.scatter(0, 0, s=20)

# create 10 random walk image
for i in range(0, 1):
    # clear previous figure
    plt.clf()

    # generate new random walk
    steps.fill_walk()

    # plot random path as scatter, and use colormap showing the sequence of the step
    plt.scatter(steps.x_values, steps.y_values, c=range(steps.num_points), cmap=plt.cm.Greens, s=1)

    # plot origin
    plt.scatter(0, 0, s=50, edgecolors='k', c='k')

    # plot end point
    plt.scatter(steps.x_values[-1], steps.y_values[-1], s=50, edgecolors='b', c='b')

    # fix axis range
    plt.axis([-500, 500, -500, 500])

    # save figure
    # plt.savefig('random_walk_' + str(i) + '.svg', bbox_inches='tight')

    # remove axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()


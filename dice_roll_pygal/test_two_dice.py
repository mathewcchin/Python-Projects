from matplotlib import pyplot as plt
import pygal

from dice import Dice

# initialize 2 dice and roll 1000 times, record result
d6 = Dice()
d6_2 = Dice(20)

results = []
for i in range(500):
    results.append(d6.roll() + d6_2.roll())

# count the occuring times of each number
num_frequency = []
for value in range(2, d6.num_sides + d6_2.num_sides + 1):
    num_frequency.append(results.count(value))

# visualize the results, create a hist
hist = pygal.Bar()

# add title and label
hist.title = "Result of rolling 1D6 1000 times"
hist.x_labels = [str(x) for x in range(2, d6.num_sides + d6_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# add data set to the hist
hist.add('D6', num_frequency)

# render to file
hist.render_to_file('dice_visual.svg')

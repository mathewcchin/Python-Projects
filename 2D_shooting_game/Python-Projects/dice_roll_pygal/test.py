from matplotlib import pyplot as plt
import pygal

from dice import Dice

# initialize one dice and roll 1000 times, record result
d6 = Dice()

results = []
for i in range(1000):
    results.append(d6.roll())

# count the occuring times of each number
num_frequency = []
for value in range(1, d6.num_sides + 1):
    num_frequency.append(results.count(value))

# visualize the results, create a hist
hist = pygal.Bar()

# add title and label
hist.title = "Result of rolling 1D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# add data set to the hist
hist.add('D6', num_frequency)
hist.add(values=50, title='D6')

# render to file
hist.render_to_file('dice_visual.svg')

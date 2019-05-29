import csv
import pygal
from datetime import datetime


date = []
high_temperature = []
low_temperature = []

# read from file, extract date and high temperature
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    reader.__next__()  # skip the first line
    for record in reader:
        date.append(datetime.strptime(record[0], '%Y-%m-%d'))
        high_temperature.append(float(record[1]))
        low_temperature.append(float(record[3]))

# plot a histogram
hist = pygal.Bar()
hist.x_labels = date  # add label to the bars
hist.add('High Temperature', high_temperature)  # add data to it
hist.add('Low Temperature', low_temperature)
hist.render_to_file('high_low_temperature.svg')

import csv
from matplotlib import pyplot as plt
from datetime import datetime


date = []
high_temperature = []
low_temperature = []

# read from file, extract date and high temperature
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    reader.__next__()  # skip the first line
    for record in reader:
        date.append(datetime.strptime(record[0], '%Y-%m-%d'))
        try:
            high_temperature.append(float(record[1]))
            low_temperature.append(float(record[3]))
        except ValueError:
            print(datetime.strptime(record[0], '%Y-%m-%d'), "missing data")
            date.pop()  # remove the date, since data is missing

# plot using matplotlib
fig = plt.figure(dpi=100, figsize=(10, 10))
# plt.plot(date, high_temperature, c='red')
# plt.plot(date, low_temperature, c='blue')
plt.scatter(date, high_temperature, s=100, edgecolors='red', c='None')
plt.scatter(date, low_temperature, s=100, edgecolors='blue', c='None')

# formating plot
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

# fill_between
plt.fill_between(date, high_temperature, low_temperature, facecolor='black', alpha=0.1)

plt.show()

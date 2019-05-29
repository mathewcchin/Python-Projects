import csv


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for index, item in enumerate(reader.__next__()):
        print(index, item)

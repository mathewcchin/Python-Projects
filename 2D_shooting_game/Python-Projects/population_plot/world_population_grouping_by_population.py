# the original svg figure shows little contrast between countries with less
# population. This is because value of China and India is too high, so the
# relative difference between other countries are small
# In this approach, we divide countries into three groups according to population
# and then we add it to the world map

import json
from pygal.maps.world import World
from country_code import find_country_code


from country_code import find_country_code


# get the raw data from file
filename = 'population_data.json'
with open(filename) as f:
    raw_data = json.load(f)

# extract data, picking those data in 2010
population_data_2010 = []

for record in raw_data:
    if record["Year"] == "2010":
        del record["Year"]
        code = find_country_code(record["Country Name"])
        if code:  # if country code was found
            record["Country Code"] = code  # update 3-digit code to 2-digit
            population_data_2010.append(record)
        else:
            print("Error: " + record["Country Name"] + " is invalid")

# store in dictionary to be worked with pygal
# pops_1: population < 10000000
# pops_2: 10000000 <= population <= 1000000000
# pops_3: population > 1000000000
pops_1, pops_2, pops_3 = {}, {}, {}

for record in population_data_2010:
    cc = find_country_code(record["Country Name"])
    population = int(float(record["Value"]))
    if population < 10000000:
        pops_1[cc] = population
    elif population <= 1000000000:
        pops_2[cc] = population
    else:
        pops_3[cc] = population


# plot
world_population_map = World()
world_population_map.title = 'World Population Map'

world_population_map.add('< 10m', pops_1)
world_population_map.add('10m - 1bn', pops_2)
world_population_map.add('>1bn', pops_3)

world_population_map.render_to_file('World Population Map (grouping countries by population).svg')

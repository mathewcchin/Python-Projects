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
population_dict_2010 = {}

for record in population_data_2010:
    population_dict_2010[find_country_code(record["Country Name"])] = int(float(record["Value"]))

# plot
world_population_map = World()
world_population_map.title = 'World Population Map'
world_population_map.add('World Population Map', population_dict_2010)
world_population_map.render_to_file('World Population Map.svg')

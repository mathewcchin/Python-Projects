import pygal
from pygal.maps.world import World


wm = World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 341260000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('North America Population.svg')


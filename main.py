from presets import *
from classes.simulation import *

def check_size(size):
    if size == None:
        result = (1000, 600)
    else: 
        result = size
    return result

bodies, size = earth_sun()
# bodies = earth_sun_moon()
# bodies = two_planets()

sim = Simulation(bodies=bodies, size=check_size(size))
sim.show_env()

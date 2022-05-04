from presets import *
from classes.simulation import *

def check_size(size):
    if size == None:
        result = (1000, 600)
    else: 
        result = size
    return result

# bodies, size = earth_sun()
# bodies, size = earth_sun_moon()
# bodies, size = two_planets()
bodies, size = two_planet_system()

sim = Simulation(bodies=bodies, size=check_size(size))
sim.show_env()

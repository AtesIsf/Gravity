from presets import *
from classes.simulation import *

bodies = earth_sun()
# bodies = earth_sun_moon()
# bodies = two_planets()

sim = Simulation(bodies=bodies)
sim.show_env()

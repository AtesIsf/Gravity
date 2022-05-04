import numpy as np
from classes.body import Body

def earth_sun():
    one = Body(
        name="Star", position=(500, 300),  
        color=(155,155,0), radius=50, mass=10.0 ** 15
    )

    two = Body(
        name="Planet", position=(700, 300), 
        color=(0, 100, 0), radius=15, mass=10.0 ** 10,
        has_trail=True, velocity=(0, 250)
    )
    return np.array((one, two)), None

def two_planets():
    one = Body(
        position=(400, 300), color = (0, 0, 155),
        radius = 15, mass = 10 ** 15,
        has_trail=True,velocity=(0, -200)
    )

    two = Body(
        position=(600, 300), color = (0, 155, 0),
        radius = 15, mass = 10 ** 15,
        has_trail=True,velocity=(0, 200)
    )
    return np.array((one, two)), None

def earth_sun_moon():
    one = Body(
        name="Star", position=(500, 300),  
        color=(155,155,0), radius=50, mass=10.0 ** 20
    )

    two = Body(
        name="Planet", position=(700, 300), 
        color=(0, 100, 0), radius=15, mass=10.0 ** 10,
        has_trail=True, velocity=(0, 200)
    )

    three = Body(
        name="Moon", position=(700, 280),
        color = (155, 155, 155), radius=5, mass=10 ** 8,
        has_trail=True, velocity=(100, 50)
    )

    return np.array((one, two, three)), None
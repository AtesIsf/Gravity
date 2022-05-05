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
        velocity=(0, 250)
    )
    return np.array((one, two)), None

def two_planets():
    one = Body(
        position=(400, 300), color = (0, 0, 155),
        radius = 15, mass = 10 ** 15,
        velocity=(0, -200)
    )

    two = Body(
        position=(600, 300), color = (0, 155, 0),
        radius = 15, mass = 10 ** 15,
        velocity=(0, 200)
    )
    return np.array((one, two)), None

def earth_sun_moon(): # TODO

    one = Body(
        name="Sun", position=(500, 300),  
        color=(155,155,0), radius=50, mass=10.0 ** 15
    )

    two = Body(
        name="Earth", position=(700, 300), 
        color=(0, 100, 0), radius=15, mass=10.0 ** 10,
        velocity=(0, 200)
    )

    three = Body(
        name="Moon", position=(725, 300),
        color = (155, 155, 155), radius=5, mass=10 ** 9,
        velocity=(0,250)
    )

    return np.array((one, two, three)), None

def cool_two_planet_system():

    one = Body(
    name="Star", position=(500, 300),  
    color=(155,155,0), radius=50, mass=10.0 ** 15
    )

    two = Body(
        position=(800, 300), 
        color=(0, 100, 0), radius=15, mass=10.0 ** 10,
        velocity=(0, 200)
    )

    three = Body(
        position=(400, 300), 
        color=(100, 0, 0), radius=15, mass=10.0 **8,
        velocity=(0, -250)
    )

    return np.array((one, two, three)), None

def simple_two_planet_system():

    one = Body(
    name="Star", position=(500, 300),  
    color=(155,155,0), radius=50, mass=10.0 ** 15
    )

    two = Body(
        position=(700, 300), 
        color=(0, 100, 0), radius=15, mass=10.0 ** 10,
        velocity=(0, 250)
    )

    three = Body(
        position=(400, 300), 
        color=(100, 0, 0), radius=15, mass=10.0 **8,
        velocity=(0, -250)
    )

    return np.array((one, two, three)), None

def three_planet_system():

    size = (1000, 800)

    one = Body(
    name="Star", position=(500, 400),  
    color=(155,155,0), radius=50, mass=10.0 ** 15
    )

    two = Body(
        position=(700, 400), 
        color=(0, 100, 0), radius=15, mass=10.0 ** 10, 
        velocity=(0, 250)
    )

    three = Body(
        position=(400, 400), 
        color=(100, 0, 0), radius=15, mass=10.0 ** 8,
        velocity=(0, -250)
    )

    four = Body(
        position=(500, 100), 
        color=(0, 0, 155), radius=15, mass=10.0 ** 12,
        velocity=(250, 0)
    )

    return np.array((one, two, three, four)), size

def asteroid():
    size = (1000, 800)

    one = Body(
        name="Star", position=(500, 400),  
        color=(155,155,0), radius=50, mass=10.0 ** 15
    )

    two = Body(
        position=(400, 400), 
        color=(0, 100, 0), radius=15, mass=10.0 ** 10,
        velocity=(0, -250)
    )

    three = Body(
        name="Asteroid I", position=(1000, 800),
        color = (100, 100, 100), radius=5, mass=10.0 ** 8,
        velocity=(-150, -200)
    )

    four = Body(
        name="Asteroid II", position=(350, 0),
        color=(155, 155, 155), radius=5, mass = 10 ** 8,
        velocity=(-50, 200)
    )

    return np.array((one, two, three, four)), size
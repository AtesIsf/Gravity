import numpy as np
import math

magnitude = lambda  arr : np.sqrt((arr[0] ** 2) + (arr[1] ** 2))

# Normalize a vector into the range 0-1
def unit_vector(vec):
    mag = magnitude(vec)
    for i in vec:
        i/=mag
    return np.array(vec)
    
class PhysicsEngine:
    
    def __init__(self, bodies):
        self.body_pos_list = []

        self.body_arr = []
        for body in bodies:
            self.body_arr.append(body)
        self.body_arr = np.array(self.body_arr)

    def compute_forces(self):
        distances = []
        forces = dict()

        # Net Force Calculation for each body
        for M in self.body_arr:
            forces[M.name] = np.zeros(2)
            for m in self.body_arr:
                if M.name == m.name:
                    continue
                distance_comps = (M.position - m.position) * np.array((-1, -1))

                if magnitude(distance_comps) == 0:
                    pass
                else:
                    # F = G (Mm)/d^2
                    force = 6.67 * (10 ** -11) * M.mass * m.mass / (magnitude(distance_comps) ** 2)
                    force *= unit_vector(distance_comps)
                    forces[M.name] += force
        return forces
                
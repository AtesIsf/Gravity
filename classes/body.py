import math
import numpy as np
import pygame
import time

TIME_STEP = 0.0005

used_names = []

class Body:                                                                         # Random capital letter
    def __init__(self, position, mass, color, has_trail = True, trail_color = None, radius=5, name=None, velocity = (0.0, 0.0), text_color = (255, 255, 255)):
        # Assign parameters
        self.position =np.array(position, dtype="float64")
        self.mass = mass
        self.color = color
        self.radius = radius
        self.life = radius # * 2000
        self.perimeter = self.radius * 2
        self.has_trail = has_trail
        if trail_color == None:
            self.trail_color = np.append(np.array(color), 100)
        else:
            self.trail_color = np.append(np.array(trail_color), 100)
        self.text_color = text_color
        self.destroyed = False

        # Create empty vectors
        self.velocity = np.array(velocity, dtype="float64")
        self.force = np.zeros((2), dtype="float64")

        # Assign random capital letter (Each name should be unique)
        if name == None:
            while True:
                nm = chr(np.random.randint(65, 91))
                if nm not in used_names:
                    break
            self.name = nm
            used_names.append(self.name)
        else:
            self.name = name

    def draw(self, surface, space, font):
        if self.destroyed:
            return
        pygame.draw.circle(surface, self.color, (self.position), self.radius, self.perimeter)
        if self.has_trail == True:
            pygame.draw.circle(space, self.trail_color, self.position, 3, 6)
        text_surface = font.render(self.name, False, self.text_color)
        surface.blit(text_surface, self.position + np.array((0, self.radius)))

    def move(self):
        if self.destroyed:
            self.life -= 1
        if self.life > 0:
            self.velocity += (self.force / self.mass) * TIME_STEP # v = u + at
            self.position += self.velocity * TIME_STEP # s = vt
            print(f"{self.name}: [{self.velocity[0]}, {self.velocity[1] * -1}]")

    def check_collision(self, other):
        collision = False
        distance_vec = self.position-other.position
        distance = math.sqrt(distance_vec[0]**2 + distance_vec[1]**2)

        if distance <= (self.radius + other.radius):
            collision = True
            if self.radius == other.radius:
                self.destroyed = True
                other.destroyed = True
            elif self.radius > other.radius:
                other.destroyed = True
            elif other.radius > self.radius:
                self.destroyed = True
        return collision            

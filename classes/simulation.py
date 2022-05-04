import pygame
import time
from classes.physics import *

class Simulation:
    def __init__(self, bodies, size=(1000, 600)):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 20)
        pygame.display.set_caption("2D Gravity Simulation")
        self.space = pygame.display.set_mode(size)
        self.trans_space = pygame.Surface(size, pygame.SRCALPHA)

        self.bodies = bodies
        self.physics_engine = PhysicsEngine(bodies=bodies)

    def show_env(self):
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            forces = self.physics_engine.compute_forces()
            for key in forces:
                for body in self.bodies:
                    if body.name == key:
                        body.force = forces[key]
            
            self.space.fill((0, 0, 0))
            self.space.blit(self.trans_space, (0,0))

            for body in self.bodies:
                body.draw(self.space, self.trans_space, self.font)

            for body in self.bodies:
                body.move()

            time.sleep(0.0005)
            pygame.display.update()

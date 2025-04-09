import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.rotation_speed = 0
        self.rotation_speed = pygame.Vector2(0, 1).rotate(self.rotation)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        # Create two smaller asteroids
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vectorA = self.velocity.rotate(angle)
        vectorB = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroidA = Asteroid(self.position.x, self.position.y, new_radius)
        asteroidA.velocity = vectorA * 1.2
        asteroidB = Asteroid(self.position.x, self.position.y, new_radius)
        asteroidB.velocity = vectorB * 1.2

import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)  # Initialize the CircleShape parent
        
        # Create a vector pointing up
        direction_vector = pygame.Vector2(0, 1)  
        
        # Rotate it to match the player's direction
        direction_vector = direction_vector.rotate(direction)
        
        # Scale it by the speed
        self.velocity = direction_vector * PLAYER_SHOOT_SPEED


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
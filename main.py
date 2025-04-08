# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import *
# First import Asteroid fully
from asteroid import Asteroid
# Then import AsteroidField
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print(f'''Starting Asteroids!\n
          Screen width: {SCREEN_WIDTH}\n
          Screen height: {SCREEN_HEIGHT}\n''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    dt = 0  # Initialize delta time

    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    #assigning groups
    Player.containers = updatable, drawable
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable


    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Properly quit pygame
                return  # Exit the function and the game loop


        screen.fill((0, 0, 0))  # Fill the screen with black

        # loop all the drawables
        for entity in drawable:
            entity.draw(screen) 
        updatable.update(dt)

        # loop all the asteroids
        for entity in asteroids:
            if entity.collides(player):
                print("Game Over!")
                pygame.quit()  # Properly quit pygame
                return


        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS


if __name__ == "__main__":
    main()
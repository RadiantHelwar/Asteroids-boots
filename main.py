# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print(f'''Starting Asteroids!\n
          Screen width: {SCREEN_WIDTH}\n
          Screen height: {SCREEN_HEIGHT}\n''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display


if __name__ == "__main__":
    main()
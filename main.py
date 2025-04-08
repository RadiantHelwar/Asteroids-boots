# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print(f'''Starting Asteroids!\n
          Screen width: {SCREEN_WIDTH}\n
          Screen height: {SCREEN_HEIGHT}\n''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    dt = 0  # Initialize delta time

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Properly quit pygame
                return  # Exit the function and the game loop


        screen.fill((0, 0, 0))  # Fill the screen with black

        player.draw(screen)  # Draw the player
        player.update(dt)

        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS


if __name__ == "__main__":
    main()
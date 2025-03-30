import pygame

from constants import *  # noqa: F403
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # noqa: F405
    dt = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with a color
        screen.fill((0, 0, 0))
        player.draw(screen)

        # Update the display
        pygame.display.flip()
        de = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

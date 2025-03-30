import pygame

from constants import *  # noqa: F403


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with a color
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
    
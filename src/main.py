import pygame

FPS = 60

SCREEN_SIZE = 600
CELL_SIZE = SCREEN_SIZE / 8

BACKGROUND = (0, 0, 0)
LIGHT_CELL = (240, 217, 181)
DARK_CELL = (181, 136, 99)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Checkers")
    clock = pygame.time.Clock()

    running = True
    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(BACKGROUND)

        # RENDER YOUR GAME HERE
        draw_board(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS

    pygame.quit()


def draw_board(screen):
    for y in range(8):
        for x in range(8):
            color = LIGHT_CELL if (x + y) % 2 == 0 else DARK_CELL
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


if __name__ == "__main__":
    main()

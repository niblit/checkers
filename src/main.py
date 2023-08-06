import pygame

FPS = 60
SCREEN_SIZE = WIDTH, HEIGHT = (600, 600)
BACKGROUND = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
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

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS

    pygame.quit()

if __name__ == "__main__":
    main()

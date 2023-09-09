import pygame
from enum import Enum

FPS = 60

SCREEN_SIZE = 600
CELL_SIZE = SCREEN_SIZE / 8

BACKGROUND = (0, 0, 0)
LIGHT_CELL = (240, 217, 181)
DARK_CELL = (181, 136, 99)


class Piece(Enum):
    Empty = 0
    White = 1
    Black = 2


black = "../assets/b.svg"
black_texture = pygame.transform.smoothscale(pygame.image.load(black), (CELL_SIZE, CELL_SIZE))

white = "../assets/w.svg"
white_texture = pygame.transform.smoothscale(pygame.image.load(white), (CELL_SIZE, CELL_SIZE))


def get_rect(x, y):
    return pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)


board = [
    [Piece.Black for _ in range(8)],
    [Piece.Black for _ in range(8)],
    [Piece.Empty for _ in range(8)],
    [Piece.Empty for _ in range(8)],
    [Piece.Empty for _ in range(8)],
    [Piece.Empty for _ in range(8)],
    [Piece.White for _ in range(8)],
    [Piece.White for _ in range(8)]
]


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
        draw_pieces(screen, board)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS

    pygame.quit()


def draw_board(screen):
    for y in range(8):
        for x in range(8):
            color = LIGHT_CELL if (x + y) % 2 == 0 else DARK_CELL
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_pieces(screen, board):
    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece == Piece.Empty:
                continue
            elif piece == Piece.Black:
                screen.blit(black_texture, get_rect(x * CELL_SIZE, y * CELL_SIZE))
            elif piece == Piece.White:
                screen.blit(white_texture, get_rect(x * CELL_SIZE, y * CELL_SIZE))


if __name__ == "__main__":
    main()

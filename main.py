import pygame
import os

pygame.init()

width, height = (700, 700)
size = width, height
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 50
        self.top = 90
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size),
                                 1)

    def get_cell(self, mouse_pos):
        celi_x = mouse_pos[0] // (self.cell_size + self.left)
        celi_y = mouse_pos[1] // (self.cell_size + self.top)
        if not (
                celi_x < 0 or celi_x >= self.width or celi_y < 0 or celi_y >= self.height):
            return celi_y, celi_x


board = Board(20, 20)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class T:
    def __init__(self):
        global board
        self.chast = list()
        self.x = 0
        self.y = 0

    def create_shape(self):
        z = load_image('tetris.png', -1)
        first_coord = (210, self.y + 18)
        screen.blit(z, (210, self.y + 18))
        self.add_in_board(first_coord)
        second_coord = (210, self.y + 48)
        screen.blit(z, second_coord)
        self.add_in_board(second_coord)
        three_cord = (210, self.y + 78)
        screen.blit(z, three_cord)
        self.add_in_board(three_cord)
        four_coord = (240, self.y + 48)
        screen.blit(z, (240, self.y + 48))
        self.add_in_board(four_coord)

    def add_in_board(self, coord):
        f = board.get_cell((coord[0], coord[1]))
        board.board[f[0]][f[1]] = 1


running = True
f = T()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    f.y += 30
    clock.tick(2)
    f.create_shape()
    board.render()
    pygame.display.flip()
pygame.display.flip()

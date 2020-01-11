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

    def get_cell(self, mouse_pos):
        celi_x = mouse_pos[0] // self.cell_size
        celi_y = mouse_pos[1] // self.cell_size
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
        self.x = 210
        self.y = 0
        self.flag = True

    def create_shape(self):
        z = load_image('tetris.png', -1)
        first_coord = (self.x, self.y + 48)
        fir = self.check_coord(first_coord)
        screen.blit(z, first_coord)
        second_coord = (self.x, self.y + 78)
        sec = self.check_coord(second_coord)
        screen.blit(z, second_coord)
        three_cord = (self.x, self.y + 108)
        three = self.check_coord(three_cord)
        screen.blit(z, three_cord)
        four_coord = (self.x + 30, self.y + 78)
        four = self.check_coord(four_coord)
        screen.blit(z, four_coord)
        clock.tick(2)
        if three[0] == 19 or board.board[three[1]][three[0] + 1] == 1 or board.board[four[0]] == 0 and \
                board.board[four[0] + 1] == 1:
            self.add_in_board(fir)
            self.add_in_board(sec)
            self.flag = False
            self.add_in_board(three)
            self.add_in_board(four)

    def check_coord(self, coord):
        f = board.get_cell((coord[0], coord[1]))
        return f

    def add_in_board(self, coord):
        board.board[coord[0]][coord[1]] = (1, 'blue')
        print(board.board)

    def second(self):
        z = load_image('tetris.png', -1)
        first_coord = (self.x, self.y + 48)
        fir = self.check_coord(first_coord)
        screen.blit(z, first_coord)
        second_coord = (self.x - 30, self.y + 48)
        sec = self.check_coord(second_coord)
        screen.blit(z, second_coord)
        three_cord = (self.x + 30, self.y + 48)
        three = self.check_coord(three_cord)
        screen.blit(z, three_cord)
        four_coord = (self.x, self.y + 78)
        four = self.check_coord(four_coord)
        screen.blit(z, four_coord)
        if four[0] == 19 or board.board[four[1]][four[0] + 1] == 1 or board.board[four[0]] == 0 and \
                board.board[four[0] + 1] == 1:
            self.add_in_board(fir)
            self.add_in_board(sec)
            self.flag = False
            self.add_in_board(three)
            self.add_in_board(four)


running = True
f = T()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                f.x += 30
            elif event.key == pygame.K_LEFT:
                f.x -= 30
            elif event.key == pygame.K_DOWN:
                f.y += 30
    if f.flag:
        screen.fill((0, 0, 0))
        f.second()
        f.y += 30
        clock.tick(2)
        pygame.display.flip()
    pygame.display.flip()

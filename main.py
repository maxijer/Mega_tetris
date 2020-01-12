import pygame
import os

pygame.init()

pygame.joystick.init()

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
        self.board = [['0'] * width for _ in range(height)]
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
        self.glav = 'create_shape'
        self.func = ['create_shape', 'second', 'three', 'four']
        self.flag = True
        self.krai_left = (7, 1)
        self.krai_right = (7, 2)
        self.krai_down = (7, 3)

    def create_shape(self):
        first_coord = (self.x, self.y + 48)
        second_coord = (self.x, self.y + 78)
        three_cord = (self.x, self.y + 108)
        four_coord = (self.x + 30, self.y + 78)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 1)

    def master_shape(self, first_coord, second_coord, three_coord,
                     four_coord, shape):  # оптимизация и расстановка фигур
        z = load_image('tetris.png', -1)
        fir = self.check_coord(first_coord)
        sec = self.check_coord(second_coord)
        three = self.check_coord(three_coord)
        four = self.check_coord(four_coord)
        screen.blit(z, first_coord)
        screen.blit(z, second_coord)
        screen.blit(z, three_coord)
        screen.blit(z, four_coord)
        if shape == 1:
            if three[0] <= 19:
                if three[0] == 19 or board.board[three[0] + 1][three[1]] != '0' or \
                        board.board[four[0] + 1][four[1]] != '0':
                    self.no_problen(fir, first_coord, sec, second_coord, three, three_coord, four,
                                    four_coord)

        elif shape == 2:
            self.krai_left = sec
            self.krai_right = three
            self.krai_down = four
            if four[0] == 19 or board.board[three[0] + 1][three[1]] != '0' or board.board[
                sec[0] + 1][sec[1]] != '0' or board.board[four[0] + 1][four[1]] != '0':
                self.no_problen(fir, first_coord, sec, second_coord, three, three_coord, four,
                                four_coord)

        elif shape == 3:
            if three[0] == 19 or board.board[four[0] + 1][four[1]] != '0' or board.board[three[0] + 1][
                three[1]] != '0':
                self.no_problen(fir, first_coord, sec, second_coord, three, three_coord, four,
                                four_coord)
        elif shape == 4:
            if sec[0] == 19 or board.board[sec[0] + 1][sec[1]] != '0' or board.board[three[0] + 1][
                three[1]] != '0' or board.board[fir[0] + 1][fir[1]] != '0':
                self.no_problen(
                    fir, first_coord, sec, second_coord, three, three_coord, four, four_coord)
                self.krai_left = sec
                self.krai_right = three
                self.krai_down = fir

    def no_problen(self, fir, first_coord, sec, second_coord, three, three_coord, four,
                   four_coord):  # добавление на доску , сокращение copy paste
        self.add_in_board(fir, first_coord)
        self.add_in_board(sec, second_coord)
        self.flag = False
        self.add_in_board(three, three_coord)
        self.add_in_board(four, four_coord)

    def check_coord(self, coord):
        f = board.get_cell((coord[0], coord[1]))
        return f

    def add_in_board(self, coord, vse):
        board.board[coord[0]][coord[1]] = (vse, 'blue')

    def second(self):
        first_coord = (self.x, self.y + 48)
        second_coord = (self.x - 30, self.y + 48)
        three_cord = (self.x + 30, self.y + 48)
        four_coord = (self.x, self.y + 78)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 2)

    def three(self):
        first_coord = (self.x, self.y + 48)
        second_coord = (self.x, self.y + 78)
        three_cord = (self.x, self.y + 108)
        four_coord = (self.x - 30, self.y + 78)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 3)

    def four(self):
        first_coord = (self.x, self.y + 48)
        second_coord = (self.x - 30, self.y + 48)
        three_cord = (self.x + 30, self.y + 48)
        four_coord = (self.x, self.y + 18)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 4)

    def game(self, position):
        if position == 1:
            if event.type == pygame.KEYDOWN:
                print(board.board)
                if event.key == pygame.K_RIGHT:
                    if f.x + 60 < 570 and f.y + 138 < 500 and (len(board.board[f.check_coord((f.x + 30, f.y))[0] + 1][
                                                   f.check_coord((f.x + 30, f.y))[
                                                       1]]) == 1 and
                                           (len(
                    board.board[f.check_coord((f.x + 30, f.y + 138))[0] + 1][
                    f.check_coord((f.x + 30, f.y + 138))[
                    1] + 1]) == 1)):
                        print(f.check_coord((f.x + 60, f.y + 180)))
                        print(board.board)
                        f.x += 30
                elif event.key == pygame.K_LEFT:
                    if f.x - 60 < 570 and (len(board.board[f.check_coord((f.x - 60, f.y + 108))[0]][
                                                   f.check_coord((f.x - 60, f.y + 108))[
                                                       1]]) == 1 and len(
                        board.board[f.check_coord((f.x - 30, f.y + 60))[0]][
                            f.check_coord((f.x - 30, f.y + 60))[
                                1]])):
                        f.x -= 30
                elif event.key == pygame.K_DOWN:
                    if f.y + 30 < 480 and len(
                            board.board[f.check_coord((f.x, f.y + 108 + 30))[0] + 1][
                                f.check_coord((f.x, f.y + 108 + 30))[1]]) == 1:
                        f.y += 30
                elif event.key == pygame.K_SPACE:
                    z = f.func.index(f.glav)
                    if f.y != 30:
                        if z == len(f.func) - 1:
                            z = -1
                            f.glav = f.func[0]
                        else:
                            f.glav = f.func[z + 1]
                        q = f'f.{f.func[z + 1]}()'

    def first_check_position(self):
        if f.x + 60 < 570:
            return True

    def first_check_2(self):
        pass


running = True
f = T()
glav = ''
go_flag = False
q = 'f.create_shape()'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        f.game(1)

    if f.flag:
        screen.fill((0, 0, 0))
        for j in range(len(board.board)):
            for i in range(len(board.board[j])):
                if len(board.board[i][j]) == 2:
                    if board.board[i][j][1] == 'blue':
                        image = load_image('tetris.png', -1)
                        r = board.board[i][j][0][0]
                        per = board.board[i][j][0][1]
                        screen.blit(image, (r, per))

        f.y += 30
        exec(q)
        clock.tick(5)
        pygame.display.flip()
    else:
        go_flag = True
    if go_flag:
        f = T()
        go_flag = False
    pygame.display.flip()

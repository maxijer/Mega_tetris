import pygame
import os
import random

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


class O:
    def __init__(self):
        global board
        self.chast = list()
        self.x = 210
        self.y = 0
        self.pos = [1, 2, 3, 4]
        self.glav = 'create_shape'
        self.func = ['create_shape']
        self.flag = True
        color = random.choice(['red', 'blue'])
        self.color = color
        if color == 'red':
            self.z = load_image('red.png', -1)
        else:
            self.z = load_image('tetris.png', -1)

    def create_shape(self):
        first_coord = (self.x, self.y + 78)
        second_coord = (self.x, self.y + 48)
        three_cord = (self.x + 30, self.y + 48)
        four_coord = (self.x + 60, self.y + 48)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 1)

    def master_shape(self, first_coord, second_coord, three_coord,
                     four_coord, shape):  # оптимизация и расстановка фигур
        fir = self.check_coord(first_coord)
        sec = self.check_coord(second_coord)
        print(sec)
        three = self.check_coord(three_coord)
        four = self.check_coord(four_coord)
        screen.blit(self.z, first_coord)
        screen.blit(self.z, second_coord)
        screen.blit(self.z, three_coord)
        screen.blit(self.z, four_coord)
        if shape == 1:
            if sec[0] <= 19:
                if sec[0] == 19 or board.board[sec[0] + 1][sec[1]] != '0' or \
                        board.board[four[0] + 1][four[1]] != '0' or \
                        board.board[four[0] + 1][
                            four[1]] != '0':
                    self.no_problen(fir, first_coord, sec, second_coord, three,
                                    three_coord, four,
                                    four_coord)

    def no_problen(self, fir, first_coord, sec, second_coord, three,
                   three_coord, four,
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
        board.board[coord[0]][coord[1]] = (vse, self.color)

    def game(self, position):
        global q
        if position == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if f.x + 60 <= 570 and f.y < 430 and len(
                            board.board[f.check_coord((f.x + 30, f.y + 78))[
                                            0] + 1][
                                f.check_coord((f.x + 30, f.y + 78))[
                                    1] + 1]) == 1 and len(
                        board.board[f.check_coord((f.x + 30, f.y + 48))[
                                        0] + 1][
                            f.check_coord((f.x + 30, f.y + 38))[1]]) == 1:
                        f.x += 30
                elif event.key == pygame.K_LEFT:
                    if f.x - 60 > 10 and (len(board.board[f.check_coord(
                            (f.x - 30, f.y + 48))[0] + 1][
                                                  f.check_coord(
                                                      (f.x - 30, f.y + 48))[
                                                      1] + 1]) == 1 and f.y < 430 and (
                                                  len(
                                                      board.board[
                                                          f.check_coord((
                                                                  f.x - 30,
                                                                  f.y + 78))[
                                                              0] + 1][
                                                          f.check_coord((
                                                                  f.x - 30,
                                                                  f.y + 78))[
                                                              1]]) == 1)):
                        f.x -= 30
                elif event.key == pygame.K_DOWN:
                    if f.y + 30 < 480 and len(
                            board.board[
                                f.check_coord((f.x, f.y + 108))[0] + 1][
                                f.check_coord((f.x, f.y + 108))[1]]) == 1 and \
                            len(board.board[
                                    f.check_coord((f.x + 30, f.y + 108))[
                                        0] + 1][
                                    f.check_coord((f.x + 30, f.y + 108))[
                                        1]]) == 1:
                        f.y += 30


class S:
    def __init__(self):
        global board
        self.chast = list()
        self.x = 210
        self.y = 0
        self.pos = [1, 2, 3, 4]
        self.glav = 'create_shape'
        self.func = ['create_shape']
        self.flag = True
        color = random.choice(['red', 'blue'])
        self.color = color
        if color == 'red':
            self.z = load_image('red.png', -1)
        else:
            self.z = load_image('tetris.png', -1)

    def create_shape(self):
        first_coord = (self.x, self.y + 48)
        second_coord = (self.x, self.y + 78)
        three_cord = (self.x + 30, self.y + 48)
        four_coord = (self.x + 30, self.y + 18)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 1)

    def master_shape(self, first_coord, second_coord, three_coord,
                     four_coord, shape):  # оптимизация и расстановка фигур
        self.krai_up = self.check_coord(four_coord)
        self.krai_right = self.check_coord(three_coord)
        self.krai_left = self.check_coord(first_coord)
        self.krai_down = self.check_coord(second_coord)
        screen.blit(self.z, first_coord)
        screen.blit(self.z, second_coord)
        screen.blit(self.z, three_coord)
        screen.blit(self.z, four_coord)
        if shape == 1:
            if self.krai_down[0] <= 19:
                if self.krai_down[0] == 19 or board.board[self.krai_down[0] + 1][
                    self.krai_down[1]] != '0' or \
                        board.board[self.krai_right[0] + 1][self.krai_right[1]] != '0':
                    self.no_problen(self.krai_up, four_coord, self.krai_right, three_coord,
                                    self.krai_left,
                                    first_coord, self.krai_down,
                                    second_coord)

    def no_problen(self, fir, first_coord, sec, second_coord, three,
                   three_coord, four,
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
        board.board[coord[0]][coord[1]] = (vse, self.color)

    def game(self, position):
        global q
        if position == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if f.x + 60 <= 570 and f.y < 430 and len(
                            board.board[f.check_coord((f.x + 30, f.y + 78))[
                                            0] + 1][
                                f.check_coord((f.x + 30, f.y + 78))[
                                    1] + 1]) == 1 and len(
                        board.board[f.check_coord((f.x + 30, f.y + 48))[
                                        0] + 1][
                            f.check_coord((f.x + 30, f.y + 38))[1]]) == 1:
                        f.x += 30
                elif event.key == pygame.K_LEFT:
                    if f.x - 60 > 10 and (len(board.board[f.check_coord(
                            (f.x - 30, f.y + 48))[0] + 1][
                                                  f.check_coord(
                                                      (f.x - 30, f.y + 48))[
                                                      1] + 1]) == 1 and f.y < 430 and (
                                                  len(
                                                      board.board[
                                                          f.check_coord((
                                                                  f.x - 30,
                                                                  f.y + 78))[
                                                              0] + 1][
                                                          f.check_coord((
                                                                  f.x - 30,
                                                                  f.y + 78))[
                                                              1]]) == 1)):
                        f.x -= 30
                elif event.key == pygame.K_DOWN:
                    if f.y + 30 < 480 and len(
                            board.board[
                                f.check_coord((f.x, f.y + 108))[0] + 1][
                                f.check_coord((f.x, f.y + 108))[1]]) == 1 and \
                            len(board.board[
                                    f.check_coord((f.x + 30, f.y + 108))[
                                        0] + 1][
                                    f.check_coord((f.x + 30, f.y + 108))[
                                        1]]) == 1:
                        f.y += 30


def move(f, hod):
    if hod == 'left':
        if f.krai_left[1] >= 3 and f.y < 470 and board.board[
            f.krai_left[0]][f.krai_left[1] - 1] == '0' and board.board[f.krai_down[0]][
            f.krai_down[1] - 1] == '0' and \
                board.board[f.krai_up[0]][f.krai_up[1] - 1] == '0' and \
                board.board[f.krai_right[0]][f.krai_right[1] - 1] == '0' and f.y < 500 and board.board[
            f.krai_left[0] + 1][f.krai_left[1] - 1] == '0' and board.board[f.krai_down[0] + 1][
            f.krai_down[1] - 1] == '0' and \
                board.board[f.krai_up[0] + 1][f.krai_up[1] - 1] == '0' and \
                board.board[f.krai_right[0] + 1][f.krai_right[1] - 1] == '0' and f.y < 500:
            return True
    elif hod == 'right':
        if f.krai_right[1] <= 18 and f.y < 470 and board.board[
            f.krai_left[0]][f.krai_left[1] + 1] == '0' and board.board[f.krai_down[0]][
            f.krai_down[1] + 1] == '0' and \
                board.board[f.krai_up[0]][f.krai_up[1] + 1] == '0' and \
                board.board[f.krai_right[0]][f.krai_right[1] + 1] == '0' and f.y < 470 and board.board[
            f.krai_left[0] + 1][f.krai_left[1] + 1] == '0' and board.board[f.krai_down[0] + 1][
            f.krai_down[1] + 1] == '0' and \
                board.board[f.krai_up[0] + 1][f.krai_up[1] + 1] == '0' and \
                board.board[f.krai_right[0] + 1][f.krai_right[1] + 1] == '0':
            return True
    return False


class I:
    def __init__(self):
        global board, game1
        self.chast = list()
        self.x = 210
        self.y = 0
        self.pos = [1, 2]
        self.glav = 'create_shape'
        self.func = ['create_shape', 'second']
        self.flag = True
        color = random.choice(['red', 'blue'])
        self.color = color
        if color == 'red':
            self.z = load_image('red.png', -1)
        else:
            self.z = load_image('tetris.png', -1)

    def create_shape(self):
        first_coord = (self.x, self.y + 48)
        second_coord = (self.x, self.y + 78)
        three_cord = (self.x, self.y + 108)
        four_coord = (self.x, self.y + 138)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 1)

    def master_shape(self, first_coord, second_coord, three_coord,
                     four_coord, shape):  # оптимизация и расстановка фигур
        self.krai_up = self.check_coord(first_coord)
        self.krai_right = self.check_coord(second_coord)
        self.krai_left = self.check_coord(three_coord)
        self.krai_down = self.check_coord(four_coord)
        screen.blit(self.z, first_coord)
        screen.blit(self.z, second_coord)
        screen.blit(self.z, three_coord)
        screen.blit(self.z, four_coord)
        if shape == 1:
            if self.krai_down[0] == 19 or board.board[self.krai_down[0] + 1][self.krai_down[1]] != '0':
                self.no_problen(self.krai_up, first_coord, self.krai_right, second_coord,
                                self.krai_left,
                                three_coord, self.krai_down,
                                four_coord)

    def no_problen(self, fir, first_coord, sec, second_coord, three,
                   three_coord, four,
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
        board.board[coord[0]][coord[1]] = (vse, self.color)

    def second(self):
        first_coord = (self.x + 30, self.y + 48)
        second_coord = (self.x + 60, self.y + 48)
        three_cord = (self.x + 90, self.y + 48)
        four_coord = (self.x + 120, self.y + 48)
        self.master_shape(first_coord, second_coord, three_cord, four_coord, 2)

    def game(self, position):
        global q
        if position == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if move(f, 'left'):
                        f.x -= 30
                elif event.key == pygame.K_RIGHT:
                    if move(f, 'right'):
                        f.x += 30
                elif event.key == pygame.K_DOWN:
                    if move(f, 'down'):
                        f.y += 30
        elif position == 2:
            fir = self.check_coord((f.x, f.y + 48))
            sec = self.check_coord((f.x, self.y + 78))
            three = self.check_coord((f.x, self.y + 108))
            four = self.check_coord((f.x, self.y + 138))
            print(board.board)
            global game1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if four[1] + 1 <= 19 and board.board[four[0]][four[1] + 1] == '0' and f.y < 430 and \
                            board.board[four[0] + 1][four[1] + 1] == '0':
                        f.x += 30
                elif event.key == pygame.K_LEFT:
                    if fir[1] - 1 >= 2 and board.board[four[0]][four[1] - 1] == '0' and f.y <= 430 and \
                            board.board[four[0] + 1][four[1] - 1] == '0':
                        f.x -= 30
                elif event.key == pygame.K_DOWN:
                    if f.y + 138 < 480 and board.board[four[0] + 2][four[1]] == '0':
                        f.y += 30
                elif event.key == pygame.K_SPACE:
                    z = self.func.index(f.glav)
                    if board.board[sec[0]][sec[1] + 1] == '0' and board.board[sec[0]][sec[1] + 2] and \
                            board.board[sec[0]][sec[1] + 3] and board.board[sec[0]][sec[1] + 2]:
                        f.glav = f.func[0]
                        game1 = 2
                        f.glav = f.func[z + 1]
                    q = f'f.{f.func[z + 1]}()'


class T:
    def __init__(self):
        global board
        self.chast = list()
        self.x = 210
        self.pos = [1, 2, 3, 4]
        self.y = 0
        self.glav = 'create_shape'
        self.func = ['create_shape', 'second', 'three', 'four']
        self.flag = True
        self.flag_create = False
        color = random.choice(['red', 'blue'])
        self.color = color
        if color == 'red':
            self.z = load_image('red.png', -1)
        else:
            self.z = load_image('tetris.png', -1)

    def create_shape(self):
        first_coord = (self.x, self.y + 48)
        second_coord = (self.x, self.y + 78)
        three_cord = (self.x, self.y + 108)
        four_coord = (self.x + 30, self.y + 78)
        self.master_shape(first_coord, second_coord, three_cord, four_coord,
                          1)

    def master_shape(self, first_coord, second_coord, three_coord,
                     four_coord, shape):  # оптимизация и расстановка фигур
        if shape == 1:
            self.krai_up = self.check_coord(first_coord)
            self.krai_left = self.check_coord(second_coord)
            self.krai_down = self.check_coord(three_coord)
            self.krai_right = self.check_coord(four_coord)
            screen.blit(self.z, first_coord)
            screen.blit(self.z, second_coord)
            screen.blit(self.z, three_coord)
            screen.blit(self.z, four_coord)
            if self.krai_down[0] <= 19:
                if self.krai_down[0] == 19 or board.board[self.krai_down[0] + 1][
                    self.krai_down[1]] != '0' or \
                        board.board[self.krai_right[0] + 1][self.krai_right[1]] != '0':
                    self.no_problen(self.krai_up, first_coord, self.krai_left, second_coord,
                                    self.krai_right,
                                    three_coord, self.krai_down,
                                    four_coord)

        elif shape == 2:
            self.krai_up = self.check_coord(first_coord)
            self.krai_left = self.check_coord(second_coord)
            self.krai_down = self.check_coord(four_coord)
            self.krai_right = self.check_coord(three_coord)
            screen.blit(self.z, first_coord)
            screen.blit(self.z, second_coord)
            screen.blit(self.z, three_coord)
            screen.blit(self.z, four_coord)
            if self.krai_down[0] == 19 or board.board[self.krai_down[0] + 1][
                self.krai_down[1]] != '0' or \
                    board.board[
                        self.krai_left[0] + 1][self.krai_left[1]] != '0' or \
                    board.board[self.krai_right[0] + 1][
                        self.krai_right[1]] != '0':
                self.no_problen(self.krai_up, first_coord, self.krai_left, second_coord,
                                self.krai_right,
                                three_coord, self.krai_down,
                                four_coord)

        elif shape == 3:
            self.krai_up = self.check_coord(first_coord)
            self.krai_left = self.check_coord(four_coord)
            self.krai_down = self.check_coord(three_coord)
            self.krai_right = self.check_coord(second_coord)
            screen.blit(self.z, first_coord)
            screen.blit(self.z, second_coord)
            screen.blit(self.z, three_coord)
            screen.blit(self.z, four_coord)
            if self.krai_down[0] == 19 or board.board[self.krai_down[0] + 1][
                self.krai_down[1]] != '0' or \
                    board.board[
                        self.krai_left[0] + 1][self.krai_left[1]] != '0' or \
                    board.board[self.krai_right[0] + 1][
                        self.krai_right[1]] != '0':
                self.no_problen(self.krai_up, first_coord, self.krai_left, second_coord,
                                self.krai_down,
                                three_coord, self.krai_right,
                                four_coord)

        elif shape == 4:
            self.krai_up = self.check_coord(four_coord)
            self.krai_left = self.check_coord(second_coord)
            self.krai_down = self.check_coord(first_coord)
            self.krai_right = self.check_coord(three_coord)
            screen.blit(self.z, first_coord)
            screen.blit(self.z, second_coord)
            screen.blit(self.z, three_coord)
            screen.blit(self.z, four_coord)
            if self.krai_down[0] == 19 or board.board[self.krai_down[0] + 1][
                self.krai_down[1]] != '0' or \
                    board.board[
                        self.krai_left[0] + 1][self.krai_left[1]] != '0' or \
                    board.board[self.krai_right[0] + 1][
                        self.krai_right[1]] != '0':
                self.no_problen(self.krai_up, four_coord, self.krai_left, second_coord,
                                self.krai_down,
                                first_coord, self.krai_right,
                                three_coord)

    def no_problen(self, fir, first_coord, sec, second_coord, three,
                   three_coord, four,
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
        board.board[coord[0]][coord[1]] = (vse, self.color)

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
        global game1
        global q
        if position == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if move(f, 'right'):
                        f.x += 30
                elif event.key == pygame.K_LEFT:
                    if move(f, 'left'):
                        f.x -= 30
        if position == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if move(f, 'right'):
                        f.x += 30
                elif event.key == pygame.K_LEFT:
                    if move(f, 'left'):
                        f.x -= 30
        if position == 3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if f.x + 60 <= 570 and (len(board.board[f.check_coord(
                            (f.x + 30, f.y + 30))[0] + 1][
                                                    f.check_coord(
                                                        (f.x + 30, f.y + 30))[
                                                        1]]) == 1 and f.y < 430 and (
                                                    len(
                                                        board.board[
                                                            f.check_coord((
                                                                    f.x + 30,
                                                                    f.y + 108))[
                                                                0] + 1][
                                                            f.check_coord((
                                                                    f.x + 30,
                                                                    f.y + 108))[
                                                                1]]) == 1) and len(
                        board.board[f.check_coord((f.x + 60, f.y + 78))[0] + 1]
                        [f.check_coord((f.x + 60, f.y + 78))[1]]) == 1):
                        f.x += 30
                elif event.key == pygame.K_LEFT:
                    if f.x - 30 > 80 and (f.y < 430 and (len(
                            board.board[
                                f.check_coord((f.x - 60, f.y + 108))[0] + 1][
                                f.check_coord((f.x - 60, f.y + 108))[
                                    1]]) == 1) and
                                          board.board[f.check_coord(
                                              (f.x + 30, f.y + 30))[0] + 1][
                                              f.check_coord(
                                                  (f.x + 30, f.y + 30))[1]] and
                                          board.board[f.check_coord(
                                              (f.x - 30, f.y + 48))[0] + 1][
                                              f.check_coord(
                                                  (f.x + 30, f.y + 48))[
                                                  1]] and len(
                                board.board[
                                    f.check_coord((f.x - 30, f.y + 108))[
                                        0] + 1][
                                    f.check_coord((f.x - 30, f.y + 108))[
                                        1]]) == 1):
                        f.x -= 30
                        f.glav = 'four'
        if position == 4:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if move(f, 'right'):
                            f.x += 30
                    elif event.key == pygame.K_LEFT:
                        if move(f, 'left'):
                            f.x -= 30


running = True
f = S()
game1 = 1
glav = ''
go_flag = False
q = 'f.create_shape()'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        f.game(game1)

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
                    elif board.board[i][j][1] == 'red':
                        image = load_image('red.png', -1)
                        r = board.board[i][j][0][0]
                        per = board.board[i][j][0][1]
                        screen.blit(image, (r, per))

        f.y += 30
        exec(q)
        clock.tick(5)
        board.render()
        pygame.display.flip()
    else:
        go_flag = True
    if go_flag:
        f = S()
        go_flag = False
    pygame.display.flip()

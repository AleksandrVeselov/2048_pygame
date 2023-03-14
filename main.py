import sys

from game_logics import *
import pygame


def draw_interface(game_screen, massiv: list[list[int]]) -> None:
    """Отрисовка интерфейса на экране"""

    pygame.draw.rect(screen, WHITE, TITLE_REC)  # отрисовка хэдера
    font = pygame.font.SysFont('stxingkai', 70)  # Задание шрифта

    # Цикл для отрисовки ячеек
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]  # значение из игрового поля по соответсвующим координатам
            text = font.render(f'{value}', True, BLACK)  # отрисовка шрифта
            w = column * SIZE_BLOCK + (column + 1) * MARGIN  # координата х начала ячейки
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + 110  # координата у начала ячейки
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))  # Отрсиовка ячейки

            # Если значение не равно 0
            if value != 0:
                font_w, font_h = text.get_size()  # ширина и высота цифры
                text_x = w + (SIZE_BLOCK - font_w) / 2  # координата х цифры
                text_y = h + (SIZE_BLOCK - font_h) / 2  # координата у цифры
                screen.blit(text, (text_x, text_y))  # помещение цифры на экран

# Игровое поле
mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

BLOCKS = 4  # Количество ячеек на графическом экране
SIZE_BLOCK = 110  # Размер ячейки на графическом экране
MARGIN = 10  # Отступ между ячейками
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN  # Ширина графического окна
HEIGHT = WIDTH + 110  # Высота графического окна
TITLE_REC = (0, 0, WIDTH, 110)  # координаты начала и конца прямоугольника заголовка
WHITE = (255, 255, 255)  # Белый цвет
GRAY = (130, 130, 130)  # Серый цвет
BLACK = (0, 0, 0)
COLORS = {0: (130, 130, 130),
          2: (255, 255, 255),
          4: (255, 255, 128),
          8: (255, 255, 0),
          16: (255, 155, 0),
          32: (130, 255, 0)}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра 2048')
draw_interface(screen, mas)
pygame.display.update()

# Цикл обработки событий pygame
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mas = move_left(mas)  # смещение цифр влево

            elif event.key == pygame.K_RIGHT:
                mas = move_right(mas)  # смещение цифр вправо
            elif event.key == pygame.K_UP:
                mas = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas = move_down(mas)
            empty = get_empty_list(mas)  # Список номеров клеток игрового поля со значением 0
            random.shuffle(empty)  # Перемешивание списка
            random_num = empty.pop()  # Удаление из списка номера пустой клетки и запись его в переменную
            i, j = get_index_from_number(random_num)  # получение координат из номера клетки
            print(i, j)
            mas = insert_2_or_4(mas, i, j)  # Вставка по полученным координатам случайного числа (2 или 4)
            print(mas)
            draw_interface(screen, mas)
            pygame.display.update()

#TODO part 8
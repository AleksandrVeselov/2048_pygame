import sys

from game_logics import *
import pygame

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

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра 2048')

# Цикл обработки событий pygame
while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, WHITE, TITLE_REC)
            for row in range(BLOCKS):
                for column in range(BLOCKS):
                    w = column * SIZE_BLOCK + (column + 1) * MARGIN
                    h = row * SIZE_BLOCK + (row + 1) * MARGIN + 110
                    pygame.draw.rect(screen, GRAY, (w, h, SIZE_BLOCK, SIZE_BLOCK))
            # input()
            empty = get_empty_list(mas)  # Список номеров клеток игрового поля со значением 0
            random.shuffle(empty)  # Перемешивание списка
            random_num = empty.pop()  # Удаление из списка номера пустой клетки и запись его в переменную
            i, j = get_index_from_number(random_num)  # получение координат из номера клетки
            print(i, j)
            mas = insert_2_or_4(mas, i, j)  # Вставка по полученным координатам случайного числа (2 или 4)
            print(mas)
    pygame.display.update()

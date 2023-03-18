import sys

from game_logics import *
import pygame
import data_base

GAMERS_DB = data_base.return_best_players()  # Лучшие игроки из базы данных
USERNAME = None  # Имя пользователя

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
TEXT_COLOR = (255, 127, 0)  # цвет текста
COLORS = {0: (130, 130, 130),
          2: (255, 255, 255),
          4: (255, 255, 128),
          8: (255, 255, 0),
          16: (255, 155, 0),
          32: (130, 255, 0),
          64: (180, 255, 32),
          128: (255, 21, 80),
          256: (200, 81, 255)}
score = 0  # количество набранных очков


def draw_top_gamers():
    """Отрисовка трех лучших игроков"""
    font_top = pygame.font.SysFont('simsun', 22)
    font_gamers = pygame.font.SysFont('simsun', 14)
    text_head = font_top.render('Best tries', True, TEXT_COLOR)
    screen.blit(text_head, (250, 5))

    index = 0
    for player in GAMERS_DB:
        name, score = player
        header = f'{index + 1}. {name} - {score}'
        text_gamer = font_gamers.render(header, True, TEXT_COLOR)
        screen.blit(text_gamer, (250, 30 + 20 * index))
        index += 1


def draw_interface(game_screen, massiv: list[list[int]], score: int, delta=0) -> None:
    """Отрисовка интерфейса на экране"""

    pygame.draw.rect(screen, WHITE, TITLE_REC)  # отрисовка хэдера
    font = pygame.font.SysFont('stxingkai', 70)  # Задание шрифта
    font_score = pygame.font.SysFont('simsun', 48)  # шрифт набранных очков
    font_delta = pygame.font.SysFont('simsun', 32)  # шрифт дельты (на сколько очков изменилось в результате хода)
    text_score = font_score.render('Score: ', True, TEXT_COLOR)
    text_score_value = font_score.render(f'{score}', True, TEXT_COLOR)
    screen.blit(text_score, (20, 35))  # отрисовка текста "score"
    screen.blit(text_score_value, (175, 35))  # отрисовка количества очков

    if delta > 0:
        text_delta = font_delta.render(f'+{delta}', True, TEXT_COLOR)
        screen.blit(text_delta, (170, 75))  # отрисовка дельты
    draw_top_gamers()

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


def draw_intro():
    """Рисование стартового экрана"""
    img2028 = pygame.image.load('1404598408_1.jpg')  # Загрузка каринки
    font = pygame.font.SysFont('stxingkai', 70)  # Задание шрифта
    text_welcome = font.render('Welcome! ', True, WHITE)
    name = 'Введите имя'  # Имя
    is_find_name = False  # Флаг для выхода из цикла

    # Основной цикл
    while not is_find_name:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Если нажата клавиша с буквой
                if event.unicode.isalpha():
                    if name == 'Введите имя':
                        name = event.unicode
                    else:
                        name += event.unicode

                # Если нажата BACKSPASE - удаление символов
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                # Если нажата ENTER - запись имени в переменную
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True

        screen.fill(BLACK)  # Заливка экрана черным цветом
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2028, [200, 200]), [10, 10])
        screen.blit(text_welcome, (230, 80))  # отрисовка текста "score"
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)

def draw_gameover():
    """Рисование конечного экрана"""
    img2028 = pygame.image.load('1404598408_1.jpg')  # Загрузка каринки
    font = pygame.font.SysFont('stxingkai', 60)  # Задание шрифта
    text_gameover = font.render('Game over!', True, WHITE)
    text_score = font.render(f'Вы набрали {score}', True, WHITE)
    best_score = GAMERS_DB[0][1]  # Лучший результат

    if score > best_score:
        text = 'Рекорд побит'

    else:
        text = f'Рекорд {best_score}'

    text_record = font.render(text, True, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        screen.blit(text_gameover, (230, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2028, [200, 200]), [10, 10])
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра 2048')

draw_intro()
draw_interface(screen, mas, score)
pygame.display.update()

# Цикл обработки событий pygame
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)  # смещение цифр влево

            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)  # смещение цифр вправо
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)

            score += delta  # прибавление дельты к текущему количеству очков

            if is_zero_in_mas(mas):
                empty = get_empty_list(mas)  # Список номеров клеток игрового поля со значением 0
                random.shuffle(empty)  # Перемешивание списка
                random_num = empty.pop()  # Удаление из списка номера пустой клетки и запись его в переменную
                i, j = get_index_from_number(random_num)  # получение координат из номера клетки
                print(i, j)
                mas = insert_2_or_4(mas, i, j)  # Вставка по полученным координатам случайного числа (2 или 4)
                print(mas)
            draw_interface(screen, mas, score, delta)
            pygame.display.update()


draw_gameover()

#TODO part 11
import random
from typing import Tuple, List


def pretty_print(massiv: list[list[int]]) -> None:
    """Построчный вывод массива"""
    print('-' * 10)
    for row in massiv:
        print(*row)
    print('-' * 10)


def get_empty_list(massiv: list[list[int]]) -> list[int]:
    """
    Возвращает номера клеток массива, значения в которых равны 0
    :param massiv: массив игрового поля
    :return: список свободных ячеек
    """

    empty = []  # список клеток

    for i in range(4):
        for j in range(4):
            if massiv[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def get_number_from_index(i: int, j: int) -> int:
    """
    Возвращает порядковый номер элемента по индексу
    :param i: номер столбца
    :param j: номер строки
    :return: порядковый номер
    """
    return i * 4 + j + 1


def get_index_from_number(num: int) -> tuple:
    """
    Рассчитывает индекс элемента по его порядковому номеру
    :param num: порядковый номер ячейки
    :return: кортеж (номер строки, номер столбца)
    """
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or_4(massiv: list[list[int]], x: int, y: int):
    """
    Вставляет 2 или 4 в место c координатами x, y в массиве
    :param massiv: массив игрового поля
    :param x: номер строки
    :param y: номер столбца
    :return: массив игрового поля с вставленными в него числами 2 или 4
    """
    if random.random() <= 0.75:
        massiv[x][y] = 2
    else:
        massiv[x][y] = 4
    return massiv


def is_zero_in_mas(mas: list[list]) -> bool:
    """
    Проверяет есть ли в массиве свободные места (равные 0)
    :param mas: массив игрового поля
    :return: True/False
    """
    for row in mas:
        if any(map(lambda x: x == 0, row)):
            return True
    return False


def move_left(massiv: list[list[int]]) -> tuple:
    """
    Перемещение цифр влево
    :param massiv: массив игрового поля
    :return: массив игрового поля со сдвинутыми влево цифрами
    """
    delta = 0  # на сколько изменятся очки

    for row in massiv:

        # Удаление нулей из массива
        while 0 in row:
            row.remove(0)

        # Заполнение нулями свободных ячеек
        while len(row) != 4:
            row.append(0)

    # Сложение соседних равных друг другу чисел, не равных нулю
    for i in range(4):
        for j in range(3):
            if massiv[i][j] == massiv[i][j + 1] and massiv[i][j] != 0:
                massiv[i][j] *= 2
                delta += massiv[i][j]
                massiv[i].pop(j + 1)
                massiv[i].append(0)

    return massiv, delta


def move_right(massiv: list[list[int]]) -> tuple:
    """
    Перемещение цифр влево
    :param massiv: массив игрового поля
    :return: массив игрового поля со сдвинутыми вправо цифрами
    """
    delta = 0   # на сколько изменятся очки

    for row in massiv:

        # Удаление нулей из массива
        while 0 in row:
            row.remove(0)

        # Заполнение нулями свободных ячеек
        while len(row) != 4:
            row.insert(0, 0)

        # Сложение соседних равных друг другу чисел, не равных нулю
        for i in range(4):
            for j in range(3, 0, -1):
                if massiv[i][j] == massiv[i][j - 1] and massiv[i][j] != 0:
                    massiv[i][j] *= 2
                    delta += massiv[i][j]
                    massiv[i].pop(j - 1)
                    massiv[i].insert(0, 0)

    return massiv, delta


def move_up(massiv: list[list[int]]) -> tuple:
    """
    Смещение цифр игрового поля вверх
    :param massiv: Массив игрового поля
    :return: массив игрового поля со сдвинутыми вверх цифрами
    """
    delta = 0   # на сколько изменятся очки

    for j in range(4):
        column = []  # колонка
        for i in range(4):
            # Если элемент из колонки не равен нулю
            if massiv[i][j] != 0:
                column.append(massiv[i][j])

        # Заполнение колонки нулями
        while len(column) != 4:
            column.append(0)

        # Сложение соседних одинаковых цифр и заполнение пустых мест нулями
        for i in range(3):
            if column[i] == column[i + 1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i + 1)
                column.append(0)

        # Заполнение колонки цифрами из column
        for i in range(4):
            massiv[i][j] = column[i]

    return massiv, delta


def move_down(massiv: list[list[int]]) -> tuple[list[list[int]], int]:
    """
    Перемещение цифр массива вниз
    :param massiv: Массив игрового поля
    :return: массив игрового поля со сдвинутыми вниз цифрами
    """
    delta = 0   # на сколько изменятся очки

    for j in range(4):
        column = []   # колонка
        for i in range(4):
            # Если элемент из колонки не равен нулю
            if massiv[i][j] != 0:
                column.append(massiv[i][j])

        # Заполнение колонки нулями
        while len(column) != 4:
            column.insert(0, 0)

        # Сложение соседних одинаковых цифр и заполнение пустых мест нулями
        for i in range(3, 0, -1):
            if column[i] == column[i - 1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i - 1)
                column.insert(0, 0)

        # Заполнение колонки цифрами из column
        for i in range(4):
            massiv[i][j] = column[i]

    return massiv, delta


def can_move(massiv: list[list[int]]) -> bool:
    """
    Проверка возможно ли еще сдвинуть цифры
    :param massiv: Массив игрового поля
    :return: True или False
    """
    for i in range(3):
        for j in range(3):
            if massiv[i][j] == massiv[i][j + 1] or massiv[i][j] == massiv[i - 1][j]:
                return True
    return False


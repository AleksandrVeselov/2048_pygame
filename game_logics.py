import random


def pretty_print(massiv: list[list]) -> None:
    """Построчный вывод массива"""
    print('-' * 10)
    for row in massiv:
        print(*row)
    print('-' * 10)


def get_empty_list(massiv):
    """Возвращает индексы массива, значения в которых равны 0"""
    empty = []
    for i in range(4):
        for j in range(4):
            if massiv[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def get_number_from_index(i, j):
    """Возвращает порядковый номер элемента по индексу"""
    return i * 4 + j + 1


def get_index_from_number(num):
    """Рассчитывает индекс элемента по его порядковому номеру"""
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or_4(massiv, x, y):
    """Вставляет 2 или 4 в место c координатами x, y в массиве"""
    if random.random() <= 0.75:
        massiv[x][y] = 2
    else:
        massiv[x][y] = 4
    return massiv


def is_zero_in_mas(mas: list[list]) -> bool:
    """
    Проверяет есть ли в массиве свободные места (равные 0)
    :param mas: массив с числами
    :return: True/False
    """
    for row in mas:
        if any(map(lambda x: x == 0, row)):
            return True
    return False

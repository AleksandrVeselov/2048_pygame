import sqlite3

database = [('Александр', 400),
            ('Александр', 1000),
            ('Миша', 700),
            ('Вася', 600),
            ('Маша', 580)]


def return_best_players(base: list[tuple], count: int) -> list[tuple]:
    """Сортирует и возвращает переданное ей количество лучших результатов"""
    sorted_players = sorted(base, key=lambda x: x[1])
    return sorted_players[-1:count:-1]


def add_to_database(base: list[tuple], name, score) -> None:
    """Добавляет в базу данных результат игрока и его имя"""
    base.append((name, score))



from game_logics import *

# Игровое поле
mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

while is_zero_in_mas(mas):
    input()
    empty = get_empty_list(mas)  # Список номеров клеток игрового поля со значением 0
    random.shuffle(empty)  # Перемешивание списка
    random_num = empty.pop()  # Удаление из списка номера пустой клетки и запись его в переменную
    i, j = get_index_from_number(random_num)  # получение координат из номера клетки
    print(i, j)
    mas = insert_2_or_4(mas, i, j)  # Вставка по полученным координатам случайного числа (2 или 4)
    print(mas)
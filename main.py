from game_logics import *


mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

while is_zero_in_mas(mas):
    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num = empty.pop()
    i, j = get_index_from_number(random_num)
    print(i, j)
    mas = insert_2_or_4(mas, i, j)
    print(mas)
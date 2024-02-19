from globales import *


def backtracking(echiquier: list, pos: tuple, nb_cases_visite: int) -> bool:

    result: bool = False

    if nb_cases_visite == SIZE ** 2:
        result = True
    else:
        pass

    return result


def get_new_possible_pos(pos: tuple) -> list:
    
    if len(pos) != 2:
        raise Exception("pos doit avoir 2 valeurs: x et y")
    if not (isinstance(pos[0], int) and isinstance(pos[1], int)):
        raise Exception("pos doit conteir des nombres entiers")
    if pos[0] < 0 or pos[0] > SIZE or pos[1] < 0 or pos[1] > SIZE:
        raise ValueError(f"les valeurs de pos doivent être comprises entre 0 et {SIZE}")
    
    pos_list = list()

    pos_list.append((pos[0] + 2, pos[1] + 1))
    pos_list.append((pos[0] + 2, pos[1] - 1))
    pos_list.append((pos[0] - 2, pos[1] + 1))
    pos_list.append((pos[0] - 2, pos[1] - 1))
    pos_list.append((pos[0] + 1, pos[1] + 2))
    pos_list.append((pos[0] + 1, pos[1] - 2))
    pos_list.append((pos[0] - 1, pos[1] + 2))
    pos_list.append((pos[0] - 1, pos[1] - 2))

    i = 0
    while i < len(pos_list):
        if (pos_list[i][0] < 0) or (pos_list[i][1] < 0):
            pos_list.pop(i)
        elif (pos_list[i][0] >= 8) or (pos_list[i][1] >= 8):
            pos_list.pop(i)
        else:
            i += 1

    return pos_list

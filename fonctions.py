from globales import SIZE


def backtracking(echiquier: list, pos: tuple, nb_cases_visite: int = 0, cases_visites: list = list()) -> tuple:

    if not isinstance(echiquier, list):
        raise TypeError("L'echiquier doit être de type list")
    if not isinstance(pos, tuple):
        raise TypeError("pos doit être de type tuple")
    if not isinstance(nb_cases_visite, int):
        raise TypeError("nb_cases_visites doit être de type int")
    if not isinstance(cases_visites, list):
        raise TypeError("cases_visites doit être de type list")

    cases_visites += [pos]
    result = (False, cases_visites)
    echiquier[pos[0]][pos[1]] = True
    # print(nb_cases_visite)
    if nb_cases_visite == SIZE ** 2:
        result = (True, result[1])
    else:
        new_possible_pos = get_new_possible_pos(echiquier, pos)
        i = 0
        while not result[0] and i < len(new_possible_pos):
            result = backtracking(echiquier, new_possible_pos[i], nb_cases_visite + 1, result[1])
            if not result[0]:
                tmp = result[1]
                tmp.pop()
                result = (result[0], tmp)
                echiquier[pos[0]][pos[1]] = False
            i += 1

    return result


def get_new_possible_pos(echiquier: list, pos: tuple) -> list:
    
    if len(pos) != 2:
        raise Exception("pos doit avoir 2 valeurs: x et y")
    if not (isinstance(pos[0], int) and isinstance(pos[1], int)):
        raise Exception("pos doit contenir des nombres entiers")
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
        # Si une position est en dehors de l'échiquier
        if (pos_list[i][0] < 0) or (pos_list[i][1] < 0):
            pos_list.pop(i)
        elif (pos_list[i][0] >= 8) or (pos_list[i][1] >= 8):
            pos_list.pop(i)
        # Si on est déjà passé par la case
        elif echiquier[pos_list[i][0]][pos_list[i][1]]:
            pos_list.pop(i)
        else:
            i += 1

    return pos_list

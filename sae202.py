from globales import *
from echiquier import Echec
from fonctions import *

echiquier = [[False for _ in range(SIZE)] for _ in range(SIZE)]

def init_echiq():
    for x in range(SIZE):
        for y in range(SIZE):
            if echiquier[x][y]:
                pass


def main():
    """ Fonction main """
    echec = Echec()
    echec.placerCavalier((4, 0))
    pos_list = backtracking(echiquier, (4, 0), 0)[1]
    print(pos_list)
    for pos in pos_list:
        echec.deplacerCavalier(pos)
    echec.afficher()


if __name__ == "__main__":

    main()


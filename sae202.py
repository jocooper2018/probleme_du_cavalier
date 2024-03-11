from globales import SIZE
from echiquier import Echec
from fonctions import backtracking

echiquier = [[False for _ in range(SIZE)] for _ in range(SIZE)]

#def init_echiq():
#    for x in range(SIZE):
#        for y in range(SIZE):
#            if echiquier[x][y]:
#                pass


def main():
    """ Fonction main """
    echec = Echec()
    i, j = 0, 0
    echiquier = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    echec.placerCavalier((i, j))
    result = backtracking(echiquier, (i, j))


    if not result[0]:
        print("c pas bon")
    print(result)
    for pos in result[1]:
        echec.deplacerCavalier(pos)
    echec.afficher()


if __name__ == "__main__":

    main()


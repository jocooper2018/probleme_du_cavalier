from echiquier import Echec
import time

# Taille de l'échiquier
from globales import *

# Déplacements possibles pour le cavalier
deplacements_x = [2, 1, -1, -2, -2, -1, 1, 2]
deplacements_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Vérifier si le prochain mouvement est valide
def est_valide(x, y, echiquier):
    return x >= 0 and y >= 0 and x < SIZE and y < SIZE and echiquier[x][y] == -1

# Trouver un chemin hamiltonien pour le cavalier
def trouver_chemin_hamiltonien():
    echiquier = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]
    echiquier[X][Y] = 0

    if not trouver_chemin_util(X, Y, 1, echiquier, deplacements_x, deplacements_y):
        print("Pas de solution")
        return None
    else:
        return echiquier

# Fonction utilitaire récursive pour trouver le chemin
def trouver_chemin_util(x, y, etape, echiquier, dx, dy):
    if etape == SIZE * SIZE:
        return True

    for i in range(8):
        prochain_x = x + dx[i]
        prochain_y = y + dy[i]
        if est_valide(prochain_x, prochain_y, echiquier):
            echiquier[prochain_x][prochain_y] = etape
            if trouver_chemin_util(prochain_x, prochain_y, etape + 1, echiquier, dx, dy):
                return True
            echiquier[prochain_x][prochain_y] = -1

    return False

# Appeler la fonction pour trouver le chemin hamiltonien
if __name__ == "__main__": 
    start_time = time.time()
    board = trouver_chemin_hamiltonien()
    tempsTotal = time.time() - start_time
    if board is not None:
        echec = Echec()
        echec.placerCavalier((X, Y))
        for i in range(1, SIZE**2):
            trouver = False
            x = 0
            while not trouver and x < SIZE:
                y = 0
                while not trouver and y < SIZE:
                    if board[x][y] == i:
                        trouver = True
                    y += 1
                x += 1
            echec.deplacerCavalier((x-1, y-1))
        echec.afficher(tempsTotal)
        
def is_valid_move(board, x, y, n):
    """
    Vérifie si le mouvement (x, y) est valide sur l'échiquier de taille n x n.
    """
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def get_move_counts(board, x, y, n):
    """
    Retourne le nombre de mouvements possibles à partir de la position (x, y) sur l'échiquier de taille n x n.
    """
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    count = 0
    for dx, dy in moves:
        if is_valid_move(board, x + dx, y + dy, n):
            count += 1
    return count

def warnsdorff_tour(n):
    """
    Résout le problème du tour du cavalier en utilisant l'algorithme de Warnsdorff.
    """
    # Initialisation de l'échiquier
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # Liste des mouvements possibles du cavalier
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Position initiale
    x, y = 0, 0
    move_count = 0

    # Réalisation du tour
    while move_count < n*n:
        board[x][y] = move_count
        move_count += 1

        # Recherche du prochain mouvement valide avec le moins de mouvements possibles
        next_moves = [(x + dx, y + dy) for dx, dy in moves
                      if is_valid_move(board, x + dx, y + dy, n)]
        next_moves.sort(key=lambda pos: get_move_counts(board, pos[0], pos[1], n))

        # Choix du prochain mouvement
        if next_moves:
            x, y = next_moves[0]
        else:
            break

    return board

# Exemple d'utilisation avec un échiquier de taille 8x8
tour_solution = warnsdorff_tour(8)
for row in tour_solution:
    print(row)
    
if __name__ == "__main__":
    start = time.time()
    board = warnsdorff_tour()
    if board is not None:
        echec = Echec()
        echec.placerCavalier((0, 0))
        for i in range(1, SIZE**2+1):
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
        tempsTotal = time.time()-start
        echec.afficher(tempsTotal)

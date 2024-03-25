from echiquier import Echec
from globales import *
import time

def is_valid_move(board, move, visited):
    x, y = move
    return 0 <= x < SIZE and 0 <= y < SIZE and board[x][y] == 0 and (x, y) not in visited

def get_valid_moves(board, x, y, visited):
    moves = [
        (x + 1, y + 2), (x + 2, y + 1),
        (x + 2, y - 1), (x + 1, y - 2),
        (x - 1, y - 2), (x - 2, y - 1),
        (x - 2, y + 1), (x - 1, y + 2)
    ]
    return [move for move in moves if is_valid_move(board, move, visited)]

def get_move_counts(board, x, y, visited):
    return [(move, len(get_valid_moves(board, move[0], move[1], visited))) for move in get_valid_moves(board, x, y, visited)]

def solve_cavalier(board, x, y, visited, move_count):
    if move_count == SIZE**2:
        return True
    for move, _ in sorted(get_move_counts(board, x, y, visited), key=lambda x: x[1]):
        visited.append(move)
        board[move[0]][move[1]] = move_count + 1
        if solve_cavalier(board, move[0], move[1], visited, move_count + 1):
            return True
        visited.pop()
        board[move[0]][move[1]] = 0
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def knight_tour():
    board = [[0] * SIZE for _ in range(SIZE)]
    start_x, start_y = X, Y  # Start position
    visited = [(start_x, start_y)]
    board[start_x][start_y] = 1
    if solve_cavalier(board, start_x, start_y, visited, 1):
        print("Solution found:")
        return board
    else:
        print("No solution found")
        return None

if __name__ == "__main__":
    start = time.time()
    board = knight_tour()
    tempsTotal = time.time() - start
    if board is not None:
        echec = Echec()
        echec.placerCavalier((X, Y))
        for i in range(1, SIZE**2 + 1):
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

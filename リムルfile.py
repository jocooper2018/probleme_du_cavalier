from echiquier import Echec


def is_valid_move(board, move, visited):
    x, y = move
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == 0 and (x, y) not in visited

def get_valid_moves(board, x, y, visited):
    moves = [
        (x + 1, y + 2), (x + 2, y + 1),
        (x + 2, y - 1), (x + 1, y - 2),
        (x - 1, y - 2), (x - 2, y - 1),
        (x - 2, y + 1), (x - 1, y + 2)
    ]
    return [move for move in moves if is_valid_move(board, move, visited)]

def solve_cavalier(board, x, y, visited, move_count):
    if move_count == 64:
        return True
    for move in get_valid_moves(board, x, y, visited):
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
    board = [[0] * 8 for _ in range(8)]
    start_x, start_y = 0, 0  # Start position
    visited = [(start_x, start_y)]
    board[start_x][start_y] = 1
    if solve_cavalier(board, start_x, start_y, visited, 1):
        print("Solution found:")
        return board
    else:
        print("No solution found")
        return None

if __name__ == "__main__":
    board = knight_tour()
    if board is not None:
        echec = Echec()
        echec.placerCavalier((0, 0))
        for i in range(1, 65):
            trouver = False
            x = 0
            while not trouver and x < 8:
                y = 0
                while not trouver and y < 8:
                    if board[x][y] == i:
                        trouver = True
                    y += 1
                x += 1
            echec.deplacerCavalier((x-1, y-1))
        echec.afficher()
        
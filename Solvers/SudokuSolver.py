import numpy as np
from collections import Counter

def find_block_indexes(i):
    br = i//3
    brs = 3*br
    bre = 3*(br+1)

    bc = i%3
    bcs = 3*bc
    bce = 3*(bc+1)

    coordinates = []

    for x in range(brs, bre):
        for y in range(bcs, bce):
            coordinates.append((x, y))

    return tuple(coordinates)


def find_block_values(board, i):
    br = i//3
    brs = 3*br
    bre = 3*(br+1)

    bc = i%3
    bcs = 3*bc
    bce = 3*(bc+1)

    return board[brs:bre, bcs:bce].flatten()


def find_valid_moves(board, x, y):
    row = set(board[x,:])
    col = set(board[:,y])
    block = set(find_block_values(board, 3*(x//3) + (y//3)))
    moves = {i for i in range(1,10)} - row.union(col).union(block)
    return moves


def check_complete(A):
    return Counter(A)[0] == 0 and len(set(A)) == len(A)


def check_solution(board):
    correct = True
    for i in range(9):
        row = board[i,:]
        col = board[:,i]
        block = find_block_values(board, i)

        correct = correct and check_complete(row) and check_complete(col) and check_complete(block)

    return correct


def unique_valid(valid, x, y):
    row = [valid[x][y] - valid[x][i] for i in range(9)]
    col = [valid[x][y] - valid[x][i] for i in range(9)]
    block = [valid[x][y] - valid[a][b] for a, b in find_block_indexes(3*(x//3) + (y//3))]

FOUND = False

def solver(board, num):
    global FOUND
    if not FOUND:
        if check_solution(board):
            FOUND = True
            print(board)
        else:
            x = num // 9
            y = num % 9

            if board[x][y] == 0:
                for move in find_valid_moves(board, x, y):
                    board[x][y] = move
                    solver(np.array(board), num + 1)

            else:
                solver(np.array(board), num + 1)

board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

board = np.array(board)

solver(np.array(board), 0)

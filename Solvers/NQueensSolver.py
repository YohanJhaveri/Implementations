def NQueens(n):
    num_solutions = 0
    board = [[0 for x in range(n)] for y in range (n)]
    queens = []

    row = 0
    col = 0

    while True:
        if len(queens) < n:
            if col == n:

                """
                once you have run out of safe positions on that row,
                backtrack and find a new safe position for the previous queen

                """

                if row == 0:
                    # once the first queen is popped off, this means all solutions have been found
                    print(num_solutions)
                    return

                prev = queens.pop()
                row = prev[0]
                col = prev[1]
                board[row][col] = 0
                col += 1

            elif is_safe(board, (row,col)):

                """
                once you have found a safe position for the current row's queen,
                move on to the next row to find a safe position for the next queen

                """

                queens.append((row,col))
                board[row][col] = 1
                row += 1
                col = 0

            else:

                """
                if the current position is not safe,
                move over to the next column and check if that position is safe

                """

                col += 1

        else:

            """
            once you have found all n queens,
            move the last queen over to the next column to find more solutions

            """

            print_board(board)
            num_solutions += 1

            prev = queens.pop()
            row = prev[0]
            col = prev[1]
            board[row][col] = 0
            col += 1


def is_safe(board, coordinates):
    c_x = coordinates[0]
    c_y = coordinates[1]
    n = len(board)

    queens = []

    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                queens.append((x,y))

    for queen in queens:
        if queen[0] == coordinates[0]: return False # checks if there is another queen on the same row
        if queen[1] == coordinates[1]: return False
        if abs(coordinates[0] - queen[0]) == abs(coordinates[1] - queen[1]): return False

    return True


def print_board(board):
    print()

    marking = ' '
    for x in range(len(board)):
        marking += ' ' + str(x)
    print(marking)

    for index, x in enumerate(board):
        row = str(index) + ' '
        for y in x:
            row += ('Q' if y == 1 else '-') + ' '
        print(row)

    print()


NQueens(6)

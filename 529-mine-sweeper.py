click= [3,0]
board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]


def updateBoard(board, click):
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board

    def help(board, click):
        res = 0
        p = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        row_range = [i for i in range(0, len(board))]
        column_range = [i for i in range(0,len(board[0]))]
        for i in p:
            row = click[0] + i[0]
            column = click[1] + i[1]
            if row in row_range and column in column_range:
                if board[row][column] in ['M', 'X']:
                    res += 1
        if res > 0:
            board[click[0]][click[1]] = str(res)
        if res == 0:
            board[click[0]][click[1]] = 'B'
            for i in p:
                row = click[0] + i[0]
                column = click[1] + i[1]
                if row in row_range and column in column_range:
                    if board[row][column] == 'E':
                        help(board, [row, column])

    help(board, click)
    return board
a = updateBoard(board,click)
print(a)

def game_of_life(board):
    def count_live_neighbors(x, y):
        live_neighbors = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and 0 <= i < len(board) and 0 <= j < len(board[0]):
                    live_neighbors += board[i][j] & 1
        return live_neighbors
    for i in range(len(board)):
        for j in range(len(board[0])):
            live_neighbors = count_live_neighbors(i, j)
            if board[i][j] == 1 and 2 <= live_neighbors <= 3:
                board[i][j] |= 2
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] |= 2
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] >>= 1
    return board
print(game_of_life([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
print(game_of_life([[1, 1], [1, 0]]))
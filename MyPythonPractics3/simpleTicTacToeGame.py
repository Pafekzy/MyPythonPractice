board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('|'.join(row))
        print('-' * 5)

def check_winner():
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 

#simpleTicTacToeGame

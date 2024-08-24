        7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != ' ':
            return board[pattern[0]]
    return None

def tic_tac_toe():
    player = 'X'
    for _ in range(9):
        print_board()
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = player
            winner = check_winner()
            if winner:
                print_board()
                print(f"Player {winner} wins!")
                return
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
    print("It's a tie!")

tic_tac_toe()


#Simple Tic-Tac-Toe Game (Continued)
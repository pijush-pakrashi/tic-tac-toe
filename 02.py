# A simple Tic-Tac-Toe game in Python for two players.
def display_board(board):
    # The board is a list of lists, e.g., [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("\n")
    
    for row in range(3):
        print(f" {board[row][0]} | {board[row][1]} | {board[row][2]} ")
        if row < 2:
            print("---|---|---")
    print("\n")

def check_win(board, player):
    #chaking rows:
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    
    # Checking columns:
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
            
    # Checking diagonals:
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True     #jo candition win hoga too true return kardo:

    return False #jo candition win nahi hoga too false return kardo:

def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False # ager empty space hoga too draw nahi hoga
    return True # Board full hoga too draw hoga

def main():
    print("Welcome to TIC-TAC-TOE GAME👋!")
    print("Player 1 is X and Player 2 is O.")
    
    while True:
        # Initialize the game board
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
        current_player = 'X'
        game_over = False
        
        while not game_over:
            display_board(board)
            print(f"Player {current_player}'s turn.")
            
            # Get player input with validation
            try:
                row = int(input("Enter row (1, 2, or 3): ")) - 1
                col = int(input("Enter column (1, 2, or 3): ")) - 1
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid input. Row and column must be between 1 and 3.")
                    continue
                
                if board[row][col] != ' ':
                    print("That spot is already taken! Choose another.")
                    continue
                    
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            # Place the player's mark on the board
            board[row][col] = current_player
            
            # Check for a win
            if check_win(board, current_player):
                display_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                game_over = True
            
            # Check for a draw
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                game_over = True
            
            # Switch to the other player if the game is not over
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        
        # Ask if players want to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break
    
    print("Thanks for playing! Goodbye.")

# Run the game
if __name__ == "__main__":
    main()






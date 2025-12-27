import math

# Initialize the board: a simple list of 9 spaces
board = [' ' for _ in range(9)]

def print_board():
    """Prints the current state of the board."""
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(b, player):
    """Checks if the specified player ('X' or 'O') has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    return any(all(b[i] == player for i in condition) for condition in win_conditions)

def is_board_full(b):
    """Checks if there are no more moves left."""
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    """
    The Minimax Algorithm. 
    AI is 'O' (Maximizing), Human is 'X' (Minimizing).
    """
    if check_winner(b, 'O'): return 10 - depth
    if check_winner(b, 'X'): return depth - 10
    if is_board_full(b): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_best_move():
    """Calculates the best possible move for the AI."""
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    """Main loop to run the game."""
    print("Welcome to Tic-Tac-Toe AI (Unbeatable)!")
    print("Instructions: Enter 1-9 to place your 'X' on the board.")
    print_board()

    while True:
        # Human Turn
        try:
            choice = int(input("\nYour move (1-9): ")) - 1
            if board[choice] != ' ':
                print("Invalid move! Cell already taken.")
                continue
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 9.")
            continue

        board[choice] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("\nCongratulations! You won! (This shouldn't happen!)")
            break
        if is_board_full(board):
            print("\nIt's a Draw!")
            break

        # AI Turn
        print("\nAI is thinking...")
        ai_move = get_best_move()
        board[ai_move] = 'O'
        print_board()

        if check_winner(board, 'O'):
            print("\nAI Wins! Better luck next time.")
            break
        if is_board_full(board):
            print("\nIt's a Draw!")
            break

if __name__ == "__main__":
    play_game()
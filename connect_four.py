ROW_SIZE: int = 6
COL_SIZE: int = 7

def create_board():
    return [[' ' for i in range(COL_SIZE)] for i in range(ROW_SIZE)]

def print_board(board):
    
    for i in range(COL_SIZE):
        print('  '+str(i)+' ', end="")
    print("\n")
    
    for row in board:
        print('| '+' | '.join(row)+' |')
    print("+---" * 7 + "+")
    
def get_player_move(player):
    
    while True:
        try:
            col = int(input("Player {}, choose a column (0-6): ".format(player)))
            if col in range(COL_SIZE):
                return col 
            else:
                print("Invalid column. Choose a column between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def is_valid_move(board, col):
    return board[0][col] == ' '

def drop_piece(board, col, current_player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = current_player
            return True
    return False

def check_status(board, current_player):
    for c in range(7 - 3):
        for r in range(6):
            if board[r][c] == current_player and board[r][c+1] == current_player and board[r][c+2] == current_player and board[r][c+3] == current_player:
                return True

    for c in range(7):
        for r in range(6 - 3):
            if board[r][c] == current_player and board[r+1][c] == current_player and board[r+2][c] == current_player and board[r+3][c] == current_player:
                return True

    for c in range(7 - 3):
        for r in range(6 - 3):
            if board[r][c] == current_player and board[r+1][c+1] == current_player and board[r+2][c+2] == current_player and board[r+3][c+3] == current_player:
                return True

    for c in range(7 - 3):
        for r in range(3, 6):
            if board[r][c] == current_player and board[r-1][c+1] == current_player and board[r-2][c+2] == current_player and board[r-3][c+3] == current_player:
                return True

    return False

def is_board_full(board):
    for i in board[0]:
        if i == ' ':
            return False 
    return True
    
def toggle_player(player):
    return 'O' if player == 'X' else 'X'

def start_game():
    board = create_board()
    print_board(board)
    current_player = 'X'
    GAME_OVER: bool = False
    
    while not GAME_OVER:
        col = get_player_move(current_player)
        
        if is_valid_move(board, col):
            drop_piece(board, col, current_player)
            print_board(board)
            
            if check_status(board, current_player):
                print("Player {} wins!".format(current_player))
                GAME_OVER = True
                break
            
            if is_board_full(board):
                print("The game is a draw!")
                GAME_OVER = True
                break
            
            current_player = toggle_player(current_player)
        else:
            print("Column is full. Choose another column.")
                 
start_game()
# Connect Four Game

This is a simple implementation of the classic Connect Four game in Python. The game allows two players to take turns dropping discs into a 6x7 grid, with the goal of connecting four of their own pieces in a row, column, or diagonal.

## Features

- Two-player game
- 6x7 grid
- Detects win conditions (horizontal, vertical, and diagonal)
- Detects draw conditions (board is full)

## Requirements

- Python 3

## How to Play

1. Clone the repository:

   ```bash
   git clone https://github.com/Arvind-Sabarinathan/connect-4.git
   cd connect-4
   ```
2. Run the game:

    ```cmd
   python connect_four.py
    ```
   
3. Follow the prompts to play the game.

## Game Rules
- Players take turns choosing a column to drop their piece (X or O).
- A piece will occupy the lowest available space within the chosen column.
- The first player to connect four of their discs in a row (horizontally, vertically, or diagonally) wins the game.
- If the board is full and no player has connected four discs, the game is a draw.

## Code Review

### create_board

Initializes an empty 6x7 game board.

```py
def create_board():
    return [[' ' for i in range(COL_SIZE)] for i in range(ROW_SIZE)]
```

- This function creates and returns a 6x7 grid (list of lists) filled with empty spaces (' ').

### print_board

Displays the current state of the game board.

```py
def print_board(board):
    for i in range(COL_SIZE):
        print('  '+str(i)+' ', end="")
    print("\n")
    
    for row in board:
        print('| '+' | '.join(row)+' |')
    print("+---" * 7 + "+")
```

- This function prints the game board row by row, adding borders to separate columns.

### get_player_move

Prompts the player to choose a column.

```py
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
```

- This function repeatedly prompts the player to enter a valid column number until a valid input is received.

### is_valid_move

Checks if a move is valid (i.e., the column is not full).

```py
def is_valid_move(board, col):
    return board[0][col] == ' '
```

- This function checks if the topmost cell of the column is empty, indicating that the column is not full.

### drop_piece()

Drops a piece into the specified column.

```py
def drop_piece(board, col, current_player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = current_player
            return True
    return False
```

- This function places the disc in the lowest available row within the specified column.

- It iterates from the bottom row to the top row of the column.

### check_status

Checks if the current player has won the game.

```py
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
```

- This function checks for four consecutive discs of the same type in horizontal, vertical, and diagonal directions to determine if the current player has won.

### is_board_full

Checks if the board is full.

```py
def is_board_full(board):
    for i in board[0]:
        if i == ' ':
            return False 
    return True
```

- This function checks if there are any empty spaces left in the top row of the board, indicating whether the board is full.

### toggle_player

Switches the current player.

```py
def toggle_player(player):
    return 'O' if player == 'X' else 'X'
```

- This function switches the current player between 'X' and 'O'.

### play_game

Main function to play the game.

```py
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
```

- This is the main function that initializes the game, manages the game loop, and handles player turns.

- It continuously prompts players for their moves, updates the board, and checks for win or draw conditions.


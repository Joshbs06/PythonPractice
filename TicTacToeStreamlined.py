def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! Actual: {actual} != Expected: {expected}")

def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)
 
def winning_line(strings):
    piece = strings[0]
    if piece == ' ':
        return False
    for entry in strings:
        if piece != entry:
            return False
    return True

def row_winner(board):
    for row in board:
        if winning_line(row):
            return True
    return False

def column_winner(board):
    for col in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[col])
        if winning_line(column):
            return True
    return False

def diagonal_winner(board):
    forDiagonal = []
    revDiagonal = []
    
    for i in range(len(board)):
        forDiagonal.append(board[i][i])
        revDiagonal.append(board[i][-i-1])
    
    return winning_line(forDiagonal) or winning_line(revDiagonal)

def get_move():
    print('Enter row:')
    row = int(input()) - 1
    print('Enter column:')
    col = int(input()) - 1
    return row, col

def check_move(board, row, col):
    return board[row][col] == ' '

def play_move(board, player):
    print(f'{player} to play.')
    
    while True:
        row, col = get_move()

        if check_move(board, row, col):
            board[row][col] = player
            print(format_board(board))
            return
        print("Invalid move. Try again.")

def make_board(size):
    return [[' '] * size for _ in range(size)]

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))

    totalPossibleMoves = board_size * board_size
    
    player1Turn = True
    hasWinner = False
    
    for i in range(totalPossibleMoves):
        
        if player1Turn:
            play_move(board, player1)
            player1Turn = False
            if winner(board):
                print_winner(player1)
                hasWinner = True
                break
        else:
            play_move(board, player2)
            player1Turn = True
            if winner(board):
                print_winner(player2)
                hasWinner = True
                break
    
    if not hasWinner:
        print_draw()

boardSize = int(input("Enter board size:"))
play_game(boardSize, 'X', 'O')

#Test Cases
# assert_equal(8

#     winner(
#         [
#             ['X', 'X', 'X', ' '],
#             ['X', 'X', ' ', ' '],
#             ['X', ' ', 'O', 'X'],
#             [' ', ' ', 'O', 'X']
#         ]
#     ),
#     False
# )
# assert_equal(
#     winner(
#         [
#             ['X', ' ', 'X'],
#             ['O', 'X', 'O'],
#             ['O', 'O', 'O']
#         ]
#     ),
#     True
# )
# assert_equal(
#     winner(
#         [
#             ['X', ' '],
#             ['X', 'O']
#         ]
#     ),
#     True
# )
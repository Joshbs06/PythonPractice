def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! Actual: {actual} != Expected: {expected}")

def format_board(board):
    joined_rows = []
    board_length = len(board)
    separator = "-+"
    
    row_separator = "  " + (separator * (board_length - 1)) + "-"
    
    header = " "
    for i in range(1, board_length + 1):
        header += " " + str(i) 
    
    for i in range(board_length + 1):
        
        if i == 0:
            joined_rows.append(header)
        else:
            joined_rows.append(f'{i} {"|".join(board[i - 1])}')
        
        if i != board_length:
            joined_rows.append(row_separator)
            
    return "\n".join(joined_rows)

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def row_winner(board):
    colCount = len(board)
    rowMatches = False
    
    for row in board:
        rowValue = ""
        for col in range(colCount):
            if col == 0:
                rowValue = row[0]
                if rowValue == ' ':
                    break
            else:
                if rowValue == row[col]:
                    rowMatches = True
                else:
                    rowMatches = False
                    break
        
        if rowMatches:
            break
        
    return rowMatches

def column_winner(board):
    colCount = len(board[0])
    colMatches = False
    
    for col in range(colCount):
        colValue = ""
        for row in range(colCount):
            if row == 0:
                colValue = board[0][col]
                if colValue == ' ':
                    break
            else:
                if colValue == board[row][col]:
                    colMatches = True
                else:
                    colMatches = False
                    break
                
        if colMatches:
            break
        
    return colMatches

def diagonal_winner(board):
    counter = len(board)
    revCounter = -1
    
    forMatches = False
    revMatches = False
    
    forValue = ""
    revValue = ""
    
    for count in range(counter):
        if count == 0:
            forValue = board[count][count]
            if forValue == ' ':
                break
        else:
            if forValue == board[count][count]:
                forMatches = True
            else:
                forMatches = False
                break
    
    for count in range(counter):
        if count == 0:
            revValue = board[count][revCounter]
            if revValue == ' ':
                break
        else:
            if revValue == board[count][revCounter]:
                revMatches = True
            else:
                revMatches = False
                break
        revCounter -= 1 
    
    return forMatches or revMatches

def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))

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

play_game(3, 'X', 'O')

#Test Cases
assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O', 'X'],
            [' ', 'O', 'X', ' '],
            ['X', 'X', ' ', 'X'],
            ['X', ' ', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    diagonal_winner(
        [
            ['X', 'X', ' '],
            ['X', ' ', 'O'],
            [' ', 'O', 'O']
        ]
    ),
    False
)

board = [['S', 'M', ' ', 'M'], ['S', 'S', 'S', ' '], ['S', 'S', 'S', 'S'], [' ', 'M', ' ', 'S']]

assert_equal(
    diagonal_winner(board), True    
)
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

assert_equal(
    winner(
        [
            ['X', 'X', 'X', ' '],
            ['X', 'X', ' ', ' '],
            ['X', ' ', 'O', 'X'],
            [' ', ' ', 'O', 'X']
        ]
    ),
    False
)
assert_equal(
    winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    winner(
        [
            ['X', ' '],
            ['X', 'O']
        ]
    ),
    True
)
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! Actual: {actual} != Expected: {expected}")

def format_board(board):
    result = ""
    for i in range(len(board)):
        for char in board[i]:
            result += char
        
        if i != len(board) - 1:
            result += '\n'
    return result

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
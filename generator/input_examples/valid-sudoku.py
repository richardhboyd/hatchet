def isValidSudoku(board):
    
    # Initialize a set to store seen numbers
    seen = set()
    
    # Check each row
    for row in board:
        for num in row:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        seen.clear()
        
    # Check each column
    for col in zip(*board):
        for num in col:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        seen.clear()
    
    # Check each 3x3 box
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            for row in board[i:i+3]:
                for num in row[j:j+3]:
                    if num != '.':
                        if num in seen:
                            return False
                        seen.add(num)
            seen.clear()
    
    # If no duplicate found
    return True
    

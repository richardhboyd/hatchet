def capture(board):
    m = len(board)
    n = len(board[0])
    
    # Step 1: Identify border O's and mark them as #
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and (i == 0 or i == m-1 or j == 0 or j == n-1):
                board[i][j] = '#'
    
    # Step 2: Capture surrounded O's by flipping them to X        
    for i in range(1, m-1):
        for j in range(1, n-1):
            if board[i][j] == 'O':
                board[i][j] = 'X'
    
    # Step 3: Flip border # back to O      
    for i in range(m):
        for j in range(n):
            if board[i][j] == '#':
                board[i][j] = 'O'
                
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
capture(board)
print(board)

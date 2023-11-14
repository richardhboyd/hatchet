def gameOfLife(board):
    # Neighbors array to find 8 neighboring cells for a given cell
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

    rows = len(board)
    cols = len(board[0])

    # Create a copy of the original board to store the next state
    # This allows us to update the board "in-place" 
    copy_board = [[board[i][j] for j in range(cols)] for i in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            
            # Count live neighbors
            live_neighbors = 0
            for neighbor in neighbors:
                r = i + neighbor[0]
                c = j + neighbor[1]
                
                # Check boundary and count neighbor only if in bounds
                if (r < rows and r >= 0) and (c < cols and c >= 0) and (board[r][c] == 1):
                    live_neighbors += 1

            # Rule 1 or Rule 3        
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                copy_board[i][j] = 0
            # Rule 4
            if board[i][j] == 0 and live_neighbors == 3:
                copy_board[i][j] = 1

    # Update original board 
    for i in range(rows):
        for j in range(cols):
            board[i][j] = copy_board[i][j]

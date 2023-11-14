def uniquePaths(m, n):
    grid = [[0 for x in range(n)] for y in range(m)] 
    for i in range(m):
        grid[i][0] = 1
    
    for j in range(n):
        grid[0][j] = 1
        
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
            
    return grid[m-1][n-1]


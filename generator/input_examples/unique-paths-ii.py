def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid) 
    n = len(obstacleGrid[0])
    
    # Initialze DP array with 0s
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    # Base cases
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
    return dp[-1][-1]

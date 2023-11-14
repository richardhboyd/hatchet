def largestSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    dp = [[0 for j in range(n)] for i in range(m)]
    maxSize = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1 
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                maxSize = max(maxSize, dp[i][j])
        
    return maxSize**2

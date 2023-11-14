import math

def minPathSum(grid):
  
  m = len(grid)
  n = len(grid[0])

  # Create a 2D array to store the minimum path sums
  dp = [[math.inf for _ in range(n)] for _ in range(m)]
  
  # Base cases
  dp[0][0] = grid[0][0]
  
  # Fill in the first row
  for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]
    
  # Fill in the first column  
  for i in range(1, m):
    dp[i][0] = dp[i-1][0] + grid[i][0]
    
  # Fill remaining grid  
  for i in range(1, m):
    for j in range(1, n):
      dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

  # Bottom right element will hold the minimum path sum  
  return dp[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid)) # 7


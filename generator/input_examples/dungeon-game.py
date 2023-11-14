import sys

def calculateMinimumHP(dungeon):
  m = len(dungeon)
  n = len(dungeon[0])

  # Initialize DP table with max value
  dp = [[sys.maxsize] * (n+1) for _ in range(m+1)]
  dp[m][n-1] = 1
  
  # Populate DP table bottom up
  for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
      min_health = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
      dp[i][j] = max(min_health, 1)
  
  return dp[0][0]

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(calculateMinimumHP(dungeon)) # 7

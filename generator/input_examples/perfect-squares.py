import math

def numSquares(n):
  if n < 2:
    return n
  
  squares = []
  i = 1  
  while i * i <= n:
    squares.append(i*i)
    i += 1

  dp = [float('inf')] * (n+1)
  dp[0] = 0
  
  for s in squares:
    for j in range(s, n+1):
      dp[j] = min(dp[j], dp[j-s] + 1)

  return dp[-1]

n = 12
print(numSquares(n))

n = 13  
print(numSquares(n))

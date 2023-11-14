def minimumTotal(triangle):
    if not triangle:
        return 0
    
    n = len(triangle)
    dp = [0] * (n + 1)
    for row in triangle[::-1]:
        for i, num in enumerate(row):
            dp[i] = num + min(dp[i], dp[i+1])
    
    return dp[0]

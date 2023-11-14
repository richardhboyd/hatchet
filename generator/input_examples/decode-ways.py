def numDecodings(s):
    if len(s) == 0 or s[0] == '0': 
        return 0
    
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0
    
    for i in range(2, len(s) + 1):
        one_digit = int(s[i-1])
        two_digit = int(s[i-2:i])
        
        if one_digit >= 1:
            dp[i] += dp[i-1]
        if two_digit >= 10 and two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[len(s)]

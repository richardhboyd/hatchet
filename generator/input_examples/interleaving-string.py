def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    
    dp = [False] * (len(s2) + 1)
    dp[0] = True
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i==0 and j==0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j-1] and s2[j] == s3[i+j]
            elif j == 0: 
                dp[j] = dp[j] and s1[i] == s3[i+j]
            else:
                dp[j] = (dp[j] and s1[i] == s3[i+j]) or (dp[j-1] and s2[j] == s3[i+j])
    
    return dp[-1]

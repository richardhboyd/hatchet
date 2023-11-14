def max_robbery(nums):
    n = len(nums)
    
    # Base cases
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    # DP array where dp[i] is max robbed up to house i
    dp = [0] * n
    
    # Rob 1st house and nth house
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Try robbing houses 2 to n-1
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
    # Rob 1st and nth, or 2nd to n-1th
    return max(dp[n-1], dp[n-2] + nums[0])


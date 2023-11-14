def houseRobber(nums):
  if len(nums) == 0:
    return 0
  
  dp = [0 for _ in range(len(nums))]
  dp[0] = nums[0]
  
  for i in range(1, len(nums)):
    if i == 1:
      dp[i] = max(nums[0], nums[1]) 
    else:
      dp[i] = max(dp[i-2] + nums[i], dp[i-1])

  return dp[-1]


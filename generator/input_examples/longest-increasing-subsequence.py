def lengthOfLIS(nums):
  LIS = [1] * len(nums)

  for i in range(len(nums)-1, -1, -1):
    for j in range(i+1, len(nums)):
      if nums[i] < nums[j]:
        LIS[i] = max(LIS[i], 1 + LIS[j])

  return max(LIS)

nums = [10,9,2,5,3,7,101,18] 
print(lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]  
print(lengthOfLIS(nums))

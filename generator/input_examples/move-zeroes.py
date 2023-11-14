def moveZeroes(nums):
  
  # First pass - move all non-zero elements to the front
  nonZeroIndex = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[nonZeroIndex] = nums[i]
      nonZeroIndex += 1
        
  # Second pass - fill remaining indices with 0s
  for i in range(nonZeroIndex, len(nums)):
    nums[i] = 0

  return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums)) # [1,3,12,0,0]

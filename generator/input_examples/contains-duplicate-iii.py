def find_pair(nums, indexDiff, valueDiff):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
        return True
  
  return False


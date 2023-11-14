def missingNumber(nums):
  n = len(nums)
  total = n*(n+1)//2
  
  array_sum = sum(nums)
  
  return total - array_sum

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))

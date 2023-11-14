def contains_duplicate(nums):
  num_set = set()
  for n in nums:
    if n in num_set:
      return True
    num_set.add(n)
  return False

print(contains_duplicate([1,2,3,1])) # True
print(contains_duplicate([1,2,3,4])) # False 
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True

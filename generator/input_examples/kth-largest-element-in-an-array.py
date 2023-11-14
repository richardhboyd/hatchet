import random

def findKthLargest(nums, k):
  pivot = random.choice(nums)
  left = [x for x in nums if x > pivot]
  mid = [x for x in nums if x == pivot]
  right = [x for x in nums if x < pivot]
  
  L = len(left)
  M = len(mid)
  
  if k <= L:
      return findKthLargest(left, k)
  elif k > L + M:
      return findKthLargest(right, k - L - M)  
  else:
      return mid[0]

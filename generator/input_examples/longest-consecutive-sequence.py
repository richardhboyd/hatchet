def longestConsecutive(nums):
  num_set = set(nums)
  longest = 0
  
  for n in nums:
    if (n - 1) not in num_set:
      length = 0
      while (n + length) in num_set:
        length += 1
      longest = max(length, longest)

  return longest

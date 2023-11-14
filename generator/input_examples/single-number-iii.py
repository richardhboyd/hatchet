def find_two_unique(nums):
  result = 0
  for num in nums:
    result ^= num
  
  # result now contains XOR of the two unique elements
  
  # Get the rightmost set bit
  rightmost_set_bit = 1
  while (result & rightmost_set_bit) == 0:
    rightmost_set_bit <<= 1
    
  num1, num2 = 0, 0
  
  for num in nums:
    if (num & rightmost_set_bit) != 0:
      num1 ^= num
    else:
      num2 ^= num
      
  return [num1, num2]

def next_permutation(nums):
  n = len(nums)

  # Step 1: find the largest index k such that nums[k] < nums[k+1]
  k = -1
  for i in range(n-1):
    if nums[i] < nums[i+1]:
      k = i

  # Step 2: if no such index exists, the permutation is sorted in descending order, 
  # reverse to ascending order
  if k == -1:
    nums.reverse()
    return

  # Step 3: find the largest index l greater than k such that nums[k] < nums[l]
  l = -1
  for i in range(k+1, n):
    if nums[k] < nums[i]:
      l = i

  # Step 4: swap nums[k] and nums[l] 
  nums[k], nums[l] = nums[l], nums[k]

  # Step 5: reverse the sequence from k+1 to the end
  left = k + 1
  right = n - 1

  while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1


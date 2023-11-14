def maximumGap(nums):
  if len(nums) < 2:
    return 0
  
  min_num = min(nums)
  max_num = max(nums)
  bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
  
  buckets = [[] for _ in range((max_num - min_num) // bucket_size + 1)]
  for num in nums:
    buckets[(num - min_num) // bucket_size].append(num)
  
  prev = min_num
  max_diff = 0
  for bucket in buckets:
    if bucket:
      max_diff = max(max_diff, min(bucket) - prev)
      prev = max(bucket)
      
  return max_diff

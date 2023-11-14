def minSubArrayLen(target, nums):
    total = left = 0
    result = len(nums) + 1 # start with invalid length
    
    for right, n in enumerate(nums):
        total += n
        
        while total >= target:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
        
    return result if result <= len(nums) else 0

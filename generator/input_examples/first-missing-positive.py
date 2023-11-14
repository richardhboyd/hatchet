def firstMissingPositive(nums):
    n = len(nums)
    
    # Mark elements as negative to indicate presence
    for i in range(n):
        num = abs(nums[i])
        if num <= n and nums[num-1] > 0:
            nums[num-1] *= -1
            
    # Find the first positive number
    for i in range(n):
        if nums[i] > 0:
            return i+1
        
    return n+1

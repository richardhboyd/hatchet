def threeSumClosest(nums, target):
    
    nums.sort()
    closest = float('inf')
    
    for i in range(len(nums)-2):
        l = i+1
        r = len(nums)-1
        
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(closest - target):
                closest = s
            
            if s < target:
                l += 1
            elif s > target: 
                r -= 1
            else:
                return target
    
    return closest

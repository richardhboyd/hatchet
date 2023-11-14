def fourSum(nums, target):
    result = []
    nums.sort()
    
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        for j in range(i+1, len(nums)-2): 
            if j > i+1 and nums[j] == nums[j-1]:
                continue
                
            left = j + 1
            right = len(nums) - 1
            
            while left < right:
                quad = [nums[i], nums[j], nums[left], nums[right]]
                if sum(quad) == target:
                    result.append(quad)
                    
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        
                elif sum(quad) < target:
                    left += 1
                else:
                    right -= 1
                    
    return result
    
    
nums = [1,0,-1,0,-2,2] 
target = 0
print(fourSum(nums, target))

# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

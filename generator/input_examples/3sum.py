def threeSum(nums):
    result = []
    nums.sort()
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left = i+1
        right = len(nums) - 1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
                
    return result

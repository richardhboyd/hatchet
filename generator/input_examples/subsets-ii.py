def subsets(nums):
    res = [[]]
    
    for num in nums:
        res += [item + [num] for item in res if item + [num] not in res]
        
    return res

nums = [1,2,2] 
print(subsets(nums))

nums = [0]
print(subsets(nums))

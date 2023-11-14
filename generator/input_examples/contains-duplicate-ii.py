def containsNearbyDuplicate(nums, k):
    seen = {}
    for i, v in enumerate(nums):
        if v in seen and i - seen[v] <= k:
            return True
        seen[v] = i
    return False

print(containsNearbyDuplicate([1,2,3,1], 3)) # True
print(containsNearbyDuplicate([1,0,1,1], 1)) # True 
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False

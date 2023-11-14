from itertools import permutations

def find_permutations(nums):
    perms = permutations(nums)
    perm_set = set()
    
    for perm in perms:
        perm_set.add(perm)
        
    return list(perm_set)

nums = [1,1,2] 
print(find_permutations(nums))

nums = [1,2,3]
print(find_permutations(nums))

from itertools import chain, combinations

def powerset(nums):
    ps = [[]]
    for num in nums:
        ps.extend(combinations(ps, num))
    return ps

nums = [1,2,3] 
print(powerset(nums))


from itertools import combinations

def find_combinations(k, n):
    combos = []
    
    # Generate all combinations of k numbers from 1 to 9
    nums = [i for i in range(1, 10)]
    for c in combinations(nums, k):
        if sum(c) == n:
            combos.append(list(c))
            
    return combos

print(find_combinations(3, 7))
print(find_combinations(3, 9)) 
print(find_combinations(4, 1))

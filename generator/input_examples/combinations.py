from itertools import combinations

def get_k_combinations(n, k):
    result = []
    for combo in combinations(range(1, n+1), k):
        result.append(list(combo))
    return result

n = 4 
k = 2
print(get_k_combinations(n, k))


from itertools import combinations

def combinationSum(candidates, target):
    results = []
    candidates.sort()

    def backtrack(remain, comb, start):
        if remain == 0:
            results.append(list(comb))
            return
        elif remain < 0:
            return
        
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i + 1)
            comb.pop()

    backtrack(target, [], 0)
    return results

candidates = [10,1,2,7,6,1,5] 
target = 8
print(combinationSum(candidates, target))

# Output:
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

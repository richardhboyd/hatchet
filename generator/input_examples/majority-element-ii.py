from collections import defaultdict

def majority_element(nums):
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
        
    n = len(nums)
    threshold = n//3
    
    result = []
    for num,count in counts.items():
        if count > threshold:
            result.append(num)
            
    return result

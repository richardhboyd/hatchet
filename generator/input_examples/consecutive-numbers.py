from typing import List

def findConsecutiveNums(logs: List[List[int]]) -> List[int]:
    result = []
    curr_num = None
    count = 0
    
    for log in logs:
        if log[1] == curr_num:
            count += 1
        else:
            curr_num = log[1]
            count = 1
        
        if count >= 3 and curr_num not in result:
            result.append(curr_num)
            
    return result

logs = [[1,1], [2,1], [3,1], [4,2], [5,1], [6,2], [7,2]]

print(findConsecutiveNums(logs))
# [1]

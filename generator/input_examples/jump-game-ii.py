def minJumps(nums):
    jumps = 0
    currentJumpEnd = 0
    farthest = 0
    
    for i in range(len(nums)-1):
        farthest = max(farthest, i + nums[i])
        if i == currentJumpEnd:
            jumps += 1
            currentJumpEnd = farthest
            
    return jumps

def trap(height):
    if not height:
        return 0
    
    left_max = [height[0]] + [0] * (len(height) - 1)
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i])
        
    right_max = [0] * (len(height) - 1) + [height[-1]]
    for i in range(len(height)-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
        
    trapped = 0
    for i in range(len(height)):
        trapped += min(left_max[i], right_max[i]) - height[i]
        
    return trapped

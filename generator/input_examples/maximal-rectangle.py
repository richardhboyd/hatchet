def largestRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    left = [0] * cols 
    right = [cols] * cols
    height = [0] * cols
    
    maxArea = 0
    
    for i in range(rows):
        cur_left = 0
        cur_right = cols
        
        for j in range(cols):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0
        
        for j in range(cols):
            if matrix[i][j] == '1': 
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1
                
        for j in range(cols-1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right) 
            else:
                right[j] = cols
                cur_right = j
                
        for j in range(cols):
            maxArea = max(maxArea, height[j] * (right[j] - left[j]))
            
    return maxArea

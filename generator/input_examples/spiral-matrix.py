def spiralOrder(matrix):
    result = []
    if not matrix:
        return result
    
    m = len(matrix) 
    n = len(matrix[0])
    
    top = 0
    bottom = m-1
    left = 0 
    right = n-1
    
    dir = 0 # 0: go right, 1: go down, 2: go left, 3: go up
    
    while top <= bottom and left <= right:
        
        if dir == 0: # go right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            dir = 1
        
        elif dir == 1: # go down
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            dir = 2
            
        elif dir == 2: # go left
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            dir = 3
            
        else: # go up
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
            dir = 0
        
    return result

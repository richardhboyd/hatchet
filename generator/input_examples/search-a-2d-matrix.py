def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    
    low = 0
    high = m * n - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_element = matrix[mid//n][mid%n]
        
        if target == mid_element:
            return True
        elif target < mid_element:
            high = mid - 1
        else:
            low = mid + 1
            
    return False

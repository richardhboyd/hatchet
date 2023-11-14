def mySqrt(x):
    if x < 0:
        raise ValueError('Negative number not supported')
    
    if x == 0 or x == 1:
        return x
    
    left = 1
    right = x
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_squared = mid * mid
        
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

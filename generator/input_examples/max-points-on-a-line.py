from collections import defaultdict

def maxPoints(points):
    n = len(points)
    if n <= 2:
        return n
    
    max_points = 0
    
    for i in range(n):
        slopes = defaultdict(int)
        duplicates = 1
        
        for j in range(i+1, n):
            if points[i] == points[j]:
                duplicates += 1
            else:
                dx = points[j][0] - points[i][0] 
                dy = points[j][1] - points[i][1]
                
                if dx == 0:
                    slope = 0
                else:
                    slope = dy/dx
                
                slopes[slope] += 1
        
        max_points = max(max_points, duplicates)
        max_points = max(max_points, max(slopes.values()) + duplicates)
        
    return max_points

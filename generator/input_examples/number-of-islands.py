def numIslands(grid):
    if not grid:
        return 0
    
    count = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if explore(grid, i, j, visited):
                count += 1
    return count

def explore(grid, i, j, visited):
    rowInbounds = 0 <= i < len(grid)
    colInbounds = 0 <= j < len(grid[0])
    if not rowInbounds or not colInbounds:
        return False
    
    if grid[i][j] == '0' or (i, j) in visited:
        return False
    
    visited.add((i, j))
    explore(grid, i+1, j, visited)
    explore(grid, i-1, j, visited)
    explore(grid, i, j+1, visited) 
    explore(grid, i, j-1, visited)
    return True

def generate_spiral_matrix(n):
  matrix = [[0 for _ in range(n)] for _ in range(n)]
  counter = 1
  start_row = 0
  end_row = n - 1
  start_col = 0 
  end_col = n - 1
  
  while start_row <= end_row and start_col <= end_col:
      
    # Traverse Right
    for i in range(start_col, end_col + 1):
      matrix[start_row][i] = counter
      counter += 1
      
    start_row += 1
      
    # Traverse Down
    for i in range(start_row, end_row + 1):
      matrix[i][end_col] = counter
      counter += 1
      
    end_col -= 1
      
    # Traverse Left  
    for i in range(end_col, start_col - 1, -1):
      matrix[end_row][i] = counter
      counter += 1
      
    end_row -= 1
    
    # Traver Up
    for i in range(end_row, start_row - 1, -1):
      matrix[i][start_col] = counter
      counter += 1
      
    start_col += 1
      
  return matrix

n = 3
print(generate_spiral_matrix(n))

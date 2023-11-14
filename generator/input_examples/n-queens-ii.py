def num_queens_solutions(n):
  def backtrack(row, col_placements):
    if row == n:
      return 1
    
    solutions = 0
    for col in range(n):
      if is_valid_placement(row, col, col_placements):
        col_placements[row] = col
        solutions += backtrack(row + 1, col_placements)
    return solutions
        
  def is_valid_placement(row, col, col_placements):
    for prev_row, prev_col in enumerate(col_placements):
      if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
        return False
    return True

  return backtrack(0, [0]*n)

print(num_queens_solutions(4)) # 2
print(num_queens_solutions(1)) # 1

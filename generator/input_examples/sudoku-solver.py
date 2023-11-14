board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - - - ")

    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print(" | ", end="")

      if j == 8:
        print(board[i][j])
      else:
        print(str(board[i][j]) + " ", end="")

def find_empty(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == '.':
        return (i, j) 
  return None

def valid(board, num, pos):

  # Check row
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and pos[1] != i:
      return False

  # Check column
  for i in range(len(board)):
    if board[i][pos[1]] == num and pos[0] != i:
      return False

  # Check box
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range(box_y*3, box_y*3 + 3):
    for j in range(box_x * 3, box_x*3 + 3):
      if board[i][j] == num and (i,j) != pos:
        return False

  return True

def solve(board):
  find = find_empty(board)
  if not find:
    return True
  else:
    row, col = find

  for i in range(1,10):
    if valid(board, str(i), (row, col)):
      board[row][col] = str(i)

      if solve(board):
        return True

      board[row][col] = '.'

  return False


print_board(board)
solve(board)
print("___________________")
print_board(board)

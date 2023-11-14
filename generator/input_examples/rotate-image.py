def rotate_matrix(matrix):
  n = len(matrix)
  
  # Transpose the matrix
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
  # Reverse each row
  for i in range(n):
    matrix[i] = matrix[i][::-1]

if __name__ == '__main__':
  
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  print("Original Matrix:")
  for row in matrix:
    print(row)

  rotate_matrix(matrix)
  
  print("\nRotated Matrix:")
  for row in matrix:
    print(row)

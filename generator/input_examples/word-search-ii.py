def findWords(board, words):
    rows, cols = len(board), len(board[0])
    result = []
    
    def backtrack(r, c, visited, curr_word):
        if curr_word in words:
            result.append(curr_word)
            words.remove(curr_word)
            
        visited.add((r, c))
        
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] not in visited and board[nr][nc] == curr_word[len(visited)-1]:
                backtrack(nr, nc, visited, curr_word + board[nr][nc])
                
        visited.remove((r, c))
        
    for r in range(rows):
        for c in range(cols):
            backtrack(r, c, set(), board[r][c])
            
    return result

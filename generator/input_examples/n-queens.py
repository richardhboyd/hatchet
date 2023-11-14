def solveNQueens(n):
    def backtrack(row, cols, pie, na):
        if row >= n:
            result.append(cols[:]) 
            return
        
        for col in range(n):
            if col in cols or row + col in pie or row - col in na:
                continue
            
            cols.append(col)
            pie.add(row + col)
            na.add(row - col)
            
            backtrack(row + 1, cols, pie, na)
            
            cols.pop()
            pie.remove(row + col)
            na.remove(row - col)
            
    result = []
    backtrack(0, [], set(), set())
    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

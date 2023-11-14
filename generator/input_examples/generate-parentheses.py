def generate_parentheses(n):
    results = []
    
    def backtrack(left, right, slate):
        if len(slate) == 2 * n:
            results.append(''.join(slate))
            return
        
        if left < n:
            slate.append('(')
            backtrack(left+1, right, slate)
            slate.pop()
            
        if right < left:
            slate.append(')')
            backtrack(left, right+1, slate)
            slate.pop()
            
    backtrack(0, 0, [])
    return results
